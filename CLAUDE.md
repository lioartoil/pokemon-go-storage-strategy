# CLAUDE.md

> **Project Context** | Pokemon GO Storage Management System | Updated: 2026-02-06

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
├── README.md                            # Main entry point & project overview
├── POKEGENIE_NAMING.md                  # PokeGenie Name Generator specs (352 lines)
├── STORAGE_STRATEGY_CORRECTED.md        # Core 13-category strategy (486 lines)
├── SUMMARY.md                           # Tag reorganization summary
├── docs/
│   ├── strategies/                      # Storage strategies
│   │   ├── STRATEGY_MODERATE_PVP.md     # Active strategy (moderate approach)
│   │   ├── STRATEGY_REVISIONS_FINAL.md  # Alternative (aggressive collector)
│   │   └── STRATEGY_ANALYSIS.md         # Strategy comparison
│   ├── guides/                          # Implementation guides
│   │   ├── PHASE_1_IMPLEMENTATION.md    # Master League reduction (300-400 slots)
│   │   ├── META_UPDATE_GUIDE.md         # PvP meta tracking workflow
│   │   ├── RAID_META_UPDATE_GUIDE.md    # Raid attacker updates
│   │   └── META_SHIFT_IMPACT.md         # Recent meta changes
│   └── reference/                       # Quick reference docs
│       ├── TAG_SYSTEM.md                # 43-tag system documentation
│       ├── STORAGE_QUICK_REFERENCE.md   # Daily decision flowchart
│       └── FAVORITE_QUERIES.md          # 40 saved search queries
├── meta/                                # Meta data files
│   ├── cp10000_all_overall_rankings.csv # PvPoke Master League rankings
│   ├── raid_attackers_by_type.json
│   └── pokemongohub/                    # API responses
├── leagues/                             # Generation-specific PvP tracking
└── scripts/                             # Python automation scripts
```

## Recent Work (2026-02-06)

### Session Summary: Comprehensive Raid Attacker Re-Audit

**Major Achievement**: Deep re-audit found 11 additional missing attackers (mostly 2025 GO Fest/event releases), updated ranking corrections across 9 type sections, expanded queries from 53→60 non-shadow and 37→41 shadow species. Deferred tier methodology recalibration to separate issue.

### Earlier (2026-01-28): Initial Raid Attacker Audit & Query Split

**Achievement**: Initial audit added 4 missing attackers (Necrozma formes, Lunala, Blacephalon), removed Giratina, split query into non-shadow/shadow.

1. **Missing Attackers Identified & Added** (via web research):
   - **Dawn Wings Necrozma** (Ghost #1, 10-12 count) - legendary fusion, dominates Ghost type
   - **Dusk Mane Necrozma** (Steel #1, 10-12 count) - dethroned Metagross as #1 Steel
   - **Lunala** (Ghost #7, S-tier, 6-8 count) - excellent TDO
   - **Blacephalon** (Fire/Ghost Ultra Beast, 6-8 count) - glass cannon

2. **Giratina Removed**:
   - Research showed Giratina Origin is Ghost #16 (A+ tier, DPS: 14.6)
   - Outclassed by Mega Gengar, Shadow Chandelure, Shadow Gengar, Dawn Wings Necrozma
   - Was in old query but NOT in RAID_ATTACKER_COUNTS.md - discrepancy resolved

3. **Query Split** (non-shadow vs shadow):
   - Non-Shadow: 55 species (was 64 combined, now includes necrozma, lunala, blacephalon)
   - Shadow: 37 species (unchanged from previous)
   - Removed giratina from both

4. **NOT Added** (verified via research):
   - Solgaleo - F-Tier (no Steel fast move, terrible for raids)
   - Necrozma base form - not a top attacker on its own

5. **Files Updated**:
   - `docs/reference/RAID_ATTACKER_COUNTS.md` - Quick Ref Table, Ghost/Steel/Fire sections, Tier summaries, footer
   - `CLAUDE.md` - Replaced single query with two separate queries
   - `MASTER_LEAGUE_CHECKLIST.md` - Updated raid attacker tagging section

6. **Git Commits** (this session):
   - `f906eec` - docs(raid): add Necrozma formes, Lunala, Blacephalon to raid attackers
   - `33e7f00` - docs: update session handoff with 2026-01-18 quick win strategy work

### Earlier Work (2026-01-18): Quick Win Storage Optimization & Query Testing

1. **New Strategy Documents Created**: QUICK_WIN_STRATEGY.md, MASTER_LEAGUE_CHECKLIST.md, OTHER_QUICK_WINS.md, ACTION_PLAN_2026-01-18.md
2. **Search Query Development**: Built complete queries excluding ALL 14 protected categories, tested against collection
3. **RAID_ATTACKER_COUNTS.md**: Added Heatran (6) and Shadow Heatran (6-8)
4. **11 Git Commits**: b9fdabb through 5f66a37

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

| Favorite | Prefix | Categories | Description                      |
| -------- | ------ | ---------- | -------------------------------- |
| (none)   | ⇄      | #10-13     | Transfer/Trade queue (default)   |
| ₁        | ₁      | #1a, #1b   | PvP IV (GL/UL/LL)                |
| ₂        | ₂      | #2, Manual | Master League + High IV override |
| ₃        | ₃      | #3         | Shiny Pokemon                    |
| ₄        | ₄      | #4         | Costumed Pokemon                 |
| ₅        | ₅      | #5         | Shadow Pokemon                   |
| ₆        | ₆      | #6         | XXS/XXL size extremes            |
| ₇        | ₇      | #7         | Background Pokemon               |
| ₈        | ₈      | #8         | Dynamax Pokemon                  |
| ₉        | ₉      | #9         | Gigantamax Pokemon               |

**Evolution Stage Symbols**: Ⓑ (Baby), ⓪ (Basic), ① (Stage 1), ② (Stage 2), Ⓜ (Mega), Ⓟ (Primal)

**League Symbols**: Ⓖ (Great ≤1500), Ⓤ (Ultra ≤2500), ⓛ (Little ≤500), (none) = Master (unlimited)

**Shadow/Purified**: ● (Shadow), ○ (Purified)

**Raid Attacker Queries** (to exclude from transfers):

**Non-Shadow Query** (59 species):

```
!shadow&(rayquaza,mewtwo,groudon,kyogre,kyurem,terrakion,reshiram,zekrom,xerneas,yveltal,hoopa,heracross,pheromosa,tyranitar,garchomp,blaziken,gengar,sceptile,kartana,lucario,metagross,gardevoir,mamoswine,weavile,glaceon,landorus,xurkitree,electivire,rampardos,swampert,volcarona,roserade,chandelure,espeon,alakazam,togekiss,primarina,granbull,hydreigon,salamence,dragonite,palkia,dialga,heatran,regigigas,staraptor,pinsir,deoxys,beedrill,necrozma,lunala,blacephalon,zacian,zamazenta,eternatus,keldeo,regieleki,diancie,charizard)
```

**Shadow Query** (40 species):

```
shadow&(mewtwo,salamence,dragonite,tyranitar,heatran,groudon,kyogre,garchomp,blaziken,chandelure,gengar,mamoswine,weavile,honchkrow,rampardos,rhyperior,electivire,raikou,zapdos,magnezone,moltres,darmanitan,machamp,excadrill,swampert,venusaur,tangrowth,scizor,alakazam,granbull,regigigas,staraptor,toxicroak,latios,metagross,gardevoir,darkrai,conkeldurr,dialga,palkia)
```

### Current State

**Completed (2026-02-06)**:

- [x] Comprehensive re-audit found 11 additional missing attackers (2025 releases)
- [x] Added Crowned Sword Zacian (Steel #1), Crowned Shield Zamazenta (Steel #2)
- [x] Added Eternatus (Dragon #1, Poison #1, 1 per account)
- [x] Added Keldeo Resolute (Fighting #3, 1-2 per account)
- [x] Added Regieleki (Electric #2), Mega Diancie (Rock #1), Mega Charizard Y (Fire #2)
- [x] Added Shadow Darkrai, Shadow Conkeldurr, Shadow Dialga, Shadow Palkia to shadow query
- [x] Updated ranking corrections in Steel/Dragon/Poison/Electric/Fighting/Fairy/Rock/Dark/Fire sections
- [x] Rechecked attacker criteria methodology — tier mapping has inconsistencies (deferred to separate issue)
- [x] Updated queries: non-shadow 53→60 species, shadow 37→41 species
- [x] Validated queries via `scripts/validate_raid_queries.py`: removed scizor (non-shadow, Bug #25), sceptile (shadow, Grass #11); added Shadow Gardevoir to table (Fairy #4); final: 59 non-shadow, 40 shadow

**Completed (2026-01-28)**:

- [x] Initial audit added 4 attackers (Necrozma formes, Lunala, Blacephalon)
- [x] Removed Giratina (Ghost #16, outclassed)
- [x] Split raid attacker query into non-shadow and shadow

**Completed (2026-01-18)**:

- [x] Created 4 strategy documents (QUICK_WIN_STRATEGY, MASTER_LEAGUE_CHECKLIST, OTHER_QUICK_WINS, ACTION_PLAN)
- [x] Tested all queries against actual collection (most returned 0 - well-organized)
- [x] Added Heatran and Shadow Heatran to RAID_ATTACKER_COUNTS.md

**In Progress**:

- [ ] **Tag all raid attackers with `#Attackers`** using both queries (non-shadow + shadow)
- [ ] Run `#Attackers` count to compare against recommended totals
- [ ] Continue testing Priority 7-10 based on cleanup potential

**Deferred (Separate Issue)**:

- [ ] **Tier methodology recalibration** - [GitHub Issue #1](https://github.com/lioartoil/pokemon-go-storage-strategy/issues/1) - Define explicit ER thresholds, resolve rank-to-count inversions, reduce 6/6-8 plateau

### Next Session Priorities

1. **Tag All Raid Attackers** (IMMEDIATE)
   - Run non-shadow query (60 species) and shadow query (41 species) separately
   - See "Raid Attacker Queries" section above for exact queries
   - Tag all results with `#Attackers`

2. **Determine Next Quick Win by Cleanup Yield**
   - User's collection is well-organized; most categories have 0 transfer candidates
   - Need to identify which categories actually have cleanup potential

3. **Decision Pending: Prioritization Method**
   - Current: Fixed priority order (ML > GL > UL > LL > Raid Attackers)
   - Alternative: Prioritize by cleanup yield (whichever category removes most Pokemon)

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
- `docs/reference/RAID_ATTACKER_COUNTS.md` - Exact retention counts per attacker (updated 2026-02-06 with Zacian/Zamazenta, Eternatus, Keldeo, Regieleki, +more)

**Meta Data**:

- `meta/cp10000_all_overall_rankings.csv` - PvPoke Master League top 200
- `meta/raid_attackers_by_type.json` - GamePress raid attacker data

**Automation Scripts**:

- `scripts/validate_raid_queries.py` - Validates queries and audits freshness
- `scripts/fetch_pokemongohub.py` - Refreshes PokemonGOHub API cache (Playwright)

### Git Status

**Branch**: develop (main branch)
**Clean working tree**: Yes (all changes committed)
**GitHub Issues**: [#1](https://github.com/lioartoil/pokemon-go-storage-strategy/issues/1) - Recalibrate raid attacker count tier methodology
**Recent commits** (most recent first):

1. `d43c84f` (2026-02-06) - docs(raid): add 11 missing raid attackers from 2025 releases
2. `a7719de` (2026-02-06) - docs: update session handoff with 2026-01-28 raid attacker audit
3. `f906eec` (2026-01-28) - docs(raid): add Necrozma formes, Lunala, Blacephalon to raid attackers
4. `33e7f00` (2026-01-28) - docs: update session handoff with 2026-01-18 quick win strategy work
5. `b9fdabb` (2026-01-18) - docs(raid): add Heatran and Shadow Heatran to raid attacker lists

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

**Current Session (2026-02-06)**: Comprehensive Raid Attacker Re-Audit

**Session Goal**: Justify attacker criteria methodology and verify completeness of raid attacker lists.

**Key Findings**:

1. **Tier Mapping NOT Optimal**: 47% of Pokemon in 6/6-8 tiers, rank-to-count inversions found (deferred to separate issue)
2. **11 Additional Missing Attackers Found** (mostly 2025 releases):
   - Crowned Sword Zacian (Steel #1, Fairy #2) — dethroned Dusk Mane Necrozma
   - Crowned Shield Zamazenta (Steel #2)
   - Eternatus (Dragon #1, Poison #1, Overall #4) — 1 per account
   - Keldeo Resolute (Fighting #3, best non-Mega) — 1-2 per account
   - Regieleki (Electric #2, S-Tier)
   - Mega Diancie (Rock #1 Mega) — 1 per account
   - Mega Charizard Y (Fire #2, S-Tier)
   - Shadow Darkrai (Dark #4), Shadow Conkeldurr (Fighting #7)
   - Shadow Dialga (Steel #6), Shadow Palkia (Dragon #5)
3. **Queries Updated**: Non-shadow 53→60, Shadow 37→41

**Raid Attacker Queries** (updated 2026-02-06):

**Non-Shadow Query** (59 species):

```
!shadow&(rayquaza,mewtwo,groudon,kyogre,kyurem,terrakion,reshiram,zekrom,xerneas,yveltal,hoopa,heracross,pheromosa,tyranitar,garchomp,blaziken,gengar,sceptile,kartana,lucario,metagross,gardevoir,mamoswine,weavile,glaceon,landorus,xurkitree,electivire,rampardos,swampert,volcarona,roserade,chandelure,espeon,alakazam,togekiss,primarina,granbull,hydreigon,salamence,dragonite,palkia,dialga,heatran,regigigas,staraptor,pinsir,deoxys,beedrill,necrozma,lunala,blacephalon,zacian,zamazenta,eternatus,keldeo,regieleki,diancie,charizard)
```

**Shadow Query** (40 species):

```
shadow&(mewtwo,salamence,dragonite,tyranitar,heatran,groudon,kyogre,garchomp,blaziken,chandelure,gengar,mamoswine,weavile,honchkrow,rampardos,rhyperior,electivire,raikou,zapdos,magnezone,moltres,darmanitan,machamp,excadrill,swampert,venusaur,tangrowth,scizor,alakazam,granbull,regigigas,staraptor,toxicroak,latios,metagross,gardevoir,darkrai,conkeldurr,dialga,palkia)
```

**Immediate Next Action**: Tag all raid attackers with `#Attackers` using both queries above.

**Deferred**:

- [ ] **Tier methodology recalibration** — [GitHub Issue #1](https://github.com/lioartoil/pokemon-go-storage-strategy/issues/1) for ER thresholds, rank-to-count inversions, 6/6-8 plateau

---

_Session handoff updated: 2026-02-06_
