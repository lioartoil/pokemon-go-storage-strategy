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

### Session Summary

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

- [x] Category renumbering (#1→#1a/#1b, renumber #3-14)
- [x] PokeGenie format corrections (15 generators documented)
- [x] Symbol legend cleanup and standardization
- [x] Documentation updates (POKEGENIE_NAMING.md, STORAGE_STRATEGY_CORRECTED.md)
- [x] Raid attacker exclusion query created
- [x] Git commits (4 commits on 2025-10-14)
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

**Meta Data**:
- `meta/cp10000_all_overall_rankings.csv` - PvPoke Master League top 200
- `meta/raid_attackers_by_type.json` - GamePress raid attacker data

### Git Status

**Branch**: Main (no branches)
**Clean working tree**: Yes (all changes committed)
**Recent commits** (2025-10-14):
1. `b02bf69` - Fix High IV format: rank field always filled with rank number
2. `8e5a847` - Fix High IV format and add Mega/Primal evolution stages
3. `e9c5b5e` - Fix PokeGenie naming format and symbol corrections
4. `c1f5f5b` - Restructure category numbering: #1 → #1a/#1b subcategories

### Questions/Considerations

**PokeGenie Generator Setup**:
- Verify generator priority order (default at top, Favorite-specific below)
- Confirm "Has 2nd move" condition works as expected for High IV (2) generator
- Test if Favorite assignments auto-apply correctly

**Phase 1 Implementation Safety**:
- Double-check raid attacker query catches all important species
- Consider creating backup tag `#BeforePhase1` before transfers
- Confirm transfer candidates aren't tagged with `#Kept`, `#Attackers`, or high PvP ranks

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

_Session handoff updated: 2025-10-14 17:45 PST_
