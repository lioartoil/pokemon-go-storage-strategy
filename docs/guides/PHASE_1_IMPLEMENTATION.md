# Phase 1 Implementation Guide - Master League Reduction

**Date**: 2025-10-12
**Strategy**: Moderate PvP Approach (STRATEGY_MODERATE_PVP.md)
**Target**: Free 376-476 slots (Week 1)

---

## Overview

Phase 1 focuses on quick wins to immediately free storage space with minimal effort. This phase targets:

1. Master League PvP reduction (300-400 slots)
2. Transfer Queue clearance (76 slots)

**Total Expected**: 376-476 slots freed

---

## Priority 1: Master League PvP Reduction

**Current Status**: 2,037 Pokemon in Master League category
**Target**: 1,400-1,700 Pokemon (reduce by 300-400)

### Retention Rules (Moderate Approach)

| Pokemon Type        | Rank Range | Action                          |
| ------------------- | ---------- | ------------------------------- |
| Final Evolution     | Rank 21+   | **TRANSFER**                    |
| Final Evolution     | Rank 11-20 | Keep 1 copy                     |
| Final Evolution     | Rank ≤10   | Keep 2 copies                   |
| Non-Final Evolution | Any        | Keep 2 copies (future-proofing) |

### Step-by-Step Process

#### Step 1: Identify Transfer Candidates (Rank 21+)

**⚠️ CRITICAL: Exclusions First!**

Before transferring ANY Pokemon, exclude these categories:

1. **Other League Tags**: `!great&!ultra&!little` (already useful elsewhere)
2. **Raid/Gym Tags**: `!raid&!gym` (if you use these tags)
3. **Legendaries/Mythicals**: `!legendary&!mythical&!ultra beasts` (always keep, expensive to get)
4. **Shadows**: `!shadow` (valuable for raids even with bad PvP IVs)
5. **Special Moves**: `!@special` (legacy moves are irreplaceable)

**Search Query**:

```
4*&!lucky&!shiny&!costume&!shadow&!@special&!legendary&!mythical&!ultra beasts&!great&!ultra&!little
```

**What this finds**: Non-legendary, non-shadow, regular Pokemon with 4★ IVs that aren't already tagged for other leagues.

**Then manually filter for**:

1. **Master League eligible** (CP > 2500 capable when maxed)
2. **Final evolutions only** (keep 2 of non-final evolutions for future-proofing)
3. **Check PokeGenie**: ML Rank 21+ = _Candidate_ for transfer
4. **Double-check NOT a raid attacker** (see exclusion list below)

#### Step 1.5: Raid/Gym Attacker Exclusion List

**⚠️ NEVER TRANSFER THESE** (even if ML Rank 21+, they're valuable for raids):

**For exact recommended counts per attacker, see**: `docs/reference/RAID_ATTACKER_COUNTS.md`

**Top Priority Raid Attackers** (keep 6-12 each unless noted\*, verified 2025-10-14):

- **Normal**: Shadow Regigigas, Shadow Staraptor, Regigigas
- **Fighting**: Mega Lucario, Mega Blaziken, Lucario, Terrakion, Shadow Machamp
- **Flying**: Mega Rayquaza, Rayquaza, Shadow Salamence, Shadow Honchkrow, Shadow Moltres
- **Poison**: Mega Gengar, Shadow Gengar, Gengar, Shadow Toxicroak, Roserade
- **Ground**: Primal Groudon, Mega Garchomp, Shadow Groudon, Shadow Garchomp, Shadow Excadrill, Shadow Rhyperior, Landorus
- **Rock**: Shadow Rampardos, Shadow Tyranitar, Mega Tyranitar, Terrakion, Rampardos
- **Bug**: Mega Heracross, Pheromosa, Mega Beedrill, Volcarona, Shadow Scizor
- **Ghost**: Mega Gengar, Shadow Chandelure, Shadow Gengar, Chandelure, Giratina
- **Steel**: Mega Lucario, Shadow Metagross, Shadow Excadrill, Mega Metagross, Metagross, Dialga
- **Fire**: Mega Blaziken, Shadow Chandelure, Shadow Darmanitan, Reshiram, Shadow Moltres, Blaziken
- **Water**: Primal Kyogre, Shadow Kyogre, Palkia (Origin), Mega Swampert, Shadow Swampert, Kyogre
- **Grass**: Mega Sceptile, Kartana, Shadow Sceptile, Shadow Tangrowth, Shadow Venusaur, Roserade
- **Electric**: Shadow Electivire, Xurkitree, Shadow Raikou, Zekrom, Shadow Zapdos, Shadow Magnezone, Electivire
- **Psychic**: Shadow Mewtwo, Mega Alakazam, Mewtwo, Deoxys (Attack: 3-4 only\*), Shadow Metagross, Shadow Latios, Espeon, Alakazam
- **Ice**: **Kyurem (White/Black): 10-12 each\*\***, Shadow Mamoswine, Shadow Weavile, Kyurem (regular), Mamoswine, Weavile, Glaceon
- **Dragon**: Mega Rayquaza, Rayquaza, Shadow Salamence, Mega Garchomp, Shadow Dragonite, Shadow Garchomp, Palkia, Salamence, Dragonite, Dialga
- **Dark**: Shadow Honchkrow, Shadow Tyranitar, Yveltal, Hoopa (Unbound), Tyranitar, Shadow Weavile, Hydreigon
- **Fairy**: Mega Gardevoir, Shadow Gardevoir, Xerneas, Gardevoir, Togekiss, Primarina, Granbull

**\*Exception**: Deoxys (Attack Forme) is a glass cannon with extremely low bulk (TDO: 171.8). Keep only 3-4 copies instead of 6-12. Other Deoxys formes (Normal, Defense, Speed) are not top raid attackers - only keep for PvP if needed.

**\*\*Ice Exception**: Kyurem (White) and Kyurem (Black) are the #1 and #2 Ice-type raid attackers (DPS: 30.6 and 27.2 respectively), significantly outperforming Shadow Mamoswine. Keep 10-12 copies of each forme. Regular Kyurem is weaker (DPS: 18.9), keep only 6-8.

**Master League Top 20 Meta** (also exclude):

- Top 20 from `meta/cp10000_all_overall_rankings.csv`: Zacian, Palkia (Origin), Zamazenta, Dialga (Origin), Kyurem (White), Zekrom, Kyurem (Black), Reshiram, Florges, Lugia, Metagross, Necrozma (Dawn Wings), Eternatus, Palkia (Shadow), Lunala, Ho-Oh, Groudon, Necrozma (Dusk Mane), Dialga (Shadow), Latios (Shadow)

**Example SAFE Transfers** (Non-legendary, Non-raid-meta, ML Rank 21+):

- Snorlax (ML Rank 135+, niche raid use only)
- Slaking (ML Rank 380, very niche)
- Gyarados (ML Rank 47-50, borderline - check if you need water attackers)
- Hippowdon (ML Rank 78+, niche)
- Ursaluna (ML Rank 74+, but check if useful for ground raids)

**Note**: This requires PokeGenie scanning AND manual verification against raid attacker list. When in doubt, KEEP IT!

#### Step 2: Reduce Rank 11-20 Copies

For Rank 11-20 final evolutions, keep only 1 copy (transfer extras).

**How to identify**:

1. Use PokeGenie to see Master League ranks
2. Filter for Pokemon with Rank 11-20
3. If you have multiple copies, keep the best one
4. Transfer duplicates

#### Step 3: Reduce Rank ≤10 Copies

For Rank ≤10 final evolutions, reduce from 3 → 2 copies.

**How to identify**:

1. Use PokeGenie to see Master League ranks
2. Filter for Pokemon with Rank ≤10
3. If you have 3+ copies, keep best 2
4. Transfer extras

#### Step 4: Non-Final Evolution Check

Keep 2 copies of non-final evolutions (e.g., Dragonair, Zweilous).

**Why**: Future evolution releases or move updates might make them relevant.

### Expected Results

- **300-400 Pokemon transferred**
- **Storage freed**: 300-400 slots
- **Time required**: 2-4 hours (requires manual PokeGenie scanning)

---

## Priority 2: Clear Transfer Queue

**Current Status**: 76 Pokemon tagged `home` (transfer queue)
**Target**: 0 Pokemon (clear all during 2× candy event)

### When to Transfer

Wait for 2× Transfer Candy event (typically monthly). This maximizes candy gains.

**Upcoming Events**: Check in-game news for next 2× candy event.

### Transfer Process

1. **Filter by Tag**: Use in-game search `home`
2. **Mass Transfer**: Select all, transfer during event
3. **Remove Tag**: Clear `home` tag system after transfer

### Expected Results

- **76 Pokemon transferred**
- **Storage freed**: 76 slots
- **Time required**: 5-10 minutes (during event)
- **Bonus**: +152 candy (with 2× event)

---

## Phase 1 Summary

| Priority  | Category                    | Expected Savings  | Time Required |
| --------- | --------------------------- | ----------------- | ------------- |
| 1         | Master League (Rank 21+)    | 300-400 slots     | 2-4 hours     |
| 2         | Transfer Queue (`home` tag) | 76 slots          | 5-10 minutes  |
| **TOTAL** | **Phase 1**                 | **376-476 slots** | **2-5 hours** |

**Storage After Phase 1**: 9,708-9,808 / 10,500 (692-792 free, ~7-8%)

---

## Tools Required

1. **PokeGenie** - For Master League IV rank checking
2. **In-game Tags** - For transfer queue management
3. **Spreadsheet** (optional) - For tracking what to transfer

---

## Safety Checks

Before transferring ANY Pokemon, verify:

- ✅ **Not tagged**: `great`, `ultra`, `little`, `keep`, `transfer`, `raid`, `power`, `tm`
- ✅ **Not special**: Not shiny, costume, shadow, XXS, XXL, special background
- ✅ **Not legendary/mythical**: Not rare Pokemon
- ✅ **Not @special**: Doesn't have legacy/special moves
- ✅ **Not favorite**: Not starred in-game

**ALWAYS double-check before mass transfer!**

---

## Common Mistakes to Avoid

- ❌ **DON'T** transfer Pokemon with special moves (@special)
- ❌ **DON'T** transfer shadows (even if rank 21+, keep for raids)
- ❌ **DON'T** transfer legendaries/mythicals without careful review
- ❌ **DON'T** transfer during non-event times (miss 2× candy)
- ❌ **DON'T** rush - take time to verify each batch

---

## Progress Tracking

Use this checklist to track your progress:

### Week 1 Checklist

- [ ] Day 1-2: Scan all Master League Pokemon with PokeGenie
- [ ] Day 3-4: Transfer Rank 21+ final evolutions (300-400 Pokemon)
- [ ] Day 5-6: Reduce Rank 11-20 to 1 copy each
- [ ] Day 7: Reduce Rank ≤10 to 2 copies each
- [ ] Wait for 2× candy event: Clear `home` tag transfers (76 Pokemon)

### Success Metrics

After completing Phase 1, you should have:

- ✅ 692-792 free slots (~7-8%)
- ✅ All Master League Pokemon at proper copy counts
- ✅ Transfer queue cleared
- ✅ Ready for Phase 2 (Great/Ultra/Little League reduction)

---

## Next Steps

Once Phase 1 is complete:

1. **Monitor free space** for 1 week
2. **Proceed to Phase 2** (STRATEGY_MODERATE_PVP.md - Priority 3 & 4)
3. **Reassess strategy** if free space drops below 7% (735 slots)

---

## Need Help?

**Reference Documents**:

- `STRATEGY_MODERATE_PVP.md` - Full moderate strategy
- `SEARCH_QUERIES.md` - All query strings
- `META_UPDATE_GUIDE.md` - Meta data information

**Key Insight**: Phase 1 is the EASIEST phase because Master League is your lowest priority. This gives immediate relief without touching your core collecting categories.

---

_Phase 1 Implementation Guide - Created 2025-10-12_
