# Emergency Storage Reduction Guide

**Date**: 2026-02-15
**Current Storage**: 11,155 / 11,325 (170 free, ~1.5%)
**Target**: Free 200-300 additional slots (→ 370-470 free, ~3-4%)
**Completed**: Steps 0 (tag Attackers) and 1 (clear `#home` transfer queue)

---

## Tag Inventory Snapshot

### Storage Workflow

| Tag          | Count | Purpose                                           |
| ------------ | ----- | ------------------------------------------------- |
| **Kept**     | 5,774 | Permanent keep                                    |
| **Transfer** | 3,344 | Lucky Trade Queue (3+ yr aging) — DO NOT TRANSFER |
| **Home**     | 0     | Transfer queue (CLEARED)                          |
| **Review**   | 0     | Needs recheck                                     |

### IV Rank Tags

| Tag        | Count | Strategy Rule                                          |
| ---------- | ----- | ------------------------------------------------------ |
| Rank1      | 807   | KEEP ALL — best rank (globally or personal)            |
| Rank2      | 550   | KEEP ALL                                               |
| Rank3      | 478   | KEEP ALL                                               |
| Rank4-20   | 2,339 | Keep 1 copy                                            |
| Rank21-50  | 608   | GL/UL/LL: keep 1 copy; ML: transfer                    |
| Rank51-100 | 401   | GL/UL/LL: currently keep all (1/species); ML: transfer |

### Trophy IV Tags

| Tag    | Count | Rule                   |
| ------ | ----- | ---------------------- |
| First  | 310   | KEEP (globally #1 IVs) |
| Second | 238   | KEEP (globally #2 IVs) |
| Third  | 244   | KEEP (globally #3 IVs) |

### Battle Roles

| Tag       | Count | Rule                        |
| --------- | ----- | --------------------------- |
| Attackers | 531   | PROTECTED (raid attackers)  |
| Def1      | 9     | PROTECTED (gym defender T1) |
| Def2      | 3     | PROTECTED                   |
| Def2.5    | 11    | PROTECTED                   |

### League Tags

| Tag    | Count |
| ------ | ----- |
| Great  | 831   |
| Ultra  | 519   |
| Little | 675   |

### Other Tags

| Category        | Tags & Counts                                                                                  |
| --------------- | ---------------------------------------------------------------------------------------------- |
| Evolution       | Baby (39), Basic (1,801), Stage1 (1,898), Stage2 (762), Final (486)                            |
| Evolution Needs | SpecialEvolve (1), ItemEvolve (35), LocationEvolve (6), TimeEvolve (2)                         |
| Buddy           | InTraining (1,798), CurrentBuddy (3), Buddy1Km (16), Buddy3Km (1), Buddy5Km (2), Buddy20Km (0) |
| Resources       | Trade (2,354), NeedCandy (21), NeedPurified (9), PowerUp (4)                                   |
| Special         | Mega (355), Var1 (156), Var2 (75), Var3 (64), Var4 (67)                                        |

---

## Safety Query Template

All transfer queries use this base exclusion to protect the 13 storage categories:

```
!#Attackers&!lucky&!shiny&!shadow&!costume&!@special&!legendary&!mythical&!xxs&!xxl&!#First&!#Second&!#Third
```

| Exclusion                  | Reason                                    | Category         |
| -------------------------- | ----------------------------------------- | ---------------- |
| `!#Attackers`              | Raid attackers (531 tagged)               | Battle Role      |
| `!lucky`                   | Lucky Pokemon (collector value)           | Protected        |
| `!shiny`                   | Shiny = Category #3                       | Protected        |
| `!shadow`                  | Shadow = Category #5, +20% atk bonus      | Protected        |
| `!costume`                 | Costume = Category #4, rare collector     | Protected        |
| `!@special`                | Legacy/special moves                      | Protected        |
| `!legendary&!mythical`     | Legendary/Mythical (rare, personal ranks) | Protected        |
| `!xxs&!xxl`                | Size extremes = Category #6               | Protected        |
| `!#First&!#Second&!#Third` | Trophy IVs (globally best, irreplaceable) | Trophy Protected |

---

## Prioritized Transfer Opportunities

### Opportunity 1: Rank 51-100 Full Transfer

| Attribute      | Value                                                          |
| -------------- | -------------------------------------------------------------- |
| **Pool**       | 401 Pokemon                                                    |
| **Est. Yield** | 250-320 slots                                                  |
| **Speed**      | Fast (~5 min) — search, scan, mass transfer                    |
| **Risk**       | Low-Medium — removing entire tier, but PvP is minimal priority |

**Query**:

```
#rank51-100&!#Attackers&!lucky&!shiny&!shadow&!costume&!@special&!legendary&!mythical&!xxs&!xxl&!#First&!#Second&!#Third
```

**What you lose**: All non-protected Pokemon with globally rank 51-100 IVs for their species/league. These are mediocre IVs — you own 50+ better for each species.

**What you keep**: Any Rank51-100 that is also shiny, lucky, shadow, costume, legendary, mythical, xxs, xxl, trophy IV, or raid attacker.

---

### Opportunity 2: Rank 51-100 Meta-Only Filter

| Attribute      | Value                                                    |
| -------------- | -------------------------------------------------------- |
| **Pool**       | 401 Pokemon                                              |
| **Est. Yield** | 150-250 slots                                            |
| **Speed**      | Medium (~15 min) — need to cross-reference meta lists    |
| **Risk**       | Low — keeps meta-relevant species, only removes off-meta |

**Approach**: Keep Rank 51-100 Pokemon that are in the top-20 GL/UL/LL meta. Transfer the rest.

**Challenge**: Requires knowing which species are current meta (see STRATEGY_MODERATE_PVP.md for meta lists). More manual effort than Opportunity 1.

---

### Opportunity 3: Rank 21-50 Duplicate Trimming

| Attribute      | Value                                                             |
| -------------- | ----------------------------------------------------------------- |
| **Pool**       | 608 Pokemon                                                       |
| **Est. Yield** | 50-150 slots                                                      |
| **Speed**      | Slow (~20-30 min) — sort by name, identify duplicates per species |
| **Risk**       | Low — only removing excess copies, keeping best 1 per species     |

**Query**:

```
#rank21-50&!#Attackers&!lucky&!shiny&!shadow&!costume&!@special&!legendary&!mythical
```

**Approach**: Sort by Name. For each species with multiple Rank21-50 copies, keep the best one and transfer the rest.

**Note**: ML strategy says Rank 21+ = transfer. But currently these are kept for GL/UL/LL depth.

---

### Opportunity 4: Untagged Commons Sweep

| Attribute      | Value                                                   |
| -------------- | ------------------------------------------------------- |
| **Pool**       | Unknown                                                 |
| **Est. Yield** | 0-200 slots (possibly 0 — collection is well-organized) |
| **Speed**      | Medium (~10-15 min)                                     |
| **Risk**       | Very low — these are unreviewed Pokemon                 |

**Query**:

```
!4*&!shiny&!lucky&!shadow&!costume&!@special&!legendary&!mythical&!#Attackers&!#rank1&!#rank2&!#rank3&!#rank4-20&!#rank21-50&!#rank51-100&!#great&!#ultra&!#little&!#First&!#Second&!#Third
```

**Note**: In Jan 2026, most queries returned 0 (well-organized). Yield depends on how many Pokemon caught since then without being reviewed.

---

### Opportunity 5: Trade Pool Review (2,354)

| Attribute      | Value                                            |
| -------------- | ------------------------------------------------ |
| **Pool**       | 2,354 Pokemon                                    |
| **Est. Yield** | 0-400 slots (highly variable)                    |
| **Speed**      | Very slow (~30-60 min) — manual duplicate review |
| **Risk**       | Medium — user values trading (#3 priority)       |

**Approach**: Review for species with excessive copies in the trading pool. Keep 3-5 per species for trading, transfer rest.

**Caution**: This touches the #3 priority (Trading). Only recommended if other opportunities are exhausted.

---

### Opportunity 6: InTraining Review (1,798)

| Attribute      | Value                                          |
| -------------- | ---------------------------------------------- |
| **Pool**       | 1,798 Pokemon                                  |
| **Est. Yield** | 0-200 slots (if stale training targets exist)  |
| **Speed**      | Very slow (~30-60 min) — manual review         |
| **Risk**       | Medium — might remove active training projects |

**Question**: Are all 1,798 Pokemon genuinely in active power-up projects? Some may be stale. This is a large pool (16% of collection).

---

## Priority Summary

| Priority | Opportunity               | Est. Yield | Speed     | Risk     | Target Met?   |
| -------- | ------------------------- | ---------- | --------- | -------- | ------------- |
| **1**    | Rank 51-100 Full Transfer | 250-320    | Fast      | Low-Med  | Yes (alone)   |
| **2**    | Rank 51-100 Meta-Only     | 150-250    | Medium    | Low      | Probably      |
| **3**    | Rank 21-50 Duplicates     | 50-150     | Slow      | Low      | With #1 or #2 |
| **4**    | Untagged Commons          | 0-200      | Medium    | Very Low | Unknown       |
| **5**    | Trade Pool Review         | 0-400      | Very Slow | Medium   | Possibly      |
| **6**    | InTraining Review         | 0-200      | Very Slow | Medium   | Unknown       |

**Emergency target**: 200-300 additional slots (current: 170 free → target: 370-470 free)

**Recommended combinations**:

- **Fast**: Opportunity 1 alone meets the target
- **Conservative**: Opportunities 2 + 3 for similar yield with lower risk
- **Thorough**: Opportunities 1 + 3 + 4 for maximum reduction

---

_Emergency Reduction Guide — Created 2026-02-15_
