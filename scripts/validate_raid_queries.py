#!/usr/bin/env python3
"""
Validate raid attacker queries against RAID_ATTACKER_COUNTS.md reference table.

Two modes:
  Default:  Validate queries in CLAUDE.md and MASTER_LEAGUE_CHECKLIST.md match the table
  --audit:  Compare table against cached PokemonGOHub API data for freshness

Usage:
    python scripts/validate_raid_queries.py          # validate queries
    python scripts/validate_raid_queries.py --audit   # freshness audit
"""

import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
REFERENCE_FILE = PROJECT_ROOT / "docs" / "reference" / "RAID_ATTACKER_COUNTS.md"

QUERY_FILES = [
    PROJECT_ROOT / "CLAUDE.md",
    PROJECT_ROOT / "MASTER_LEAGUE_CHECKLIST.md",
]

POKEMONGOHUB_DIR = PROJECT_ROOT / "meta" / "pokemongohub"

# Prefixes to strip when extracting base species name
# Order matters: longer/more specific prefixes must come before shorter ones
FORM_PREFIXES = [
    "Apex Shadow ",  # Must come before "Shadow "
    "Mega ", "Shadow ", "Primal ",
    "Crowned Sword ", "Crowned Shield ",
    "Dawn Wings ", "Dusk Mane ",
    "Origin Forme ", "Aria Forme ",
    "Therian Forme ", "Incarnate Forme ",
    "Sky Forme ", "Resolute Forme ",
    "White ", "Black ",
]

# Suffixes to strip (parenthetical forme names, Mega X/Y, non-parenthetical forme names)
FORM_SUFFIX_PATTERN = re.compile(
    r"(\s*\(.*?\)|\s+[XY]|\s+Unbound|\s+Resolute)\s*$"
)


def extract_base_species(name: str) -> tuple[str, bool]:
    """Extract base species name and shadow status from a Pokemon name.

    Returns (base_species_lowercase, is_shadow).
    """
    is_shadow = name.startswith("Shadow ")

    clean = name
    for prefix in FORM_PREFIXES:
        if clean.startswith(prefix):
            clean = clean[len(prefix):]
            break

    clean = FORM_SUFFIX_PATTERN.sub("", clean)
    return clean.strip().lower(), is_shadow


def parse_reference_table() -> tuple[set[str], set[str], list[dict]]:
    """Parse Quick Reference Table from RAID_ATTACKER_COUNTS.md.

    Returns (non_shadow_species, shadow_species, all_entries).
    """
    non_shadow = set()
    shadow = set()
    entries = []

    with open(REFERENCE_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    in_table = False
    for line in lines:
        stripped = line.strip()

        # Detect table start (header row with "Pokemon")
        if "| Pokemon" in stripped and "| Count" in stripped:
            in_table = True
            continue

        # Skip separator row
        if in_table and stripped.startswith("| ---"):
            continue

        # End of table
        if in_table and not stripped.startswith("|"):
            break

        if not in_table:
            continue

        # Parse table row: | **Name** | **Count** | Types | Reasoning |
        cells = [c.strip() for c in stripped.split("|")]
        # cells[0] is empty (before first |), cells[1] is Pokemon name
        if len(cells) < 3:
            continue

        raw_name = cells[1].replace("**", "").strip()
        if not raw_name:
            continue

        count = cells[2].replace("**", "").strip() if len(cells) > 2 else ""
        types_covered = cells[3].strip() if len(cells) > 3 else ""

        base, is_shadow = extract_base_species(raw_name)
        entries.append({
            "raw_name": raw_name,
            "base_species": base,
            "is_shadow": is_shadow,
            "count": count,
            "types": types_covered,
        })

        if is_shadow:
            shadow.add(base)
        else:
            non_shadow.add(base)

    return non_shadow, shadow, entries


def extract_queries_from_file(filepath: Path) -> list[dict]:
    """Extract raid attacker queries from a file.

    Returns list of {line_num, query_type ('non_shadow'|'shadow'), species: set}.
    """
    queries = []
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for i, line in enumerate(lines, 1):
        # Match: !shadow&(species,species,...) or shadow&(species,species,...)
        for match in re.finditer(r"(!?)shadow&\(([^)]+)\)", line):
            is_non_shadow = match.group(1) == "!"
            species_str = match.group(2)
            species = {s.strip().lower() for s in species_str.split(",")}
            queries.append({
                "line_num": i,
                "query_type": "non_shadow" if is_non_shadow else "shadow",
                "species": species,
            })

    return queries


def validate_queries():
    """Mode 1: Validate queries match the reference table."""
    print("=== Raid Attacker Query Validation ===\n")

    # Parse reference table
    table_non_shadow, table_shadow, entries = parse_reference_table()
    print(f"Source of truth: {REFERENCE_FILE.relative_to(PROJECT_ROOT)}")
    print(f"  Non-shadow species: {len(table_non_shadow)}")
    print(f"  Shadow species: {len(table_shadow)}")
    print()

    all_ok = True
    all_non_shadow_queries = []
    all_shadow_queries = []

    # Extract and check queries from each file
    for filepath in QUERY_FILES:
        if not filepath.exists():
            print(f"WARNING: {filepath.name} not found, skipping")
            continue

        queries = extract_queries_from_file(filepath)
        rel_path = filepath.relative_to(PROJECT_ROOT)

        for q in queries:
            label = f"{rel_path} (line {q['line_num']})"
            species = q["species"]
            count = len(species)

            if q["query_type"] == "non_shadow":
                expected = table_non_shadow
                expected_label = "non-shadow"
                all_non_shadow_queries.append((label, species))
            else:
                expected = table_shadow
                expected_label = "shadow"
                all_shadow_queries.append((label, species))

            status = "OK" if species == expected else "MISMATCH"
            icon = "✅" if status == "OK" else "❌"
            print(f"  {label}: {count} {expected_label} species {icon}")

            if species != expected:
                all_ok = False
                missing = expected - species
                extra = species - expected
                if missing:
                    print(f"    Missing from query: {sorted(missing)}")
                if extra:
                    print(f"    Extra in query: {sorted(extra)}")

    # Cross-file consistency
    print(f"\n--- Cross-file Consistency ---")

    def check_consistency(queries_list, label):
        nonlocal all_ok
        if len(queries_list) < 2:
            print(f"  {label}: only {len(queries_list)} instance(s), skipping")
            return
        first_label, first_species = queries_list[0]
        all_match = all(s == first_species for _, s in queries_list[1:])
        if all_match:
            print(f"  All {label} queries match ✅")
        else:
            all_ok = False
            print(f"  {label} queries DIFFER ❌")
            for qlabel, qspecies in queries_list:
                diff = qspecies.symmetric_difference(first_species)
                if diff:
                    print(f"    {qlabel} differs by: {sorted(diff)}")

    check_consistency(all_non_shadow_queries, "non-shadow")
    check_consistency(all_shadow_queries, "shadow")

    # Generate correct queries if drift detected
    if not all_ok:
        print(f"\n--- Generated Correct Queries ---")
        ns_sorted = sorted(table_non_shadow)
        s_sorted = sorted(table_shadow)
        print(f"\nNon-shadow ({len(ns_sorted)} species):")
        print(f"!shadow&({','.join(ns_sorted)})")
        print(f"\nShadow ({len(s_sorted)} species):")
        print(f"shadow&({','.join(s_sorted)})")

    print()
    if all_ok:
        print("✅ All queries are accurate and consistent.")
    else:
        print("❌ Discrepancies found. See details above.")

    return all_ok


def freshness_audit():
    """Mode 2: Compare reference table against cached PokemonGOHub API data."""
    print("=== Freshness Audit ===\n")

    # Check cache exists
    if not POKEMONGOHUB_DIR.exists():
        print(f"ERROR: Cache directory not found: {POKEMONGOHUB_DIR}")
        print("Run: python scripts/fetch_pokemongohub.py")
        return False

    # Report cache age
    json_files = list(POKEMONGOHUB_DIR.glob("*_response.json"))
    if not json_files:
        print("ERROR: No cached API data found.")
        print("Run: python scripts/fetch_pokemongohub.py")
        return False

    oldest_mtime = min(os.path.getmtime(f) for f in json_files)
    cache_date = datetime.fromtimestamp(oldest_mtime).strftime("%Y-%m-%d")
    cache_age_days = (datetime.now() - datetime.fromtimestamp(oldest_mtime)).days

    print(f"Cache: {POKEMONGOHUB_DIR.relative_to(PROJECT_ROOT)}/ ({len(json_files)} files)")
    print(f"Cache date: {cache_date} ({cache_age_days} days old)")
    if cache_age_days > 90:
        print(f"⚠️  Cache is >{90} days old. Refresh with: python scripts/fetch_pokemongohub.py")
    print()

    # Parse reference table
    table_non_shadow, table_shadow, entries = parse_reference_table()
    all_table_species = table_non_shadow | table_shadow

    # Check each type's API data against table
    types_ok = 0
    types_with_gaps = 0
    all_missing = []

    for json_file in sorted(json_files):
        type_name = json_file.stem.replace("_response", "").capitalize()

        try:
            with open(json_file, "r", encoding="utf-8") as f:
                data = json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            print(f"--- {type_name} ---")
            print(f"  ERROR reading cache: {e}")
            types_with_gaps += 1
            continue

        results = data.get("results", [])

        # Filter out Mega/Primal evolutions (only need 1 per raid team)
        # then take top-5 non-Mega/Primal attackers
        filtered = [
            r for r in results
            if not r.get("attacker", {}).get("name", "").startswith(("Mega ", "Primal "))
        ]
        top_n = filtered[:5]

        # Extract base species from API top-5 (excl. Megas/Primals)
        api_species = []
        for entry in top_n:
            attacker = entry.get("attacker", {})
            name = attacker.get("name", "")
            dps = entry.get("dps", 0)

            # Extract base species using same logic as table parsing
            base, _ = extract_base_species(name)

            api_species.append({
                "name": name,
                "base": base,
                "dps": dps,
                "rank": len(api_species) + 1,
            })

        # Check if API top-10 are in our table
        missing = []
        for sp in api_species:
            if sp["base"] not in all_table_species:
                missing.append(sp)

        if missing:
            types_with_gaps += 1
            print(f"--- {type_name} (top 5, excl. Megas/Primals) ---")
            for m in missing:
                print(f"  ⚠️  {m['name']} (API #{m['rank']}, DPS: {m['dps']:.1f}) not in reference table")
            all_missing.extend(missing)
        else:
            types_ok += 1
            print(f"--- {type_name} (top 5, excl. Megas/Primals) --- All covered ✅")

    # Summary
    total = types_ok + types_with_gaps
    print(f"\nSummary: {types_ok}/{total} types fully covered", end="")
    if types_with_gaps > 0:
        print(f", {types_with_gaps} type(s) have gaps")
    else:
        print()

    if all_missing:
        print(f"\nPotentially missing species ({len(all_missing)} total):")
        seen = set()
        for m in all_missing:
            if m["base"] not in seen:
                seen.add(m["base"])
                print(f"  - {m['name']} (DPS: {m['dps']:.1f})")

    return types_with_gaps == 0


def main():
    if "--audit" in sys.argv:
        ok = freshness_audit()
    else:
        ok = validate_queries()

    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
