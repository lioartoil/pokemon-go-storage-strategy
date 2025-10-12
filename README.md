# Pokemon GO Storage Management System

**Last Updated**: 2025-10-12
**Storage**: 10,184 / 10,500 Pokemon (316 free, ~3%)
**Strategy**: Moderate PvP Approach
**Target**: 9,200-9,600 Pokemon (900-1,300 free, ~9-12%)

---

## Quick Start

1. **Current System**: [Tag System Documentation](docs/reference/TAG_SYSTEM.md)
2. **Active Strategy**: [Moderate PvP Approach](docs/strategies/STRATEGY_MODERATE_PVP.md)
3. **Implementation**: [Phase 1 Guide](docs/guides/PHASE_1_IMPLEMENTATION.md)
4. **Quick Reference**: [Storage Quick Reference](docs/reference/STORAGE_QUICK_REFERENCE.md)

---

## Project Structure

```
pokemon/
├── README.md                          # This file
├── docs/
│   ├── strategies/                    # Storage strategies
│   │   ├── STRATEGY_MODERATE_PVP.md   # Current strategy (moderate)
│   │   ├── STRATEGY_REVISIONS_FINAL.md # Aggressive collector approach
│   │   └── STRATEGY_ANALYSIS.md       # Detailed analysis
│   ├── guides/                        # Implementation guides
│   │   ├── PHASE_1_IMPLEMENTATION.md  # Master League reduction
│   │   ├── META_UPDATE_GUIDE.md       # Meta shift tracking
│   │   ├── RAID_META_UPDATE_GUIDE.md  # Raid attacker updates
│   │   └── META_SHIFT_IMPACT.md       # Recent meta changes
│   └── reference/                     # Quick reference docs
│       ├── TAG_SYSTEM.md              # Tag system documentation
│       ├── STORAGE_QUICK_REFERENCE.md # Quick decisions
│       └── SEARCH_QUERIES.md          # Query string library
├── meta/                              # Meta data files
│   ├── cp10000_all_overall_rankings.csv
│   ├── raid_attackers_by_type.json
│   ├── RAID_ATTACKER_COMPARISON.md
│   └── pokemongohub/                  # API responses
└── scripts/                           # Automation scripts
    ├── parse_raid_attackers.py
    └── compare_raid_sources.py
```

---

## Current Tag System (43 tags, 86% capacity)

### Tag Categories

| Category             | Count | Purpose                              |
| -------------------- | ----- | ------------------------------------ |
| Evolution Management | 9     | Track target stages & requirements   |
| Buddy System         | 6     | Prioritize buddies & power-ups       |
| PvP System           | 12    | Personal ranks + absolute ranks      |
| Battle Roles         | 4     | Raids & gym defense tiers            |
| Resource Management  | 6     | Actions needed (candy, TM, purify)   |
| Storage Workflow     | 4     | Transfer pipeline & review queue     |
| Special Categories   | 3     | Forms that can't be queried          |

**Full documentation**: [TAG_SYSTEM.md](docs/reference/TAG_SYSTEM.md)

### Key Tag Concepts

**Personal Collection Ranks** (`Rank1`, `Rank2`, `Rank3`, `Rank4-20`, `Rank21-50`, `Rank51-100`):
- Track best **you own** for each species/league
- Used for retention decisions

**Absolute IV Ranks** (`First`, `Second`, `Third`):
- Track theoretical best **possible in game**
- Used for trophy Pokemon

**Example**: `Rank1` + `Rank2` + `Second` = "My best in one league, second-best in another, and #2 globally"

---

## Storage Strategy

### Current Approach: Moderate PvP

**Target savings**: 900-1,300 slots (976-1,376 gross, accounting for catches)

**Priority order**:
1. **Phase 1** (Week 1): Master League reduction (300-400 slots)
2. **Phase 2** (Weeks 2-3): Great/Ultra/Little League reduction (600-900 slots)

**Retention rules** (aligned with tag system):
- **Rank ≤10**: Keep 2 copies (GL/UL/ML)
- **Rank 11-50**: Keep 1 copy (GL/UL), keep 1 if ≤20 (ML)
- **Rank 51-100**: Keep 1 copy meta only (GL/UL), transfer (ML)
- **Rank 101+**: Transfer (all leagues)

**Strategy details**: [STRATEGY_MODERATE_PVP.md](docs/strategies/STRATEGY_MODERATE_PVP.md)

---

## Recent Updates

### 2025-10-12: Tag System Reorganization
- ✅ Cleaned up 6 unused tags
- ✅ Renamed all tags to PascalCase (no spaces)
- ✅ Adjusted rank tags for strategy alignment:
  - `Rank4-19` → `Rank4-20`
  - `Rank20-82` → `Rank21-50`
  - `Rank83-205` → `Rank51-100`
- ✅ Added `LuckyTrade` tag for Category 14
- ✅ Updated all documentation

### 2025-10-12: Raid Meta Update
- ✅ Updated raid attacker exclusion list (66 → 102+ species)
- ✅ Compared GamePress vs PokemonGOHub (46.7% agreement)
- ✅ Created automated update workflow

### 2025-10-12: Meta Shift Analysis
- ✅ Analyzed PvP meta shifts since early 2025
- ✅ Updated top 20 lists for GL/UL
- ✅ Documented impact on storage decisions

---

## Implementation Progress

### Phase 1: Master League Reduction (Week 1)

**Target**: 376-476 slots freed

- [ ] Day 1-2: Scan all Master League Pokemon with PokeGenie
- [ ] Day 3-4: Transfer Rank 21+ final evolutions (300-400 slots)
- [ ] Day 5-6: Reduce Rank 11-20 to 1 copy each
- [ ] Day 7: Reduce Rank ≤10 to 2 copies each
- [ ] Wait for 2× candy event: Clear `Home` tag transfers (76 slots)

**Guide**: [PHASE_1_IMPLEMENTATION.md](docs/guides/PHASE_1_IMPLEMENTATION.md)

### Phase 2: GL/UL/LL Reduction (Weeks 2-3)

**Target**: 600-900 slots freed

- [ ] Reduce Category 1 (GL/UL): 400-600 slots
- [ ] Reduce Category 2 (LL): 200-300 slots

---

## Maintenance Schedule

### Monthly Tasks
- [ ] Check for PvP meta shifts (use `META_UPDATE_GUIDE.md`)
- [ ] Update raid attacker list if move rebalance
- [ ] Clear transfer queue during 2× candy events

### Quarterly Tasks
- [ ] Review storage strategy effectiveness
- [ ] Reassess if free space < 7% (switch to aggressive?)
- [ ] Update meta rankings from PvPoke/GamePress

### When Meta Changes
- [ ] Follow `META_UPDATE_GUIDE.md` workflow
- [ ] Update top 20 lists in strategy docs
- [ ] Adjust retention decisions if needed

---

## Common Queries

### Storage Management
```
# Find transfer candidates (GL/UL Rank 101+)
Great&Rank51-100&!attackers&!def1

# Find duplicate IVs needing review
#Review

# Find lucky trade candidates
#LuckyTrade&4*
```

### Resource Management
```
# Pokemon needing actions
#NeedCandy | #NeedPurified | #PowerUp | #TM

# Pokemon ready to evolve
#SpecialEvolve | #ItemEvolve | #LocationEvolve | #TimeEvolve
```

### Trophy Pokemon
```
# Absolute top 3 ranks globally
#First | #Second | #Third

# Personal best per league
Great&Rank1 | Ultra&Rank1 | Little&Rank1
```

**Full query library**: [SEARCH_QUERIES.md](docs/reference/SEARCH_QUERIES.md)

---

## Tools & Resources

### Internal Tools
- **PokeGenie**: IV rank checking (required for Phase 1)
- **In-game tags**: Storage workflow management
- **Spreadsheet** (optional): Track transfer candidates

### External Resources
- **PvPoke**: Meta rankings (pvpoke.com)
- **GamePress**: Raid attacker DPS rankings
- **PokemonGOHub**: Boss-specific raid counters

### Scripts
- `scripts/parse_raid_attackers.py`: Extract top 10 attackers per type from GamePress CSV
- `scripts/compare_raid_sources.py`: Compare GamePress vs PokemonGOHub data

---

## When to Reassess Strategy

**Switch to Aggressive Approach if**:
1. Free space drops below 7% (735 slots) consistently
2. You confirm you won't do competitive PvP
3. Community Day/GO Fest storage pressure remains high

**Signs Moderate Approach is Working**:
1. Free space stays above 9% (945 slots)
2. No storage pressure during events
3. You have PvP options for research tasks

**Aggressive strategy**: [STRATEGY_REVISIONS_FINAL.md](docs/strategies/STRATEGY_REVISIONS_FINAL.md)

---

## Contributing

To update meta data:
1. Follow `META_UPDATE_GUIDE.md` workflow
2. Run `scripts/parse_raid_attackers.py` for raid updates
3. Update strategy docs with new top 20 lists
4. Commit changes with clear message

---

## Version History

- **2025-10-12**: Tag system reorganization, rank alignment fix, raid meta update
- **2025-10-11**: Moderate PvP strategy selection, Phase 1 implementation guide
- **2025-10-11**: Initial storage analysis, strategy comparison

---

_Pokemon GO Storage Management System - Comprehensive documentation for sustainable storage management with moderate PvP approach_
