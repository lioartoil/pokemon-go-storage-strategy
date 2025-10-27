# CLAUDE.md

> **Project Context** | Pokemon GO Storage Management System | Updated: 2025-10-14

## Project Overview

This is a comprehensive Pokemon GO storage management system designed to optimize storage for 10,184 Pokemon across 10,500 slots (~3% free). The project includes:

- **Storage Strategy**: 13-category system (#1a, #1b, #2-#13) with detailed retention rules
- **PokeGenie Integration**: 15 Name Generators aligned with Favorite groups ₁-₉
- **Tag System**: 43 tags (86% capacity) for workflow management
- **Documentation**: Complete strategy docs, implementation guides, and quick reference materials
- **Meta Tracking**: PvP rankings, raid attackers, and meta shift monitoring

**User Profile**: Collecting > Raids > Trading >>> PvP (minimal)

## Repository Structure

```
pokemon/
├── README.md                           # Main entry point & project overview
├── POKEGENIE_NAMING.md                 # PokeGenie Name Generator specs (352 lines)
├── STORAGE_STRATEGY_CORRECTED.md      # Core 13-category strategy (486 lines)
├── SUMMARY.md                          # Tag reorganization summary
├── docs/
│   ├── strategies/                     # Storage strategies
│   │   ├── STRATEGY_MODERATE_PVP.md   # Active strategy (moderate approach)
│   │   ├── STRATEGY_REVISIONS_FINAL.md # Alternative (aggressive collector)
│   │   └── STRATEGY_ANALYSIS.md       # Strategy comparison
│   ├── guides/                         # Implementation guides
│   │   ├── PHASE_1_IMPLEMENTATION.md  # Master League reduction (300-400 slots)
│   │   ├── META_UPDATE_GUIDE.md       # PvP meta tracking workflow
│   │   ├── RAID_META_UPDATE_GUIDE.md  # Raid attacker updates
│   │   └── META_SHIFT_IMPACT.md       # Recent meta changes
│   └── reference/                      # Quick reference docs
│       ├── TAG_SYSTEM.md              # 43-tag system documentation
│       ├── STORAGE_QUICK_REFERENCE.md # Daily decision flowchart
│       └── FAVORITE_QUERIES.md        # 40 saved search queries
├── meta/                               # Meta data files
│   ├── cp10000_all_overall_rankings.csv # PvPoke Master League rankings
│   ├── raid_attackers_by_type.json
│   └── pokemongohub/                  # API responses
├── leagues/                            # Generation-specific PvP tracking
└── scripts/                            # Python automation scripts
```

## Recent Work (2025-10-14)

### Session Summary (Latest: Raid Attacker Analysis)

Completed comprehensive raid attacker retention analysis and documentation:

1. **Raid Attacker Analysis**: Analyzed 100+ raid attackers across 18 types to determine exact retention counts (1-12 range)
2. **RAID_ATTACKER_COUNTS.md**: Created 534-line reference document with detailed recommendations per Pokemon
3. **Key Determinations**: Mega Rayquaza (12), Shadow Mewtwo (12), Rayquaza (12), Mewtwo (10-12), Terrakion (8-10), Deoxys Attack (3-4), Mega Beedrill (1-2)
4. **Phase 1 Updates**: Added Deoxys exception, updated references, fixed cSpell warnings

### Earlier Work (2025-10-14)

Completed category renumbering restructure and PokeGenie naming format corrections:

1. **Category Restructure**: Merged Categories #1 (Great/Ultra League) and #2 (Little League) into #1a and #1b subcategories, renumbered all subsequent categories (#3→#2, #4→#3, etc., #14→#13)
2. **PokeGenie Format Corrections**: Applied extensive format and symbol corrections across 15 Name Generators
3. **Documentation Updates**: Updated both POKEGENIE_NAMING.md and STORAGE_STRATEGY_CORRECTED.md for consistency
4. **Raid Attacker Query**: Created comprehensive query string for tagging raid/gym attackers to prevent accidental transfers

### Key Technical Decisions

**Category Numbering (#1a/#1b Structure)**:
- **Rationale**: Categories #1 and #2 both used PokeGenie Favorite ₁ and identical PvP IV ranking format
- **Solution**: Made them subcategories (#1a = Great/Ultra League, #1b = Little League)
- **Benefit**: Perfect 1:1 alignment between Favorite groups (₁-₉) and category numbers (#1a/#1b, #2-#9)

**PokeGenie Format Standardization**:
- All Favorite ₂ generators (High IV, Dynamax, Gigantamax) use identical format: `₂{Stage}{●/○}{Name}{Rank}{IV}{Lvl}{Atk}{Atk2}{Leg}`
- Rank field ALWAYS filled with rank number (auto-conditions: Pokemon's rank; manual: Master League rank)
- Shadow/XXS/XXL formats simplified to match Shiny/Costume patterns
- Level format uses `②`, `⑮`, `⑳` for whole levels and `②½`, `⑮½`, `⑳½` for half-levels

**Symbol Standardization**:
- Added `ⓛ` for Little League (was missing)
- Added `Ⓜ` (Mega) and `Ⓟ` (Primal) evolution stages
- Removed unused symbols: `⊖`, `⊕`, `•` (Default)
- Fixed Costume prefix: `₃` → `₄`

**Raid Attacker Count Methodology**:
- **Performance-based**: DPS, TDO, Estimator Rating (ER) from GamePress data
- **Type coverage**: Single-type vs dual-type attackers (dual-type = higher value)
- **Rarity tiers**: Giovanni-only (12), Legendaries (6-12), Ultra Beasts (6-8), Common (1-6)
- **Raid frequency**: Type usage frequency in meta (Dragon/Fighting = high, Bug/Normal = low)
- **Accessibility**: Common spawns vs event-exclusive vs trade-evolution
- **Special exceptions**: Glass cannons (lower counts), extremely accessible (minimal counts)

### Implementation Details

**Category Mapping** (Favorite → Category alignment):

| Favorite | Prefix | Categories | Description |
|----------|--------|------------|-------------|
| (none) | ⇄ | #10-13 | Transfer/Trade queue (default) |
| ₁ | ₁ | #1a, #1b | PvP IV (GL/UL/LL) |
| ₂ | ₂ | #2, Manual | Master League + High IV override |
| ₃ | ₃ | #3 | Shiny Pokemon |
| ₄ | ₄ | #4 | Costumed Pokemon |
| ₅ | ₅ | #5 | Shadow Pokemon |
| ₆ | ₆ | #6 | XXS/XXL size extremes |
| ₇ | ₇ | #7 | Background Pokemon |
| ₈ | ₈ | #8 | Dynamax Pokemon |
| ₉ | ₉ | #9 | Gigantamax Pokemon |

**Evolution Stage Symbols**: Ⓑ (Baby), ⓪ (Basic), ① (Stage 1), ② (Stage 2), Ⓜ (Mega), Ⓟ (Primal)

**League Symbols**: Ⓖ (Great ≤1500), Ⓤ (Ultra ≤2500), ⓛ (Little ≤500), (none) = Master (unlimited)

**Shadow/Purified**: ● (Shadow), ○ (Purified)

**Raid Attacker Query** (102+ species to exclude from transfers):
```
regigigas,staraptor,lucario,blaziken,machamp,rayquaza,salamence,honchkrow,moltres,gengar,toxicroak,roserade,groudon,garchomp,excadrill,rhyperior,landorus,rampardos,tyranitar,terrakion,heracross,pheromosa,beedrill,volcarona,scizor,chandelure,giratina,metagross,dialga,darmanitan,reshiram,kyogre,palkia,swampert,sceptile,kartana,tangrowth,venusaur,electivire,xurkitree,raikou,zekrom,zapdos,magnezone,mewtwo,alakazam,deoxys,latios,espeon,mamoswine,weavile,kyurem,glaceon,dragonite,yveltal,hoopa,hydreigon,gardevoir,xerneas,togekiss,primarina,granbull
```

### Current State

**Completed Today (2025-10-14)**:
- [x] Category renumbering (#1→#1a/#1b, renumber #3-14)
- [x] PokeGenie format corrections (15 generators documented)
- [x] Symbol legend cleanup and standardization
- [x] Documentation updates (POKEGENIE_NAMING.md, STORAGE_STRATEGY_CORRECTED.md)
- [x] Raid attacker exclusion query created
- [x] **Raid attacker analysis** (100+ Pokemon across 18 types)
- [x] **RAID_ATTACKER_COUNTS.md created** (534 lines, exact counts 1-12)
- [x] **Phase 1 guide updated** (Deoxys exception added)
- [x] **cSpell fixes** (formes, Eeveelution, Entei, Therian)
- [x] Git commits (7 commits on 2025-10-14)

**Next Actions**:
- [ ] **Configure 6 new PokeGenie generators** (#9-14: Shadow, XXS/XXL, Background, Dynamax, Gigantamax, Transfer)
- [ ] Test PokeGenie naming with sample Pokemon
- [ ] Begin Phase 1 implementation (Master League reduction)

### Next Session Priorities

1. **Configure PokeGenie Generators** (30-45 min)
   - Add 6 new generators (#9-14) in PokeGenie app
   - Verify generator order matches priority (Trade at top, Transfer at bottom)
   - Test with sample Pokemon to verify naming formats

2. **Tag Raid Attackers** (15 min)
   - Use raid attacker query in Pokemon GO
   - Tag all results with `#Attackers`
   - Verify no false positives

3. **Begin Phase 1: Master League Reduction** (Week 1)
   - Reference: `docs/guides/PHASE_1_IMPLEMENTATION.md`
   - Scan all Master League Pokemon with PokeGenie
   - Transfer Rank 21+ final evolutions (exclude #Attackers)
   - Target: Free 300-400 slots

### Important Files/Locations

**Core Documentation**:
- `POKEGENIE_NAMING.md` - Complete Name Generator specs (15 generators, 352 lines)
- `STORAGE_STRATEGY_CORRECTED.md` - 13-category retention rules (486 lines)
- `README.md` - Project overview and quick start guide
- `docs/guides/PHASE_1_IMPLEMENTATION.md` - Step-by-step ML reduction guide

**Reference Materials**:
- `docs/reference/TAG_SYSTEM.md` - 43-tag system documentation
- `docs/reference/FAVORITE_QUERIES.md` - 40 saved search queries
- `docs/reference/STORAGE_QUICK_REFERENCE.md` - Daily decision flowchart
- `docs/reference/RAID_ATTACKER_COUNTS.md` - **NEW**: Exact retention counts per attacker (534 lines)

**Meta Data**:
- `meta/cp10000_all_overall_rankings.csv` - PvPoke Master League top 200
- `meta/raid_attackers_by_type.json` - GamePress raid attacker data

### Git Status

**Branch**: develop (main branch)
**Clean working tree**: Yes (all changes committed)
**Recent commits** (2025-10-14, 7 total today):
1. `ef27250` - fix(cspell): add Pokemon-related terms to dictionary
2. `b59ac9e` - docs(raid): add comprehensive raid attacker retention counts reference
3. `e4c2b6d` - fix(cspell): add 'formes' to dictionary
4. `9f280be` - docs(phase1): add Deoxys (Attack) exception to raid attacker list
5. `2abed9d` - Add comprehensive session handoff to CLAUDE.md
6. `b02bf69` - Fix High IV format: rank field always filled with rank number
7. `8e5a847` - Fix High IV format and add Mega/Primal evolution stages

### Questions/Considerations

**PokeGenie Generator Setup**:
- Verify generator priority order (default at top, Favorite-specific below)
- Confirm "Has 2nd move" condition works as expected for High IV (2) generator
- Test if Favorite assignments auto-apply correctly

**Phase 1 Implementation Safety**:
- Double-check raid attacker query catches all important species
- Consider creating backup tag `#BeforePhase1` before transfers
- Confirm transfer candidates aren't tagged with `#Kept`, `#Attackers`, or high PvP ranks

**Raid Attacker Retention Questions**:
- Is RAID_ATTACKER_COUNTS.md too long at 534 lines? (Decision: No, appropriate for comprehensive reference)
- Should we create a condensed quick-reference version? (Not needed - users can Ctrl+F)
- Exact counts determined for key attackers:
  - Mega Rayquaza: 12 (dominates Dragon + Flying, ER: 81.15)
  - Shadow Mewtwo: 12 (Giovanni-only, dominates Psychic, ER: 63.29)
  - Rayquaza: 12 (Rank #2 in Dragon + Flying, ER: 59.08)
  - Mewtwo: 10-12 (excellent backup, accessible legendary)
  - Terrakion: 8-10 (Fighting #8 / Rock #5, dual coverage)
  - Deoxys (Attack): 3-4 (glass cannon, TDO: 171.8)
  - Mega Beedrill: 1-2 (Weedle common, cheapest Mega)

**Future Considerations**:
- Create one-page PokeGenie Quick Reference Card for daily use
- Monitor if moderate strategy provides enough free space (target: 9-12%)
- Reassess if need to switch to aggressive strategy after Phase 1

### Storage Metrics

**Current**: 10,184 / 10,500 Pokemon (316 free, ~3%)
**Target**: 9,200-9,600 Pokemon (900-1,300 free, ~9-12%)
**Phase 1 Goal**: Free 300-400 slots (Master League reduction)
**Phase 2 Goal**: Free 600-900 slots (Great/Ultra/Little League reduction)

### Key Constraints

- PokeGenie Favorite limit: 10 groups (₀-₉)
- PokeGenie tag limit: 50 tags (43 used, 7 free)
- Pokemon GO name limit: 12 characters (all formats comply)
- User priority: Collecting > Raids > Trading >>> PvP (minimal)

---

## Session Notes

**Session Focus**: Raid Attacker Retention Analysis

**Key Accomplishments**:
- Analyzed 100+ raid attackers across all 18 types
- Created comprehensive retention guide (RAID_ATTACKER_COUNTS.md, 534 lines)
- Determined exact counts for each attacker based on performance, rarity, type coverage
- Updated Phase 1 guide with Deoxys exception and reference links
- Fixed all cSpell warnings

**Methodology Applied**:
- Performance metrics: DPS, TDO, Estimator Rating from GamePress
- Type coverage weighting: Dual-type attackers valued higher
- Rarity tiers: Giovanni-only (12), Legendaries (6-12), Commons (1-6)
- Raid frequency: Adjusted for type usage in meta
- Special cases: Glass cannons (lower), Extremely accessible (minimal)

**Key Insights**:
- Mega Rayquaza dominates 2 types with massive ER gap (81.15 vs next at ~60)
- Shadow Mewtwo is irreplaceable (Giovanni-only, ER: 63.29)
- Deoxys Attack is glass cannon exception (TDO: 171.8, keep only 3-4)
- Mega Beedrill is budget option (Weedle common, keep only 1-2)
- Dual-type coverage significantly increases retention value

---

_Session handoff updated: 2025-10-14 22:30 PST_
