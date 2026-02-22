# Master League Reduction - Detailed Checklist

**Created**: 2026-01-18
**Revised**: 2026-02-06 (Updated raid attacker queries — added 11 new attackers)
**Target**: Free 300-400 slots
**Time Required**: 2-4 hours
**Difficulty**: ⚠️ Medium (requires PokeGenie IV rank scanning)

---

## Collector-First Principle

**⚠️ IMPORTANT: This checklist protects 4★ Pokemon and uses IV Rank for decisions.**

### **Why 4★ Are Protected**

| Fact | Implication |
|------|-------------|
| 4★ = 15/15/15 IVs | Always Rank 1 IVs for Master League |
| 1/4096 catch odds (wild) | Extremely rare collector trophies |
| Your 265 4★ = 2.4% storage | Small footprint, high value |

**Conclusion**: KEEP ALL 4★ as collector trophies. Target duplicates with IV Rank >20.

---

## Overview

This checklist provides step-by-step instructions for reducing Master League Pokemon based on **IV Rank** to free 300-400 storage slots.

**IV Rank Retention Rules** (from STRATEGY_REVISIONS_FINAL.md):

| IV Rank | Action | Rationale |
|---------|--------|-----------|
| Rank ≤10 | Keep up to 2 copies | Best IVs for that species |
| Rank 11-20 | Keep 1 copy | Good IVs, worth keeping |
| Rank >20 | Transfer | Inferior duplicates |

**What You'll Do**:
1. Find Master League candidates (NOT 4★, NOT protected categories)
2. Scan each with PokeGenie for **IV Rank**
3. Transfer: IV Rank >20 duplicates
4. Reduce: IV Rank 11-20 to 1 copy each
5. Keep: IV Rank ≤10 up to 2 copies each

---

## Prerequisites

Before starting, verify:

- [ ] ✅ PokeGenie app installed and Name Generators configured
- [ ] ✅ Raid attackers tagged with `#Attackers` in Pokemon GO
- [ ] ✅ You've cleared transfer queue (Priority 1) for practice
- [ ] ✅ You have 2-4 hours of uninterrupted time
- [ ] ✅ Phone battery >80% or charger nearby

**⚠️ CRITICAL**: If raid attackers are NOT tagged yet, STOP and tag them first. Use these queries:

**Non-Shadow Query** (48 species):
```
!shadow&alakazam,beedrill,blacephalon,blaziken,charizard,deoxys,dialga,diancie,eternatus,garchomp,gardevoir,gengar,groudon,heatran,heracross,hoopa,hydreigon,kartana,keldeo,kyogre,kyurem,landorus,lucario,lunala,metagross,mewtwo,necrozma,palkia,pheromosa,pinsir,rampardos,rayquaza,regieleki,regigigas,reshiram,salamence,sceptile,scizor,swampert,terrakion,tyranitar,volcarona,xerneas,xurkitree,yveltal,zacian,zamazenta,zekrom
```

**Shadow Query** (37 species):
```
shadow&alakazam,blaziken,chandelure,conkeldurr,darkrai,darmanitan,dialga,dragonite,electivire,excadrill,garchomp,gardevoir,gengar,groudon,heatran,honchkrow,kyogre,latios,machamp,magnezone,mamoswine,metagross,mewtwo,moltres,palkia,raikou,rampardos,regigigas,rhyperior,salamence,staraptor,swampert,tangrowth,toxicroak,tyranitar,weavile,zapdos
```

Tag all results with `#Attackers` tag.

---

## Step-by-Step Process

### **Phase 1: Setup & Initial Filtering (15 minutes)**

#### Step 1.1: Open Pokemon GO and Create Working Tag

**Action**: Create a temporary tag for today's work

1. Open Pokemon GO
2. Go to Pokemon storage
3. Tap magnifying glass (search)
4. Tap tag icon
5. Create new tag: `MLReview` (Master League Review)

**Why**: This tag helps you mark candidates for review without transferring immediately.

---

#### Step 1.2: Run Initial Search Query

**Search Query** (copy exactly):
```
3*&!4*&!lucky&!shiny&!costume&!shadow&!@special&!legendary&!mythical&!ultra beasts&!great&!ultra&!little&!#Attackers&!home&!transfer&!xxs&!xxl&!background&!gigantamax&!dynamax&!#rank1&!#rank2&!#rank3&!#rank4-20&!#rank21-50&!#rank51-100&cp2500-
```

**What this finds**:
- ✅ 3★ (82.2-97.8% IV) Pokemon - good but not collector trophies
- ✅ **NOT 4★** - these are protected as collector trophies
- ✅ Regular (not special in any way)
- ✅ NOT already used in other leagues
- ✅ NOT raid attackers
- ✅ NOT legendaries/mythicals/ultra beasts
- ✅ NOT in transfer/trade queues (Categories 12 & 14)
- ✅ NOT XXS/XXL size extremes (Category 7)
- ✅ NOT Background (Category 8), Gigantamax (Category 9), Dynamax (Category 10)
- ✅ CP 2500+ capable (Master League relevant)

**Expected Results**: 100-300 Pokemon (varies by your collection)

**If you get 0 results**: Your collection is already well-organized! All Master League Pokemon have been reviewed. Instead:
1. Search for already-tagged transfer candidates: `#rank21-50,#rank51-100&!great&!ultra&!little&!lucky&!#Attackers&!gigantamax&!dynamax&!@special&!legendary&!mythical`
2. Review results: Only transfer if you have BETTER duplicates of that species (Rank 21+ doesn't mean auto-transfer if it's your best one)
3. If no transfer candidates, skip to other priorities (see QUICK_WIN_STRATEGY.md)

**Action**: Tag all results with `MLReview`

1. Tap first Pokemon
2. Swipe through each one quickly
3. For each: Tap tag icon → Select `MLReview`
4. Move to next

**Time**: 10-15 minutes for 100 Pokemon

---

#### Step 1.3: Verify Search Results

**Action**: Spot-check a few Pokemon to ensure query worked

**Good Examples** (should be in results):
- Regular Snorlax (3★) - low-meta, transfer candidate
- Regular Slaking (3★) - low-meta, transfer candidate
- Regular Hippowdon (3★) - low-meta, transfer candidate

**Bad Examples** (should NOT be in results):
- Any 4★ Pokemon (excluded by `!4*` - **collector trophies**)
- Shadow Mewtwo (excluded by `!shadow`)
- Lucky Dragonite (excluded by `!lucky`)
- Shiny Rayquaza (excluded by `!shiny`)
- Costume Pikachu (excluded by `!costume`)
- Lucario (excluded by `!#Attackers`)
- Azumarill tagged `great` (excluded by `!great`)

**If you see 4★ Pokemon**: Your search query is wrong. Make sure `!4*` is included. 4★ are PROTECTED.

**If you see other bad examples**: Re-check the query and re-run.

---

### **Phase 2: PokeGenie IV Rank Scanning (1-2 hours)**

**Key Insight**: We check **IV Rank within species**, NOT species meta ranking.

**Why IV Rank?**
- IV Rank tells you how good THIS Pokemon's IVs are compared to others of the same species
- You're a collector, not a competitive PvP player
- Keep your best specimens, transfer inferior duplicates
- Species meta ranking is irrelevant if you don't do PvP

**IV Rank Retention Rules**:

| IV Rank | Action | Example |
|---------|--------|---------|
| Rank ≤10 | Keep up to 2 copies | Snorlax IV Rank 5 → KEEP |
| Rank 11-20 | Keep 1 copy | Snorlax IV Rank 15 → Keep 1 |
| Rank >20 | Transfer | Snorlax IV Rank 50 → TRANSFER |

---

#### Step 2.1: Set Up PokeGenie Scanning

**Action**: Open PokeGenie, prepare for batch scanning

1. Open PokeGenie app
2. Tap "Scan" button
3. Switch to Pokemon GO
4. Search: `#MLReview` (shows only tagged Pokemon)

**You should see**: The Pokemon you tagged in Phase 1

---

#### Step 2.2: Scan and Tag by IV Rank

**Workflow** (for each Pokemon in `#MLReview`):

1. **In Pokemon GO**: Tap a Pokemon from `#MLReview` results
2. **PokeGenie auto-scans**: Wait 2-3 seconds for scan overlay
3. **Check Master League IV Rank**: Look at "Master League" section in overlay
   - If **IV Rank ≤10**: Tag with `MLKeep2` (keep up to 2 copies)
   - If **IV Rank 11-20**: Tag with `MLKeep1` (keep 1 copy)
   - If **IV Rank >20**: Tag with `MLTransfer` (transfer candidate)
4. **Move to next**: Swipe left to next Pokemon, repeat

**Pro Tips**:
- **Speed scanning**: PokeGenie scans automatically when you open Pokemon details
- **Batch tagging**: Scan 10-20 Pokemon, then tag them all at once
- **Group by species**: When reducing duplicates, keep best IV Rank, transfer rest
- **Take breaks**: Do 25 Pokemon, take 5 min break, repeat

**Time Estimate**:
- 100 Pokemon: 45 min - 1 hour
- 200 Pokemon: 1.5-2 hours
- 300 Pokemon: 2-3 hours

---

#### Step 2.3: Track Your Findings

**Optional but recommended**: Keep a tally on paper or notes app

| Category | Count | Tag |
|----------|-------|-----|
| IV Rank ≤10 (Keep 2) | ??? | `MLKeep2` |
| IV Rank 11-20 (Keep 1) | ??? | `MLKeep1` |
| IV Rank >20 (Transfer) | ??? | `MLTransfer` |

**Why track**: Helps you estimate total slots you'll free

**Estimated savings**:
- Each Rank 21+ = 1 Pokemon transferred = 1 slot
- Each Rank 11-20 with duplicates = 0-2 slots (depends on copies you have)
- Each Rank ≤10 with 3+ copies = 1+ slots

**Expected totals** (from your 50-150 candidates):
- Rank 21+: 30-60 Pokemon → **30-60 slots**
- Rank 11-20 duplicates: 10-30 Pokemon → **10-30 slots**
**Expected savings from 3★ low-meta species**: 200-400 slots

---

#### Step 2.4: Expand to 2★ and Lower (Optional - More Slots)

**Why**: 2★ and lower Pokemon have even less collector value

**New Search Query**:
```
!4*&!3*&!lucky&!shiny&!costume&!shadow&!@special&!legendary&!mythical&!ultra beasts&!great&!ultra&!little&!#Attackers&!home&!transfer&!xxs&!xxl&!background&!gigantamax&!dynamax&!#rank1&!#rank2&!#rank3&!#rank4-20&!#rank21-50&!#rank51-100&cp2500-
```

**What this finds**:
- 2★ and lower (0-82.2% IVs) - minimal collector value
- Master League capable (CP 2500+)
- NOT protected categories (all 14 categories excluded)

**Expected Results**: 50-200 Pokemon

**Action**:
1. Tag all results with `MLReview2`
2. These are almost all transfer candidates (low IVs, not special)
3. Keep 1 of each species if you want (for Pokedex living dex)
4. Transfer duplicates and extras freely

**Expected additional savings from 2★ and lower**: 50-150 slots

**TOTAL EXPECTED (3★ + 2★ and lower)**: 250-550 slots ✅

---

**Note on 4★ Pokemon**:

Your 4★ Pokemon are **completely excluded** from this process. They are:
- Protected as collector trophies
- Always Rank 1 IVs for Master League
- Not worth the 2.4% storage they use to sacrifice

---

### **Phase 3: Safety Verification (15 minutes)**

#### Step 3.1: Double-Check Transfer Candidates

**Search**: `#MLTransfer`

**For EACH Pokemon, verify** (spot-check 10-20 randomly):

- [ ] **NOT 4★ (100% IV)** ← MOST IMPORTANT - collector trophies, NEVER transfer
- [ ] NOT shiny (should be filtered, but double-check)
- [ ] NOT shadow (should be filtered, but double-check)
- [ ] NOT legendary/mythical (should be filtered, but double-check)
- [ ] NOT tagged `#Attackers` (should be filtered, but double-check)
- [ ] NOT tagged `great`, `ultra`, `little` (should be filtered, but double-check)
- [ ] IS final evolution (e.g., Snorlax, not Munchlax)
- [ ] IS low-meta species (Rank 50+ in Master League meta)

**Common safe transfers** (3★ and lower of these species):
- Snorlax (Meta Rank 148)
- Slaking (Meta Rank 380)
- Hippowdon
- Cloyster
- Kingler

**RED FLAGS** (should NOT be in transfer list):
- **ANY 4★ Pokemon** ← STOP IMMEDIATELY, remove from list
- Any shadow Pokemon
- Any legendary (Mewtwo, Rayquaza, etc.)
- Lucario, Machamp, Garchomp (raid attackers)
- Anything with `@special` move
- Azumarill, Medicham, Bastiodon (Great League meta)

**If you see a 4★**: STOP → Remove it → It should never have been in the list
**If you see other red flags**: Remove from `MLTransfer` tag immediately

---

#### Step 3.2: Final Evolution Check

**Why**: You should only transfer **final evolutions** from Rank 21+ list

**Action**: Search `#MLTransfer`, look for any middle evolutions

**Examples of middle evolutions** (should NOT be transferred):
- Dragonair (middle evolution, keep 2)
- Zweilous (middle evolution, keep 2)
- Sligoo (middle evolution, keep 2)
- Hakamo-o (middle evolution, keep 2)

**If you find middle evolutions**:
1. Remove from `MLTransfer` tag
2. Keep 2 copies for future-proofing
3. These have potential for future releases or move updates

---

#### Step 3.3: Species Duplication Check

**Action**: Sort `MLTransfer` results by Pokemon name

**Look for**: Same species appearing multiple times

**Decision tree**:

1. **If same species, same rank** (e.g., 2× Snorlax both Rank 135):
   - Keep best IVs (if IVs differ slightly)
   - OR keep lowest CP (saves dust if you ever want to max it)
   - Transfer the other(s)

2. **If same species, different ranks** (e.g., Snorlax Rank 30 and Rank 80):
   - KEEP Rank 30 (better, even though both >21)
   - Transfer Rank 80

**Why**: No need to keep multiple copies of Rank 21+ Pokemon

---

### **Phase 4: Execute Transfers (30-60 minutes)**

#### Step 4.1: Transfer Rank 21+ Pokemon

**Search**: `#MLTransfer` or `#T`

**Expected**: 30-250 Pokemon (depending on 4★ only vs 4★+3★)

**⚠️ FINAL SAFETY CHECK**:

Before transferring, ask yourself:
- Am I 100% certain these are all Rank 21+ final evolutions?
- Did I double-check for shadows, legendaries, raid attackers?
- Am I okay with permanently losing these Pokemon?

**If YES to all → Proceed**

**Transfer Workflow**:

1. **Small batches**: Transfer 10-20 at a time, not all at once
2. **Verify each batch**:
   - Tap first Pokemon
   - Swipe through the batch
   - Confirm all are safe to transfer
3. **Transfer**:
   - Tap ☰ menu
   - Select "Transfer"
   - Confirm
4. **Repeat** for next batch

**Why small batches**: If you make a mistake, you only lose 10-20 Pokemon, not all 250

**Time**: 30-60 minutes for 200-250 Pokemon

**Result**: **30-250 slots freed** ✅

---

#### Step 4.2: Reduce Rank 11-20 to 1 Copy

**Search**: `#MLReduce1` or `#R1`

**For each species**:

1. **Count copies**: How many of this species do you have?
   - If 1 copy → KEEP, remove tag
   - If 2+ copies → Proceed to step 2

2. **Choose best copy**:
   - Highest IVs (if small difference)
   - OR lowest CP (saves dust)
   - OR best moveset (has @special move or good raid moves)

3. **Transfer extras**: Keep 1, transfer rest

**Example**:
- You have 3× Gyarados, all Rank 15
- Compare IVs: 15/15/15, 15/14/15, 15/15/14
- Keep 15/15/15 (perfect)
- Transfer other 2

**Expected**: 10-100 Pokemon transferred (depends on duplicates you have)

**Result**: **10-100 slots freed** ✅

---

#### Step 4.3: Reduce Rank ≤10 to 2 Copies

**Search**: `#MLReduce2` or `#R2`

**For each species**:

1. **Count copies**: How many of this species do you have?
   - If 1-2 copies → KEEP, remove tag
   - If 3+ copies → Proceed to step 2

2. **Choose best 2 copies**:
   - Highest IVs (top 2)
   - OR 1 maxed + 1 low CP (flexibility)
   - OR 1 with @special + 1 with normal moveset

3. **Transfer extras**: Keep 2, transfer rest

**Example**:
- You have 4× Metagross, all Rank 5
- IVs: 15/15/15, 15/15/14, 15/14/15, 14/15/15
- Keep: 15/15/15 + 15/15/14 (best 2 IVs)
- Transfer: 15/14/15 + 14/15/15

**Expected**: 10-50 Pokemon transferred

**Result**: **10-50 slots freed** ✅

---

### **Phase 5: Cleanup & Verification (15 minutes)**

#### Step 5.1: Remove Temporary Tags

**Action**: Delete the temporary tags you created

1. Search: `#MLReview` → Select all → Remove tag → Delete tag
2. Search: `#MLReview3` → Select all → Remove tag → Delete tag
3. Search: `#MLTransfer` → Should be empty (all transferred) → Delete tag
4. Search: `#MLReduce1` → Should be empty (all reduced) → Delete tag
5. Search: `#MLReduce2` → Should be empty (all reduced) → Delete tag

**Why**: Keeps your tag system clean

---

#### Step 5.2: Count Your Savings

**Action**: Check your storage numbers

1. Go to Pokemon storage screen
2. Look at top-right corner: `X / 11,325`
3. Calculate free space: `11,325 - X = FREE`

**Before Master League Reduction**: ~304 free
**After Master League Reduction**: ??? free

**Expected gain**: 300-400 slots

**Math check**:
- If you started with 11,021 Pokemon
- If you freed 300-400 slots
- You should now have: 10,621-10,721 Pokemon
- Free space: 604-704 slots (~5-6%)

**If your numbers are close to expected** → SUCCESS ✅

---

#### Step 5.3: Celebrate & Document

**You just freed 300-400 slots!** 🎉

**Action**: Update your progress tracking

1. Note new storage count
2. Update `QUICK_WIN_STRATEGY.md` if you're tracking there
3. Take a break - you earned it!

---

## Troubleshooting

### **Problem**: "I can't find many Rank 21+ Pokemon"

**Possible causes**:
1. Your Master League Pokemon are already well-optimized
2. Most of your 4★ Pokemon are raid attackers (properly tagged)
3. You don't have many Master League eligible Pokemon

**Solutions**:
- Expand to 3★ Pokemon (Step 2.4)
- Check Great/Ultra League instead (Priority 7-8 in Quick-Win Strategy)
- This is actually GOOD - it means you've been selective already

---

### **Problem**: "PokeGenie shows different ranks in different leagues"

**Example**: Snorlax is Rank 135 in Master League but Rank 5 in Great League

**Solution**:
- If it's Rank ≤20 in ANY league, KEEP IT (even if Rank 21+ in Master)
- The search query `!great&!ultra&!little` should have filtered these out
- If you see this, the Pokemon might not be properly tagged in-game

**Action**:
1. Tag it with appropriate league tag (`great`, `ultra`, or `little`)
2. Remove from Master League transfer candidates
3. Keep it for the league where it's Rank ≤20

---

### **Problem**: "I accidentally transferred something I wanted"

**Bad news**: You cannot reverse transfers in Pokemon GO

**Prevention**:
- ALWAYS transfer in small batches (10-20 at a time)
- ALWAYS do final safety check before each batch
- When in doubt, DON'T transfer - tag it for later review

**Lesson**: This is why we have extensive safety checks

---

### **Problem**: "This is taking too long"

**Solutions**:

**Option 1: Do only 4★ Pokemon** (30-60 slots, 1 hour)
- Skip 3★ scanning (Step 2.4)
- Do 3★ in Week 2 instead

**Option 2: Do fewer batches** (per day)
- Day 1: Scan 50 Pokemon (30 min)
- Day 2: Scan 50 Pokemon (30 min)
- Day 3: Transfer all (30 min)

**Option 3: Reduce scanning thoroughness**
- Only scan Pokemon you recognize as low-ranked
- Trust your intuition more (e.g., Snorlax is obviously not top tier)

---

### **Problem**: "PokeGenie won't scan / crashes"

**Common causes**:
1. Overlay permission disabled
2. App needs update
3. Phone RAM full

**Solutions**:
1. Reinstall PokeGenie
2. Restart phone
3. Enable overlay permission in phone settings
4. Update PokeGenie to latest version

---

## Expected Results Summary

### **By The Numbers**

| Pokemon Group | Starting | Transferred | Remaining | Slots Freed |
|---------------|----------|-------------|-----------|-------------|
| 4★ Rank 21+ | 30-60 | 30-60 | 0 | 30-60 |
| 3★ Rank 21+ | 150-250 | 150-250 | 0 | 150-250 |
| Rank 11-20 duplicates | 60-130 | 10-100 | 50-30 | 10-100 |
| Rank ≤10 extras | 30-70 | 10-50 | 60-40 | 10-50 |
| **TOTAL** | **270-510** | **200-460** | **110-70** | **200-460** |

**Conservative estimate**: 200-300 slots freed
**Optimistic estimate**: 300-460 slots freed
**Average**: ~300-400 slots freed ✅

---

### **Storage Status**

**Before**:
- Pokemon: 11,021 / 11,325
- Free: 304 slots (~2.7%)
- Status: ⚠️ CRITICAL for Community Day player

**After**:
- Pokemon: 10,561-10,821 / 11,325
- Free: 504-764 slots (~4.5-6.7%)
- Status: ⚠️ Still tight, but breathing room gained

**Next step**:
- Combine with Priority 1 (transfer queue +76 slots)
- Combine with Priority 4-6 (lucky/event/evolution cleanup +250-450 slots)
- **Total after Week 1**: 1,034-1,384 free slots (~9-12%) ✅

---

## Quick Reference (Collector-First)

### **Search Queries**

**3★ Master League candidates** (primary target):
```
3*&!4*&!lucky&!shiny&!costume&!shadow&!@special&!legendary&!mythical&!ultra beasts&!great&!ultra&!little&!#Attackers&!home&!transfer&!xxs&!xxl&!background&!gigantamax&!dynamax&!#rank1&!#rank2&!#rank3&!#rank4-20&!#rank21-50&!#rank51-100&cp2500-
```

**2★ and lower candidates** (secondary target):
```
!4*&!3*&!lucky&!shiny&!costume&!shadow&!@special&!legendary&!mythical&!ultra beasts&!great&!ultra&!little&!#Attackers&!home&!transfer&!xxs&!xxl&!background&!gigantamax&!dynamax&!#rank1&!#rank2&!#rank3&!#rank4-20&!#rank21-50&!#rank51-100&cp2500-
```

**4★ Pokemon** (NEVER TRANSFER - collector trophies):
```
4*
```
Use this query only to VERIFY they're excluded from transfer candidates.

**View transfer candidates**:
```
#MLTransfer
```

---

### **Decision Flow (Collector-First)**

```
Is it 4★ (100% IV)?
        ↓
   ┌────┴────┐
   ↓         ↓
  YES        NO
   ↓         ↓
 KEEP     Check IV Rank (PokeGenie)
(trophy)      ↓
         ┌────┼────┬────┐
         ↓    ↓    ↓    ↓
       ≤10  11-20  >20
         ↓    ↓    ↓
      Keep 2 Keep 1 TRANSFER
```

---

### **Safety Checklist** (Use before EVERY transfer batch)

Before transferring, verify Pokemon is:
- [ ] **NOT 4★ (100% IV)** ← MOST IMPORTANT - collector trophy
- [ ] NOT shiny
- [ ] NOT shadow
- [ ] NOT legendary/mythical/ultra beast
- [ ] NOT costume
- [ ] NOT @special (legacy move)
- [ ] NOT tagged `#Attackers`
- [ ] NOT tagged `great`, `ultra`, `little`
- [ ] NOT tagged `keep`, `power`, `tm`
- [ ] IS final evolution
- [ ] IS IV Rank >20 (verified via PokeGenie scan)

**If you see a 4★ → STOP → Remove it immediately**
**If ALL boxes checked → SAFE to transfer**

---

## Next Steps

After completing this checklist:

1. **Update progress**: Mark Week 1 - Priority 2 complete in `QUICK_WIN_STRATEGY.md`
2. **Continue to Priority 3-6**: Lucky duplicates, event cleanup, evolutions
3. **Monitor free space**: Should be at 4.5-6.7% after this priority alone
4. **Week 2**: Repeat this process for Great/Ultra/Little Leagues (if needed)

---

## Reference Documents

- `QUICK_WIN_STRATEGY.md` - Overall strategy and timeline
- `docs/reference/RAID_ATTACKER_COUNTS.md` - Which Pokemon to exclude (raid attackers)
- `docs/guides/PHASE_1_IMPLEMENTATION.md` - Original Phase 1 guide
- `POKEGENIE_NAMING.md` - PokeGenie setup (if you need to reconfigure)

---

_Master League Reduction Checklist - Created 2026-01-18_
