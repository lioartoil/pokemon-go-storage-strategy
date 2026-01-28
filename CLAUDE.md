# CLAUDE.md

> **Project Context** | Pokemon GO Storage Management System | Updated: 2026-01-18

## Project Overview

This is a comprehensive Pokemon GO storage management system designed to optimize storage for 11,021 Pokemon across 11,325 slots (~2.7% free). The project includes:

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

## Recent Work (2026-01-18)

### Session Summary: Quick Win Storage Optimization & Query Testing

**Major Achievement**: Created comprehensive quick-win storage optimization strategy with tested search queries.

1. **New Strategy Documents Created**:
   - `QUICK_WIN_STRATEGY.md` - Collector-first approach with 10 prioritized quick wins
   - `MASTER_LEAGUE_CHECKLIST.md` - Detailed step-by-step Master League reduction guide
   - `OTHER_QUICK_WINS.md` - Analysis of all quick-win categories beyond Master League
   - `ACTION_PLAN_2026-01-18.md` - Command center with timeline and quick reference

2. **Search Query Development & Testing**:
   - Built complete search queries excluding ALL 14 protected categories
   - Tested queries against actual collection - most returned 0 results (well-organized collection)
   - Implemented two-step process: Step 1 (find unreviewed) → Step 2 (find transfer candidates)
   - Critical syntax corrections: `#` prefix for tags, comma precedence over `&`, league filtering

3. **RAID_ATTACKER_COUNTS.md Updated**:
   - Added Heatran (6 count) and Shadow Heatran (6-8 count) - released December 2025
   - Updated Quick Reference Table and Fire/Steel type sections

4. **Git Commits** (11 commits this session):
   - `b9fdabb` - docs(raid): add Heatran and Shadow Heatran to raid attacker lists
   - `0d718bd` - docs: clarify two-step process for all league priorities
   - `fcc23bc` - docs: use evolve keyword for non-final evolution query
   - `4d1d7fd` - docs: enhance Priority 6 queries with full exclusions
   - `401558c` - docs: clarify costume retention rule as 2 per costume
   - `4114e9c` - docs: expand transfer candidate query and duplicate guidance
   - `f35de9a` - docs: add league exclusions to transfer candidate query
   - `4fc8d36` - docs: add guidance for when unreviewed query returns 0 results
   - `94c9617` - docs: add rank tag exclusions to search queries
   - `2660433` - docs: add complete category exclusions to search queries
   - `5f66a37` - docs: replace species meta ranking with IV rank approach

### Key Technical Learnings (2026-01-18)

**Pokemon GO Search Syntax**:
- Comma (`,`) has HIGHER precedence than ampersand (`&`)
- Tags need `#` prefix: `!#rank1` not `!rank1`
- Reserved keywords: `lucky`, `shiny`, `shadow`, `costume`, `xxs`, `xxl`, `background`, `gigantamax`, `dynamax`, `evolve`, `baby`

**Tagging System Clarification**:
- `home` tag = Category 12 (Transfer Queue) - NOT the same as `transfer`
- `transfer` tag = Category 14 (Lucky Queue)
- No `master` tag exists

**Two-Step Query Process**:
- **Step 1 (Find Unreviewed)**: Excludes ALL rank tags (`!#rank1&!#rank2&!#rank3&!#rank4-20&!#rank21-50&!#rank51-100`)
- **Step 2 (Find Transfer Candidates)**: Includes rank tags for Rank 21+ (`#rank21-50,#rank51-100`)

**Well-Organized Collection Finding**:
- User's collection returned 0 results for most queries
- Indicates excellent organization - all Pokemon already reviewed/tagged
- This is GOOD - means systematic approach is working

### Earlier Work (2025-11-02): Kyurem Formes & Fusion Mechanics

**Critical Discovery**: White Kyurem and Black Kyurem were missing from raid attacker documentation.

1. **Kyurem Formes Added**: Identified and documented missing elite Ice attackers
   - **White Kyurem**: #1 Ice attacker (DPS: 30.6, TDO: 733.5) → 10-12 copies
   - **Black Kyurem**: #2 Ice attacker (DPS: 27.2, TDO: 652.0) → 10-12 copies
   - Regular Kyurem: Downgraded from 8 to 6-8 copies (formes are superior)

2. **Fusion Mechanics Research**: NO buddy walking for fusion energy (event-locked, ~10 raids per forme)

### Earlier Work (2025-10-14): Raid Attacker Analysis & Category Restructure

1. **Raid Attacker Analysis**: Analyzed 100+ raid attackers across 18 types (retention counts 1-12)
2. **Category Restructure**: Merged #1/#2 into #1a/#1b subcategories, renumbered #3-14

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

**Kyurem Fusion Mechanics** (NEW 2025-11-02):
- **Fusion Energy NOT available from buddy walking** (unlike Mega/Primal Energy)
- White Kyurem requires: 1,000 Blaze Fusion Energy + 30 Kyurem Candy + 30 Reshiram Candy
- Black Kyurem requires: 1,000 Volt Fusion Energy + 30 Kyurem Candy + 30 Zekrom Candy
- Energy sources: Raids (~100/raid), Special Research (50), Promo codes only
- Fusions are **permanent** and **multiple allowed** (unlike Megas/Primals)
- **Accessibility concern**: Event-locked, requires ~10 raids per forme to obtain 1,000 energy
- **Data sources**: GamePress (raid_attackers_by_type.json) + PokeMonGo Hub (pokemongohub/ice_response.json)

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

**Raid Attacker Queries** (to exclude from transfers):

**Non-Shadow Query** (55 species):
```
!shadow&(rayquaza,mewtwo,groudon,kyogre,kyurem,terrakion,reshiram,zekrom,xerneas,yveltal,hoopa,heracross,pheromosa,tyranitar,garchomp,blaziken,gengar,sceptile,kartana,lucario,metagross,gardevoir,mamoswine,weavile,glaceon,landorus,xurkitree,electivire,rampardos,swampert,volcarona,roserade,chandelure,espeon,alakazam,togekiss,primarina,granbull,hydreigon,salamence,dragonite,palkia,dialga,heatran,regigigas,staraptor,pinsir,deoxys,beedrill,scizor,necrozma,lunala,blacephalon)
```

**Shadow Query** (37 species):
```
shadow&(mewtwo,salamence,dragonite,tyranitar,heatran,groudon,kyogre,garchomp,blaziken,chandelure,gengar,mamoswine,weavile,honchkrow,rampardos,rhyperior,electivire,raikou,zapdos,magnezone,moltres,darmanitan,machamp,excadrill,swampert,venusaur,tangrowth,scizor,alakazam,granbull,regigigas,staraptor,toxicroak,latios,metagross,gardevoir,sceptile)
```

### Current State

**Completed (2026-01-18)**:
- [x] Created `QUICK_WIN_STRATEGY.md` - Collector-first approach with 10 prioritized quick wins
- [x] Created `MASTER_LEAGUE_CHECKLIST.md` - Detailed step-by-step guide
- [x] Created `OTHER_QUICK_WINS.md` - Analysis of all quick-win categories
- [x] Created `ACTION_PLAN_2026-01-18.md` - Command center with timeline
- [x] Tested all queries against actual collection (most returned 0 - well-organized)
- [x] Added Heatran and Shadow Heatran to RAID_ATTACKER_COUNTS.md
- [x] 11 git commits documenting all changes

**Query Testing Results** (2026-01-18):
- Master League: 0 unreviewed, 20 tagged Rank 21+ (all best specimens - no transfers)
- Lucky: 92 Pokemon, no duplicates
- Costume: 720 Pokemon, no 3+ duplicates
- Priority 6a (evolve): 0 results
- Priority 6b (baby): 0 results
- Great League Step 1: 68 Pokemon found, none eligible, all now tagged
- Ultra League Step 1: 0 results

**In Progress**:
- [ ] **Tag all raid attackers with `#Attackers`** using the complete query (64 species)
- [ ] Run `#Attackers` count to compare against recommended totals
- [ ] Continue testing Priority 7-10 based on cleanup potential

### Next Session Priorities

1. **Tag All Raid Attackers** (IMMEDIATE)
   - Run complete query (64 species including Heatran):
   ```
   regigigas,staraptor,lucario,blaziken,machamp,rayquaza,salamence,honchkrow,moltres,gengar,toxicroak,roserade,groudon,garchomp,excadrill,rhyperior,landorus,rampardos,tyranitar,terrakion,heracross,pheromosa,beedrill,volcarona,scizor,chandelure,giratina,metagross,dialga,darmanitan,reshiram,kyogre,palkia,swampert,sceptile,kartana,tangrowth,venusaur,electivire,xurkitree,raikou,zekrom,zapdos,magnezone,mewtwo,alakazam,deoxys,latios,espeon,mamoswine,weavile,kyurem,glaceon,dragonite,yveltal,hoopa,hydreigon,gardevoir,xerneas,togekiss,primarina,granbull,heatran,pinsir
   ```
   - Tag all results with `#Attackers`

2. **Determine Next Quick Win by Cleanup Yield**
   - User's collection is well-organized; most categories have 0 transfer candidates
   - Need to identify which categories actually have cleanup potential
   - Run counts on remaining categories (Raid Attacker Excess, etc.)

3. **Decision Pending: Prioritization Method**
   - Current: Fixed priority order (ML > GL > UL > LL > Raid Attackers)
   - Alternative: Prioritize by cleanup yield (whichever category removes most Pokemon)
   - For minimal PvP player, all league categories have equal low priority

### Important Files/Locations

**Quick Win Strategy (NEW 2026-01-18)**:
- `QUICK_WIN_STRATEGY.md` - Collector-first approach with 10 prioritized quick wins
- `MASTER_LEAGUE_CHECKLIST.md` - Detailed step-by-step Master League reduction guide
- `OTHER_QUICK_WINS.md` - Analysis of all quick-win categories beyond Master League
- `ACTION_PLAN_2026-01-18.md` - Command center with timeline and quick reference

**Core Documentation**:
- `POKEGENIE_NAMING.md` - Complete Name Generator specs (15 generators, 352 lines)
- `STORAGE_STRATEGY_CORRECTED.md` - 13-category retention rules (486 lines)
- `docs/strategies/STRATEGY_REVISIONS_FINAL.md` - Aggressive collector strategy (source of retention rules)
- `docs/guides/PHASE_1_IMPLEMENTATION.md` - Step-by-step ML reduction guide

**Reference Materials**:
- `docs/reference/TAG_SYSTEM.md` - 43-tag system documentation
- `docs/reference/FAVORITE_QUERIES.md` - 40 saved search queries
- `docs/reference/STORAGE_QUICK_REFERENCE.md` - Daily decision flowchart
- `docs/reference/RAID_ATTACKER_COUNTS.md` - Exact retention counts per attacker (updated with Heatran)

**Meta Data**:
- `meta/cp10000_all_overall_rankings.csv` - PvPoke Master League top 200
- `meta/raid_attackers_by_type.json` - GamePress raid attacker data

### Git Status

**Branch**: develop (main branch)
**Clean working tree**: Yes (all changes committed)
**Recent commits** (most recent first):
1. `b9fdabb` (2026-01-18) - docs(raid): add Heatran and Shadow Heatran to raid attacker lists
2. `0d718bd` (2026-01-18) - docs: clarify two-step process for all league priorities
3. `fcc23bc` (2026-01-18) - docs: use evolve keyword for non-final evolution query
4. `4d1d7fd` (2026-01-18) - docs: enhance Priority 6 queries with full exclusions
5. `401558c` (2026-01-18) - docs: clarify costume retention rule as 2 per costume
6. `4114e9c` (2026-01-18) - docs: expand transfer candidate query and duplicate guidance
7. `f35de9a` (2026-01-18) - docs: add league exclusions to transfer candidate query
8. `4fc8d36` (2026-01-18) - docs: add guidance for when unreviewed query returns 0 results
9. `94c9617` (2026-01-18) - docs: add rank tag exclusions to search queries
10. `2660433` (2026-01-18) - docs: add complete category exclusions to search queries
11. `5f66a37` (2026-01-18) - docs: replace species meta ranking with IV rank approach

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
  - **Kyurem (White)**: 10-12 (Ice #1, DPS: 30.6, 62% better than Shadow Mamoswine)
  - **Kyurem (Black)**: 10-12 (Ice #2, DPS: 27.2, excellent)
  - Mewtwo: 10-12 (excellent backup, accessible legendary)
  - Terrakion: 8-10 (Fighting #8 / Rock #5, dual coverage)
  - Kyurem (regular): 6-8 (downgraded since formes are superior)
  - Deoxys (Attack): 3-4 (glass cannon, TDO: 171.8)
  - Mega Beedrill: 1-2 (Weedle common, cheapest Mega)

**Kyurem Forme Accessibility Consideration**:
- **Question**: Should 10-12 count be adjusted given fusion energy limitations?
- **Current stance**: Keep 10-12 for players willing to invest in raids (elite performance justifies effort)
- **Alternative**: Could lower to 6-8 due to event-locked accessibility (~10 raids per forme required)
- **Decision pending**: User preference needed on accessibility vs performance tradeoff

**Future Considerations**:
- Create one-page PokeGenie Quick Reference Card for daily use
- Monitor if moderate strategy provides enough free space (target: 9-12%)
- Reassess if need to switch to aggressive strategy after Phase 1

### Storage Metrics

**Current**: 11,021 / 11,325 Pokemon (304 free, ~2.7%)
**Target**: 9,627 Pokemon (1,698 free, ~15%)
**Phase 1 Finding**: Master League returned 0 transfer candidates (collection well-organized)
**Challenge**: Most quick-win categories returning 0 results - need to find alternative cleanup sources

### Key Constraints

- PokeGenie Favorite limit: 10 groups (₀-₉)
- PokeGenie tag limit: 50 tags (43 used, 7 free)
- Pokemon GO name limit: 12 characters (all formats comply)
- User priority: Collecting > Raids > Trading >>> PvP (minimal)

---

## Session Notes

**Current Session (2026-01-18)**: Quick Win Storage Optimization & Query Testing

**Session Goal**: Optimize storage for Community Day/event play style with target 15% free space (1,698 slots).

**Key Findings**:
1. **Well-Organized Collection**: Most queries returned 0 results - user's collection is already well-organized
2. **No Easy Transfer Candidates**: Master League (0), Great League (0 eligible), Ultra League (0), Priority 6a/6b (0)
3. **Complete Queries Built**: All search queries now exclude ALL 14 protected categories correctly

**Critical Syntax Corrections Made**:
- Tags need `#` prefix: `!#rank1` not `!rank1`
- Comma has higher precedence than `&` in Pokemon GO search
- Must exclude ALL protected categories including `gigantamax`, `dynamax` (separate from `background`)

**Files Created This Session**:
1. `QUICK_WIN_STRATEGY.md` - Main strategy document
2. `MASTER_LEAGUE_CHECKLIST.md` - Step-by-step checklist
3. `OTHER_QUICK_WINS.md` - Analysis of all categories
4. `ACTION_PLAN_2026-01-18.md` - Command center

**Files Modified**:
- `docs/reference/RAID_ATTACKER_COUNTS.md` - Added Heatran, Shadow Heatran, Dawn Wings Necrozma, Dusk Mane Necrozma, Lunala, Blacephalon

**Raid Attacker Queries** (updated 2026-01-28):

**Non-Shadow Query** (55 species):
```
!shadow&(rayquaza,mewtwo,groudon,kyogre,kyurem,terrakion,reshiram,zekrom,xerneas,yveltal,hoopa,heracross,pheromosa,tyranitar,garchomp,blaziken,gengar,sceptile,kartana,lucario,metagross,gardevoir,mamoswine,weavile,glaceon,landorus,xurkitree,electivire,rampardos,swampert,volcarona,roserade,chandelure,espeon,alakazam,togekiss,primarina,granbull,hydreigon,salamence,dragonite,palkia,dialga,heatran,regigigas,staraptor,pinsir,deoxys,beedrill,scizor,necrozma,lunala,blacephalon)
```

**Shadow Query** (37 species):
```
shadow&(mewtwo,salamence,dragonite,tyranitar,heatran,groudon,kyogre,garchomp,blaziken,chandelure,gengar,mamoswine,weavile,honchkrow,rampardos,rhyperior,electivire,raikou,zapdos,magnezone,moltres,darmanitan,machamp,excadrill,swampert,venusaur,tangrowth,scizor,alakazam,granbull,regigigas,staraptor,toxicroak,latios,metagross,gardevoir,sceptile)
```

**Immediate Next Action**: Tag all raid attackers with `#Attackers` using both queries above.

**Changes Made (2026-01-28)**:
- Added Dawn Wings Necrozma, Dusk Mane Necrozma (10-12 count each)
- Added Lunala, Blacephalon (6-8 count each)
- Removed Giratina (Ghost #16, not a top attacker)
- Split into separate non-shadow and shadow queries

---

_Session handoff updated: 2026-01-28_
