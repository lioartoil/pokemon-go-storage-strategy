# CLAUDE.md

> **Project Context** | Pokemon GO Storage + Violet Playthrough | Updated: 2026-03-08

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
│   ├── pvpoke_ml_rankings.json          # PvPoke ML PvP rankings (JSON)
│   ├── raid_attackers_by_type.json      # GamePress raid attackers (fallback)
│   ├── cross_reference_results.json     # Cross-reference output
│   ├── pokebase/                        # PokeBase DPS calc data
│   └── pokemongohub/                    # PokemonGOHub API responses
├── violet/                              # Pokemon Violet playthrough tracker
│   └── playthrough.md                   # Party, box, and detailed Pokemon records
├── leagues/                             # Generation-specific PvP tracking
└── scripts/                             # Python automation scripts
```

## Recent Work

### Session (2026-03-08): Pokemon Violet Playthrough — Batch Updates

1. **Party updates across 3 screenshot batches** (IMG_9887→9922):
   - Larb (Fuecoco): Lv.17→19, Oran Berry consumed (no held item)
   - Kai Yang (Fletchling): Lv.15→16, berry swap Chesto→Cheri
   - Tod Mun (Pawmi): Lv.14→15, berry swap Chesto→Persim (Natural Cure synergy)
   - Bua Loy (Azurill): Lv.13→15, berry swap Cheri→Pecha, learned **Bounce** (replaced Helping Hand)
   - Carpaccio (Magikarp): Lv.10→12
   - Macaron (Ralts): Lv.10→12, learned **Psybeam** via TM (replaced Confusion)
2. **5 new boxed Pokemon** (box: 17→22):
   - Sunsnack (Sunkern F Lv.7) — Mild, **HA: Solar Power**, Def 26/31
   - Brioche (Fidough F Lv.6) — Quiet, Own Tempo, Atk 14/19
   - Broccoli (Bonsly F Lv.6) — Lonely, Rock Head, Speed 17/22/27
   - Nutella (Skwovet F Lv.8) — Hardy, Cheek Pouch, Speed 26/31
   - Sorbet (Surskit M Lv.8) — Sassy, Swift Swim, Sp.Atk 25/30
3. **Berry reassignment** (strategic): Cheri for Electric weakness (Kai Yang), Persim for confusion-only coverage (Tod Mun has Natural Cure for other statuses on switch), Pecha for Poison weakness (Fairy types)
4. **IV estimates** calculated for all new catches using base stats + nature + characteristic
5. **Catch/box evaluations** for Bonsly, Skwovet, Surskit, Shroodle — all boxed (team slots locked for final evolutions)

### Session (2026-03-05): Unicode Symbol Replacement

1. **MAJOR**: Replaced 15 blocked Unicode symbols in PokeGenie naming system
   - Pokemon GO update blocked Enclosed Alphanumerics (U+2460-U+24FF), Geometric Shapes (U+25A0-U+25FF), Arrows (U+2190-U+21FF)
   - Shadow: ● → `•` (bullet), Purified: ○ → `°` (degree)
   - Stages: ⓪→`0`, ①→`1`, ②→`2`, Ⓑ→`.` (dot), Ⓜ→`M`, Ⓟ→`P`
   - Leagues: Ⓖ→`G`, Ⓤ→`U`, ⓛ→`C` (Cup, sorts before G)
   - Transfer: ⇄→`~`, Levels: ②→`2`, ⑮→`15`, ⑳→`20`
   - Still working: ₁-₉ (subscripts), ⁰-⁹ (superscripts), ½, ㈩
2. Sort order fixes: `.` (Baby) < `0` (Basic), `C` (Cup) < `G` (Great) < `U` (Ultra)
3. Added `prompt.md` to `.gitignore`
4. Pokemon GO name sort order finding: `-` (dash) does NOT sort before digits — game has non-ASCII collation for hyphens

### Session (2026-02-25): Data Refresh + 15 New Species + 41 Megas

1. Refreshed all 3 data sources: PokeBase (1,658 entries), PokemonGOHub (18 types), PvPoke ML (397 entries)
2. Fixed `ACCOUNT_LIMITED` in `cross_reference_raid_sources.py` from 1→2 (normal + shiny)
3. Updated `LEGENDARY_UB_MYTHICAL` set: added enamorus, tapu lele, tapu koko, thundurus, nihilego, shaymin, zarude, zygarde, zeraora, latios, latias
4. Updated `ACCESSIBLE` set: added ~50 species (Mega base forms + new shadow species)
5. **MAJOR**: Added 15 new species to `docs/reference/RAID_ATTACKER_COUNTS.md`
   - Enamorus (4), Tapu Lele (4), Tapu Koko (3), Shaymin Sky (3), Zarude (3), Nihilego (3)
   - Shadow Toucannon (2), Shadow Vikavolt (1), Shadow Delphox (1), etc.
6. **MAJOR**: Added 41 Mega entries + 2 merges (all Megas with ER >= 40, incl. datamined)
   - Merged: Mewtwo (ER 50.28→65.02, count 5→6), Heatran (ER 41.93→55.92, count 3→6)
   - New entries: Mega Rayquaza (6), Mega Garchomp (5), Mega Salamence (5), Mega Metagross (5), etc.
   - Final: ~459 copies across 146 species (up from ~329 across 90)
7. Updated raid attacker queries: 94 non-shadow, 46 shadow (up from 48/37)

### Session (2026-02-21): Multi-Source Cross-Reference + ML PvP Modifier

1. Created `scripts/fetch_pokebase.py` — Playwright scraper for PokeBase DPS calc (1,658 Pokemon with ER)
2. Created `scripts/cross_reference_raid_sources.py` — cross-references 4 data sources
3. Refreshed all data sources: PokeBase (new), PokemonGOHub, PvPoke ML rankings
4. Fetched PvPoke ML rankings → `meta/pvpoke_ml_rankings.json` (397 entries)
5. **MAJOR**: Updated `docs/reference/RAID_ATTACKER_COUNTS.md` with fresh cross-referenced data
   - ER values updated from PokeBase 2026-02-21 (all 90 species now have fresh ER)
   - Added 5th modifier: ML PvP top-50 (+1 for dual-use PvP value)
   - Added PvP column to Quick Reference Table
   - 29 species qualify for ML PvP modifier
   - Total: ~326 copies across 90 species (down from ~358, ER values shifted)
6. Updated raid attacker queries: 48 non-shadow, 37 shadow (down from 59/40)

### Session (2026-02-16): Tier Methodology Recalibration (Issue #1) + Doc Fixes

1. Fixed TAG_SYSTEM.md: added LL alignment table, fixed GL/UL "meta only", fixed Transfer tag description
2. Updated STRATEGY_MODERATE_PVP.md: LL alignment with GL/UL breakpoints
3. Added emergency reduction guide (`docs/guides/EMERGENCY_REDUCTION_GUIDE.md`)
4. **MAJOR**: Rewrote `docs/reference/RAID_ATTACKER_COUNTS.md` with ER-based tier methodology
   - 6 tiers (S/A/B/C/D/E) based on Estimator Rating + 4 modifiers (dual-type, legendary, accessible, glass cannon)
   - Merged Mega/Primal into base form entries, capped at 6 per species
   - Resolved all 3 rank-to-count inversions, eliminated all count ranges
   - ~358 copies across 90 species (down from ~530 across 110 entries)
5. Closed GitHub Issue #1 (commit `3d8f4ec` with `Closes #1`)

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

- All Favorite ₂ generators (High IV, Dynamax, Gigantamax) use identical format: `₂{Stage}{•/°}{Name}{Rank}{IV}{Lvl}{Atk}{Atk2}{Leg}`
- Rank field ALWAYS filled with rank number (auto-conditions: Pokemon's rank; manual: Master League rank)
- Shadow/XXS/XXL formats simplified to match Shiny/Costume patterns
- Level format uses `2`, `15`, `20` for whole levels and `2½`, `15½`, `20½` for half-levels

**Symbol Standardization**:

- Added `C` for Little League/Cup (was missing)
- Added `M` (Mega) and `P` (Primal) evolution stages
- Removed unused symbols: `⊖`, `⊕`, `•` (Default)
- Fixed Costume prefix: `₃` → `₄`

**Raid Attacker Count Methodology (ER-Based — Cross-Referenced)**:

- **ER Source**: PokeBase DPS Calculator (primary, 2026-02-21), GamePress (fallback)
- **ER Tiers**: S(≥60)→6, A(55-59.9)→5, B(50-54.9)→4, C(45-49.9)→3, D(40-44.9)→2, E(<40)→1
- **5 Modifiers**: +1 dual-type, +1 legendary/UB/mythical, +1 ML PvP top-50, -1 accessible, -1 glass cannon (TDO<300)
- **Caps**: Max 6, min 1, account-limited = account limit, Giovanni-only = keep all
- **Mega/Primal merge**: Same physical Pokemon → single entry using best ER
- **Total**: ~459 copies across 146 tracked species

### Implementation Details

**Category Mapping** (Favorite → Category alignment):

| Favorite | Prefix | Categories | Description                      |
| -------- | ------ | ---------- | -------------------------------- |
| (none)   | ~      | #10-13     | Transfer/Trade queue (default)   |
| ₁        | ₁      | #1a, #1b   | PvP IV (GL/UL/LL)                |
| ₂        | ₂      | #2, Manual | Master League + High IV override |
| ₃        | ₃      | #3         | Shiny Pokemon                    |
| ₄        | ₄      | #4         | Costumed Pokemon                 |
| ₅        | ₅      | #5         | Shadow Pokemon                   |
| ₆        | ₆      | #6         | XXS/XXL size extremes            |
| ₇        | ₇      | #7         | Background Pokemon               |
| ₈        | ₈      | #8         | Dynamax Pokemon                  |
| ₉        | ₉      | #9         | Gigantamax Pokemon               |

**Evolution Stage Symbols**: . (Baby), 0 (Basic), 1 (Stage 1), 2 (Stage 2), M (Mega), P (Primal)

**League Symbols**: C (Little/Cup ≤500), G (Great ≤1500), U (Ultra ≤2500), (none) = Master (unlimited)

**Shadow/Purified**: • (Shadow), ° (Purified)

**Raid Attacker Queries** (to exclude from transfers):

**Non-Shadow Query** (94 species):

```
!shadow&absol,aerodactyl,alakazam,ampharos,banette,baxcalibur,beedrill,blacephalon,blastoise,blaziken,chandelure,charizard,chesnaught,darkrai,delphox,deoxys,dialga,diancie,dragonite,drampa,eelektross,emboar,enamorus,eternatus,excadrill,feraligatr,froslass,gallade,garchomp,gardevoir,gengar,glimmora,golisopod,golurk,greninja,groudon,gyarados,hawlucha,heatran,heracross,hoopa,houndoom,hydreigon,kartana,keldeo,kyogre,kyurem,landorus,latias,latios,lopunny,lucario,lunala,manectric,meganium,meowstic,metagross,mewtwo,necrozma,nihilego,palkia,pheromosa,pidgeot,pinsir,pyroar,rampardos,rayquaza,regieleki,regigigas,reshiram,salamence,sceptile,scizor,scovillain,shaymin,skarmory,staraptor,starmie,swampert,tapu,terrakion,tyranitar,venusaur,victreebel,volcarona,xerneas,xurkitree,yveltal,zacian,zamazenta,zarude,zeraora,zekrom,zygarde
```

**Shadow Query** (46 species):

```
shadow&alakazam,blaziken,chandelure,chesnaught,conkeldurr,darkrai,darmanitan,delphox,dialga,dragonite,electivire,excadrill,garchomp,gardevoir,gengar,gigalith,greninja,groudon,heatran,honchkrow,kingler,kyogre,latios,machamp,magnezone,mamoswine,metagross,mewtwo,moltres,palkia,porygon-z,raikou,rampardos,regigigas,rhyperior,salamence,staraptor,swampert,tangrowth,toucannon,toxicroak,tyranitar,tyrantrum,vikavolt,weavile,zapdos
```

**Attacker Tag Filter** (non-shadow, exclude tracked species):

```
!shadow&!absol&!aerodactyl&!alakazam&!ampharos&!banette&!baxcalibur&!beedrill&!blacephalon&!blastoise&!blaziken&!chandelure&!charizard&!chesnaught&!darkrai&!delphox&!deoxys&!dialga&!diancie&!dragonite&!drampa&!eelektross&!emboar&!enamorus&!eternatus&!excadrill&!feraligatr&!froslass&!gallade&!garchomp&!gardevoir&!gengar&!glimmora&!golisopod&!golurk&!greninja&!groudon&!gyarados&!hawlucha&!heatran&!heracross&!hoopa&!houndoom&!hydreigon&!kartana&!keldeo&!kyogre&!kyurem&!landorus&!latias&!latios&!lopunny&!lucario&!lunala&!manectric&!meganium&!meowstic&!metagross&!mewtwo&!necrozma&!nihilego&!palkia&!pheromosa&!pidgeot&!pinsir&!pyroar&!rampardos&!rayquaza&!regieleki&!regigigas&!reshiram&!salamence&!sceptile&!scizor&!scovillain&!shaymin&!skarmory&!staraptor&!starmie&!swampert&!tapu&!terrakion&!tyranitar&!venusaur&!victreebel&!volcarona&!xerneas&!xurkitree&!yveltal&!zacian&!zamazenta&!zarude&!zeraora&!zekrom&!zygarde&attackers
```

### Current State

**Completed (2026-03-05)**:

- [x] Replaced 15 blocked Unicode symbols in PokeGenie naming system
- [x] Fixed sort order: Baby (`.`) before Basic (`0`), Little League (`C`) before Great (`G`)
- [x] Added `prompt.md` to `.gitignore`

**Completed (2026-02-25)**:

- [x] Refreshed all 3 data sources (PokeBase, PokemonGOHub, PvPoke ML rankings)
- [x] Added 15 new species to RAID_ATTACKER_COUNTS.md
- [x] Added 41 new Mega entries + 2 merges (Mewtwo→6, Heatran→6) — ~459 copies across 146 species
- [x] Updated raid attacker queries (94 non-shadow, 46 shadow)
- [x] Fixed account-limited counts in cross-reference script (1→2)

**Completed (2026-02-21)**: Cross-referenced 4 data sources, added ML PvP modifier
**Completed (2026-02-16)**: Tier methodology recalibration (Issue #1), doc fixes
**Completed (2026-02-14)**: Validation scripts, query fixes, PokemonGOHub cache refresh

**In Progress**:

- [ ] **EMERGENCY: Free 200-300 storage slots** (11,235/11,325 = 0.8% free)
- [ ] Re-tag raid attackers with `#Attackers` using updated queries (94+46 species)
- [ ] Run `#Attackers` count to compare against recommended totals (~459 copies)

### Next Session Priorities

1. **Re-tag `#Attackers`** (~10 min) — SAFETY PREREQUISITE before any transfers
   - Run non-shadow query (94 species) and shadow query (46 species)
   - Tag all untagged results with `#Attackers`

2. **Emergency Storage Reduction** (~50 min, target 200-350 slots freed)
   - Step 1: Clear `#home` transfer queue (~76+ slots)
   - Step 2: Mass transfer `#rank51-100` (~50-100 slots)
   - Step 3: Trim `#rank21-50` duplicates (~50-100 slots)
   - Step 4: Duplicate sweep of untagged commons (~50+ slots)

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
- `docs/reference/RAID_ATTACKER_COUNTS.md` - ER-based attacker retention counts (updated 2026-02-25; 146 species, ~459 copies)

**Meta Data**:

- `meta/cp10000_all_overall_rankings.csv` - PvPoke Master League top 200
- `meta/raid_attackers_by_type.json` - GamePress raid attacker data

**Automation Scripts**:

- `scripts/validate_raid_queries.py` - Validates queries and audits freshness
- `scripts/fetch_pokemongohub.py` - Refreshes PokemonGOHub API cache (Playwright)

### Git Status

**Branch**: develop (main branch)
**Clean working tree**: Yes (all changes committed and pushed)
**GitHub Issues**: [#1](https://github.com/lioartoil/pokemon-go-storage-strategy/issues/1) - CLOSED (recalibrated 2026-02-16)
**Recent commits** (most recent first):

1. `9a4421d` (2026-03-05) - fix(naming): change Baby stage symbol from - to . for correct sort order
2. `86e3932` (2026-03-05) - fix(naming): adjust Baby and Little League symbols for correct sort order
3. `c057e95` (2026-03-05) - fix(naming): replace blocked Unicode symbols with compatible alternatives
4. `48a8f15` (2026-03-05) - chore: add prompt.md to .gitignore
5. `cd42963` (2026-02-25) - feat(raid): add 41 Mega entries and merge 2 existing (146 species, ~459 copies)

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
- Pokemon GO blocked Unicode: Enclosed Alphanumerics (⓪-⑳, Ⓐ-Ⓩ), Geometric Shapes (●○), Arrows (⇄)
- Pokemon GO name sort: `-` (dash) does NOT sort before digits; `.!,+#(*` DO sort before digits
- User priority: Collecting > Raids > Trading >>> PvP (minimal)

---

## Session Notes

**Current Session (2026-03-08)**: Pokemon Violet Playthrough — Party/Box Updates

### Violet Playthrough State

- **Party (6/6)**: Larb Lv.19, Kai Yang Lv.16, Tod Mun Lv.15, Bua Loy Lv.15, Carpaccio Lv.12, Macaron Lv.12
- **Box**: 22 Pokemon (food-themed names, Thai + international)
- **Final evolutions**: Skeledirge, Talonflame, Pawmot, Azumarill, Gyarados, Gardevoir
- **Key file**: `violet/playthrough.md` — full party/box tables + detailed IV estimates for all 28 Pokemon
- **Memory file**: `~/.claude/projects/.../memory/pokemon-violet-playthrough.md` — compact summary
- **Workflow**: User sends screenshots (HEIC) → Claude converts via `sips` → reads stats/nature/characteristic → calculates IVs → updates files
- **Pending**: Shroodle catch (recommended name: Wasabi or Sriracha) — screenshots not yet received

### Pokemon GO Emergency Queries

**Step 0 — Tag Attackers First** (see Raid Attacker Queries in Implementation Details above)
**Step 1 — Transfer Queue**: `#home`
**Step 2 — Rank 51-100**: `#rank51-100&!#Attackers&!lucky&!shiny&!@special&!legendary&!mythical`
**Step 3 — Rank 21-50 Excess**: `#rank21-50&!#Attackers&!lucky&!shiny&!@special&!legendary&!mythical`
**Step 4 — Untagged Duplicates**: `!4*&!shiny&!lucky&!shadow&!costume&!@special&!legendary&!mythical&!#Attackers&!#rank1&!#rank2&!#rank3&!#rank4-20&!#great&!#ultra&!#little`

---

_Session handoff updated: 2026-03-08_
