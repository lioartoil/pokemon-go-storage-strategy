#!/usr/bin/env python3
"""
Parse comprehensive DPS/TDO data to extract top raid attackers by type.
Source: GamePress Comprehensive DPS Spreadsheet
"""

import csv
import json
from collections import defaultdict
from pathlib import Path

# Pokemon type effectiveness mapping
POKEMON_TYPES = {
    'Normal': ['Slaking', 'Regigigas', 'Snorlax', 'Blissey', 'Chansey', 'Lickilicky', 'Lickitung', 'Ursaluna', 'Ursaring', 'Pidgeot', 'Staraptor', 'Porygon-Z', 'Tauros', 'Kangaskhan', 'Ditto', 'Bewear', 'Zangoose', 'Furfrou', 'Braviary', 'Bouffalant', 'Gumshoos', 'Pyroar', 'Diggersby', 'Bunnelby', 'Purugly', 'Glameow', 'Ambipom', 'Aipom', 'Bibarel', 'Bidoof', 'Castform', 'Chatot', 'Cinccino', 'Dunsparce', 'Exploud', 'Greedent', 'Heliolisk', 'Kecleon', 'Linoone', 'Loudred', 'Meloetta', 'Miltank', 'Minccino', 'Obstagoon', 'Persian', 'Rattata', 'Raticate', 'Regigigas', 'Sawsbuck', 'Sentret', 'Skitty', 'Slakoth', 'Smeargle', 'Spinda', 'Stantler', 'Swellow', 'Taillow', 'Teddiursa', 'Unfezant', 'Vigoroth', 'Watchog', 'Whismur', 'Wigglytuff', 'Yungoos', 'Zangoose', 'Zigzagoon'],
    'Fighting': ['Terrakion', 'Lucario', 'Conkeldurr', 'Machamp', 'Keldeo', 'Pheromosa', 'Blaziken', 'Breloom', 'Hariyama', 'Toxicroak', 'Heracross', 'Sirfetch\'d', 'Zamazenta', 'Urshifu', 'Marshadow', 'Buzzwole', 'Mienshao', 'Infernape', 'Emboar', 'Gallade', 'Poliwrath', 'Primeape', 'Medicham', 'Hitmonchan', 'Hitmonlee', 'Hitmontop', 'Chesnaught', 'Pangoro', 'Hawlucha', 'Throh', 'Sawk', 'Scrafty', 'Cobalion', 'Virizion', 'Kommo-o', 'Hakamo-o'],
    'Flying': ['Rayquaza', 'Moltres', 'Honchkrow', 'Yveltal', 'Staraptor', 'Ho-Oh', 'Lugia', 'Tornadus', 'Pidgeot', 'Unfezant', 'Braviary', 'Skarmory', 'Salamence', 'Dragonite', 'Altaria', 'Charizard', 'Gyarados', 'Aerodactyl', 'Articuno', 'Zapdos', 'Crobat', 'Togekiss', 'Gliscor', 'Landorus', 'Thundurus', 'Noivern', 'Talonflame', 'Corviknight'],
    'Poison': ['Nihilego', 'Roserade', 'Overqwil', 'Gengar', 'Toxtricity', 'Victreebel', 'Vileplume', 'Scolipede', 'Dragalge', 'Drapion', 'Muk', 'Crobat', 'Toxicroak', 'Tentacruel', 'Salazzle', 'Eternatus', 'Naganadel'],
    'Ground': ['Groudon', 'Garchomp', 'Rhyperior', 'Excadrill', 'Landorus', 'Krookodile', 'Mamoswine', 'Donphan', 'Golurk', 'Golem', 'Nidoking', 'Nidoqueen', 'Flygon', 'Rhydon', 'Gliscor', 'Swampert', 'Gastrodon', 'Ting-Lu'],
    'Rock': ['Rampardos', 'Rhyperior', 'Terrakion', 'Tyranitar', 'Gigalith', 'Aerodactyl', 'Golem', 'Regirock', 'Sudowoodo', 'Omastar', 'Armaldo', 'Kabutops', 'Archeops', 'Barbaracle', 'Lycanroc'],
    'Bug': ['Pheromosa', 'Genesect', 'Volcarona', 'Scizor', 'Vikavolt', 'Heracross', 'Yanmega', 'Beedrill', 'Pinsir', 'Scyther', 'Durant', 'Escavalier', 'Accelgor', 'Armaldo', 'Crustle', 'Forretress', 'Shuckle', 'Ledian', 'Ariados'],
    'Ghost': ['Giratina', 'Chandelure', 'Gengar', 'Banette', 'Drifblim', 'Mismagius', 'Sableye', 'Spiritomb', 'Jellicent', 'Cofagrigus', 'Dusknoir', 'Dusclops', 'Trevenant', 'Gourgeist', 'Decidueye', 'Dhelmise', 'Polteageist', 'Cursola', 'Dragapult', 'Spectrier', 'Lunala', 'Marshadow', 'Calyrex', 'Hoopa'],
    'Steel': ['Metagross', 'Dialga', 'Excadrill', 'Scizor', 'Genesect', 'Jirachi', 'Lucario', 'Aggron', 'Empoleon', 'Cobalion', 'Bisharp', 'Heatran', 'Magnezone', 'Steelix', 'Forretress', 'Skarmory', 'Durant', 'Escavalier', 'Ferrothorn', 'Melmetal', 'Zamazenta', 'Registeel', 'Kartana', 'Celesteela', 'Necrozma', 'Solgaleo'],
    'Fire': ['Reshiram', 'Chandelure', 'Blaziken', 'Moltres', 'Charizard', 'Darmanitan', 'Entei', 'Flareon', 'Heatran', 'Infernape', 'Typhlosion', 'Arcanine', 'Magmortar', 'Emboar', 'Delphox', 'Victini', 'Ho-Oh', 'Simisear', 'Rapidash', 'Ninetales', 'Torkoal', 'Houndoom', 'Talonflame', 'Cinderace', 'Incineroar', 'Volcarona', 'Salazzle', 'Blacephalon'],
    'Water': ['Kyogre', 'Swampert', 'Kingler', 'Samurott', 'Feraligatr', 'Blastoise', 'Empoleon', 'Gyarados', 'Greninja', 'Milotic', 'Vaporeon', 'Walrein', 'Clawitzer', 'Seismitoad', 'Primarina', 'Inteleon', 'Gastrodon', 'Azumarill', 'Lapras', 'Suicune', 'Kingdra', 'Starmie', 'Tentacruel', 'Palkia', 'Sharpedo'],
    'Grass': ['Kartana', 'Zarude', 'Roserade', 'Tangrowth', 'Venusaur', 'Sceptile', 'Torterra', 'Leafeon', 'Exeggutor', 'Chesnaught', 'Celebi', 'Shaymin', 'Virizion', 'Breloom', 'Victreebel', 'Vileplume', 'Meganium', 'Serperior', 'Decidueye', 'Tsareena', 'Carnivine', 'Abomasnow', 'Trevenant', 'Dhelmise', 'Rillaboom', 'Calyrex'],
    'Electric': ['Zekrom', 'Electivire', 'Magnezone', 'Luxray', 'Xurkitree', 'Raikou', 'Zapdos', 'Thundurus', 'Jolteon', 'Ampharos', 'Electabuzz', 'Manectric', 'Zebstrika', 'Heliolisk', 'Alolan Golem', 'Electrode', 'Pachirisu', 'Emolga', 'Stunfisk', 'Lanturn', 'Toxtricity', 'Tapu Koko', 'Regieleki', 'Zeraora'],
    'Psychic': ['Mewtwo', 'Espeon', 'Alakazam', 'Latios', 'Latias', 'Metagross', 'Azelf', 'Gallade', 'Exeggutor', 'Gardevoir', 'Bronzong', 'Hypno', 'Jynx', 'Slowbro', 'Slowking', 'Starmie', 'Mr. Mime', 'Wobbuffet', 'Girafarig', 'Grumpig', 'Medicham', 'Lugia', 'Ho-Oh', 'Celebi', 'Jirachi', 'Deoxys', 'Uxie', 'Mesprit', 'Cresselia', 'Victini', 'Reuniclus', 'Gothitelle', 'Necrozma', 'Lunala', 'Solgaleo', 'Tapu Lele', 'Calyrex', 'Hoopa'],
    'Ice': ['Mamoswine', 'Glaceon', 'Weavile', 'Kyurem', 'Avalugg', 'Abomasnow', 'Walrein', 'Jynx', 'Cloyster', 'Piloswine', 'Lapras', 'Articuno', 'Regice', 'Glalie', 'Froslass', 'Beartic', 'Cryogonal', 'Vanilluxe', 'Aurorus', 'Alolan Ninetales', 'Alolan Sandslash', 'Galarian Darmanitan', 'Galarian Mr. Mime', 'Eiscue', 'Arctovish', 'Arctozolt', 'Glastrier', 'Calyrex', 'Baxcalibur', 'Chien-Pao'],
    'Dragon': ['Rayquaza', 'Palkia', 'Salamence', 'Dragonite', 'Dialga', 'Garchomp', 'Zekrom', 'Reshiram', 'Kyurem', 'Latios', 'Latias', 'Haxorus', 'Kingdra', 'Flygon', 'Altaria', 'Dragapult', 'Hydreigon', 'Duraludon', 'Eternatus', 'Regidrago', 'Giratina', 'Naganadel', 'Ultra Necrozma'],
    'Dark': ['Darkrai', 'Tyranitar', 'Weavile', 'Hydreigon', 'Honchkrow', 'Houndoom', 'Absol', 'Sharpedo', 'Bisharp', 'Zoroark', 'Krookodile', 'Sableye', 'Mightyena', 'Cacturne', 'Crawdaunt', 'Spiritomb', 'Drapion', 'Scrafty', 'Alolan Muk', 'Alolan Raticate', 'Alolan Persian', 'Grimmsnarl', 'Obstagoon', 'Pangoro', 'Yveltal', 'Guzzlord', 'Hoopa', 'Zarude'],
    'Fairy': ['Togekiss', 'Gardevoir', 'Primarina', 'Granbull', 'Xerneas', 'Sylveon', 'Clefable', 'Wigglytuff', 'Azumarill', 'Florges', 'Aromatisse', 'Slurpuff', 'Mr. Mime', 'Rapidash', 'Alolan Ninetales', 'Grimmsnarl', 'Alcremie', 'Tapu Koko', 'Tapu Lele', 'Tapu Bulu', 'Tapu Fini', 'Zacian', 'Zamazenta', 'Enamorus']
}

def normalize_pokemon_name(name):
    """Normalize Pokemon name for comparison."""
    # Remove parenthetical forms for type matching
    base_name = name.split(' (')[0]
    # Handle Mega/Shadow/Primal prefixes
    for prefix in ['Mega ', 'Shadow ', 'Primal ']:
        if base_name.startswith(prefix):
            base_name = base_name[len(prefix):]
    # Handle special cases
    if base_name.startswith('Alolan '):
        base_name = base_name[7:]
    if base_name.startswith('Galarian '):
        base_name = base_name[9:]
    if base_name.startswith('Hisuian '):
        base_name = base_name[8:]
    if base_name.startswith('Paldean '):
        base_name = base_name[8:]
    return base_name

def get_pokemon_types(pokemon_name):
    """Determine which type(s) a Pokemon belongs to based on name."""
    normalized = normalize_pokemon_name(pokemon_name)
    types = []

    for type_name, pokemon_list in POKEMON_TYPES.items():
        if normalized in pokemon_list or any(p.startswith(normalized) for p in pokemon_list):
            types.append(type_name)

    # Special handling for dual-type Pokemon that can be used for either type
    # This is based on their attacking type, not defensive typing
    return types

def parse_dps_csv(csv_path):
    """Parse the comprehensive DPS CSV and extract top attackers by type."""
    type_attackers = defaultdict(list)

    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)

        for row in reader:
            pokemon = row['Pokemon']
            fast_move = row['Fast Move']
            charged_move = row['Charged Move']
            dps = float(row['DPS'])
            tdo = float(row['TDO'])
            er = float(row['ER'])

            # Determine attack type based on moves
            # We'll categorize by the Pokemon's primary attack type
            pokemon_types = get_pokemon_types(pokemon)

            if not pokemon_types:
                continue

            for ptype in pokemon_types:
                # Store unique Pokemon (not every moveset)
                existing = [p['name'] for p in type_attackers[ptype]]
                if pokemon not in existing:
                    type_attackers[ptype].append({
                        'name': pokemon,
                        'fast_move': fast_move,
                        'charged_move': charged_move,
                        'dps': dps,
                        'tdo': tdo,
                        'er': er
                    })

    # Sort each type by DPS and take top 10
    for ptype in type_attackers:
        type_attackers[ptype] = sorted(
            type_attackers[ptype],
            key=lambda x: x['dps'],
            reverse=True
        )[:10]

    return type_attackers

def main():
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    csv_path = project_root / 'meta' / 'comprehensive_dps.csv'
    output_path = project_root / 'meta' / 'raid_attackers_by_type.json'

    print(f"Parsing DPS data from: {csv_path}")
    type_attackers = parse_dps_csv(csv_path)

    # Create output structure
    output = {
        'last_updated': '2025-10-12',
        'source': 'GamePress Comprehensive DPS/TDO Spreadsheet',
        'types': {}
    }

    for ptype in sorted(type_attackers.keys()):
        output['types'][ptype] = {
            'top_attackers': [
                {
                    'rank': i + 1,
                    'pokemon': attacker['name'],
                    'dps': attacker['dps'],
                    'tdo': attacker['tdo'],
                    'er': attacker['er']
                }
                for i, attacker in enumerate(type_attackers[ptype])
            ]
        }

    # Write JSON output
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2)

    print(f"\nExtracted top 10 attackers for {len(output['types'])} types")
    print(f"Output written to: {output_path}")

    # Print summary
    print("\n=== Summary ===")
    for ptype in sorted(output['types'].keys()):
        attackers = output['types'][ptype]['top_attackers']
        top_3 = [a['pokemon'] for a in attackers[:3]]
        print(f"{ptype:12} - {', '.join(top_3)}")

if __name__ == '__main__':
    main()
