# CLAUDE.md

> **Project Context** | Pokemon GO Storage Management System | Updated: 2026-02-14

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

## Recent Work

### Session (2026-02-14): Validation Scripts + Query Fixes

1. Created `scripts/validate_raid_queries.py` — two-mode: query consistency + freshness audit (top-5, excl. Megas/Primals)
2. Created `scripts/fetch_pokemongohub.py` — Playwright-based PokemonGOHub cache refresh
3. Added `requirements.txt` (playwright>=1.40.0)
4. Fixed 3 query discrepancies: removed scizor (non-shadow, Bug #25), sceptile (shadow, Grass #11); added Shadow Gardevoir to table (Fairy #4)
5. Refreshed PokemonGOHub cache (18 types, 50 results each)
6. Final validated counts: 59 non-shadow, 40 shadow

### Earlier (2026-02-06): Comprehensive Raid Attacker Re-Audit

Deep re-audit found 11 additional missing attackers (2025 releases), updated rankings across 9 type sections, expanded queries 53→60 non-shadow, 37→41 shadow. Deferred tier methodology to GitHub Issue #1.

### Earlier (2026-01-28): Initial Raid Attacker Audit

Added 4 attackers (Necrozma formes, Lunala, Blacephalon), removed Giratina (Ghost #16), split query into non-shadow/shadow.

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

### Earlier (2025-11-02): Added Kyurem White/Black as Ice #1/#2

### Earlier (2025-10-14): Analyzed 100+ raid attackers, restructured to #1a/#1b categories

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

**Completed (2026-02-14)**:

- [x] Created validation + cache refresh automation scripts
- [x] Fixed 3 query/table discrepancies, validated all 6 queries across 3 files
- [x] Refreshed PokemonGOHub cache (18 types, 50 results each)
- [x] Raid attacker queries finalized: 59 non-shadow, 40 shadow

**Completed (2026-02-06)**: Re-audit added 11 attackers (Zacian, Zamazenta, Eternatus, Keldeo, Regieleki, etc.)
**Completed (2026-01-28)**: Added Necrozma formes, Lunala, Blacephalon; removed Giratina; split queries
**Completed (2026-01-18)**: Created 4 strategy docs, tested all queries (most returned 0 - well-organized)

**In Progress**:

- [ ] **EMERGENCY: Free 200-300 storage slots** (11,235/11,325 = 0.8% free)
- [ ] Finish tagging raid attackers with `#Attackers` (mostly done)
- [ ] Run `#Attackers` count to compare against recommended totals

**Deferred**: [GitHub Issue #1](https://github.com/lioartoil/pokemon-go-storage-strategy/issues/1) — Tier methodology recalibration

### Next Session Priorities

1. **Finish `#Attackers` Tagging** (~10 min) — SAFETY PREREQUISITE before any transfers
   - Run non-shadow query (59 species) and shadow query (40 species)
   - Tag all untagged results with `#Attackers`

2. **Emergency Storage Reduction** (~50 min, target 200-350 slots freed)
   - Step 1: Clear `#home` transfer queue (~76+ slots)
   - Step 2: Mass transfer `#rank51-100` (~50-100 slots)
   - Step 3: Trim `#rank21-50` duplicates (~50-100 slots)
   - Step 4: Duplicate sweep of untagged commons (~50+ slots)
   - See "Session Notes" for exact search queries

3. **Run `#Attackers` count** vs recommended totals in RAID_ATTACKER_COUNTS.md

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

1. `91ede0a` (2026-02-14) - data: refresh PokemonGOHub cache (2026-02-14)
2. `27b01ec` (2026-02-14) - fix(raid): resolve 3 query/table discrepancies from validation
3. `cc04015` (2026-02-14) - feat(scripts): add raid attacker validation and cache refresh scripts
4. `d43c84f` (2026-02-06) - docs(raid): add 11 missing raid attackers from 2025 releases
5. `a7719de` (2026-02-06) - docs: update session handoff with 2026-01-28 raid attacker audit

### Questions/Considerations

- Create one-page PokeGenie Quick Reference Card for daily use
- Monitor if moderate strategy provides enough free space (target: 9-12%)
- Reassess if need to switch to aggressive strategy after Phase 1

### Storage Metrics

**Current**: 11,235 / 11,325 Pokemon (90 free, ~0.8%) — CRITICAL
**Target**: 9,627 Pokemon (1,698 free, ~15%)
**Immediate Target**: Free 200-300 slots to play comfortably
**Challenge**: Well-organized collection — most quick-win categories return 0. Focus on ranked/tagged excess.

### Key Constraints

- PokeGenie Favorite limit: 10 groups (₀-₉)
- PokeGenie tag limit: 50 tags (43 used, 7 free)
- Pokemon GO name limit: 12 characters (all formats comply)
- User priority: Collecting > Raids > Trading >>> PvP (minimal)

---

## Session Notes

**Current Session (2026-02-14)**: Validation Scripts + Emergency Storage Reduction

**Emergency Reduction Queries** (run in Pokemon GO, in this order):

**Step 0 — Tag Attackers First** (see Raid Attacker Queries in Implementation Details above)

**Step 1 — Transfer Queue**: `#home`

**Step 2 — Rank 51-100**: `#rank51-100&!#Attackers&!lucky&!shiny&!@special&!legendary&!mythical`

**Step 3 — Rank 21-50 Excess**: `#rank21-50&!#Attackers&!lucky&!shiny&!@special&!legendary&!mythical`
Sort by name → keep best 1 per species, transfer rest.

**Step 4 — Untagged Duplicates**: `!4*&!shiny&!lucky&!shadow&!costume&!@special&!legendary&!mythical&!#Attackers&!#rank1&!#rank2&!#rank3&!#rank4-20&!#great&!#ultra&!#little`
Sort by name → transfer lowest-IV duplicates.

**Deferred**: Tier methodology recalibration — [GitHub Issue #1](https://github.com/lioartoil/pokemon-go-storage-strategy/issues/1)

---

_Session handoff updated: 2026-02-14_
