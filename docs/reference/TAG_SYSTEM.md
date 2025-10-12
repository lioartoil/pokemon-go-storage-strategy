# Pokemon GO Tag System Documentation

**Date**: 2025-10-12
**Current Tags**: 43 tags (after cleanup)
**Tag Naming Convention**: PascalCase (no spaces)
**Capacity**: 43/50 (86%)

---

## Your Current Tag System (Post-Cleanup)

### Evolution Management (9 tags)

1. `Baby` - Baby Pokemon (target stage)
2. `Basic` - Basic stage (target stage)
3. `Stage1` - First evolution (target stage)
4. `Stage2` - Second evolution (target stage)
5. `Final` - Final evolution (target stage)
6. `SpecialEvolve` - Needs special evolution method
7. `ItemEvolve` - Needs evolution item
8. `LocationEvolve` - Needs specific location
9. `TimeEvolve` - Needs specific time/weather

**Purpose**: Track intended evolution stage and required evolution conditions

### Buddy System (6 tags)

10. `Buddy1Km` - 1km candy distance species
11. `Buddy3Km` - 3km candy distance species
12. `Buddy5Km` - 5km candy distance species
13. `Buddy20Km` - 20km candy distance species
14. `CurrentBuddy` - Currently active buddy
15. `InTraining` - Being powered up

**Purpose**: Prioritize buddies and track power-up projects

### PvP System (12 tags)

**League Tags**:

16. `Great` - Great League eligible (Rank 1-100)
17. `Ultra` - Ultra League eligible (Rank 1-100)
18. `Little` - Little League eligible (Rank 1-100)

**Personal Collection Ranks** (best you own):

19. `Rank1` - Your #1 best for species/league
20. `Rank2` - Your #2 best for species/league
21. `Rank3` - Your #3 best for species/league
22. `Rank4-20` - Your 4-20 best (great tier)
23. `Rank21-50` - Your 21-50 best (good tier)
24. `Rank51-100` - Your 51-100 best (decent tier)

**Absolute IV Ranks** (theoretical best globally):

25. `First` - #1 rank possible in game
26. `Second` - #2 rank possible in game
27. `Third` - #3 rank possible in game

**Purpose**: Track both personal collection quality and trophy Pokemon

**Example**: Pokemon with `Rank1`, `Rank2`, `Second` means:

- `Rank1` = Best YOU own in one league
- `Rank2` = Second best YOU own in another league
- `Second` = #2 best possible in entire game

### Battle Roles (4 tags)

28. `Attackers` - Raid attackers
29. `Def1` - Gym defender tier 1 (highest priority)
30. `Def2` - Gym defender tier 2
31. `Def2.5` - Gym defender tier 2.5

**Purpose**: Prioritize Pokemon for raids and gym defense

### Resource Management (6 tags)

32. `NeedCandy` - Have buddy distance, need to claim candy
33. `NeedPurified` - Shadows to purify
34. `PowerUp` - Marked for power up
35. `TM` - Needs move changes (TM/Elite TM)
36. `Trade` - For general trading
37. `LuckyTrade` - For lucky friend trades (Category 14)

**Purpose**: Track different resource needs and actions

**Clarification**:

- `NeedCandy` = Have distance, swap buddy to claim
- `InTraining` = Currently walking for candy

### Storage Workflow (4 tags)

38. `Home` - Transfer queue (batch during 2× candy events)
39. `Transfer` - Marked for immediate transfer
40. `Kept` - Permanent keep
41. `Review` - Needs recheck for duplicates

**Purpose**: Two-stage transfer workflow (immediate vs batched)

### Special Categories (3 tags)

42. `Mega` - Mega-capable Pokemon
43. `Var1` - Form variant 1 (e.g., Deoxys Attack)
44. `Var2` - Form variant 2 (e.g., Deoxys Defense)

**Purpose**: Handle edge cases where query strings fail

**Note**: `Event` and `Costume` tags are optional additions (45-46)

---

## Rank Tag Alignment with Strategy

Your rank tags now align with STRATEGY_MODERATE_PVP.md:

### Great & Ultra League (Category 1)

| Strategy Breakpoint | Your Tags                 | Copies to Keep     |
| ------------------- | ------------------------- | ------------------ |
| Rank ≤10            | `Rank1`, `Rank2`, `Rank3` | 2 copies           |
| Rank 11-50          | `Rank4-20`, `Rank21-50`   | 1 copy             |
| Rank 51-100         | `Rank51-100`              | 1 copy (meta only) |
| Rank 101+           | (no tag)                  | Transfer           |

### Master League (Category 3)

| Strategy Breakpoint | Your Tags                 | Copies to Keep |
| ------------------- | ------------------------- | -------------- |
| Rank ≤10            | `Rank1`, `Rank2`, `Rank3` | 2 copies       |
| Rank 11-20          | `Rank4-20`                | 1 copy         |
| Rank 21+            | `Rank21-50`, `Rank51-100` | Transfer       |

**Alignment**: Perfect! Your tags now match strategy breakpoints.

---

## Tag Changes Made

### Tags Deleted (6 tags)

- ❌ `Ready` - Not used
- ❌ `Candidates` - Not used
- ❌ `Archived` - Not used
- ❌ `Luckies` - Use `lucky` query string
- ❌ `DoubleCandy` - Not used
- ❌ `Aged` - Not used

### Tags Renamed to PascalCase

- `In Training` → `InTraining`
- `Need Candy` → `NeedCandy`
- `Need Purified` → `NeedPurified`
- `Power Up` → `PowerUp`
- `Current Buddy` → `CurrentBuddy`
- `Special Evolve` → `SpecialEvolve`
- `Item Evolve` → `ItemEvolve`
- `Location Evolve` → `LocationEvolve`
- `Time Evolve` → `TimeEvolve`
- `Stage 1` → `Stage1`
- `Stage 2` → `Stage2`
- `Buddy1km` → `Buddy1Km`
- `Buddy3km` → `Buddy3Km`
- `Buddy5km` → `Buddy5Km`
- `Buddy20km` → `Buddy20Km`
- `var1` → `Var1`
- `var2` → `Var2`

### Tags Renamed for Clarity

- `Waiting` → `Review`

### Tags Added (3 tags)

- ✅ `TM` - Needs move changes
- ✅ `LuckyTrade` - For lucky friend trades
- ✅ `Review` - Needs recheck (renamed from `Waiting`)

### Tags Adjusted for Alignment (3 tags)

- `Rank4-19` → `Rank4-20` (includes Rank 20 for ML)
- `Rank20-82` → `Rank21-50` (better alignment)
- `Rank83-205` → `Rank51-100` (matches GL/UL strategy)

**Before**: 46 tags (with 6 unused)
**After**: 43 tags (86% capacity)
**Freed**: 3 slots (after adding TM, LuckyTrade, Review)

---

## Query String Reference

Use these instead of tags:

```
# IV Filters
4*              # 100% IV (hundo)
0*              # 0% IV (nundo)
shiny&4*        # Shiny hundo (shundo)

# Special Status
shiny           # Shiny Pokemon
lucky           # Lucky Pokemon
shadow          # Shadow Pokemon
purified        # Purified Pokemon
costume         # Costume Pokemon

# Size
xxs             # XXS size
xxl             # XXL size

# Moves
@special        # Legacy/special moves

# Evolution Stage (current, not target)
evolve0         # Basic stage
evolve1         # Stage 1
evolve2         # Stage 2
evolve3         # Final evolution
baby            # Baby Pokemon

# Regions
alola           # Alolan forms
galar           # Galarian forms
hisui           # Hisuian forms
paldea          # Paldean forms

# Combined Queries
Great&Rank1             # Personal best Rank 1 in Great League
Great&Rank1&First       # Personal best + absolute #1 globally
lucky&4*                # Lucky hundo
shadow&4*               # Shadow hundo
```

---

## Common Tag Combinations

### Find transfer candidates

```
Great&Rank51-100&!attackers&!def1&!def2&!def2.5
```

Finds Great League Rank 51-100 that aren't used for raids/gyms

### Find trophy Pokemon

```
#First | #Second | #Third
```

All Pokemon with absolute top 3 ranks globally

### Find Pokemon needing resources

```
#NeedCandy | #NeedPurified | #PowerUp | #TM
```

All Pokemon needing some action

### Find lucky trade candidates

```
#LuckyTrade&4*
```

Hundos marked for lucky trades

---

_Tag System Documentation - Updated 2025-10-12_
