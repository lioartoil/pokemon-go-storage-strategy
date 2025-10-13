# Pokemon GO Storage Strategy (CORRECTED)

**Current Utilization**: 10,184 / 10,500 (316 free slots, ~3% free)
**Last Updated**: 2025-10-13 (Category renumbering: #1a/#1b structure)

---

## User Profile

**Primary Focus**: Collecting > Raids > Trading >>> PvP
**Activity Level**: Daily (10+ remote raids, local raids when available)
**PvP Participation**: Minimal (only for research/challenges)
**Free Time Goal**: Maximize efficiency to reduce daily management time

**Tools Used**:

- Great/Ultra/Little League IV ranking: PokeGenie
- Master League IV ranking: IV4U (https://iv4u.lima-city.de/en)

---

## Core Principles

1. **Species Separation**: Mega, Shadow, Shiny, Costumed, and Background variants are treated as separate species
2. **IV Ranking**: Pokemon are evaluated based on their PvP IV rankings (optimal stat distributions for specific CP caps)
3. **Multi-Category Eligibility**: Pokemon may qualify for multiple categories, but count as 1 Pokemon only
4. **Priority Hierarchy**: Competitive leagues (1a-2) > Special variants (3-9) > Reserves (10-12) > Trade queue (13)
5. **Special Move Bonus**: Each category gets +1 slot if no current Pokemon has a special/legacy move

---

## Category Priority Hierarchy (Overlap Handling)

When a Pokemon qualifies for multiple categories, use this hierarchy:

**Example**: Shiny Shadow Charizard with rank #5 IV for Great League

1. **Check Category 1a-2** (Competitive leagues): If rank #5 qualifies for Category 1a and is in best 3 for species → **Category 1a**
2. **Else check Category 5** (Shadow): If not in best 3 for Category 1a, check if in best 2 shadow → **Category 5**
3. **Else check Category 3** (Shiny): If not in best 2 shadow, check if in best 2 shiny → **Category 3**
4. Continue down hierarchy...

**Result**: Pokemon counts as **1 total** in highest priority category it qualifies for.

---

## Category Breakdown

### Category 1a: Great & Ultra League Competitive Pokemon

**Total**: 1,370 Pokemon

**Criteria**:

- Great League: CP ≤ 1,500
- Ultra League: CP ≤ 2,500
- IV Rank ≤ 205 for each species

**Retention Rules** (CORRECTED):

- Rank ≤ 10: Keep best **3** Pokemon per species
- Rank ≥ 11: Keep **0** Pokemon if rank ≤ 10 already exists, otherwise keep **1**
- **Special Move Bonus**: +1 slot if no Pokemon has legacy/special move
- Mega and Shadow forms counted as separate species

**Purpose**: Maintain competitive roster for Great and Ultra League PvP (minimal use)

**User Notes**: Since PvP is minimal priority, this category is a candidate for aggressive reduction.

---

### Category 1b: Little League Competitive Pokemon

**Total**: 498 Pokemon

**Criteria**:

- Little League: CP ≤ 500
- Species must be in top 60th percentile (see `go/little-percentile-60.csv`)
- IV Rank thresholds vary by species percentile

**Retention Rules** (CORRECTED):

- **All species**: If rank ≤ 19, keep according to rules below
- **60th+ percentile species**: If rank 20-205, keep according to rules below
- **<60th percentile species**: If rank 20-205, discard
- Rank ≤ 10: Keep best **3** Pokemon per species
- Rank ≥ 11: Keep **0** Pokemon if rank ≤ 10 already exists, otherwise keep **1**
- **Special Move Bonus**: +1 slot if no Pokemon has legacy/special move
- Mega and Shadow forms counted as separate species

**Purpose**: Specialized roster for Little League cups (minimal use)

**User Notes**: Since PvP is minimal priority, this category is a candidate for aggressive reduction.

**Reference**: See `go/little-percentile-60.csv` for species viability rankings

---

### Category 2: Master League Competitive Pokemon

**Total**: 2,037 Pokemon

**Criteria**:

- Master League: Any CP (unlimited)
- IV Rank ≤ 19 for each species

**Retention Rules**:

**For Final Evolution & Mega Pokemon**:

- Rank ≤ 10: Keep best **3** Pokemon per species
- Rank 11-19: Keep **0** Pokemon if rank ≤ 10 already exists, otherwise keep **1**

**For Non-Final Evolution Pokemon**:

- Keep best **2** Pokemon per species
- **Rationale**: Future-proofing for new moves, forms, or final evolutions

**Special Move Bonus**: +1 slot per evolution stage if no Pokemon has legacy/special move

**Shadow Forms**: Counted as separate species

**Purpose**: High-IV Pokemon for Master League and raid battles

**User Notes**:

- Since PvP is minimal priority, final evolution retention can be reduced
- Non-final evolutions provide future-proofing for meta shifts

---

### Category 3: Shiny Pokemon

**Total**: 1,058 Pokemon

**Criteria**:

- Any Shiny Pokemon

**Retention Rules**:

- Keep best **2** IV-ranked Pokemon per species and form
- **Special Move Bonus**: +1 slot if no Pokemon has legacy/special move
- Shadow forms counted as separate species

**Purpose**: Collecting rare variants and trading value

**User Notes**: This aligns with collecting priority - keep current strategy.

---

### Category 4: Costumed Pokemon

**Total**: 324 Pokemon

**Criteria**:

- Any Pokemon with special costume/outfit

**Retention Rules**:

- Keep best **2** IV-ranked Pokemon per species, form, and costume combination
- **Special Move Bonus**: +1 slot if no Pokemon has legacy/special move
- Shadow forms counted as separate species

**Purpose**: Limited-time event collectibles

**User Notes**: This aligns with collecting priority - keep current strategy.

---

### Category 5: Shadow Pokemon

**Total**: 394 Pokemon

**Criteria**:

- Any Shadow Pokemon (including those not meeting competitive thresholds)

**Retention Rules**:

- Keep best **2** IV-ranked Pokemon per species
- **Special Move Bonus**: +1 slot if no Pokemon has legacy/special move

**Purpose**: Future purification, special moves, or potential PvP use

**Note**: Shadow Pokemon qualifying for competitive leagues (Categories 1a-2) count in highest priority category only

**User Notes**: This aligns with collecting priority - keep current strategy.

---

### Category 6: Size Extremes (XXS & XXL)

**Total**: 1,058 Pokemon

**Criteria**:

- Smallest (XXS) or Largest (XXL) Pokemon owned for each species

**Retention Rules**:

- Keep **1** smallest (XXS) per species
- Keep **1** largest (XXL) per species

**Purpose**: Size collecting and potential future gameplay features

**User Notes**: This aligns with collecting priority - keep current strategy.

---

### Category 7: Background Pokemon

**Total**: 150 Pokemon

**Criteria**:

- Pokemon with special catch backgrounds (e.g., location-based, event-based)

**Retention Rules**:

- Keep best **2** IV-ranked Pokemon per species and background type
- **Special Move Bonus**: +1 slot if no Pokemon has legacy/special move

**Purpose**: Rare location/event markers

**User Notes**: This aligns with collecting priority - keep current strategy.

---

### Category 8: Gigantamax Pokemon

**Total**: 17 Pokemon

**Criteria**:

- Pokemon with Gigantamax capability

**Retention Rules**:

- Keep best **2** Pokemon per species

**Purpose**: Special battle mechanic availability

---

### Category 9: Dynamax Pokemon

**Total**: 45 Pokemon

**Criteria**:

- Pokemon with Dynamax capability

**Retention Rules**:

- Keep best **2** Pokemon per species

**Purpose**: Special battle mechanic availability

---

### Category 10: Legendary & Ultra Beast Reserve

**Total**: 643 Pokemon

**Criteria**:

- Legendary or Ultra Beast Pokemon
- Does NOT meet criteria for Categories 1a-9

**Retention Rules**:

- Keep top **10** Pokemon per species, sorted by:
  1. Level (highest first)
  2. IV total (highest first)
- Shiny, Costumed, Background, Gigantamax, and Dynamax forms counted as separate species

**Purpose**: High-quality legendary Pokemon for raids and trading

**User Notes**:

- This aligns with raiding priority
- Consider keeping 12 for frequently used raid attackers (Kyogre, Groudon, Rayquaza, etc.)

---

### Category 11: Legendary/Mythical/Ultra Beast Transfer Queue

**Total**: 76 Pokemon (CORRECTED to include Ultra Beasts)

**Criteria**:

- Legendary Pokemon from Category 10 that didn't make top 10
- **All Ultra Beasts that didn't make top 10** (CORRECTED)
- All Mythical Pokemon (generally cannot be traded)

**Retention Rules**:

- Keep ALL until 2× Candy transfer events

**Purpose**: Maximize candy gain during transfer bonus events

**User Notes**: Daily task - audit this category every day (as you currently do)

---

### Category 12: General Population Reserve

**Total**: 2,441 Pokemon

**Criteria**:

- Any Pokemon not meeting Categories 1a-11

**Retention Rules**:

- Keep top **2** Pokemon per species, sorted by:
  1. Level (highest first)
  2. IV total (highest first)
- Shiny, Costumed, Background, Gigantamax, and Dynamax forms counted as separate species

**Purpose**: General backup and evolution fodder

**User Notes**: This aligns with collecting priority (living dex + 1 extra).

---

### Category 13: Lucky Trade Candidates

**Total**: <100 Pokemon (estimated)

**Criteria**:

- Pokemon from Category 12 that didn't make top 2
- Age ≥ 364 days (will be kept until age ≥ 1,095 days / 3 years)

**Retention Rules**:

- Keep ALL until age reaches 3+ years (1,095 days)
- Trade with Best/Ultra friends once they reach 3 years for maximum 20% lucky chance
- **Exception**: Keep 2016-2019 Pokemon for guaranteed lucky trades (35 trade limit)

**Purpose**: Maximize Lucky Trade probability with aged Pokemon

**Lucky Trade Mechanics** (Silph Road Research):

- 0-364 days: 5% lucky chance
- 365-729 days (1 year): 10% lucky chance
- 730-1,094 days (2 years): 15% lucky chance
- **1,095+ days (3+ years): 20% lucky chance (MAXIMUM)**

**Action**: Trade immediately once Pokemon reach 3 years old (no benefit to holding longer)

**Query Suggestion**: To count Category 13, search for:

- Age filter: 364+ days to 3 years
- Exclude: Pokemon in Categories 1a-12

---

## Storage Summary

| Category  | Description        | Count       | % of Total | User Priority |
| --------- | ------------------ | ----------- | ---------- | ------------- |
| 1a        | Great/Ultra League | 1,370       | 13.5%      | ⚠️ Low (PvP)  |
| 1b        | Little League      | 498         | 4.9%       | ⚠️ Low (PvP)  |
| 2         | Master League      | 2,037       | 20.0%      | ⚠️ Low (PvP)  |
| 3         | Shiny              | 1,058       | 10.4%      | ✅ High       |
| 4         | Costumed           | 324         | 3.2%       | ✅ High       |
| 5         | Shadow             | 394         | 3.9%       | ✅ High       |
| 6         | XXS/XXL            | 1,058       | 10.4%      | ✅ High       |
| 7         | Background         | 150         | 1.5%       | ✅ High       |
| 8         | Gigantamax         | 17          | 0.2%       | ✅ High       |
| 9         | Dynamax            | 45          | 0.4%       | ✅ High       |
| 10        | Legendary Reserve  | 643         | 6.3%       | ✅ High       |
| 11        | Transfer Queue     | 76          | 0.7%       | ✅ High       |
| 12        | General Reserve    | 2,441       | 24.0%      | ✅ High       |
| 13        | Lucky Trade Queue  | <100        | <1%        | ✅ High       |
| **Total** |                    | **10,184+** | **~97%**   |               |

**Free Space**: 316 slots (~3%)

**Optimization Opportunity**: Categories 1a-2 (PvP) = 3,905 Pokemon (38.3%) with LOW priority for your goals

---

## Maintenance Procedures

### Daily Tasks (Corrected)

- **Audit Categories 1a-2 for duplicates** (you currently do this - confirmed)
- Review and transfer Category 13 Pokemon that have aged 3+ years
- Transfer duplicate catches that don't meet any category criteria
- Check Category 11 for 2× candy event opportunities

### Weekly Tasks

- Review legendary raid catches (Category 10)
- Evaluate new shiny/costumed additions (Categories 3-4)

### Event-Based Tasks

- During 2× Transfer Candy: Clear Category 11
- During Lucky Trade Events: Prioritize Category 13 trades (3+ years old)
- After Community Day: Evaluate CD shinies

### Monthly Tasks

- Verify IV rankings haven't shifted due to game balance changes
- Review and prune Category 12 for Pokemon that have aged enough for Category 13

---

## Special Move Criteria (ADDED)

**Rule**: For each category, add +1 extra slot for Pokemon with legacy/special moves if no current kept Pokemon has that move.

**Examples of Special/Legacy Moves**:

- Community Day exclusive moves (Frenzy Plant, Blast Burn, Hydro Cannon, etc.)
- Legacy moves (Shadow Claw Gengar, Dragon Breath Charizard, etc.)
- Elite TM only moves
- Event-exclusive moves

**Application**:

- If you have 3× rank #1-10 Venusaur for Great League, but none have Frenzy Plant
- Keep 1 additional Venusaur with Frenzy Plant (even if rank 50)
- Once you have one with Frenzy Plant, no additional bonus slots

---

## Query Suggestions

### Count Category 14 (Lucky Trade Candidates)

PokeGenie or in-game search:

```
age364- & !age1095-
```

Then manually exclude Pokemon counted in Categories 1-13.

**Estimated**: <100 Pokemon

### Identify Special Move Pokemon

In-game search:

```
@special
```

Or use PokeGenie's move filter.

---

## Corrected Understanding

1. ✅ **Lucky trades cap at 3 years** (20% chance) - your strategy was correct
2. ✅ **Non-final evolutions** - kept for future-proofing (valid reason)
3. ✅ **Daily audits** - Categories 1-3 audited daily (confirmed)
4. ✅ **Ultra Beasts** - included in Category 12 transfer queue
5. ✅ **Special moves** - bonus slot criteria documented
6. ✅ **Overlap handling** - Pokemon count as 1 in highest priority category

---

## Related Files

- `STORAGE_STRATEGY.md` - Original strategy documentation (superseded by this file)
- `STORAGE_QUICK_REFERENCE.md` - Daily decision-making guide
- `STRATEGY_ANALYSIS.md` - Analysis vs best practices
- `IMPROVEMENT_RECOMMENDATIONS_REVISED.md` - Updated recommendations based on collecting focus
- `pokedex.md` - Master Pokedex tracking
- `go/little-percentile-60.csv` - Little League species viability data
- `leagues/` - League-specific tracking by generation

---

_Category renumbering (#1a/#1b structure): 2025-10-13_
