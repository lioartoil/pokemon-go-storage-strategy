#!/usr/bin/env python3
"""
Compare raid attacker data from GamePress and PokemonGOHub.
Generate a comparison report showing agreements and discrepancies.
"""

import json
from pathlib import Path
from collections import defaultdict

def normalize_pokemon_name(name):
    """Normalize Pokemon name for comparison."""
    # Remove parenthetical forms for matching
    name = name.split(' (')[0]
    # Standardize spacing
    name = name.replace('-', ' ').replace('  ', ' ').strip()
    # Lowercase for case-insensitive matching
    return name.lower()

def parse_pokemongohub_data(pogo_dir):
    """Parse PokemonGOHub API responses."""
    type_attackers = {}

    for json_file in pogo_dir.glob('*_response.json'):
        type_name = json_file.stem.replace('_response', '').capitalize()

        try:
            with open(json_file, 'r') as f:
                data = json.load(f)

            # Extract top 10 attackers
            attackers = []
            if 'results' in data:
                for result in data['results'][:10]:
                    attacker_data = result.get('attacker', {})
                    name = attacker_data.get('name', '')
                    form = attacker_data.get('form', '')

                    # Build full name
                    full_name = name
                    if form and form not in ['Normal', 'Standard', None]:
                        # Form already includes "Shadow", "Mega", etc. in the name
                        # Just use the name as-is from PokemonGOHub
                        pass

                    attackers.append({
                        'name': full_name,
                        'normalized': normalize_pokemon_name(full_name),
                        'dps': result.get('dps', 0),
                        'tdo': result.get('tdo', 0),
                        'score': result.get('score', 0)
                    })

            type_attackers[type_name] = attackers

        except Exception as e:
            print(f"Error parsing {json_file}: {e}")
            type_attackers[type_name] = []

    return type_attackers

def load_gamepress_data(gamepress_file):
    """Load GamePress data from JSON."""
    with open(gamepress_file, 'r') as f:
        data = json.load(f)

    type_attackers = {}
    for type_name, type_data in data['types'].items():
        attackers = []
        for attacker in type_data['top_attackers']:
            attackers.append({
                'name': attacker['pokemon'],
                'normalized': normalize_pokemon_name(attacker['pokemon']),
                'dps': attacker['dps'],
                'tdo': attacker['tdo']
            })
        type_attackers[type_name] = attackers

    return type_attackers

def compare_sources(gamepress, pokemongohub):
    """Compare the two sources and generate comparison data."""
    comparison = {}

    # Map GamePress type names to PokemonGOHub type names
    type_mapping = {
        'Bug': 'Bug',
        'Dark': 'Dark',
        'Dragon': 'Dragon',
        'Electric': 'Electric',
        'Fairy': 'Fairy',
        'Fighting': 'Fighting',
        'Fire': 'Fire',
        'Flying': 'Flying',
        'Ghost': 'Ghost',
        'Grass': 'Grass',
        'Ground': 'Ground',
        'Ice': 'Ice',
        'Normal': 'Normal',
        'Poison': 'Poison',
        'Psychic': 'Psychic',
        'Rock': 'Rock',
        'Steel': 'Steel',
        'Water': 'Water'
    }

    for gp_type, pogo_type in type_mapping.items():
        gp_attackers = gamepress.get(gp_type, [])
        pogo_attackers = pokemongohub.get(pogo_type, [])

        # Get top 5 from each source
        gp_top5 = [a['normalized'] for a in gp_attackers[:5]]
        pogo_top5 = [a['normalized'] for a in pogo_attackers[:5]]

        # Find agreements (in both top 5)
        agreements = []
        for i, gp_name in enumerate(gp_top5):
            if gp_name in pogo_top5:
                gp_rank = i + 1
                pogo_rank = pogo_top5.index(gp_name) + 1
                agreements.append({
                    'name': gp_attackers[i]['name'],
                    'gamepress_rank': gp_rank,
                    'pokemongohub_rank': pogo_rank
                })

        # Find GamePress exclusives (in GP top 5 but not POGO top 5)
        gp_exclusives = []
        for i, gp_name in enumerate(gp_top5):
            if gp_name not in pogo_top5:
                gp_exclusives.append({
                    'name': gp_attackers[i]['name'],
                    'rank': i + 1
                })

        # Find PokemonGOHub exclusives (in POGO top 5 but not GP top 5)
        pogo_exclusives = []
        for i, pogo_name in enumerate(pogo_top5):
            if pogo_name not in gp_top5:
                pogo_exclusives.append({
                    'name': pogo_attackers[i]['name'],
                    'rank': i + 1
                })

        comparison[gp_type] = {
            'agreements': agreements,
            'gamepress_exclusives': gp_exclusives,
            'pokemongohub_exclusives': pogo_exclusives,
            'agreement_percentage': (len(agreements) / 5 * 100) if agreements else 0
        }

    return comparison

def generate_markdown_report(comparison, output_file):
    """Generate a detailed markdown comparison report."""
    lines = [
        "# Raid Attacker Comparison: GamePress vs PokemonGOHub",
        "",
        f"**Date**: 2025-10-12",
        f"**GamePress Source**: Comprehensive DPS/TDO Spreadsheet",
        f"**PokemonGOHub Source**: API (db.pokemongohub.net/api/counters)",
        "",
        "---",
        "",
        "## Summary",
        "",
        "Comparison of top 5 raid attackers per type from both sources.",
        ""
    ]

    # Calculate overall statistics
    total_agreements = sum(len(data['agreements']) for data in comparison.values())
    total_possible = len(comparison) * 5
    overall_agreement = (total_agreements / total_possible * 100)

    lines.extend([
        f"**Overall Agreement**: {total_agreements}/{total_possible} Pokemon ({overall_agreement:.1f}%)",
        "",
        "| Type | Agreement | GP Exclusives | POGO Exclusives |",
        "| ---- | --------- | ------------- | --------------- |"
    ])

    for type_name in sorted(comparison.keys()):
        data = comparison[type_name]
        lines.append(
            f"| **{type_name}** | {len(data['agreements'])}/5 ({data['agreement_percentage']:.0f}%) | "
            f"{len(data['gamepress_exclusives'])} | {len(data['pokemongohub_exclusives'])} |"
        )

    lines.extend([
        "",
        "---",
        "",
        "## Detailed Comparison by Type",
        ""
    ])

    for type_name in sorted(comparison.keys()):
        data = comparison[type_name]

        lines.extend([
            f"### {type_name}",
            ""
        ])

        # Agreements
        if data['agreements']:
            lines.append("**✅ Agreements** (in both top 5):")
            lines.append("")
            for agree in data['agreements']:
                lines.append(
                    f"- **{agree['name']}** - "
                    f"GamePress #{agree['gamepress_rank']}, "
                    f"PokemonGOHub #{agree['pokemongohub_rank']}"
                )
            lines.append("")

        # GamePress exclusives
        if data['gamepress_exclusives']:
            lines.append("**📊 GamePress Exclusives** (in GP top 5, not in POGO top 5):")
            lines.append("")
            for exclusive in data['gamepress_exclusives']:
                lines.append(f"- {exclusive['name']} (GP #{exclusive['rank']})")
            lines.append("")

        # PokemonGOHub exclusives
        if data['pokemongohub_exclusives']:
            lines.append("**🎮 PokemonGOHub Exclusives** (in POGO top 5, not in GP top 5):")
            lines.append("")
            for exclusive in data['pokemongohub_exclusives']:
                lines.append(f"- {exclusive['name']} (POGO #{exclusive['rank']})")
            lines.append("")

        lines.append("---")
        lines.append("")

    # Recommendations
    lines.extend([
        "## Recommendations",
        "",
        "### High Agreement Types (80%+ match)",
        ""
    ])

    high_agreement = [t for t, d in comparison.items() if d['agreement_percentage'] >= 80]
    if high_agreement:
        for type_name in sorted(high_agreement):
            lines.append(f"- **{type_name}**: {comparison[type_name]['agreement_percentage']:.0f}% - Sources agree strongly")
        lines.append("")
        lines.append("**Action**: Current list is well-supported by both sources.")
    else:
        lines.append("_None found_")

    lines.extend([
        "",
        "### Low Agreement Types (<60% match)",
        ""
    ])

    low_agreement = [t for t, d in comparison.items() if d['agreement_percentage'] < 60]
    if low_agreement:
        for type_name in sorted(low_agreement):
            lines.append(f"- **{type_name}**: {comparison[type_name]['agreement_percentage']:.0f}% - Significant differences")
        lines.append("")
        lines.append("**Action**: Review discrepancies and consider updating based on movesets/availability.")
    else:
        lines.append("_None found_")

    lines.extend([
        "",
        "---",
        "",
        "## Methodology",
        "",
        "**GamePress Data**:",
        "- Source: Comprehensive DPS/TDO spreadsheet",
        "- Metric: Raw DPS (Damage Per Second)",
        "- Conditions: Neutral matchup, no weather boost",
        "",
        "**PokemonGOHub Data**:",
        "- Source: API endpoint for type-specific counters",
        "- Metric: Combo DPS (combined fast + charge move)",
        "- Conditions: T5 raid boss simulation, extreme weather",
        "",
        "**Comparison Method**:",
        "- Compare top 5 attackers per type",
        "- Name normalization handles Mega/Shadow/Primal variants",
        "- Agreement = Pokemon appears in both sources' top 5",
        "",
        "---",
        "",
        f"_Report generated: 2025-10-12_"
    ])

    # Write to file
    with open(output_file, 'w') as f:
        f.write('\n'.join(lines))

    print(f"\nComparison report written to: {output_file}")

def main():
    script_dir = Path(__file__).parent
    project_root = script_dir.parent

    # Load data
    print("Loading GamePress data...")
    gamepress_file = project_root / 'meta' / 'raid_attackers_by_type.json'
    gamepress_data = load_gamepress_data(gamepress_file)

    print("Loading PokemonGOHub data...")
    pogo_dir = project_root / 'meta' / 'pokemongohub'
    pokemongohub_data = parse_pokemongohub_data(pogo_dir)

    print("\nComparing sources...")
    comparison = compare_sources(gamepress_data, pokemongohub_data)

    # Generate report
    output_file = project_root / 'meta' / 'RAID_ATTACKER_COMPARISON.md'
    generate_markdown_report(comparison, output_file)

    # Print summary
    print("\n=== SUMMARY ===")
    high_agreement = sum(1 for d in comparison.values() if d['agreement_percentage'] >= 80)
    medium_agreement = sum(1 for d in comparison.values() if 60 <= d['agreement_percentage'] < 80)
    low_agreement = sum(1 for d in comparison.values() if d['agreement_percentage'] < 60)

    print(f"High agreement (80%+): {high_agreement} types")
    print(f"Medium agreement (60-79%): {medium_agreement} types")
    print(f"Low agreement (<60%): {low_agreement} types")

    total_agreements = sum(len(d['agreements']) for d in comparison.values())
    total_possible = len(comparison) * 5
    print(f"\nOverall: {total_agreements}/{total_possible} Pokemon agree ({total_agreements/total_possible*100:.1f}%)")

if __name__ == '__main__':
    main()
