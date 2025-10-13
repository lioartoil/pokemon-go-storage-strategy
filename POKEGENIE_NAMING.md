<!-- cSpell: ignore Metagr Rayqua Venu Venusa Venusau -->

# PokeGenie Name Generator - Setup Reference

**Date**: 2025-10-12
**Purpose**: PokeGenie naming strategy for 14-category storage system

---

## Purpose

**Names are for SORTING after filtering**:

1. Filter by species (e.g., "Charmander")
2. Names sort by priority (best IVs first)
3. Make retention decisions

**Example**: Filter "Charmander" → Names sorted:

- `₁Ⓖ⓪Char84aa㈩` (GL Rank 84 - Category #1a)
- `₂⓪Char15⁹¹②A` (ML Rank 15, 91% IV, Lvl 2 - Category #2)
- `⇄②⁴⁵⓪Char㈩` (Transfer, Lvl 2, 45% IV - Categories #10-13)

---

## Name Generator Setup (15 Total)

### Core Generators (9 Current)

| #   | Name             | Prefix | Condition          | Favorite | Categories | Example           |
| --- | ---------------- | ------ | ------------------ | -------- | ---------- | ----------------- |
| 1   | **Trade**        | ⇄      | Default            | (none)   | #10-13     | `⇄②⁴⁵⓪Char㈩`     |
| 2   | **PVP IV (PvP)** | ₁      | PvP Rank % ≥ 97.5% | (auto)   | #1a, #1b   | `₁Ⓖ⓪Char84aa㈩`   |
| 3   | **PVP IV (₁)**   | ₁      | Favorite ₁         | ₁        | #1a, #1b   | `₁Ⓤ①Venu38A`      |
| 4   | **High IV (IV)** | ₂      | IV ≥ 90%           | (auto)   | Auto       | `₂⓪⁹⁶②●Char⁸aa㈩` |
| 5   | **High IV (2)**  | ₂      | Has 2nd move       | (manual) | Manual     | `₂①Ve38⁹⁶②A`      |
| 6   | **High IV (₂)**  | ₂      | Favorite ₂         | ₂        | #2, Manual | `₂⓪Char15⁹¹②A`    |
| 7   | **Shiny (₃)**    | ₃      | Favorite ₃         | ₃        | #3         | `₃⓪⁸²②●Char㈩`    |
| 8   | **Costume (₄)**  | ₃      | Favorite ₄         | ₄        | #4         | `₃⓪⁷⁶②Char㈩`     |
| 9   | **Default**      | •      | Default (unused)   | (none)   | None       | `•⓪⁸²②●Char♀㈩`   |

**Note**: "Trade" is the **default generator** (no favorite assigned). It catches all Pokemon not matching other conditions.

### New Generators to Add (6 Total)

| #   | Name               | Prefix | Favorite | Categories | Format                                               | Example          |
| --- | ------------------ | ------ | -------- | ---------- | ---------------------------------------------------- | ---------------- |
| 10  | **Shadow (₅)**     | ₅      | ₅        | #5         | `₅{Stage}{IV}{Lvl}{●}{Name}{Atk}{Atk2}{Leg}`         | `₅⓪⁸²②●Char⁸a㈩` |
| 11  | **XXS/XXL (₆)**    | ₆      | ₆        | #6         | `₆{Size}{Stage}{IV}{Lvl}{Name}{Leg}`                 | `₆⊖⓪⁷⁵②Char㈩`   |
| 12  | **Background (₇)** | ₇      | ₇        | #7         | `₇{Stage}{IV}{Lvl}{Name}{Leg}`                       | `₇⓪⁸²②Char㈩`    |
| 13  | **Dynamax (₈)**    | ₈      | ₈        | #9         | `₈{Stage}{●/○}{Name}{Rank}{IV}{Lvl}{Atk}{Atk2}{Leg}` | `₈⓪Char15⁹¹②A`   |
| 14  | **Gigantamax (₉)** | ₉      | ₉        | #8         | `₉{Stage}{●/○}{Name}{Rank}{IV}{Lvl}{Atk}{Atk2}{Leg}` | `₉⓪Char15⁹¹②A`   |

**Note**: Dynamax (₈) and Gigantamax (₉) use the same format as Category #2 (High IV format) but with their own favorite prefix symbols.

---

## Favorite → Category Mapping

| Favorite   | Prefix | Categories | Description                          |
| ---------- | ------ | ---------- | ------------------------------------ |
| (none)     | ⇄      | #10-13     | Transfer/Trade queue (default)       |
| ₁          | ₁      | #1a, #1b   | PvP IV override (GL/UL/LL)           |
| ₂          | ₂      | #2, Manual | Master League PvP + High IV override |
| ₃          | ₃      | #3         | Shiny Pokemon                        |
| ₄          | ₃      | #4         | Costumed Pokemon                     |
| ₅          | ₅      | #5         | Shadow Pokemon                       |
| ₆          | ₆      | #6         | XXS/XXL size extremes                |
| ₇          | ₇      | #7         | Background Pokemon                   |
| ₈          | ₈      | #9         | Dynamax Pokemon                      |
| ₉          | ₉      | #8         | Gigantamax Pokemon                   |
| (auto-PvP) | ₁      | #1a, #1b   | Auto-assigned (PvP Rank % ≥ 97.5%)   |
| (auto-IV)  | ₂      | Auto       | Auto-assigned (IV ≥ 90%)             |

**Note on Categories #1a & #1b**: These are **subcategories** of Category #1 (PvP Competitive Pokemon) that share **Favorite ₁** because they both use PvP IV ranking format:

- **Category #1a** (Great/Ultra League): CP ≤ 1,500 or ≤ 2,500, Rank ≤ 100
- **Category #1b** (Little League): CP ≤ 500, Rank ≤ 100 (60th+ percentile) or ≤ 19 (others)

They are structured as subcategories due to different retention rules (Little League has percentile filtering) but share the same naming format and Favorite group.

**Auto-Conditions**:

- **PVP IV (PvP)**: PvP Rank % ≥ 97.5% → Prefix `₁` (Categories #1a, #1b)
- **High IV (IV)**: IV ≥ 90% → Prefix `₂` (Auto high IV)
- **High IV (2)**: Has 2nd charge move → Prefix `₂` (Manual)
- **Default (Trade)**: Everything else → Prefix `⇄` (Transfer candidates)

---

## Format Details

### Common Formats

**PvP Format** (Categories #1a-1b):

```
₁{League}{Stage}{●/○}{Name}{Rank}{Atk}{Atk2}{Leg}
Example: ₁Ⓖ⓪Char84aa㈩      (GL Rank 84, basic, no shadow)
Example: ₁Ⓜ①●Metagr15⁸A㈩   (ML Rank 15, stage 1, shadow)
Example: ₁Ⓤ①○Venu38A        (UL Rank 38, stage 1, purified)
```

**High IV / Master League Format** (Category #2, Dynamax, Gigantamax):

```
₂{Stage}{●/○}{Name}{Rank}{IV}{Lvl}{Atk}{Atk2}{Leg}
Example: ₂⓪⁹⁶②●Char⁸aa㈩      (Basic, shadow, 96% IV, Lvl 2.5, auto-condition)
Example: ₂①Ve38⁹⁶②A         (Stage 1, no shadow, Rank 38, 96% IV, Lvl 2)
Example: ₂⓪Char15⁹¹②A       (Basic, no shadow, Rank 15, 91% IV, Lvl 2)

Dynamax/Gigantamax (same format, different prefix):
Example: ₈⓪Char15⁹¹②A       (Dynamax, Rank 15, 91% IV, Lvl 2)
Example: ₉⓪Char15⁹¹②A       (Gigantamax, Rank 15, 91% IV, Lvl 2)
```

**Shiny / Costumed Format** (Categories #3-4):

```
₃{Stage}{IV}{Lvl}{●/○}{Name}{Leg}
Example: ₃⓪⁸²②●Char㈩    (Basic, 82% IV, Lvl 2.5, shadow)
Example: ₃①⁷⁶②Venu        (Stage 1, 76% IV, Lvl 2, no shadow)
```

**Transfer Format** (Categories #10-13):

```
⇄{Lvl}{IV}{Stage}{●/○}{Name}{Leg}
Example: ⇄②⁴⁵⓪Char㈩      (Lvl 2, 45% IV, basic, no shadow)
Example: ⇄②●⁷⁶①Venu       (Lvl 2.5, 76% IV, stage 1, shadow)
```

**Category-Specific Formats** (New):

```
₅{Stage}{IV}{Lvl}{●}{Name}{Atk}{Atk2}{Leg}  (Shadow - always has ●)
Example: ₅⓪⁸²②●Char⁸a㈩

₆{Size}{Stage}{IV}{Lvl}{Name}{Leg}          (XXS/XXL)
Example: ₆⊖⓪⁷⁵②Char㈩

₇{Stage}{IV}{Lvl}{Name}{Leg}                (Background)
Example: ₇⓪⁸²②Char㈩
```

**Default Format** (Unused):

```
•{Stage}{IV}{Lvl}{●/○}{Name}{Gender}{Leg}
Example: •⓪⁸²②●Char♀㈩  (Rarely used - Trade is default)
```

---

## Symbol Legend

| Symbol                                      | Meaning                            | Symbol            | Meaning         |
| ------------------------------------------- | ---------------------------------- | ----------------- | --------------- |
| `₁`, `₂`, `₃`, `₄`, `₅`, `₆`, `₇`, `₈`, `₉` | Favorite prefix                    | `⇄`               | Transfer/Trade  |
| `Ⓖ`, `Ⓤ`, `Ⓛ`, `Ⓜ`                          | League (Great/Ultra/Little/Master) | `⓪`, `①`, `②`     | Evolution stage |
| `●`                                         | Shadow                             | `○`               | Purified        |
| `②`, `⑮`, `⑳`                               | Level                              | `⁸²`, `⁹⁶`, `¹⁰⁰` | IV percentage   |
| `84`, `38`, `15`                            | PvP rank (no leading zeros)        | `⁸`, `A`, `a`     | Attack rating   |
| `㈩`                                        | Legacy move                        | `♀`, `♂`          | Gender          |
| `⊖`, `⊕`                                    | XXS/XXL                            | `•`               | Default         |

**Evolution Stage**:

- `⓪` = Basic (e.g., Charmander)
- `①` = Stage 1 (e.g., Charmeleon)
- `②` = Stage 2 (e.g., Charizard)

**Level Format**:

- `②` = Level 2
- `②●` = Level 2.5 (half-level, **NOT shadow boost**)
- `⑮` = Level 15
- `⑳` = Level 20
- `⑳●` = Level 20.5 (half-level)

**Note**: Half-levels (e.g., 2.5, 20.5) occur when powering up Pokemon at certain breakpoints. Shadow boost is NOT related to level format.

---

## Condition Recommendations

### 1. PVP IV (PvP): Change `95%` → `97.5%`

**Current**: `PvP Rank % >= 95%` (Rank ≤ ~200-205)

**Your Categories**:

- Category #1a (GL/UL): Keep Rank ≤ 100 (not 205)
- Category #1b (LL): Keep Rank ≤ 100 (60th+ percentile) or ≤ 19 (others)

**Analysis**:

- Keep Rank ≤ 100
- 100 / 4096 combinations = 2.44%
- **98% threshold** ≈ Rank 82
- **97.5% threshold** ≈ Rank 100

**Recommendation**: **Change to `PvP Rank % >= 97.5%`** (aligns with Rank ≤ 100)

**Note**: PokeGenie may only support whole numbers (97% or 98%). If 97.5% is not available, use **98%** (Rank ≤ 82, slightly more restrictive).

---

### 2. High IV (IV): Keep `90%`

**Current**: `IV >= 90%`

**Status**: ✅ **No change needed**

**Reason**: Standard threshold for high IV Pokemon

---

### 3. Trade: Keep as Default

**Current**: Default generator (no condition)

**Status**: ✅ **No change needed**

**Reason**: Default generator catches all Pokemon not assigned to other generators

---

## Duplicate Conditions (Intentional)

Some generators have duplicate formats for **manual overrides**:

**PvP Formats**:

- "PVP IV (PvP)" - Auto (PvP Rank % ≥ 97.5%)
- "PVP IV (₁)" - Manual (Favorite ₁ for GL/UL/LL)

**High IV Formats**:

- "High IV (IV)" - Auto (IV ≥ 90%)
- "High IV (2)" - Manual (Has 2nd move)
- "High IV (₂)" - Manual (Favorite ₂ for Master League + high IV)

**Purpose**: Manually favorite Pokemon that don't meet auto-criteria but need same format.

**Use Case**: You have a Rank 150 Charmander that doesn't auto-trigger "PVP IV (PvP)", but you want PvP format for Great League. Manually favorite it as ₁ → gets `₁` prefix.

---

## Implementation Steps

### 1. Update Existing Conditions

In PokeGenie Settings → Name Generator:

| Generator        | Current          | Change To                                              |
| ---------------- | ---------------- | ------------------------------------------------------ |
| **PVP IV (PvP)** | PvP Rank % ≥ 95% | **PvP Rank % ≥ 97.5%** (or 98% if 97.5% not available) |
| **High IV (IV)** | IV ≥ 90%         | ✅ Keep as-is                                          |
| **Trade**        | Default          | ✅ Keep as-is                                          |
| **Default**      | Prefix `•`       | ✅ Keep (rarely used)                                  |

**Rename Generators** (align with Favorite numbers):

| Old Name        | New Name        | Favorite | Change    |
| --------------- | --------------- | -------- | --------- |
| **PVP IV (₂)**  | **PVP IV (₁)**  | ₁        | ✅ Rename |
| **High IV (₃)** | **High IV (₂)** | ₂        | ✅ Rename |
| **Kept (₄)**    | **Shiny (₃)**   | ₃        | ✅ Rename |

### 2. Add New Generators

Create 6 new generators with formats above:

- **Costume (₄)** with Favorite ₄ → Format: `₃{Stage}{IV}{Lvl}{●/○}{Name}{Leg}` (uses same `₃` prefix as Shiny)
- **Shadow (₅)** with Favorite ₅ → Format: `₅{Stage}{IV}{Lvl}{●}{Name}{Atk}{Atk2}{Leg}`
- **XXS/XXL (₆)** with Favorite ₆ → Format: `₆{Size}{Stage}{IV}{Lvl}{Name}{Leg}`
- **Background (₇)** with Favorite ₇ → Format: `₇{Stage}{IV}{Lvl}{Name}{Leg}`
- **Dynamax (₈)** with Favorite ₈ → Format: `₈{Stage}{●/○}{Name}{Rank}{IV}{Lvl}{Atk}{Atk2}{Leg}` (same as High IV)
- **Gigantamax (₉)** with Favorite ₉ → Format: `₉{Stage}{●/○}{Name}{Rank}{IV}{Lvl}{Atk}{Atk2}{Leg}` (same as High IV)

### 3. Test with 10-20 Pokemon

- Scan test Pokemon in PokeGenie
- Assign Favorites ₁-₉
- Verify names generate correctly
- Check that Dynamax/Gigantamax use High IV format with correct prefix

### 4. Update Tags in Pokemon GO

After renaming, tag Pokemon:

- Search "₁" → Tag `#Great`, `#Ultra`, `#Little`, `#Rank1-3` (GL/UL/LL with top ranks)
- Search "₂" → Tag `#Rank4-20`, `#Rank21-50` (Master League) OR high IV non-PvP
- Search "₃" → Tag `#Kept` (Shiny or Costume)
- Search "₅" → Tag `#Kept` (Shadow)
- Search "₆" → Tag `#Kept` (XXS/XXL)
- Search "₇" → Tag `#Kept` (Background)
- Search "₈" → Tag `#Kept` (Dynamax)
- Search "₉" → Tag `#Kept` (Gigantamax)
- Search "⇄" → Tag `#Transfer`, `#Home`, `#Trade`, `#LuckyTrade`

---

## Category Reference

| Cat | Description        | Prefix | Favorite          | Retention                          |
| --- | ------------------ | ------ | ----------------- | ---------------------------------- |
| #1a | Great/Ultra League | ₁      | Auto (PvP ≥97.5%) | Keep 3 (Rank ≤10), 1 (Rank 11-100) |
| #1b | Little League      | ₁      | Auto (PvP ≥97.5%) | Keep 3 (Rank ≤10), 1 (Rank 11-100) |
| #2  | Master League      | ₂      | Favorite ₂        | Keep 3 (Rank ≤10), 1 (Rank 11-19)  |
| #3  | Shiny              | ₃      | Favorite ₃        | Keep 2 per species                 |
| #4  | Costumed           | ₃      | Favorite ₄        | Keep 2 per species                 |
| #5  | Shadow             | ₅      | Favorite ₅        | Keep 2 per species                 |
| #6  | XXS/XXL            | ₆      | Favorite ₆        | Keep 1 XXS + 1 XXL                 |
| #7  | Background         | ₇      | Favorite ₇        | Keep 2 per species                 |
| #8  | Gigantamax         | ₉      | Favorite ₉        | Keep 2 per species                 |
| #9  | Dynamax            | ₈      | Favorite ₈        | Keep 2 per species                 |
| #10 | Legendary Reserve  | ⇄      | (none)            | Keep top 10 (level+IV)             |
| #11 | Transfer Queue     | ⇄      | (none)            | Transfer at 2× candy events        |
| #12 | General Reserve    | ⇄      | (none)            | Keep top 2 (level+IV)              |
| #13 | Lucky Trade        | ⇄      | (none)            | Keep until aged 3+ years           |

**See**: STORAGE_STRATEGY_CORRECTED.md for full retention rules

---

## Usage Condition Priority

**PokeGenie applies generators in this priority order** (from PokeGenie documentation):

1. **Favorite** (₁-₉) - Highest priority
2. **Perfect IV** (100%)
3. **Has Second Charge Move**
4. **High IV** (≥ 90%)
5. **PvP IV** (≥ 97.5%)
6. **Trade** (default condition)
7. **Fully Evolved**
8. **Default** (•) - Lowest priority

**Example**: Shadow Metagross with 96% IV, Rank 15 ML, Favorite ₂

- Matches: Favorite ₂, High IV (96%)
- **Applied**: "High IV (₂)" (Favorite has highest priority)
- **Result**: `₂①●Metagr15⁹⁶②⁸A㈩`

---

## Related Files

- `STORAGE_STRATEGY_CORRECTED.md` - 13-category retention strategy (with #1a/#1b subcategories)
- `docs/reference/TAG_SYSTEM.md` - 43-tag system documentation
- `docs/reference/FAVORITE_QUERIES.md` - Search query strings
- `SUMMARY.md` - Project reorganization summary

---

_PokeGenie Name Generator Setup - Updated 2025-10-13_
