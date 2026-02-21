#!/usr/bin/env python3
"""
Cross-reference raid attacker data from multiple sources.

Compares PokeBase ER (fresh), PokemonGOHub (validation), PvPoke ML PvP (modifier),
and GamePress (fallback) against the current RAID_ATTACKER_COUNTS.md reference.

Outputs:
  meta/cross_reference_results.json  — structured merged data
  stdout                             — human-readable report

Usage:
    python scripts/cross_reference_raid_sources.py
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
REFERENCE_FILE = PROJECT_ROOT / "docs" / "reference" / "RAID_ATTACKER_COUNTS.md"
POKEBASE_FILE = PROJECT_ROOT / "meta" / "pokebase" / "comprehensive_dps.json"
POKEMONGOHUB_DIR = PROJECT_ROOT / "meta" / "pokemongohub"
PVPOKE_FILE = PROJECT_ROOT / "meta" / "pvpoke_ml_rankings.json"
GAMEPRESS_FILE = PROJECT_ROOT / "meta" / "raid_attackers_by_type.json"
OUTPUT_FILE = PROJECT_ROOT / "meta" / "cross_reference_results.json"

# --- Name normalization (from validate_raid_queries.py) ---

FORM_PREFIXES = [
    "Apex Shadow ",
    "Mega ", "Shadow ", "Primal ",
    "Crowned Sword ", "Crowned Shield ",
    "Dawn Wings ", "Dusk Mane ",
    "Origin Forme ", "Aria Forme ",
    "Therian Forme ", "Incarnate Forme ",
    "Sky Forme ", "Resolute Forme ",
    "White ", "Black ",
]

FORM_SUFFIX_PATTERN = re.compile(
    r"(\s*\(.*?\)|\s+[XY]|\s+Unbound|\s+Resolute)\s*$"
)


def normalize_name(name: str) -> str:
    """Normalize Pokemon name to a canonical lowercase key.

    Converts all naming formats to prefix style:
      "Rayquaza (Mega)" → "mega rayquaza"
      "Mega Rayquaza"   → "mega rayquaza"
      "Metagross (Shadow)" → "shadow metagross"  (PvPoke format)
      "Shadow Metagross"  → "shadow metagross"
      "Zacian - Crowned Sword" → "zacian (crowned sword)"
      "Necrozma (Dawn Wings)" → "dawn wings necrozma"
    """
    name = name.strip()

    # Convert dash-separated formes to parenthetical
    if " - " in name:
        parts = name.split(" - ", 1)
        name = f"{parts[0]} ({parts[1]})"

    # Convert suffix form indicators to prefix format
    # Handles: (Mega), (Primal), (Shadow), (Dawn Wings), (Dusk Mane)
    suffix_to_prefix = [
        "Mega", "Primal", "Shadow",
        "Dawn Wings", "Dusk Mane",
    ]
    for form in suffix_to_prefix:
        m = re.match(
            rf"^(.+?)\s*\({re.escape(form)}\)$", name, re.IGNORECASE
        )
        if m:
            name = f"{form} {m.group(1)}"
            break

    return name.lower()


# Aliases: normalized name → alternative normalized name
# Used to match across source naming differences
NAME_ALIASES = {
    # Reference table → PokeBase
    "kyurem (white)": "white kyurem",
    "kyurem (black)": "black kyurem",
    "kyurem (regular)": "kyurem",
    "zacian (crowned)": "zacian (crowned sword)",
    "zamazenta (crowned)": "zamazenta (crowned shield)",
    "keldeo (resolute)": "keldeo (resolute forme)",
    "deoxys (attack)": "deoxys (attack forme)",
    "palkia (origin)": "palkia (origin forme)",
    "dialga (origin)": "dialga (origin forme)",
    "landorus (therian)": "landorus (therian forme)",
    # Charizard Mega has X/Y forms — use best ER (Y)
    "mega charizard": "mega charizard y",
}

# Build reverse aliases too
_reverse = {v: k for k, v in NAME_ALIASES.items()}
NAME_ALIASES.update(_reverse)


def resolve_name(name: str, source_data: dict) -> str | None:
    """Try to find a matching key in source_data for the given name."""
    norm = normalize_name(name)
    if norm in source_data:
        return norm

    # Try alias
    alias = NAME_ALIASES.get(norm)
    if alias and alias in source_data:
        return alias

    return None


def extract_base_species(name: str) -> tuple[str, bool]:
    """Extract base species name and shadow status."""
    is_shadow = "shadow" in name.lower().split("(")[0]

    clean = name
    for prefix in FORM_PREFIXES:
        if clean.startswith(prefix):
            clean = clean[len(prefix):]
            break

    clean = FORM_SUFFIX_PATTERN.sub("", clean)
    return clean.strip().lower(), is_shadow


# --- Hardcoded sets ---

LEGENDARY_UB_MYTHICAL = {
    "mewtwo", "rayquaza", "groudon", "kyogre", "kyurem", "reshiram",
    "zekrom", "xerneas", "yveltal", "palkia", "dialga", "regigigas",
    "heatran", "landorus", "zacian", "zamazenta", "necrozma", "lunala",
    "eternatus", "moltres", "raikou", "zapdos", "terrakion", "darkrai",
    "regieleki", "deoxys",
    # Ultra Beasts
    "pheromosa", "kartana", "xurkitree", "blacephalon",
    # Mythical
    "hoopa", "keldeo", "diancie",
}

ACCESSIBLE = {
    "machop", "machamp", "eevee", "roselia", "weedle", "beedrill",
    "gastly", "gengar", "alakazam", "abra", "gardevoir", "ralts",
    "honchkrow", "murkrow", "sceptile", "treecko", "staraptor",
    "starly", "salamence", "bagon", "dragonite", "dratini",
    "charizard", "charmander", "pinsir", "scizor", "scyther",
    "conkeldurr", "timburr", "toxicroak", "croagunk", "swampert",
    "mudkip",
}

ACCOUNT_LIMITED = {
    "eternatus": 1,
    "keldeo": 1,
    "diancie": 1,
}

GIOVANNI_POKEMON = {
    "shadow mewtwo", "shadow regigigas", "shadow groudon", "shadow kyogre",
    "shadow moltres", "shadow raikou", "shadow zapdos", "shadow heatran",
    "shadow darkrai", "shadow palkia", "shadow dialga",
}

ML_PVP_TOP_N = 50


def load_pokebase() -> dict[str, dict]:
    """Load PokeBase ER data. Returns {normalized_name: entry}."""
    if not POKEBASE_FILE.exists():
        print(f"WARNING: {POKEBASE_FILE} not found")
        return {}

    with open(POKEBASE_FILE, encoding="utf-8") as f:
        data = json.load(f)

    result = {}
    for entry in data.get("results", []):
        key = normalize_name(entry["pokemon"])
        result[key] = {
            "pokemon": entry["pokemon"],
            "er": entry["er"],
            "dps": entry["dps"],
            "tdo": entry["tdo"],
            "source": "pokebase",
        }
    return result


def load_pokemongohub() -> dict[str, list[dict]]:
    """Load PokemonGOHub data by type. Returns {type: [entries]}."""
    if not POKEMONGOHUB_DIR.exists():
        return {}

    result = {}
    for json_file in sorted(POKEMONGOHUB_DIR.glob("*_response.json")):
        type_name = json_file.stem.replace("_response", "").capitalize()
        with open(json_file, encoding="utf-8") as f:
            data = json.load(f)
        result[type_name] = data.get("results", [])
    return result


def load_pvpoke() -> dict[str, dict]:
    """Load PvPoke ML rankings. Returns {normalized_name: entry}."""
    if not PVPOKE_FILE.exists():
        print(f"WARNING: {PVPOKE_FILE} not found")
        return {}

    with open(PVPOKE_FILE, encoding="utf-8") as f:
        data = json.load(f)

    result = {}
    for entry in data.get("rankings", []):
        key = normalize_name(entry["speciesName"])
        result[key] = {
            "speciesName": entry["speciesName"],
            "rank": entry["rank"],
            "score": entry["score"],
        }
    return result


def load_gamepress() -> dict[str, dict]:
    """Load GamePress ER data. Returns {normalized_name: entry}."""
    if not GAMEPRESS_FILE.exists():
        return {}

    with open(GAMEPRESS_FILE, encoding="utf-8") as f:
        data = json.load(f)

    result = {}
    for type_name, type_data in data.get("types", {}).items():
        for entry in type_data.get("top_attackers", []):
            key = normalize_name(entry["pokemon"])
            if key not in result or entry.get("er", 0) > result[key].get("er", 0):
                result[key] = {
                    "pokemon": entry["pokemon"],
                    "er": entry.get("er", 0),
                    "dps": entry.get("dps", 0),
                    "tdo": entry.get("tdo", 0),
                    "source": "gamepress",
                }
    return result


def parse_reference_table() -> list[dict]:
    """Parse Quick Reference Table from RAID_ATTACKER_COUNTS.md."""
    entries = []
    with open(REFERENCE_FILE, encoding="utf-8") as f:
        lines = f.readlines()

    in_table = False
    for line in lines:
        stripped = line.strip()

        if "| Pokemon" in stripped and "| Count" in stripped and "| ER" in stripped:
            in_table = True
            continue
        if in_table and stripped.startswith("| ---"):
            continue
        if in_table and not stripped.startswith("|"):
            break
        if not in_table:
            continue

        cells = [c.strip() for c in stripped.split("|")]
        if len(cells) < 6:
            continue

        raw_name = cells[1].replace("**", "").strip()
        if not raw_name:
            continue

        count_str = cells[2].replace("**", "").strip()
        er_str = cells[3].strip()
        types_covered = cells[4].strip()
        tier_calc = cells[5].strip()

        try:
            count = int(count_str)
        except ValueError:
            count = 0

        try:
            er = float(er_str.replace("~", ""))
        except ValueError:
            er = None

        entries.append({
            "raw_name": raw_name,
            "normalized": normalize_name(raw_name),
            "count": count,
            "er": er,
            "types": types_covered,
            "tier_calc": tier_calc,
        })

    return entries


def get_pokemongohub_rank(name: str, hub_data: dict) -> dict | None:
    """Find Pokemon's best rank across all types in PokemonGOHub data."""
    norm = normalize_name(name)
    best = None

    for type_name, entries in hub_data.items():
        for i, entry in enumerate(entries):
            entry_name = entry.get("attacker", {}).get("name", "")
            entry_norm = normalize_name(entry_name)

            if entry_norm == norm:
                rank = i + 1
                if best is None or rank < best["rank"]:
                    best = {
                        "type": type_name,
                        "rank": rank,
                        "dps": entry.get("dps", 0),
                        "score": entry.get("score", 0),
                    }

    # If no exact match, try aliases
    if not best:
        alias = NAME_ALIASES.get(norm)
        if alias:
            for type_name, entries in hub_data.items():
                for i, entry in enumerate(entries):
                    entry_name = entry.get("attacker", {}).get("name", "")
                    if normalize_name(entry_name) == alias:
                        rank = i + 1
                        if best is None or rank < best["rank"]:
                            best = {
                                "type": type_name,
                                "rank": rank,
                                "dps": entry.get("dps", 0),
                                "score": entry.get("score", 0),
                            }

    return best


def find_pvpoke_match(name: str, pvpoke_data: dict) -> dict | None:
    """Find Pokemon in PvPoke ML rankings."""
    # Try direct match or alias
    key = resolve_name(name, pvpoke_data)
    if key:
        return pvpoke_data[key]

    # For Mega/Primal: try finding the base species (Mega not in PvP)
    norm = normalize_name(name)
    if norm.startswith("mega ") or norm.startswith("primal "):
        base = re.sub(r"^(mega|primal)\s+", "", norm)
        if base in pvpoke_data:
            return pvpoke_data[base]

    return None


def get_type_coverage(name: str, hub_data: dict) -> list[str]:
    """Find all types where this Pokemon appears in top-5 of PokemonGOHub."""
    norm = normalize_name(name)
    alias = NAME_ALIASES.get(norm)
    types = []

    for type_name, entries in hub_data.items():
        for i, entry in enumerate(entries[:5]):
            entry_name = entry.get("attacker", {}).get("name", "")
            entry_norm = normalize_name(entry_name)

            if entry_norm == norm or (alias and entry_norm == alias):
                types.append(type_name)
                break
    return types


def calc_tier(er: float | None) -> tuple[str, int]:
    """Calculate tier and base count from ER."""
    if er is None:
        return "?", 0
    if er >= 60:
        return "S", 6
    if er >= 55:
        return "A", 5
    if er >= 50:
        return "B", 4
    if er >= 45:
        return "C", 3
    if er >= 40:
        return "D", 2
    return "E", 1


def calc_recommended_count(
    name: str, er: float | None, tdo: float | None,
    type_coverage: list[str], pvpoke_rank: int | None,
    hub_rank: dict | None,
) -> tuple[int, str]:
    """Calculate recommended count with all 5 modifiers."""
    base, is_shadow = extract_base_species(name)
    norm = normalize_name(name)

    # Account-limited override
    if base in ACCOUNT_LIMITED:
        return ACCOUNT_LIMITED[base], "Account-limited"

    tier, base_count = calc_tier(er)

    # Proxy for missing ER
    if tier == "?" and hub_rank:
        rank = hub_rank["rank"]
        # Skip Mega/Primal from ranking
        if rank <= 2:
            tier, base_count = "A", 5
        elif rank <= 5:
            tier, base_count = "B", 4
        elif rank <= 10:
            tier, base_count = "C", 3
        else:
            tier, base_count = "D", 2

    if tier == "?":
        tier, base_count = "D", 2  # fallback

    modifiers = []
    count = base_count

    # +1 Dual-type (rank #1-5 in 2+ types)
    top5_types = [t for t in type_coverage]  # already filtered to top-10
    # Check top-5 specifically
    if len(top5_types) >= 2:
        modifiers.append("+dual")
        count += 1

    # +1 Legendary/UB/Mythical
    if base in LEGENDARY_UB_MYTHICAL:
        modifiers.append("+legend")
        count += 1

    # +1 ML PvP top-50
    if pvpoke_rank is not None and pvpoke_rank <= ML_PVP_TOP_N:
        modifiers.append(f"+pvp#{pvpoke_rank}")
        count += 1

    # -1 Accessible
    if base in ACCESSIBLE:
        modifiers.append("-access")
        count -= 1

    # -1 Glass cannon
    if tdo is not None and tdo < 300:
        modifiers.append("-glass")
        count -= 1

    # Hard caps
    count = max(1, min(6, count))

    # Giovanni override
    if norm in GIOVANNI_POKEMON:
        modifiers.append("Giovanni")

    calc_str = f"{tier}({base_count})" + "".join(modifiers)
    if count != base_count + sum(
        1 for m in modifiers if m.startswith("+")
    ) - sum(
        1 for m in modifiers if m.startswith("-")
    ):
        calc_str += f"→cap{count}"

    return count, calc_str


def main():
    print("=== Raid Attacker Cross-Reference Report ===\n")

    # Load all sources
    pokebase = load_pokebase()
    hub_data = load_pokemongohub()
    pvpoke = load_pvpoke()
    gamepress = load_gamepress()
    current_table = parse_reference_table()

    print(f"Sources loaded:")
    print(f"  PokeBase:       {len(pokebase)} entries")
    print(f"  PokemonGOHub:   {sum(len(v) for v in hub_data.values())} entries across {len(hub_data)} types")
    print(f"  PvPoke ML:      {len(pvpoke)} entries")
    print(f"  GamePress:      {len(gamepress)} entries")
    print(f"  Current table:  {len(current_table)} entries")
    print()

    # Process each Pokemon in the current table
    results = []
    changes = {"increased": [], "decreased": [], "er_updated": [], "pvp_added": []}

    for entry in current_table:
        name = entry["raw_name"]
        norm = entry["normalized"]
        current_count = entry["count"]
        current_er = entry["er"]

        # Find ER: PokeBase (primary) → GamePress (fallback)
        new_er = None
        new_tdo = None
        er_source = None

        pb_key = resolve_name(name, pokebase)
        gp_key = resolve_name(name, gamepress)

        if pb_key:
            new_er = pokebase[pb_key]["er"]
            new_tdo = pokebase[pb_key]["tdo"]
            er_source = "pokebase"
        elif gp_key:
            new_er = gamepress[gp_key]["er"]
            new_tdo = gamepress[gp_key]["tdo"]
            er_source = "gamepress"

        # PokemonGOHub rank
        hub_rank = get_pokemongohub_rank(name, hub_data)

        # PvPoke ML rank
        pvpoke_match = find_pvpoke_match(name, pvpoke)
        pvpoke_rank = pvpoke_match["rank"] if pvpoke_match else None

        # Type coverage from PokemonGOHub
        type_coverage = get_type_coverage(name, hub_data)

        # Calculate recommended count
        rec_count, calc_str = calc_recommended_count(
            name, new_er, new_tdo, type_coverage, pvpoke_rank, hub_rank,
        )

        result = {
            "pokemon": name,
            "current_count": current_count,
            "recommended_count": rec_count,
            "current_er": current_er,
            "new_er": new_er,
            "er_source": er_source,
            "tdo": new_tdo,
            "hub_rank": hub_rank,
            "pvpoke_rank": pvpoke_rank,
            "pvpoke_score": pvpoke_match["score"] if pvpoke_match else None,
            "type_coverage": type_coverage,
            "tier_calc": calc_str,
            "current_types": entry["types"],
            "change": rec_count - current_count,
        }
        results.append(result)

        # Track changes
        if rec_count > current_count:
            changes["increased"].append(result)
        elif rec_count < current_count:
            changes["decreased"].append(result)

        if current_er is None and new_er is not None:
            changes["er_updated"].append(result)
        elif current_er is not None and new_er is not None and abs(current_er - new_er) > 1.0:
            changes["er_updated"].append(result)

        if pvpoke_rank is not None and pvpoke_rank <= ML_PVP_TOP_N:
            changes["pvp_added"].append(result)

    # Print report
    print("=" * 80)
    print("CROSS-REFERENCE RESULTS")
    print("=" * 80)

    # Summary stats
    total_current = sum(e["current_count"] for e in results)
    total_recommended = sum(e["recommended_count"] for e in results)

    print(f"\nTotal species: {len(results)}")
    print(f"Current copies:     {total_current}")
    print(f"Recommended copies: {total_recommended} ({total_recommended - total_current:+d})")
    print()

    # ER Updates (previously missing, now have fresh ER)
    if changes["er_updated"]:
        print(f"\n--- ER Updates ({len(changes['er_updated'])} species) ---")
        for r in sorted(changes["er_updated"], key=lambda x: -(x["new_er"] or 0)):
            old = f"{r['current_er']:.2f}" if r["current_er"] else "—"
            new = f"{r['new_er']:.2f}" if r["new_er"] else "—"
            print(f"  {r['pokemon']:30s}  {old:>8s} → {new:>8s}  ({r['er_source']})")

    # ML PvP Top-50 modifiers
    if changes["pvp_added"]:
        print(f"\n--- ML PvP Top-50 Modifier ({len(changes['pvp_added'])} species) ---")
        for r in sorted(changes["pvp_added"], key=lambda x: x["pvpoke_rank"]):
            print(f"  {r['pokemon']:30s}  PvP #{r['pvpoke_rank']:>3d}  (score {r['pvpoke_score']:.1f})")

    # Count increases
    if changes["increased"]:
        print(f"\n--- Count INCREASES ({len(changes['increased'])} species) ---")
        for r in sorted(changes["increased"], key=lambda x: -x["change"]):
            print(f"  {r['pokemon']:30s}  {r['current_count']} → {r['recommended_count']}  ({r['change']:+d})  {r['tier_calc']}")

    # Count decreases
    if changes["decreased"]:
        print(f"\n--- Count DECREASES ({len(changes['decreased'])} species) ---")
        for r in sorted(changes["decreased"], key=lambda x: x["change"]):
            print(f"  {r['pokemon']:30s}  {r['current_count']} → {r['recommended_count']}  ({r['change']:+d})  {r['tier_calc']}")

    # Full table
    print(f"\n--- Full Cross-Reference Table ---")
    print(f"{'Pokemon':30s} {'Cur':>3s} {'Rec':>3s} {'Chg':>4s} {'OldER':>8s} {'NewER':>8s} {'Src':>8s} {'PvP#':>5s} {'Calc'}")
    print("-" * 110)
    for r in results:
        old_er = f"{r['current_er']:.2f}" if r['current_er'] else "—"
        new_er = f"{r['new_er']:.2f}" if r['new_er'] else "—"
        pvp = f"#{r['pvpoke_rank']}" if r['pvpoke_rank'] else "—"
        chg = f"{r['change']:+d}" if r['change'] != 0 else "="
        src = r['er_source'] or "—"
        print(f"  {r['pokemon']:30s} {r['current_count']:>3d} {r['recommended_count']:>3d} {chg:>4s} {old_er:>8s} {new_er:>8s} {src:>8s} {pvp:>5s}  {r['tier_calc']}")

    # Save results
    output = {
        "generated": str(__import__("datetime").date.today()),
        "sources": {
            "pokebase": {"entries": len(pokebase), "file": str(POKEBASE_FILE)},
            "pokemongohub": {"types": len(hub_data), "file": str(POKEMONGOHUB_DIR)},
            "pvpoke": {"entries": len(pvpoke), "file": str(PVPOKE_FILE)},
            "gamepress": {"entries": len(gamepress), "file": str(GAMEPRESS_FILE)},
        },
        "summary": {
            "total_species": len(results),
            "current_copies": total_current,
            "recommended_copies": total_recommended,
            "net_change": total_recommended - total_current,
            "count_increases": len(changes["increased"]),
            "count_decreases": len(changes["decreased"]),
            "er_updates": len(changes["er_updated"]),
            "pvp_modifiers": len(changes["pvp_added"]),
        },
        "results": results,
    }

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)

    print(f"\nResults saved to: {OUTPUT_FILE.relative_to(PROJECT_ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
