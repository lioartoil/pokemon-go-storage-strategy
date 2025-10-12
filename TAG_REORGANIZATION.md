# Pokemon GO Tag Reorganization Guide

**Date**: 2025-10-12
**Current Tags**: 46 tags
**Target**: Streamlined hierarchy aligned with storage strategy

---

## Current Tag Analysis

### Current Tags (46 total)

**Evolution Status** (5 tags):
- `Basic`, `Stage 1`, `Stage 2`, `Final`
- `Baby`

**Evolution Methods** (3 tags):
- `Special Evolve`, `Item Evolve`, `Location Evolve`, `Time Evolve`

**Buddy Distance** (4 tags):
- `Buddy1km`, `Buddy3km`, `Buddy5km`, `Buddy20km`

**PvP Leagues** (3 tags):
- `Great`, `Ultra`, `Little`

**PvP Rankings** (5 tags):
- `Rank1`, `Rank2`, `Rank3`, `Rank4-19`, `Rank20-82`, `Rank83-205`

**Raid/Gym** (2 tags):
- `Attackers`, `Def1`, `Def2`, `Def2.5`

**Resource Management** (7 tags):
- `Need Candy`, `Need Purified`, `Double Candy`, `Power Up`
- `In Training`, `CurrentBuddy`
- `To Trade`

**Storage Workflow** (11 tags):
- `Home` (transfer queue)
- `Transfer`, `Kept`, `Archived`
- `Ready`, `Waiting`, `Candidates`
- `Aged`
- `First`, `Second`, `Third`

**Special Status** (4 tags):
- `Luckies`, `Mega`
- `var1`, `var2`

---

## Problems with Current System

### 1. Redundancy Issues

**Evolution Status Overlap**:
- `Basic`/`Stage 1`/`Stage 2`/`Final` are redundant with game's filter `evolve0`, `evolve1`, `evolve2`, `evolve3`
- **Impact**: Wasting 4/50 tag slots for info already in-game

**PvP League Overlap**:
- `Great`/`Ultra`/`Little` may overlap with `Rank1`-`Rank83-205`
- **Question**: Do ranked Pokemon automatically get both tags? (e.g., Rank1 + Great?)

**Workflow Confusion**:
- `Ready`, `Waiting`, `Candidates` - unclear distinctions
- `First`, `Second`, `Third` - purpose unclear (priority? evolution order?)
- `Kept` vs `Archived` - both seem permanent storage

### 2. Tag Limit Concerns

**Pokemon GO Tag Limits**:
- Maximum 50 tags per account
- Currently using 46/50 (92% capacity)
- Only 4 slots left for future needs

### 3. Alignment with Storage Strategy

**Missing Strategic Categories**:
- No explicit `Raid` tag (only `Attackers`)
- No `Shadow` tag (critical for raids)
- No `Collector` tag for 0%, 100%, XXS, XXL
- No `Trade Value` tag for rare/regional/shiny

**Vague Defense Tags**:
- `Def1`, `Def2`, `Def2.5` - what do these mean?
  - Different CP tiers (1500/2500/unlimited)?
  - Different gym types (normal/remote/raids)?
  - Different Pokemon quality levels?

### 4. Workflow Inefficiency

**Evolution Tracking**:
- 7 evolution-related tags but no clear workflow
- `Special Evolve` + `Item Evolve` + `Location Evolve` + `Time Evolve` = 4 tags for one action (evolving)

**Buddy System**:
- 4 distance tags + `CurrentBuddy` + `In Training` = 6 tags for buddy management
- Distance is already visible in-game

---

## Recommended Tag Reorganization

### Proposed System: 35 Tags (70% capacity)

This frees up 11 tag slots (46 → 35) while improving clarity.

#### Category 1: Core Functional (12 tags)

**PvP Rankings** (6 tags) - Keep these, they're efficient:
- `Rank1`, `Rank2`, `Rank3`, `Rank4-19`, `Rank20-82`, `Rank83-205`

**Battle Roles** (6 tags):
- `raid` - Raid attackers (replaces `Attackers`)
- `gym` - Gym defenders
- `rocket` - Rocket battle specialists
- `great` - Great League eligible (Rank 1-20)
- `ultra` - Ultra League eligible (Rank 1-20)
- `little` - Little League eligible (Rank 1-20)

**Rationale**:
- League tags now indicate "eligible for PvP" (Rank 1-20 only)
- Raid/Gym/Rocket are distinct battle contexts
- Drop `Def1`/`Def2`/`Def2.5` (replaced by `gym`)

#### Category 2: Resource Management (8 tags)

**Action Needed** (5 tags):
- `evolve` - Ready to evolve (replaces `Special Evolve`, `Item Evolve`, etc.)
- `candy` - Need candy to power up/evolve
- `purify` - Shadows to purify
- `tm` - Needs move changes (TM/Elite TM)
- `power` - Ready to power up

**Buddy System** (2 tags):
- `buddy` - Current buddy (replaces `CurrentBuddy`)
- `walk` - Needs buddy distance (replaces `In Training` + distance tags)

**Trading** (1 tag):
- `trade` - For trade (replaces `To Trade`)

**Rationale**:
- Combine 4 evolution method tags → 1 `evolve` tag
- Drop distance tags (visible in-game)
- Add `tm` tag (commonly needed)

#### Category 3: Storage Workflow (7 tags)

**Transfer Pipeline**:
- `home` - Transfer queue (keep during 2× candy events)
- `transfer` - Marked for immediate transfer

**Keepers**:
- `keep` - Permanent keep (replaces `Kept`)
- `lucky` - Lucky Pokemon (replaces `Luckies`)
- `mega` - Mega-capable (replaces `Mega`)

**Review Pipeline**:
- `review` - Needs decision (replaces `Candidates`)
- `archive` - Old event Pokemon (replaces `Archived`)

**Rationale**:
- Drop `Ready`/`Waiting`/`First`/`Second`/`Third` (unclear purpose)
- Drop `Aged` (redundant with `archive`)
- Simplify to 3-stage workflow: review → keep/transfer → home (if transfer)

#### Category 4: Special Categories (8 tags)

**Collector Values**:
- `hundo` - 100% IV (0★ or 4★)
- `nundo` - 0% IV (0★)
- `shundo` - Shiny 100%
- `xxs` - XXS size
- `xxl` - XXL size

**Trade Value**:
- `regional` - Regional exclusives
- `legacy` - Legacy moves (@special)

**Event**:
- `event` - Current event featured Pokemon

**Rationale**:
- These are collection-focused tags
- High trade value or personal collecting goals
- Drop `var1`/`var2` (unclear purpose)

---

## Tag Migration Guide

### Step 1: Create New Tags (Week 1)

**Add these 35 tags** (in-game Settings → Manage Tags):

```
Core Functional (12):
raid, gym, rocket, great, ultra, little
Rank1, Rank2, Rank3, Rank4-19, Rank20-82, Rank83-205

Resource Management (8):
evolve, candy, purify, tm, power
buddy, walk, trade

Storage Workflow (7):
home, transfer, keep, lucky, mega
review, archive

Special Categories (8):
hundo, nundo, shundo, xxs, xxl
regional, legacy, event
```

### Step 2: Migrate Old Tags (Week 2-3)

#### Migration 1: Evolution Tags → `evolve`

**Old tags to merge**:
- `Special Evolve` → `evolve`
- `Item Evolve` → `evolve`
- `Location Evolve` → `evolve`
- `Time Evolve` → `evolve`

**In-game search**:
```
Special Evolve | Item Evolve | Location Evolve | Time Evolve
```

**Action**: Select all → Add tag `evolve` → Remove old tags

**Estimated**: 100-200 Pokemon

#### Migration 2: Buddy Tags → `walk`

**Old tags to merge**:
- `Buddy1km` → `walk`
- `Buddy3km` → `walk`
- `Buddy5km` → `walk`
- `Buddy20km` → `walk`
- `In Training` → `walk`

**In-game search**:
```
Buddy1km | Buddy3km | Buddy5km | Buddy20km | In Training
```

**Action**: Select all → Add tag `walk` → Remove old tags

**Estimated**: 50-100 Pokemon

#### Migration 3: Current Buddy → `buddy`

**Old tag**: `CurrentBuddy` → `buddy`

**In-game search**: `CurrentBuddy`

**Action**: Retag as `buddy`, remove old

**Estimated**: 1 Pokemon

#### Migration 4: Defense Tags → `gym`

**Old tags to merge**:
- `Def1` → `gym`
- `Def2` → `gym`
- `Def2.5` → `gym`

**QUESTION FIRST**: What do these defense tiers mean?
- If different CP tiers: Consider keeping separate?
- If gym vs remote vs raids: Merge to `gym`
- If quality tiers: Use ranks instead?

**In-game search**:
```
Def1 | Def2 | Def2.5
```

**Action**: TBD based on your clarification

**Estimated**: 50-200 Pokemon

#### Migration 5: Attackers → `raid`

**Old tag**: `Attackers` → `raid`

**In-game search**: `Attackers`

**Action**: Retag as `raid`, remove old

**Estimated**: 100-200 Pokemon

#### Migration 6: League Tags (Keep or Refine?)

**Current tags**: `Great`, `Ultra`, `Little`

**QUESTION**: Do these mean:
- A) "Has ANY PvP rank in this league" (Rank 1-4096)
- B) "Has GOOD PvP rank in this league" (Rank 1-20)
- C) "Currently assigned to this league team" (6 Pokemon max)

**Recommendation**:
- If A: Too broad, drop these tags
- If B: Keep as `great`, `ultra`, `little` (lowercase for consistency)
- If C: Rename to `team-great`, `team-ultra`, `team-little`

**Estimated**: 1,000-3,000 Pokemon (if A), 100-300 (if B), 6-18 (if C)

#### Migration 7: Storage Workflow

**Old → New mappings**:
- `Home` → `home` (keep as-is, just lowercase)
- `Transfer` → `transfer` (keep as-is)
- `Kept` → `keep` (rename for consistency)
- `Luckies` → `lucky` (rename for consistency)
- `Archived` → `archive` (rename for consistency)
- `Candidates` → `review` (clearer purpose)
- `Ready` → DROP (or clarify purpose?)
- `Waiting` → DROP (or clarify purpose?)
- `Aged` → merge with `archive`?
- `First`, `Second`, `Third` → DROP (or clarify purpose?)

**Questions**:
1. What does `Ready` mean? (Ready for what?)
2. What does `Waiting` mean? (Waiting for what?)
3. What are `First`, `Second`, `Third` for? (Priority? Evolution order?)

#### Migration 8: Evolution Stage Tags → DROP

**Old tags to DELETE**:
- `Basic`, `Stage 1`, `Stage 2`, `Final`, `Baby`

**Rationale**: Use in-game filters instead:
- `evolve0` = Basic stage
- `evolve1` = Stage 1
- `evolve2` = Stage 2
- `evolve3` = Final evolution
- `baby` = Baby Pokemon

**Action**: Just delete these tags (info already in-game)

#### Migration 9: Special Status

**Old → New mappings**:
- `Mega` → `mega` (keep, but lowercase)
- `Luckies` → `lucky` (rename)
- `Need Candy` → `candy` (rename)
- `Need Purified` → `purify` (rename)
- `Double Candy` → DROP (use event tracker instead)
- `Power Up` → `power` (rename)
- `To Trade` → `trade` (rename)

#### Migration 10: Mystery Tags

**QUESTIONS**:
1. What is `var1` used for?
2. What is `var2` used for?

**Action**: Clarify before migrating

---

## Comparison: Before vs After

| Category | Before (46 tags) | After (35 tags) | Change |
| -------- | ---------------- | --------------- | ------ |
| **Evolution** | 8 tags (Basic, Stage 1-2, Final, Baby, Special/Item/Location/Time Evolve) | 1 tag (evolve) | -7 tags ✅ |
| **Buddy** | 6 tags (1km/3km/5km/20km, CurrentBuddy, In Training) | 2 tags (buddy, walk) | -4 tags ✅ |
| **PvP Leagues** | 3 tags (Great, Ultra, Little) | 3 tags (great, ultra, little) | No change |
| **PvP Ranks** | 5 tags (Rank1-3, Rank4-19, Rank20-82, Rank83-205) | 6 tags (+Rank83-205) | +0 tags |
| **Battle Roles** | 4 tags (Attackers, Def1, Def2, Def2.5) | 3 tags (raid, gym, rocket) | -1 tag ✅ |
| **Resources** | 4 tags (Need Candy, Need Purified, Power Up, Double Candy) | 5 tags (candy, purify, power, tm, evolve) | +1 tag |
| **Workflow** | 11 tags (Home, Transfer, Kept, etc.) | 7 tags (home, transfer, keep, review, archive, lucky, mega) | -4 tags ✅ |
| **Special** | 2 tags (var1, var2) | 8 tags (hundo, nundo, shundo, xxs, xxl, regional, legacy, event) | +6 tags |
| **TOTAL** | **46 tags (92%)** | **35 tags (70%)** | **-11 tags ✅** |

**Benefits**:
- ✅ Frees 11 tag slots (22% capacity freed)
- ✅ Clearer naming conventions (lowercase, consistent)
- ✅ Better alignment with storage strategy
- ✅ Reduces redundancy with in-game filters
- ✅ Adds missing categories (hundo, nundo, tm, rocket, regional)

---

## Questions Before Finalizing

### Critical Questions

1. **Defense Tags**: What do `Def1`, `Def2`, `Def2.5` represent?
   - Different CP tiers?
   - Different quality levels?
   - Different purposes (gym vs raids)?

2. **League Tags**: What do `Great`, `Ultra`, `Little` mean?
   - A) Any PvP rank (1-4096)?
   - B) Good PvP rank (1-20)?
   - C) Current team assignment?

3. **Workflow Tags**: What do these mean?
   - `Ready` - Ready for what action?
   - `Waiting` - Waiting for what event/resource?
   - `First`, `Second`, `Third` - Priority levels? Evolution order?
   - `Aged` - Different from `Archived`?
   - `Candidates` - Candidates for what? (transfer? power up? evolution?)

4. **Variable Tags**: What are these for?
   - `var1` - Purpose?
   - `var2` - Purpose?

5. **Buddy Distance Tags**: Do you use these to prioritize buddies?
   - If yes: Maybe keep 1 tag like `buddy-priority`?
   - If no: Safe to remove?

6. **Double Candy Tag**: Is this for events or for specific Pokemon?
   - If events: Better to use in-game event tracker
   - If specific species: Maybe keep?

### Optional Questions

7. Do you want separate tags for:
   - Shadow Pokemon? (critical for raids)
   - Purified Pokemon? (different from `purify`)
   - Costume Pokemon? (blocking evolution)

8. Do you care about:
   - XL Candy needs? (different from regular candy)
   - Best Buddy status? (CP boost)
   - Community Day moves? (different from legacy)

9. How do you currently use:
   - `To Trade` - For yourself or for others?
   - `Archived` - Truly permanent or periodic review?
   - `Kept` - Different from not having `transfer` tag?

---

## Implementation Timeline

### Week 1: Setup (1-2 hours)
- [ ] Answer clarifying questions above
- [ ] Create 35 new tags in-game
- [ ] Test new tags on 5-10 Pokemon

### Week 2: Migration Phase 1 (2-3 hours)
- [ ] Migrate evolution tags → `evolve`
- [ ] Migrate buddy tags → `walk`, `buddy`
- [ ] Migrate attacker tags → `raid`
- [ ] Test searches work correctly

### Week 3: Migration Phase 2 (2-3 hours)
- [ ] Migrate defense tags → `gym` (after clarification)
- [ ] Migrate workflow tags → new system (after clarification)
- [ ] Migrate special tags → `lucky`, `mega`, etc.
- [ ] Test workflow still functions

### Week 4: Cleanup (1 hour)
- [ ] Delete old unused tags
- [ ] Verify no Pokemon lost tags
- [ ] Update any external documentation
- [ ] Backup tag list for future reference

### Week 5: Testing (ongoing)
- [ ] Use new system for 1 week
- [ ] Identify pain points
- [ ] Adjust as needed

**Total Time**: 6-9 hours over 5 weeks

---

## Backup Plan

Before deleting ANY tags:

1. **Export Current Tags** (take screenshots):
   - Settings → Manage Tags → Screenshot full list
   - For each tag, search and screenshot count

2. **Document Current Usage** (create CSV):
   ```csv
   Tag Name,Count,Purpose,Keep/Merge/Delete
   Attackers,152,Raid attackers,Merge to 'raid'
   Def1,89,Defense tier 1,TBD (need clarification)
   ...
   ```

3. **Test Migration on 10 Pokemon First**:
   - Pick 10 diverse Pokemon
   - Migrate their tags manually
   - Verify searches work
   - Only then batch-migrate

4. **Keep Old Tags for 1 Week After Migration**:
   - Don't delete immediately
   - Run parallel systems
   - Verify nothing broken
   - Then delete old tags

---

## Next Steps

**I need your input on these questions** before I can finalize the migration guide:

1. What do `Def1`, `Def2`, `Def2.5` represent?
2. What do `Great`, `Ultra`, `Little` mean (A/B/C above)?
3. What do `Ready`, `Waiting`, `First`/`Second`/`Third`, `Aged`, `Candidates` mean?
4. What are `var1` and `var2` used for?
5. Do you want to keep buddy distance prioritization?
6. Do you want separate tags for Shadow/Costume Pokemon?

Once you answer these, I can:
- Finalize the tag list
- Create detailed migration steps
- Generate search queries for each migration
- Estimate Pokemon counts per tag

---

_Tag Reorganization Guide - Created 2025-10-12_
