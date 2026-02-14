#!/usr/bin/env python3
"""
Refresh PokemonGOHub cache using Playwright to bypass Cloudflare.

Scrapes top raid attacker data for all 18 types from db.pokemongohub.net
and saves to meta/pokemongohub/{type}_response.json.

Usage:
    python scripts/fetch_pokemongohub.py

Prerequisites:
    pip install playwright
    playwright install chromium
"""

import json
import re
import sys
import time
from datetime import date
from pathlib import Path

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    print("Error: playwright not installed.")
    print("Run: pip install playwright && playwright install chromium")
    sys.exit(1)

TYPES = [
    "bug", "dark", "dragon", "electric", "fairy", "fighting",
    "fire", "flying", "ghost", "grass", "ground", "ice",
    "normal", "poison", "psychic", "rock", "steel", "water",
]

BASE_URL = "https://db.pokemongohub.net"
TYPE_PAGE = "/pokemon-list/best-per-type/{type}"
REQUEST_DELAY = 2  # seconds between requests


def parse_table_rows(page) -> list[dict]:
    """Extract attacker data from rendered HTML table rows."""
    results = []

    rows = page.query_selector_all("table tbody tr")
    if not rows:
        # Fallback: try extracting from page text
        return parse_from_text(page)

    for row in rows:
        cells = row.query_selector_all("td")
        if len(cells) < 7:
            continue

        try:
            name = cells[1].inner_text().strip()
            fast_move = cells[2].inner_text().strip()
            charged_move = cells[3].inner_text().strip()
            dps = float(cells[4].inner_text().strip())
            tdo = float(cells[5].inner_text().strip())
            score = float(cells[6].inner_text().strip())

            results.append({
                "attacker": {"name": name},
                "qm": fast_move,
                "cm": charged_move,
                "dps": dps,
                "tdo": tdo,
                "score": score,
            })
        except (ValueError, IndexError):
            continue

    return results


def parse_from_text(page) -> list[dict]:
    """Fallback: parse attacker data from page text content."""
    results = []
    text = page.inner_text("body")

    # Match lines like: 1.\nCrowned Sword Zacian\n\nMetal Claw\n\nBehemoth Blade\n35.16\t865.1\t31.95
    # The table text is tab/newline separated
    lines = text.split("\n")

    i = 0
    while i < len(lines):
        line = lines[i].strip()
        # Look for rank number pattern (e.g., "1.", "2.")
        rank_match = re.match(r"^(\d+)\.\s*$", line)
        if rank_match and i + 1 < len(lines):
            name = lines[i + 1].strip() if i + 1 < len(lines) else ""
            # Find DPS/TDO/Score values after the name
            # They appear as tab-separated numbers
            remaining = "\t".join(lines[i + 2 : i + 8])
            numbers = re.findall(r"(\d+\.?\d*)", remaining)

            if name and len(numbers) >= 3:
                try:
                    # Last 3 numbers are typically DPS, TDO, Score
                    dps = float(numbers[-3])
                    tdo = float(numbers[-2])
                    score = float(numbers[-1])

                    results.append({
                        "attacker": {"name": name},
                        "dps": dps,
                        "tdo": tdo,
                        "score": score,
                    })
                except (ValueError, IndexError):
                    pass
        i += 1

    return results


def fetch_all_types(output_dir: Path) -> dict:
    """Fetch attacker data for all 18 types. Returns {type: result_count or error}."""
    output_dir.mkdir(parents=True, exist_ok=True)
    results = {}

    print("=== PokemonGOHub Cache Refresh (Playwright) ===\n")
    print("Launching Chromium...")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Pass Cloudflare challenge
        print("Passing Cloudflare challenge...", end=" ", flush=True)
        start = time.time()
        try:
            page.goto(BASE_URL, wait_until="domcontentloaded", timeout=60000)
            time.sleep(8)  # Wait for Cloudflare JS challenge
            title = page.title()
            elapsed = time.time() - start
            if "just a moment" in title.lower():
                print(f"FAILED (still on challenge page after {elapsed:.1f}s)")
                browser.close()
                return results
            print(f"done ({elapsed:.1f}s)")
        except Exception as e:
            print(f"FAILED ({e})")
            browser.close()
            return results

        print(f"\nFetching {len(TYPES)} types:")

        for ptype in TYPES:
            url = f"{BASE_URL}{TYPE_PAGE.format(type=ptype)}"

            try:
                response = page.goto(url, wait_until="domcontentloaded", timeout=30000)
                time.sleep(3)  # Wait for table to render

                if response is None or response.status != 200:
                    status = response.status if response else "no response"
                    results[ptype] = f"HTTP {status}"
                    print(f"  {ptype:12} FAIL (HTTP {status})")
                    continue

                # Extract table data
                attackers = parse_table_rows(page)

                if not attackers:
                    results[ptype] = "no data parsed"
                    print(f"  {ptype:12} FAIL (no data parsed)")
                    continue

                # Save in format compatible with audit script
                data = {
                    "source": "pokemongohub",
                    "type": ptype,
                    "last_fetched": str(date.today()),
                    "results": attackers,
                }

                output_file = output_dir / f"{ptype}_response.json"
                with open(output_file, "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=2)

                results[ptype] = len(attackers)
                print(f"  {ptype:12} OK ({len(attackers)} results)")

            except Exception as e:
                results[ptype] = str(e)
                print(f"  {ptype:12} FAIL ({e})")

            if ptype != TYPES[-1]:
                time.sleep(REQUEST_DELAY)

        browser.close()

    return results


def main():
    project_root = Path(__file__).parent.parent
    output_dir = project_root / "meta" / "pokemongohub"

    results = fetch_all_types(output_dir)

    # Summary
    success = sum(1 for v in results.values() if isinstance(v, int))
    total = len(TYPES)
    print(f"\nDone: {success}/{total} types refreshed")
    if success > 0:
        print(f"Cache updated: {output_dir.relative_to(project_root)}/")

    if success < total:
        failed = {k: v for k, v in results.items() if not isinstance(v, int)}
        print(f"\nFailed types: {failed}")
        sys.exit(1)


if __name__ == "__main__":
    main()
