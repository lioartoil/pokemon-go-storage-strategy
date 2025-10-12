# Pokemon GO - Favorite Search Queries

**Date**: 2025-10-12
**Tag System**: Updated to match PascalCase tags (43 tags)

---

## Daily Workflow Queries

### 1. New Untagged Pokemon

**Name**: `New Catches`
**Query**: `!#`
**Purpose**: Find all Pokemon without any tags (need to review and categorize)
**When to use**: After catching session, daily review

---

### 2. Pokemon Needing Review

**Name**: `Review Queue`
**Query**: `#Review`
**Purpose**: Find Pokemon marked for duplicate/rank recheck
**When to use**: Weekly cleanup, after PokeGenie scan

**Old version**: `#waiting` ❌ (outdated tag name)
**New version**: `#Review` ✅

---

### 3. Special Pokemon Needing Categorization

**Name**: `Special Review`
**Query**: `#Review&!legendary&!mythical&!ultra beasts`
**Purpose**: Non-legendary Pokemon in review queue (quicker to process)
**When to use**: When review queue is large, prioritize non-legendaries

**Old version**: `#waiting&!legendary&!mythical&!ultra beasts` ❌
**New version**: `#Review&!legendary&!mythical&!ultra beasts` ✅

---

### 4. Legendary Review Queue

**Name**: `Legendary Review`
**Query**: `#Review&legendary,mythical,ultra beasts`
**Purpose**: Legendary/Mythical/Ultra Beasts in review queue
**When to use**: When you want to process legendaries separately (usually keep most)

**Old version**: `legendary,mythical,ultra beasts&waiting` ❌
**New version**: `#Review&legendary,mythical,ultra beasts` ✅

---

## Resource Management Queries

### 5. Current Buddy

**Name**: `Active Buddy`
**Query**: `#CurrentBuddy`
**Purpose**: Find your currently active buddy
**When to use**: Quick access to buddy, check buddy progress

**Old version**: `#currentbuddy` ❌ (lowercase)
**New version**: `#CurrentBuddy` ✅ (PascalCase)

---

### 6. Pokemon Needing Power-Up

**Name**: `Power-Up Queue`
**Query**: `#PowerUp`
**Purpose**: Find Pokemon marked for power-up
**When to use**: When you have stardust/candy to spend

**Old version**: `#power up` ❌ (space, lowercase)
**New version**: `#PowerUp` ✅ (PascalCase)

---

### 7. Pokemon Needing TMs

**Name**: `TM Queue`
**Query**: `#TM`
**Purpose**: Find Pokemon needing move changes
**When to use**: After getting TMs from raids/GBL
**New**: ✅ (new tag added)

---

### 8. Pokemon In Training

**Name**: `Training Projects`
**Query**: `#InTraining`
**Purpose**: Find Pokemon being powered up (active projects)
**When to use**: Track ongoing power-up projects

---

## Transfer & Trade Queries

### 9. Transfer Queue (Immediate)

**Name**: `Transfer Now`
**Query**: `#Transfer&!#Home`
**Purpose**: Pokemon ready for immediate transfer (don't wait for event)
**When to use**: When you need storage space urgently

**Enhancement**: Excludes `#Home` to avoid transferring event-waiting Pokemon

---

### 10. Transfer Queue (Event Wait)

**Name**: `Event Transfer`
**Query**: `#Home`
**Purpose**: Pokemon to transfer during 2× candy events
**When to use**: During 2× transfer candy events

---

### 11. All Transfer Candidates

**Name**: `All Transfers`
**Query**: `#Transfer,#Home`
**Purpose**: See entire transfer pipeline (immediate + event)
**When to use**: Review total transfer queue size

---

### 12. Trade Queue

**Name**: `Trade Queue`
**Query**: `#Trade`
**Purpose**: Pokemon marked for general trading
**When to use**: Before trading with friends

**Old version**: `#to trade` ❌ (space, lowercase)
**New version**: `#Trade` ✅ (PascalCase)

---

### 13. Lucky Trade Candidates

**Name**: `Lucky Trades`
**Query**: `#LuckyTrade`
**Purpose**: Pokemon marked for lucky friend trades (Category 14)
**When to use**: When you have lucky friends ready to trade
**New**: ✅ (new tag added)

---

### 14. Aged Lucky Trade Candidates (Auto-find)

**Name**: `New Lucky Candidates`
**Query**: `age364-&!#Trade&!#Kept&!#Home&!traded&!legendary&!mythical&!ultra beasts&!shiny&!costume&!shadow&!xxs&!xxl&!background&!4*`
**Purpose**: Auto-find 1+ year old Pokemon not already marked for other purposes
**When to use**: Monthly review to find new lucky trade candidates

**Old version**: `age364-&!#luckies&!traded&!to trade&!kept&!home&!791` ❌
**New version**: Enhanced with more exclusions ✅

**Enhancements**:

- Changed `#to trade` → `#Trade`
- Changed `#kept` → `#Kept`
- Changed `#home` → `#Home`
- Removed `#luckies` (no longer exists, use query `lucky`)
- Added exclusions for special Pokemon (shiny, costume, shadow, size, background, hundo)
- Added legendary/mythical/ultra beast exclusions (usually keep for raids)

---

### 15. Mythical Transfer Queue (Pokemon HOME)

**Name**: `HOME Queue`
**Query**: `#Home&mythical`
**Purpose**: Mythicals to transfer to Pokemon HOME (2× candy event)
**When to use**: During 2× transfer candy events

**Enhancement**: Focuses on mythicals specifically (since most go to HOME, not Professor)

---

### 16. Mythicals Ready for HOME (Auto-find)

**Name**: `New HOME Candidates`
**Query**: `#Transfer&!#Home&mythical&151,251,385,386,491,492,494,647,648,649,718,719,720,802,893`
**Purpose**: Mythicals in transfer queue but not yet tagged for HOME
**When to use**: Monthly review to ensure mythicals are properly tagged

**Old version**: `transfer&!home,#to&traded, 151, 251, 385...` ❌ (syntax error)
**New version**: Fixed syntax, clearer purpose ✅

**Enhancements**:

- Fixed syntax: `#Transfer&!#Home` instead of `transfer&!home,#to`
- Removed `traded` (those shouldn't be in transfer queue anyway)
- Clearer purpose: finding mythicals that need `#Home` tag added

---

## Special Collections Queries

### 17. Special Pokemon (All Types)

**Name**: `All Specials`
**Query**: `shiny,legendary,mythical,ultra beasts,costume,shadow,xxs,xxl,background,4*,@special,dynamax,gigantamax`
**Purpose**: Find all "special" Pokemon worth keeping
**When to use**: Review what you're keeping vs transferring

**Old version**: `shiny,legendary,ultra beasts,+melmetal&!traded&!kept` ❌
**New version**: Comprehensive list of all special types ✅

**Enhancements**:

- Added costume, shadow, size, background, hundo, special moves, dynamax, gigantamax
- Removed `+melmetal` filter (Melmetal is already in mythical)
- Removed `!traded&!kept` (not needed for overview)

---

### 18. Specials Needing Tags

**Name**: `Untagged Specials`
**Query**: `!#&legendary,mythical,ultra beasts,xxs,xxl,costume,shiny,shadow,4*,dynamax,gigantamax,background`
**Purpose**: Find special Pokemon that somehow don't have tags yet
**When to use**: After catching special Pokemon, ensure they're categorized

**Old version**: Same ✅ (this one was already good!)

---

### 19. Kept Pokemon (Permanent Collection)

**Name**: `Kept Pokemon`
**Query**: `#Kept`
**Purpose**: Pokemon marked as permanent keep (living dex, trophies)
**When to use**: Review permanent collection

---

## Mega Evolution Queries

### 20. Mega Rank 1 (Not Yet Mega Evolved)

**Name**: `Mega First Evolve`
**Query**: `megaevolve&#Rank1&mega0&#Mega`
**Purpose**: Best IV Mega candidates that haven't mega evolved yet
**When to use**: Choose which Pokemon to mega evolve first

**Old version**: `megaevolve&rank1&mega0&mega` ❌ (missing #)
**New version**: `megaevolve&#Rank1&mega0&#Mega` ✅

**Enhancements**:

- Added `#` before `Rank1` (it's a tag)
- Added `#` before `Mega` (it's a tag)

---

### 21. Mega Rank 1 (Mega Level 1)

**Name**: `Mega Level Up`
**Query**: `megaevolve&#Rank1&mega1&#Mega`
**Purpose**: Best IV Megas at level 1 (ready to level up)
**When to use**: Planning which Megas to level up to Max

**Old version**: `megaevolve&rank1&mega1&mega` ❌ (missing #)
**New version**: `megaevolve&#Rank1&mega1&#Mega` ✅

**Enhancements**:

- Added `#` before `Rank1` (it's a tag)
- Added `#` before `Mega` (it's a tag)

---

### 22. All Mega Candidates

**Name**: `Mega Candidates`
**Query**: `megaevolve&#Mega`
**Purpose**: All Pokemon capable of Mega Evolution that you've tagged
**When to use**: Review Mega collection

---

## PvP Rank Queries

### 23. Great League Best

**Name**: `GL Top Ranks`
**Query**: `#Great&#Rank1,#Rank2,#Rank3`
**Purpose**: Your top 3 best Great League Pokemon
**When to use**: Building GL teams, reviewing GL collection

---

### 24. Ultra League Best

**Name**: `UL Top Ranks`
**Query**: `#Ultra&#Rank1,#Rank2,#Rank3`
**Purpose**: Your top 3 best Ultra League Pokemon
**When to use**: Building UL teams, reviewing UL collection

---

### 25. Little League Best

**Name**: `LL Top Ranks`
**Query**: `#Little&#Rank1,#Rank2,#Rank3`
**Purpose**: Your top 3 best Little League Pokemon
**When to use**: Building LL teams, reviewing LL collection

---

### 26. Trophy Pokemon (Global Ranks)

**Name**: `Global Best`
**Query**: `#First,#Second,#Third`
**Purpose**: Pokemon that are #1, #2, or #3 best possible IVs in entire game
**When to use**: Show off trophy collection, track absolute best

---

### 27. Raid Attackers

**Name**: `Raid Teams`
**Query**: `#Attackers`
**Purpose**: Pokemon tagged as raid attackers
**When to use**: Building raid teams, checking raid readiness

---

### 28. Gym Defenders

**Name**: `Gym Defense`
**Query**: `#Def1,#Def2,#Def2.5`
**Purpose**: Pokemon tagged as gym defenders
**When to use**: Dropping in gyms, checking defender roster

---

## Evolution Queries

### 29. Special Evolution Candidates

**Name**: `Special Evolve`
**Query**: `#SpecialEvolve`
**Purpose**: Pokemon needing special evolution methods
**When to use**: Check evolution requirements

---

### 30. Item Evolution Candidates

**Name**: `Item Evolve`
**Query**: `#ItemEvolve`
**Purpose**: Pokemon needing evolution items
**When to use**: When you get evolution items

---

### 31. Location Evolution Candidates

**Name**: `Location Evolve`
**Query**: `#LocationEvolve`
**Purpose**: Pokemon needing specific locations to evolve
**When to use**: When traveling to special locations

---

### 32. Time Evolution Candidates

**Name**: `Time Evolve`
**Query**: `#TimeEvolve`
**Purpose**: Pokemon needing specific time/weather to evolve
**When to use**: Check before evolving during events

---

## Buddy System Queries

### 33. 1km Buddy Candidates

**Name**: `Buddy 1km`
**Query**: `#Buddy1Km&#NeedCandy`
**Purpose**: 1km buddies needing candy claims
**When to use**: Choose fast buddy for candy farming

---

### 34. 3km Buddy Candidates

**Name**: `Buddy 3km`
**Query**: `#Buddy3Km&#NeedCandy`
**Purpose**: 3km buddies needing candy claims
**When to use**: Medium-distance buddy planning

---

### 35. 5km Buddy Candidates

**Name**: `Buddy 5km`
**Query**: `#Buddy5Km&#NeedCandy`
**Purpose**: 5km buddies needing candy claims
**When to use**: Standard buddy planning

---

### 36. 20km Buddy Candidates

**Name**: `Buddy 20km`
**Query**: `#Buddy20Km&#NeedCandy`
**Purpose**: 20km buddies needing candy (legendaries/mythicals)
**When to use**: Long-term buddy projects

---

### 37. All Candy Claimable

**Name**: `Claim Candy`
**Query**: `#NeedCandy`
**Purpose**: All Pokemon with buddy distance ready to claim
**When to use**: Swap buddies to claim candy

---

## Form Variant Queries

### 38. Form Variant 1

**Name**: `Variant 1`
**Query**: `#Var1`
**Purpose**: Form variant 1 (e.g., Deoxys Attack)
**When to use**: Track forms query strings can't differentiate

---

### 39. Form Variant 2

**Name**: `Variant 2`
**Query**: `#Var2`
**Purpose**: Form variant 2 (e.g., Deoxys Defense)
**When to use**: Track forms query strings can't differentiate

---

## Summary: Query Categories

**Daily Workflow** (1-4): New catches, review queue, special review, legendary review
**Resource Management** (5-8): Buddy, power-up, TM, training
**Transfer & Trade** (9-16): Transfer queues, trade queues, lucky candidates, HOME queue
**Special Collections** (17-19): All specials, untagged specials, kept Pokemon
**Mega Evolution** (20-22): Mega ranks, mega levels, mega candidates
**PvP Ranks** (23-28): League bests, trophies, raid attackers, defenders
**Evolution** (29-32): Special/item/location/time evolution
**Buddy System** (33-37): Distance buddies, candy claims
**Form Variants** (38-39): Var1, Var2

---

## Quick Reference: Old → New Tag Names

| Old Tag Name    | New Tag Name    | Change Type           |
| --------------- | --------------- | --------------------- |
| `#currentbuddy` | `#CurrentBuddy` | PascalCase            |
| `#power up`     | `#PowerUp`      | PascalCase            |
| `#waiting`      | `#Review`       | Renamed               |
| `#to trade`     | `#Trade`        | Simplified            |
| `#kept`         | `#Kept`         | PascalCase            |
| `#home`         | `#Home`         | PascalCase            |
| `#luckies`      | N/A             | Deleted (use `lucky`) |
| `rank1`         | `#Rank1`        | Added `#`             |
| `mega`          | `#Mega`         | Added `#`             |
| `#buddy1km`     | `#Buddy1Km`     | PascalCase            |
| `#buddy3km`     | `#Buddy3Km`     | PascalCase            |
| `#buddy5km`     | `#Buddy5Km`     | PascalCase            |
| `#buddy20km`    | `#Buddy20Km`    | PascalCase            |
| `#var1`         | `#Var1`         | PascalCase            |
| `#var2`         | `#Var2`         | PascalCase            |

---

## Copy-Paste Quick Reference

For easy favoriting in Pokemon GO:

```
1. New Catches: !#
2. Review Queue: #Review
3. Special Review: #Review&!legendary&!mythical&!ultra beasts
4. Legendary Review: #Review&legendary,mythical,ultra beasts
5. Active Buddy: #CurrentBuddy
6. Power-Up Queue: #PowerUp
7. TM Queue: #TM
8. Training Projects: #InTraining
9. Transfer Now: #Transfer&!#Home
10. Event Transfer: #Home
11. All Transfers: #Transfer,#Home
12. Trade Queue: #Trade
13. Lucky Trades: #LuckyTrade
14. New Lucky Candidates: age364-&!#Trade&!#Kept&!#Home&!traded&!legendary&!mythical&!ultra beasts&!shiny&!costume&!shadow&!xxs&!xxl&!background&!4*
15. HOME Queue: #Home&mythical
16. New HOME Candidates: #Transfer&!#Home&mythical&151,251,385,386,491,492,494,647,648,649,718,719,720,802,893
17. All Specials: shiny,legendary,mythical,ultra beasts,costume,shadow,xxs,xxl,background,4*,@special,dynamax,gigantamax
18. Untagged Specials: !#&legendary,mythical,ultra beasts,xxs,xxl,costume,shiny,shadow,4*,dynamax,gigantamax,background
19. Kept Pokemon: #Kept
20. Mega First Evolve: megaevolve&#Rank1&mega0&#Mega
21. Mega Level Up: megaevolve&#Rank1&mega1&#Mega
22. Mega Candidates: megaevolve&#Mega
23. GL Top Ranks: #Great&#Rank1,#Rank2,#Rank3
24. UL Top Ranks: #Ultra&#Rank1,#Rank2,#Rank3
25. LL Top Ranks: #Little&#Rank1,#Rank2,#Rank3
26. Global Best: #First,#Second,#Third
27. Raid Teams: #Attackers
28. Gym Defense: #Def1,#Def2,#Def2.5
29. Special Evolve: #SpecialEvolve
30. Item Evolve: #ItemEvolve
31. Location Evolve: #LocationEvolve
32. Time Evolve: #TimeEvolve
33. Buddy 1km: #Buddy1Km&#NeedCandy
34. Buddy 3km: #Buddy3Km&#NeedCandy
35. Buddy 5km: #Buddy5Km&#NeedCandy
36. Buddy 20km: #Buddy20Km&#NeedCandy
37. Claim Candy: #NeedCandy
38. Variant 1: #Var1
39. Variant 2: #Var2
```

**Top 10 Most Useful** (recommended for limited favorite slots):

1. `!#` - New Catches
2. `#Review` - Review Queue
3. `#Transfer,#Home` - All Transfers
4. `#PowerUp` - Power-Up Queue
5. `#CurrentBuddy` - Active Buddy
6. `#LuckyTrade` - Lucky Trades
7. `#Trade` - Trade Queue
8. `#First,#Second,#Third` - Global Best
9. `#Great&#Rank1,#Rank2,#Rank3` - GL Top Ranks
10. `!#&legendary,mythical,ultra beasts,xxs,xxl,costume,shiny,shadow,4*,dynamax,gigantamax,background` - Untagged Specials

---

_Favorite Queries - Updated 2025-10-12 for new PascalCase tag system_
