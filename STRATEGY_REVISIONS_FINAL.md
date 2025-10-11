# Pokemon GO Storage Strategy - Final Revisions

**Date**: 2025-10-11
**Based on**: User feedback and meta-awareness

---

## 🔧 Final Corrections

### 1. Category 1 (GL/UL) - Meta Pokemon Exception ✅

**Original Aggressive Recommendation**:
- Rank ≤10: Keep 1
- Rank 11+: Don't keep

**REVISED for Meta-Awareness**:

| Species Tier | Criteria | Keep Rules |
|--------------|----------|------------|
| **Tier 1: Top Meta** (Top 20 usage) | High usage in current meta | Rank ≤50: Keep 1<br>Rank ≤10: Keep 2 |
| **Tier 2: Viable** (Others) | Occasionally used | Rank ≤10: Keep 1 |
| **Tier 3: Favorites** | Your personal favorites | Rank ≤25: Keep 1 |

**Top 20 GL/UL Meta Species** (2025):
- **Great League**: Azumarill, Medicham, Skarmory, Altaria, Talonflame, Lickitung, Shadow Nidoqueen, Shadow Walrein, Shadow Swampert, Trevenant, Sableye, Registeel, Cresselia, Bastiodon, Vigoroth, Diggersby, Azu

mar

ill, Shadow Gligar, Charjabug, Lanturn
- **Ultra League**: Registeel, Cresselia, Talonflame, Trevenant, Shadow Nidoqueen, Shadow Swampert, Giratina (Altered), Shadow Machamp, Cobalion, Shadow Walrein, Tapu Fini, Swampert, Umbreon, Talonflame, Scrafty, Pidgeot, Jellicent, Mandibuzz, Steelix, Greedent

**Impact**: Adds ~100-200 Pokemon to Category 1 (still reduces from 1,370 → 400-500)

**Rationale**: Since you do occasional PvP for research/challenges, having meta options for rank ≤50 gives you competitive viability without the bloat of rank 51-205.

---

### 2. Category 3 (ML) - Raid Attacker Separation ✅

**Issue**: Master League PvP ranks ≠ Raid/Gym attacker quality

**REVISED Structure**:

#### Category 3a: Master League PvP Only
**Current**: 2,037 Pokemon
**Revised**: 200-300 Pokemon

| Pokemon Type | Retention Rule |
|--------------|----------------|
| Final Evolution | Rank ≤10: Keep 1 |
| Non-Final Evolution | Keep 2 (future-proofing) |

**Rationale**: You don't do Master League PvP competitively

---

#### Category 3b: Raid/Gym Attackers (Merged with Category 11)
**Current**: Part of Category 3 + Category 11
**Revised**: Consolidate into enhanced Category 11

**Top Raid Attackers by Type** (2025):

| Type | Top Attackers | Keep Count |
|------|---------------|------------|
| **Normal** | Slaking, Regigigas | 6 each |
| **Fighting** | Terrakion, Lucario, Conkeldurr, Machamp | 6-12 each |
| **Flying** | Rayquaza (Mega), Moltres, Honchkrow | 6-12 each |
| **Poison** | Nihilego, Roserade | 6 each |
| **Ground** | Groudon (Primal), Garchomp, Rhyperior, Excadrill | 6-12 each |
| **Rock** | Rampardos, Rhyperior, Terrakion | 6-12 each |
| **Bug** | Pheromosa, Genesect, Volcarona | 6-12 each |
| **Ghost** | Giratina (Origin), Chandelure, Gengar (Mega) | 6-12 each |
| **Steel** | Metagross (Mega), Dialga, Excadrill | 6-12 each |
| **Fire** | Reshiram, Chandelure, Blaziken (Mega), Moltres | 6-12 each |
| **Water** | Kyogre (Primal), Swampert, Kingler | 6-12 each |
| **Grass** | Kartana, Zarude, Roserade | 6-12 each |
| **Electric** | Zekrom, Electivire, Magnezone, Luxray | 6-12 each |
| **Psychic** | Mewtwo, Espeon, Alakazam | 6-12 each |
| **Ice** | Mamoswine, Glaceon, Weavile, Kyurem | 6-12 each |
| **Dragon** | Rayquaza, Palkia, Salamence, Dragonite | 6-12 each |
| **Dark** | Darkrai, Tyranitar, Weavile, Hydreigon | 6-12 each |
| **Fairy** | Togekiss, Gardevoir, Primarina | 6 each |

**Retention Rules**:
- **Frequent use** (Mewtwo, Kyogre, Groudon, Rayquaza, Mamoswine, Machamp): Keep **12**
- **Regular use** (Most legendaries): Keep **10**
- **Situational use**: Keep **6**
- **Non-Legendary raid attackers**: Keep **6** (Rhyperior, Machamp, Roserade, etc.)

**Impact**: Category 11 expands from 643 → 800-1,000 Pokemon (aligns with your raiding priority)

---

### 3. Tag System Integration ✅

**User Configuration**:
- `home` = Category 12 (Transfer queue for 2× candy events)

**Recommended Additional Tags**:
- `keep1` = Categories 1-3 (PvP)
- `keep2` = Categories 4-10 (Special variants)
- `keep3` = Categories 11-13 (Reserves)
- `trade` = Category 14 (3+ years, ready for lucky trades)

---

### 4. Special Move Tracking ✅

**User Note**: Use `@special` query to identify Pokemon with legacy moves

**Application**:
- When organizing categories, search `@special`
- Apply +1 bonus slot if no current Pokemon has the special move
- Example: If your 3× rank ≤10 Venusaur don't have Frenzy Plant, keep 1 additional with Frenzy Plant

---

### 5. PokeGenie Auto-Scan ✅

**User Confirmation**: Already enabled

**Recommended Workflow**:
1. Catch Pokemon → PokeGenie auto-scans
2. Check PvP ranks in PokeGenie app
3. Tag or transfer based on category rules
4. Use bulk operations during events

---

## 📊 Revised Storage Targets (Final)

| Category | Current | Original Revised | **FINAL Revised** | Change | Reason |
|----------|---------|------------------|-------------------|--------|--------|
| 1. GL/UL | 1,370 | 200-300 | **400-500** | +200 | Meta-awareness (rank ≤50 for top 20) |
| 2. LL | 498 | 50-100 | **50-100** | 0 | No change |
| 3a. ML PvP | 2,037 | 300-400 | **200-300** | -100 | Separate raid attackers |
| 3b. Raid/Gym | (in Cat 3) | - | **(merged to Cat 11)** | - | Move to Category 11 |
| 4-10. Special | 3,046 | 3,046 | **3,046** | 0 | No change |
| 11. Legendary + Raid | 643 | 700-800 | **800-1,000** | +200 | Include non-legendary raid attackers |
| 12. Transfer Queue | 76 | 0-76 | **0-76** | 0 | Clear during events |
| 13. General | 2,441 | 2,441 | **2,441** | 0 | No change |
| 14. Lucky Queue | <100 | <100 | **<100** | 0 | No change |
| **TOTAL** | 10,184 | 8,700-9,300 | **8,900-9,400** | - | - |

**Target Free Space**: 1,100-1,600 slots (10-15% free)

**Net Savings from Original**: 800-1,300 slots

---

## 🎯 Revised Implementation Priority

### Phase 1: Quick Wins (Week 1) - Target: 400-500 slots

**Priority 1**: Reduce Master League PvP (Category 3a)
- Transfer all rank 11-19 final evolutions
- Keep rank ≤10: 1 copy only
- Keep non-final: 2 copies (future-proofing)
- **Expected**: 400-500 slots

**Priority 2**: Clear Category 12 (Transfer Queue tagged `home`)
- Transfer during 2× candy event
- **Expected**: 76 slots

**Phase 1 Total**: 476-576 slots freed

---

### Phase 2: Major Reductions (Weeks 2-3) - Target: 500-700 slots

**Priority 3**: Reduce Great/Ultra League (Category 1) - **META-AWARE**
- **Top 20 meta species**: Keep rank ≤50 (1 copy), rank ≤10 (2 copies)
- **Other species**: Keep rank ≤10 (1 copy) only
- **Favorites**: Keep rank ≤25 (1 copy)
- **Expected**: 700-800 slots

**Priority 4**: Reduce Little League (Category 2)
- Rank ≤10 (80th+ percentile): Keep 1
- Rank ≤10 (60-79th percentile, favorites only): Keep 1
- **Expected**: 350-400 slots

**Phase 2 Total**: 1,050-1,200 slots freed

---

### Phase 3: Expansion (Week 3+) - Cost: 200-400 slots

**Priority 5**: Expand Category 11 (Legendary + Raid Attackers)
- Frequent raid attackers: 10 → 12
- Add non-legendary raid attackers: 6 each (Machamp, Rhyperior, etc.)
- **Cost**: 200-400 slots

---

### **NET TOTAL**: 1,126-1,376 slots freed (minus 200-400 expansion)

**Realistic Net Gain**: 800-1,200 slots

**Target**: 8,900-9,400 / 10,500 (1,100-1,600 free, ~10-15%)

---

## 📏 File Length Evaluation

### Current File Lengths

| File | Lines | Assessment |
|------|-------|------------|
| `STORAGE_STRATEGY_CORRECTED.md` | 486 | ⚠️ **Too long** |
| `IMPROVEMENT_RECOMMENDATIONS_REVISED.md` | 436 | ⚠️ **Too long** |
| `STORAGE_QUICK_REFERENCE.md` | 171 | ✅ **Good** |
| `SEARCH_QUERIES.md` | NEW | ✅ **Good** |
| `STRATEGY_REVISIONS_FINAL.md` (THIS FILE) | NEW | ✅ **Concise** |

### Recommendations

**For Daily Use** (Keep these handy):
1. **`STORAGE_QUICK_REFERENCE.md`** (171 lines) - Daily decisions ✅
2. **`SEARCH_QUERIES.md`** (NEW) - Search strings ✅
3. **`STRATEGY_REVISIONS_FINAL.md`** (THIS FILE) - Final strategy ✅

**For Reference** (Consult when needed):
4. `STORAGE_STRATEGY_CORRECTED.md` - Complete documentation
5. `IMPROVEMENT_RECOMMENDATIONS_REVISED.md` - Detailed analysis

**Action**: Create streamlined summary at top of both long files pointing to quick references.

---

## 🔄 Summary of All Changes

### Corrections Applied
1. ✅ Lucky trade mechanics (cap at 3 years, not 1)
2. ✅ Category retention rules (rank ≥11 logic)
3. ✅ Ultra Beasts in Category 12
4. ✅ Special move bonus documented
5. ✅ Non-final evolution justification
6. ✅ Overlap handling clarified
7. ✅ Daily audit practices confirmed

### New Additions
8. ✅ **Meta-awareness for Category 1** (top 20 species get rank ≤50)
9. ✅ **Raid attacker separation** (Category 3b merged to Category 11)
10. ✅ **Tag system integration** (`home` for transfer queue)
11. ✅ **Search query library** (with Category 14 exclusions)
12. ✅ **PokeGenie workflow** (auto-scan confirmed)

### Strategic Adjustments
- Category 1 (GL/UL): 1,370 → 400-500 (meta-aware)
- Category 3a (ML PvP): 2,037 → 200-300 (PvP only)
- Category 11 (Legendary + Raid): 643 → 800-1,000 (includes raid attackers)
- **Net savings**: 800-1,200 slots
- **Target free space**: 10-15%

---

## 🚀 Next Actions

1. **Review this file** (`STRATEGY_REVISIONS_FINAL.md`) - Quick reference
2. **Use** `SEARCH_QUERIES.md` for daily operations
3. **Implement** Phase 1 (Master League reduction) - 400-500 slots
4. **Implement** Phase 2 (GL/UL/LL reduction) - 700-1,000 slots
5. **Expand** Category 11 for raid attackers (cost: 200-400 slots)
6. **Track** monthly progress

**Result**: 1,100-1,600 free slots (~10-15%) + reduced daily management time

---

*Final revisions incorporating meta-awareness and raid attacker optimization (2025-10-11)*
