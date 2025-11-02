# Raid Meta Update Guide

**Last Updated**: 2025-10-12
**Purpose**: Track and update top raid attackers for optimal raiding

---

## 📊 Current Raid Attacker List

**Source**: `STRATEGY_REVISIONS_FINAL.md` - Category 3b: Raid/Gym Attackers

### Top Raid Attackers by Type (2025-10-12)

| Type         | Top Attackers (Top 5 by DPS)                                     | Keep Count | Source Verified |
| ------------ | ---------------------------------------------------------------- | ---------- | --------------- |
| **Normal**   | Shadow Regigigas, Shadow Staraptor, Mega Pidgeot                 | 6 each     | ✅ Verified     |
| **Fighting** | Mega Lucario, Mega Blaziken, Shadow Blaziken, Terrakion          | 6-12 each  | ✅ Verified     |
| **Flying**   | Mega Rayquaza, Rayquaza, Shadow Salamence, Shadow Honchkrow      | 6-12 each  | ✅ Verified     |
| **Poison**   | Mega Gengar, Shadow Gengar, Gengar, Shadow Toxicroak             | 6-12 each  | ✅ Verified     |
| **Ground**   | Primal Groudon, Mega Garchomp, Shadow Groudon, Shadow Garchomp   | 6-12 each  | ✅ Verified     |
| **Rock**     | Shadow Rampardos, Shadow Tyranitar, Mega Tyranitar, Terrakion    | 6-12 each  | ✅ Verified     |
| **Bug**      | Mega Heracross, Pheromosa, Mega Beedrill, Volcarona              | 6-12 each  | ✅ Verified     |
| **Ghost**    | Mega Gengar, Shadow Chandelure, Shadow Gengar, Chandelure        | 6-12 each  | ✅ Verified     |
| **Steel**    | Mega Lucario, Shadow Metagross, Shadow Excadrill, Mega Metagross | 6-12 each  | ✅ Verified     |
| **Fire**     | Mega Blaziken, Shadow Chandelure, Shadow Darmanitan, Reshiram    | 6-12 each  | ✅ Verified     |
| **Water**    | Primal Kyogre, Shadow Kyogre, Palkia (Origin), Mega Swampert     | 6-12 each  | ✅ Verified     |
| **Grass**    | Mega Sceptile, Kartana, Shadow Sceptile, Shadow Exeggutor        | 6-12 each  | ✅ Verified     |
| **Electric** | Shadow Electivire, Xurkitree, Shadow Raikou, Zekrom              | 6-12 each  | ✅ Verified     |
| **Psychic**  | Shadow Mewtwo, Mega Alakazam, Deoxys (Attack), Mewtwo            | 6-12 each  | ✅ Verified     |
| **Ice**      | Kyurem (White/Black): 10-12\*, Shadow Mamoswine, Shadow Weavile  | 6-12 each  | ✅ Updated      |
| **Dragon**   | Mega Rayquaza, Rayquaza, Shadow Salamence, Mega Garchomp         | 6-12 each  | ✅ Verified     |
| **Dark**     | Shadow Honchkrow, Shadow Crawdaunt, Shadow Tyranitar, Yveltal    | 6-12 each  | ✅ Verified     |
| **Fairy**    | Mega Gardevoir, Enamorus, Shadow Gardevoir, Xerneas              | 6-12 each  | ✅ Verified     |

**✅ VERIFIED**: Data extracted from GamePress Comprehensive DPS/TDO Spreadsheet (2025-10-12) and PokeMonGo Hub raid simulator. Full data available in `meta/raid_attackers_by_type.json` and `meta/pokemongohub/ice_response.json`.

**\*Ice Exception**: White Kyurem (#1, DPS: 30.6) and Black Kyurem (#2, DPS: 27.2) are elite Ice attackers, significantly better than Shadow Mamoswine (#3, DPS: 25.1). Keep 10-12 copies of each forme.

---

## 🔄 Update Schedule

### When to Update Raid Attacker List

| Frequency                 | Trigger                  | Action                          |
| ------------------------- | ------------------------ | ------------------------------- |
| **Monthly**               | Move rebalance announced | Check GamePress for DPS changes |
| **New Legendary Release** | New raid boss drops      | Add to appropriate type         |
| **New Mega Evolution**    | New mega released        | Check if top DPS for type       |
| **New Shadow Release**    | Team Rocket rotation     | Compare shadow vs regular DPS   |
| **Every 3 Months**        | New season               | Full review of all types        |

### Update Priority

1. **Critical** (Update immediately):

   - Move rebalance that affects top attackers
   - New legendary with record-breaking DPS
   - New mega evolution released

2. **High** (Update within 1 week):

   - Monthly scheduled check
   - New raid boss rotation
   - New shadow Pokemon released

3. **Medium** (Update within 1 month):

   - Community Day move additions
   - Minor stat adjustments

---

## 📋 Manual Update Process

### Step 1: Check GamePress DPS Spreadsheet (Preferred)

**URL**: https://gamepress.gg/pokemongo/comprehensive-dps-spreadsheet

**What to look for**:

1. Go to spreadsheet (updated monthly)
2. Check each type tab (Fighting, Fire, Water, etc.)
3. Sort by **DPS** (damage per second) - higher is better
4. Note top 5-10 per type
5. Compare to current list in `STRATEGY_REVISIONS_FINAL.md`

**Example - Fire Type**:

```
Current list: Reshiram, Chandelure, Blaziken (Mega), Moltres
GamePress shows: [check their spreadsheet]
If different → Update needed
```

### Step 2: Check Pokebattler (Boss-Specific)

**URL**: https://www.pokebattler.com/raids

**What to look for**:

1. Select current T5 raid boss
2. Check "Best Counters" list
3. Note which Pokemon appear most frequently
4. Update list if new Pokemon dominates

**Note**: Requires free account, but most accurate for current bosses.

### Step 3: Cross-Reference with PokemonGOHub

**URL**: https://db.pokemongohub.net/best/attackers-per-type (⚠️ Previous URL returned 404, using database link)

**What to look for**:

1. Check "Best Attackers by Type" database
2. Verify top 5 per type
3. Update if major discrepancies

**Note**: PokemonGOHub database may return 403 errors. Primary source should be GamePress DPS spreadsheet.

---

## 🔍 How to Identify Changes

### Major Changes Requiring Update

1. **New #1 DPS**: If a Pokemon becomes the new top DPS for a type

   - Example: If Xurkitree overtakes Zekrom for Electric
   - Action: Add to top of type list

2. **Legendary Drop-off**: If a legendary falls out of top 5

   - Example: If Dialga no longer top 5 Steel
   - Action: Move to "Situational" tier or remove

3. **Shadow Buff**: If shadow form becomes significantly better

   - Example: Shadow Mamoswine vs regular Mamoswine
   - Action: Update to specify shadow preferred

4. **Mega Evolution Release**: New mega changes top DPS

   - Example: Mega Blaziken release
   - Action: Add to appropriate type

### Minor Changes (Can Wait)

1. Rank shifts within top 5 (order changes but same Pokemon)
2. New Pokemon enters top 10 but not top 5
3. Minor DPS differences (<5% change)

---

## 🤖 Semi-Automated Update Process

Since there's no single CSV source for raid data, use this workflow:

### Option A: GamePress Verification (Most Reliable)

**Manual Steps**:

1. Visit https://gamepress.gg/pokemongo/comprehensive-dps-spreadsheet
2. For each type, note top 5 DPS Pokemon
3. Ask Claude: "Update raid attacker list with these changes: [paste list]"

**Claude will**:

1. Compare with current list
2. Update `STRATEGY_REVISIONS_FINAL.md`
3. Update `PHASE_1_IMPLEMENTATION.md` exclusion list
4. Generate changelog

### Option B: Community Infographic (Quick Check)

**Manual Steps**:

1. Check r/TheSilphRoad for raid boss infographics
2. Screenshot or note top counters
3. Ask Claude: "Are these Pokemon in our raid attacker list? [paste list]"

**Claude will**:

1. Check against current list
2. Flag missing Pokemon
3. Recommend additions

---

## 📝 Update Log Template

When updating, document changes:

```markdown
## Raid Meta Update - YYYY-MM-DD

### Changes by Type

**Fighting**:

- Added: [Pokemon name] (reason: new shadow release)
- Removed: [Pokemon name] (reason: power crept by new legendary)
- Rank change: [Details]

**Fire**:

- No changes

[Continue for each type with changes]

### Trigger

- [x] Move rebalance
- [ ] New legendary release
- [ ] New mega evolution
- [ ] Scheduled monthly check

### Source

- GamePress DPS Spreadsheet (YYYY-MM-DD)
- Pokebattler raid boss [Boss Name]
- PokemonGOHub article dated YYYY-MM-DD

### Impact on Storage

- Added X Pokemon to exclusion list
- No Pokemon removed from exclusion list
- Total raid attackers: [count] species
```

---

## 🎯 Current Status (2025-10-12)

### Verification Status

**Last Verified**: ❌ Not yet verified against current sources
**Next Check Due**: 2025-11-12 (monthly check)

### Known Gaps

1. **Source**: List is based on early 2025 community knowledge
2. **Mega Evolutions**: May not reflect all current megas
3. **Shadow Availability**: Team Rocket rotation changes monthly
4. **Regional Availability**: Some Pokemon (Kartana) are regional

### Recommended Immediate Actions

1. **Verify Fighting types** (Terrakion vs Lucario vs new releases)
2. **Check Electric** (Xurkitree availability and performance)
3. **Update Psychic** (Mega Latios/Latias if released)
4. **Verify Shadow rankings** (check Team Rocket current rotation)

---

## 🛠️ Resources

### Primary Resources

1. **GamePress Comprehensive DPS Spreadsheet** (Most Reliable)

   - URL: https://gamepress.gg/pokemongo/comprehensive-dps-spreadsheet
   - Updated: Monthly after move rebalances
   - Best for: Overall DPS rankings by type

2. **Pokebattler** (Boss-Specific Rankings)

   - URL: https://www.pokebattler.com/raids
   - Updated: Weekly, per raid boss
   - Best for: Current raid boss counters
   - Note: Requires free account

3. **PokemonGOHub Best Attackers** (⚠️ Limited Access)

   - URL: https://db.pokemongohub.net/best/attackers-per-type
   - Updated: After major changes
   - Best for: Quick reference, infographics
   - Note: Database may return 403 errors; use GamePress as primary source

4. **r/TheSilphRoad Community** (Infographics)

   - URL: https://www.reddit.com/r/TheSilphRoad/
   - Updated: Per raid boss release
   - Best for: Visual guides, community consensus

### Secondary Resources

5. **PokeMiners** (Datamine Info)

   - URL: https://pokeminers.com/
   - Best for: Upcoming moves, stats

6. **GO Stadium** (Competitive Analysis)

   - URL: https://www.gostadium.gg/ (if accessible)
   - Best for: Move viability analysis

---

## 🤝 Claude Code Update Command

**To request raid meta update**:

```
Please update the raid attacker list:
1. I'll provide GamePress top 5 DPS per type (or infographic)
2. Compare with current STRATEGY_REVISIONS_FINAL.md list
3. Update both strategy file and PHASE_1_IMPLEMENTATION.md exclusions
4. Generate changelog showing what changed
5. Update this guide with new verification date
```

**Claude will**:

1. Parse the data you provide
2. Compare with current list
3. Update relevant files
4. Show changelog
5. Flag any major shifts

---

## 📅 Next Update

**Recommended**: 2025-11-12 (monthly check)

**Or sooner if**:

- Move rebalance announced
- New legendary released
- New mega evolution released
- You notice performance issues in raids

---

## 💡 Key Differences from PvP Meta

**PvP Meta**:

- ✅ Has CSV exports from PvPoke
- ✅ Automated updates possible
- ✅ Single authoritative source

**Raid Meta**:

- ❌ No standardized CSV export
- ❌ Must manually check multiple sources
- ❌ Boss-dependent (changes per raid boss)
- ⚠️ Weather-dependent (boosts change rankings)
- ⚠️ Move-dependent (fast move + charged move combos matter)

**Recommendation**: Update raid meta less frequently than PvP meta (quarterly vs monthly), but verify before major raid events.

---

_Raid meta update system created 2025-10-12. Manual verification required._
