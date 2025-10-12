#!/bin/bash

# Fetch raid attacker data from PokemonGOHub API for all types
# Based on user-provided cURL command

TYPES=("normal" "fighting" "flying" "poison" "ground" "rock" "bug" "ghost" "steel" "fire" "water" "grass" "electric" "psychic" "ice" "dragon" "dark" "fairy")

OUTPUT_DIR="meta/pokemongohub"
mkdir -p "$OUTPUT_DIR"

echo "Fetching PokemonGOHub data for all 18 types..."

for TYPE in "${TYPES[@]}"; do
    echo "Fetching $TYPE type..."

    curl 'https://db.pokemongohub.net/api/counters' \
        -X 'POST' \
        -H 'Content-Type: text/plain;charset=UTF-8' \
        -H 'Accept: */*' \
        -H 'Sec-Fetch-Site: same-origin' \
        -H 'Accept-Language: en-GB,en;q=0.9' \
        -H 'Accept-Encoding: gzip, deflate, br' \
        -H 'Sec-Fetch-Mode: cors' \
        -H 'Origin: https://db.pokemongohub.net' \
        -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0.1 Safari/605.1.15' \
        -H "Referer: https://db.pokemongohub.net/pokemon-list/best-per-type/$TYPE" \
        -H 'Content-Length: 967' \
        -H 'Sec-Fetch-Dest: empty' \
        -H 'Priority: u=3, i' \
        --data-raw "{\"target\":{\"maxCP\":5000,\"atk\":200,\"def\":180,\"sta\":200,\"id\":0,\"name\":\"BOB\",\"pokemonId\":\"BOB\",\"type1\":\"normal\",\"isMythical\":false,\"isLegendary\":false,\"generation\":0,\"candyToEvolve\":0,\"kmBuddyDistance\":0,\"baseCaptureRate\":0,\"baseFleeRate\":0,\"kmDistanceToHatch\":0,\"thirdMoveStardust\":0,\"thirdMoveCandy\":0,\"is_deployable\":false,\"is_transferable\":false,\"isTradable\":false,\"form\":null,\"formId\":\"\",\"template_id\":\"BOB_THE_DEFENDER\",\"isAvailable\":false,\"isHidden\":false,\"disableTransferToPokemonHome\":false,\"isShinyAvailable\":false,\"isDynamaxAvailable\":false,\"dynamaxTier\":0},\"locale\":\"en\",\"targetRaidLevel\":\"5\",\"weather\":\"extreme\",\"responseSize\":400,\"includeShadowPokemon\":true,\"includeMegaPokemon\":true,\"includePrimalPokemon\":true,\"includeUnavailablePokemon\":false,\"allowLegacyMoves\":true,\"rankForType\":\"$TYPE\",\"allowMixedMovesets\":true,\"allowOfftypeAttackers\":true,\"allowedAttackerChargeMoveId\":null,\"allowedAttackerQuickMoveId\":null,\"allowOnlyDynamaxEligiblePokémon\":false}" \
        -o "$OUTPUT_DIR/${TYPE}_response.json" \
        --silent

    if [ $? -eq 0 ]; then
        echo "✓ Saved ${TYPE}_response.json"
    else
        echo "✗ Failed to fetch $TYPE"
    fi

    # Be nice to the server
    sleep 2
done

echo ""
echo "All data fetched! Files saved to $OUTPUT_DIR/"
