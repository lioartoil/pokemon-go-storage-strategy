#!/usr/bin/env python3
"""
Refresh ER (Estimator Rating) data from PokeBase DPS Calculator.

Scrapes the comprehensive DPS/TDO/ER table from pokebase.app/pokemon-go/dps-calc
and saves to meta/pokebase/comprehensive_dps.json. This replaces the need for
manual CSV downloads from the old GamePress spreadsheet.

Page structure: Each table entry renders as text lines:
    Pokemon Name
    Fast Move
    Charged Move
    DPS\\tTDO\\tER\\tCP    (tab-separated, comma-formatted numbers)

Usage:
    python scripts/fetch_pokebase.py

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

BASE_URL = "https://pokebase.app/pokemon-go/dps-calc"
PAGE_WAIT = 8  # seconds to wait for initial table render
PAGINATION_WAIT = 4  # seconds between page navigations

# Known column headers that should be skipped
SKIP_NAMES = {"Pokémon", "Pokemon", "Moves", "DPS", "TDO", "ER", "CP", "Page"}


def parse_text_entries(text: str) -> list[dict]:
    """Parse attacker data from page text content.

    The table renders as repeating 4-line groups:
        Pokemon Name
        Fast Move
        Charged Move
        DPS\\tTDO\\tER\\tCP
    """
    results = []
    lines = text.split("\n")

    i = 0
    while i < len(lines):
        line = lines[i].strip()

        # Look for a line with tab-separated numbers (DPS\tTDO\tER\tCP)
        if "\t" in line:
            parts = line.split("\t")
            nums = []
            for part in parts:
                try:
                    nums.append(float(part.strip().replace(",", "")))
                except ValueError:
                    break

            if len(nums) >= 4:
                # Walk backwards to find name and moves
                name = ""
                fast_move = ""
                charged_move = ""

                # The 3 lines before the numbers should be: name, fast_move, charged_move
                for back in range(1, min(6, i + 1)):
                    candidate = lines[i - back].strip()
                    if not candidate or candidate in SKIP_NAMES:
                        continue
                    if "\t" in candidate:
                        continue
                    # Assign in reverse order: closest = charged_move, then fast_move, then name
                    if not charged_move:
                        charged_move = candidate
                    elif not fast_move:
                        fast_move = candidate
                    elif not name:
                        name = candidate
                        break

                if name and len(name) >= 2:
                    results.append({
                        "pokemon": name,
                        "fast_move": fast_move,
                        "charged_move": charged_move,
                        "dps": round(nums[0], 2),
                        "tdo": round(nums[1], 1),
                        "er": round(nums[2], 2),
                        "cp": int(nums[3]),
                    })
        i += 1

    return results


def get_page_info(text: str) -> tuple[int, int]:
    """Extract current page and total pages from text."""
    match = re.search(r"Page\s+(\d+)\s+of\s+(\d+)", text)
    if match:
        return int(match.group(1)), int(match.group(2))
    return 1, 1


def click_next_page(page) -> bool:
    """Click the next page button. Returns False if no more pages.

    PokeBase uses Lucide SVG chevron icons with no text/aria-label.
    The chevron-right SVG path is 'm9 18 6-6-6-6'.
    Use .last to disambiguate from the settings sidebar chevron.
    """
    try:
        next_btn = page.locator(
            "button:has(path[d='m9 18 6-6-6-6'])"
        ).last
        if next_btn.is_enabled():
            next_btn.click()
            return True
    except Exception:
        pass

    return False


def fetch_all_pages(output_dir: Path) -> dict:
    """Fetch comprehensive DPS/TDO/ER data from PokeBase DPS calc."""
    output_dir.mkdir(parents=True, exist_ok=True)
    all_results = []

    print("=== PokeBase DPS Calculator Scrape ===\n")
    print("Launching Chromium...")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        print(f"Navigating to {BASE_URL}...", end=" ", flush=True)
        start = time.time()
        try:
            page.goto(BASE_URL, wait_until="domcontentloaded", timeout=60000)
            time.sleep(PAGE_WAIT)
            elapsed = time.time() - start
            print(f"done ({elapsed:.1f}s)")
        except Exception as e:
            print(f"FAILED ({e})")
            browser.close()
            return {"error": str(e), "results": []}

        body_text = page.inner_text("body")
        _, total_pages = get_page_info(body_text)
        print(f"Found {total_pages} pages of results\n")

        for page_num in range(1, total_pages + 1):
            print(f"  Page {page_num}/{total_pages}...", end=" ", flush=True)

            body_text = page.inner_text("body")
            results = parse_text_entries(body_text)

            if results:
                all_results.extend(results)
                print(f"OK ({len(results)} entries, total: {len(all_results)})")
            else:
                print("WARN (no data parsed)")

            # Navigate to next page
            if page_num < total_pages:
                if not click_next_page(page):
                    print(f"\n  Could not navigate past page {page_num}")
                    break
                time.sleep(PAGINATION_WAIT)

            # Safety limit
            if len(all_results) > 5000:
                print(f"\n  Safety limit reached ({len(all_results)} entries)")
                break

        browser.close()

    # Deduplicate: keep best ER per Pokemon name
    seen = {}
    for entry in all_results:
        name = entry["pokemon"]
        if name not in seen or entry["er"] > seen[name]["er"]:
            seen[name] = entry

    deduped = sorted(seen.values(), key=lambda x: x["er"], reverse=True)

    # Save
    data = {
        "source": "pokebase",
        "url": BASE_URL,
        "last_fetched": str(date.today()),
        "total_entries": len(deduped),
        "results": deduped,
    }

    output_file = output_dir / "comprehensive_dps.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    return {
        "total_scraped": len(all_results),
        "unique_pokemon": len(deduped),
        "output_file": str(output_file),
    }


def main():
    project_root = Path(__file__).parent.parent
    output_dir = project_root / "meta" / "pokebase"

    result = fetch_all_pages(output_dir)

    if "error" in result:
        print(f"\nFailed: {result['error']}")
        sys.exit(1)

    print(f"\nDone: {result['unique_pokemon']} unique Pokemon scraped")
    print(f"Output: {result['output_file']}")


if __name__ == "__main__":
    main()
