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

- `₁Ⓖ⓪Ch0084aa㈩` (GL Rank 84 - Category #1)
- `₂⓪Char15⁹¹②A` (ML Rank 15, 91% IV, Lvl 2 - Category #3)
- `⇄②⁴⁵⓪Ch㈩` (Transfer, Lvl 2, 45% IV - Categories #11-14)

---

## Name Generator Setup (14 Total)

### Core Generators (9 Current)

| #   | Name             | Prefix | Condition        | Favorite | Categories | Example           |
| --- | ---------------- | ------ | ---------------- | -------- | ---------- | ----------------- |
| 1   | **Trade (₁)**    | ⇄      | Default          | (none)   | #11-14     | `⇄②⁴⁵⓪Ch㈩`       |
| 2   | **Trade (₂)**    | ⇄      | Favorite ₂       | ₂        | #11-14     | `⇄②⁷⁶①Venusau`    |
| 3   | **PVP IV (PvP)** | ₁      | PvP Rank % ≥ 98% | (auto)   | #1, #2     | `₁Ⓖ⓪Ch0084aa㈩`   |
| 4   | **PVP IV (₁)**   | ₁      | Favorite ₁       | ₁        | #1, #2     | `₁Ⓤ①Venu0038A`    |
| 5   | **High IV (IV)** | ₂      | IV ≥ 90%         | (auto)   | Auto       | `₂⓪0084⁹⁶②●⁸aa㈩` |
| 6   | **High IV (2)**  | ₂      | Has 2nd move     | (manual) | Manual     | `₂①Ve0038⁹⁶②A`    |
| 7   | **High IV (₂)**  | ₂      | Favorite ₂       | ₂        | #3, Manual | `₂⓪Char15⁹¹②A`    |
| 8   | **Kept (₃)**     | ₃      | Favorite ₃       | ₃        | #4         | `₃⓪⁸²②●Ch㈩`      |
| 9   | **Default**      | •      | Default (unused) | (none)   | None       | `•⓪⁸²②●Ch♀㈩`     |

**Note**: "Trade (₁)" is the **default generator** (no favorite assigned). "Trade (₂)" is manual override with Favorite ₂.

### New Generators to Add (5 Total)

| #   | Name               | Prefix | Favorite | Categories | Format                                       | Example        |
| --- | ------------------ | ------ | -------- | ---------- | -------------------------------------------- | -------------- |
| 10  | **Shadow (₅)**     | ₅      | ₅        | #6         | `₅{Stage}{IV}{Lvl}{●}{Name}{Atk}{Atk2}{Leg}` | `₅⓪⁸²②●Ch⁸a㈩` |
| 11  | **XXS/XXL (₆)**    | ₆      | ₆        | #7         | `₆{Size}{Stage}{IV}{Lvl}{Name}{Leg}`         | `₆⊖⓪⁷⁵②Ch㈩`   |
| 12  | **Background (₇)** | ₇      | ₇        | #8         | `₇{Stage}{IV}{Lvl}{Name}{Leg}`               | `₇⓪⁸²②Ch㈩`    |
| 13  | **Dynamax (₈)**    | ₈      | ₈        | #10        | `₈{Stage}{IV}{Lvl}{Name}{Leg}`               | `₈⓪⁸²②Ch㈩`    |
| 14  | **Gigantamax (₉)** | ₉      | ₉        | #9         | `₉{Stage}{IV}{Lvl}{Name}{Leg}`               | `₉①⁹⁶②Venusau` |

**Note**: Favorite ₄ = Costume (uses same `₃` prefix as Kept).

---

## Favorite → Category Mapping

| Favorite   | Prefix | Categories | Description                          |
| ---------- | ------ | ---------- | ------------------------------------ |
| (none)     | ⇄      | #11-14     | Transfer/Trade queue (default)       |
| ₁          | ₁      | #1, #2     | PvP IV override (GL/UL/LL)           |
| ₂          | ₂      | #3, Manual | Master League PvP + High IV override |
| ₃          | ₃      | #4         | Shiny Pokemon                        |
| ₄          | ₃      | #5         | Costumed Pokemon                     |
| ₅          | ₅      | #6         | Shadow Pokemon                       |
| ₆          | ₆      | #7         | XXS/XXL size extremes                |
| ₇          | ₇      | #8         | Background Pokemon                   |
| ₈          | ₈      | #10        | Dynamax Pokemon                      |
| ₉          | ₉      | #9         | Gigantamax Pokemon                   |
| (auto-PvP) | ₁      | #1, #2     | Auto-assigned (PvP Rank % ≥ 98%)     |
| (auto-IV)  | ₂      | Auto       | Auto-assigned (IV ≥ 90%)             |

**Auto-Conditions**:

- **PVP IV (PvP)**: PvP Rank % ≥ 98% → Prefix `₁` (Categories #1, #2)
- **High IV (IV)**: IV ≥ 90% → Prefix `₂` (Auto high IV)
- **High IV (2)**: Has 2nd charge move → Prefix `₂` (Manual)
- **Default (⇄)**: Everything else → Prefix `⇄` (Transfer candidates)

---

## Format Details

### Common Formats

**PvP Format** (Categories #1-3):

```
₁{League}{Stage}{●/○}{Name}{Rank}{Atk}{Atk2}{Leg}
Example: ₁Ⓖ⓪Ch0084aa㈩      (GL Rank 84, basic, no shadow)
Example: ₁Ⓜ①●Metagr0015⁸A㈩  (ML Rank 15, stage 1, shadow)
Example: ₁Ⓤ①○Venu0038A      (UL Rank 38, stage 1, purified)
```

**High IV Format** (Auto/Manual):

```
₂{Stage}{●/○}{Name}{Rank}{IV}{Lvl}{Atk}{Atk2}{Leg}
Example: ₂⓪0084⁹⁶②●⁸aa㈩   (Basic, shadow, Rank 84, 96% IV, Lvl 2.5)
Example: ₂①Ve0038⁹⁶②A      (Stage 1, no shadow, Rank 38, 96% IV, Lvl 2)
Example: ₂⓪Char15⁹¹②A      (Basic, no shadow, Rank 15, 91% IV, Lvl 2)
```

**Kept Format** (Categories #4-10):

```
₃{Stage}{IV}{Lvl}{●/○}{Name}{Leg}
Example: ₃⓪⁸²②●Ch㈩    (Basic, 82% IV, Lvl 2.5, shadow)
Example: ₃①⁷⁶②Venusau  (Stage 1, 76% IV, Lvl 2, no shadow)
```

**Transfer Format** (Categories #11-14):

```
⇄{Lvl}{IV}{Stage}{●/○}{Name}{Leg}
Example: ⇄②⁴⁵⓪Ch㈩      (Lvl 2, 45% IV, basic, no shadow)
Example: ⇄②●⁷⁶①Venusau  (Lvl 2.5, 76% IV, stage 1, shadow)
```

**Category-Specific Formats** (New):

```
₅{Stage}{IV}{Lvl}{●}{Name}{Atk}{Atk2}{Leg}  (Shadow - always has ●)
₆{Size}{Stage}{IV}{Lvl}{Name}{Leg}          (XXS/XXL)
₇{Stage}{IV}{Lvl}{Name}{Leg}                (Background)
₈{Stage}{IV}{Lvl}{Name}{Leg}                (Dynamax)
₉{Stage}{IV}{Lvl}{Name}{Leg}                (Gigantamax)
```

**Default Format** (Unused):

```
•{Stage}{IV}{Lvl}{●/○}{Name}{Gender}{Leg}
Example: •⓪⁸²②●Ch♀㈩  (Rarely used - Trade (₁) is default)
```

---

## Symbol Legend

| Symbol                                      | Meaning                            | Symbol            | Meaning         |
| ------------------------------------------- | ---------------------------------- | ----------------- | --------------- |
| `₁`, `₂`, `₃`, `₄`, `₅`, `₆`, `₇`, `₈`, `₉` | Favorite prefix                    | `⇄`               | Transfer/Trade  |
| `Ⓖ`, `Ⓤ`, `Ⓛ`, `Ⓜ`                          | League (Great/Ultra/Little/Master) | `⓪`, `①`, `②`     | Evolution stage |
| `●`                                         | Shadow                             | `○`               | Purified        |
| `②`, `⑮`, `⑳`                               | Level                              | `⁸²`, `⁹⁶`, `¹⁰⁰` | IV percentage   |
| `0084`, `0038`                              | PvP rank                           | `⁸`, `A`, `a`     | Attack rating   |
| `㈩`                                        | Legacy move                        | `♀`, `♂`          | Gender          |
| `⊖`, `⊕`                                    | XXS/XXL                            | `•`               | Default         |

**Evolution Stage**:

- `⓪` = Basic (e.g., Charmander)
- `①` = Stage 1 (e.g., Charmeleon)
- `②` = Stage 2 (e.g., Charizard)

**Level Format**:

- `②` = Level 2
- `②●` = Level 2.5 (half-level, NOT shadow boost)
- `⑮` = Level 15
- `⑳` = Level 20
- `⑳●` = Level 20.5 (half-level)

**Note**: Half-levels (e.g., 2.5, 20.5) occur when powering up Pokemon at certain breakpoints. Shadow boost is NOT related to level format.

---

## Condition Recommendations

### 1. PVP IV (PvP): Change `95%` → `98%`

**Current**: `PvP Rank % >= 95%` (Rank ≤ ~200-205)

**Your Categories**:

- Category #1 (GL/UL): Keep Rank ≤ 100 (not 205)
- Category #2 (LL): Keep Rank ≤ 100 (60th+ percentile) or ≤ 19 (others)

**Analysis**:

- Keep Rank ≤ 100
- 100 / 4096 combinations = 2.44%
- **98% threshold** ≈ Rank 82
- **97.5% threshold** ≈ Rank 100

**Recommendation**: **Change to `PvP Rank % >= 97.5%`** (aligns with Rank ≤ 100)

**Alternative**: Keep 98% (slightly more restrictive, Rank ≤ 82)

---

### 2. High IV (IV): Keep `90%`

**Current**: `IV >= 90%`

**Status**: ✅ **No change needed**

**Reason**: Standard threshold for high IV Pokemon

---

### 3. Trade (₁): Keep as Default

**Current**: Default generator (no condition)

**Status**: ✅ **No change needed**

**Reason**: Default generator catches all Pokemon not assigned to other generators

---

## Duplicate Conditions (Intentional)

Some generators have duplicate formats for **manual overrides**:

**Trade Formats**:

- "Trade (₁)" - Default (no favorite assigned)
- "Trade (₂)" - Manual (Favorite ₂) - **May conflict with High IV (₂)** and Master League

**PvP Formats**:

- "PVP IV (PvP)" - Auto (PvP Rank % ≥ 98%)
- "PVP IV (₁)" - Manual (Favorite ₁ for GL/UL/LL)

**High IV Formats**:

- "High IV (IV)" - Auto (IV ≥ 90%)
- "High IV (2)" - Manual (Has 2nd move)
- "High IV (₂)" - Manual (Favorite ₂ for Master League + high IV)

**Purpose**: Manually favorite Pokemon that don't meet auto-criteria but need same format.

**Use Case**: You have a Rank 150 Charmander that doesn't auto-trigger "PVP IV (PvP)", but you want PvP format for Great League. Manually favorite it as ₁ → gets `₁` prefix.

**Warning**: "Trade (₂)" and "High IV (₂)" both use Favorite ₂. If you favorite a Pokemon as ₂, it will use "High IV (₂)" format (priority order: Favorite > High IV > Trade).

---

## Implementation Steps

### 1. Update Existing Conditions

In PokeGenie Settings → Name Generator:

| Generator        | Current          | Change To                     |
| ---------------- | ---------------- | ----------------------------- |
| **PVP IV (PvP)** | PvP Rank % ≥ 95% | **PvP Rank % ≥ 97.5%** or 98% |
| **High IV (IV)** | IV ≥ 90%         | ✅ Keep as-is                 |
| **Trade (₁)**    | Default          | ✅ Keep as-is                 |
| **Trade (₂)**    | Favorite ₂       | ⚠️ Optional (may conflict)    |
| **Default**      | Prefix `•`       | ✅ Keep (rarely used)         |

**Rename Generators** (align with Favorite numbers):
| Old Name | New Name | Favorite | Change |
| ---------------- | ---------------- | -------- | ------ |
| **PVP IV (₂)** | **PVP IV (₁)** | ₁ | ✅ Rename |
| **High IV (₃)** | **High IV (₂)** | ₂ | ✅ Rename |
| **Kept (₄)** | **Kept (₃)** | ₃ | ✅ Rename |

### 2. Add New Generators

Create 5 new generators with formats above:

- **Shadow (₅)** with Favorite ₅ → Format: `₅{Stage}{IV}{Lvl}{●}{Name}{Atk}{Atk2}{Leg}`
- **XXS/XXL (₆)** with Favorite ₆ → Format: `₆{Size}{Stage}{IV}{Lvl}{Name}{Leg}`
- **Background (₇)** with Favorite ₇ → Format: `₇{Stage}{IV}{Lvl}{Name}{Leg}`
- **Dynamax (₈)** with Favorite ₈ → Format: `₈{Stage}{IV}{Lvl}{Name}{Leg}`
- **Gigantamax (₉)** with Favorite ₉ → Format: `₉{Stage}{IV}{Lvl}{Name}{Leg}`

**Note**: Add Favorite ₄ for Costume if not created yet (uses same `₃` prefix as Kept).

### 3. Test with 10-20 Pokemon

- Scan test Pokemon in PokeGenie
- Assign Favorites ₁-₉
- Verify names generate correctly
- Check for conflicts (especially Favorite ₂ = both Trade, Master League, and High IV)

### 4. Update Tags in Pokemon GO

After renaming, tag Pokemon:

- Search "₁" → Tag `#Great`, `#Ultra`, `#Little`, `#Rank1-3` (GL/UL/LL with top ranks)
- Search "₂" → Tag `#Rank4-20`, `#Rank21-50` (Master League) OR high IV non-PvP
- Search "₃" → Tag `#Kept` (Shiny)
- Search "₄" → Tag `#Kept` (Costume)
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
| #1  | Great/Ultra League | ₁      | Auto (PvP ≥97.5%) | Keep 3 (Rank ≤10), 1 (Rank 11-100) |
| #2  | Little League      | ₁      | Auto (PvP ≥97.5%) | Keep 3 (Rank ≤10), 1 (Rank 11-100) |
| #3  | Master League      | ₂      | Favorite ₂        | Keep 3 (Rank ≤10), 1 (Rank 11-19)  |
| #4  | Shiny              | ₃      | Favorite ₃        | Keep 2 per species                 |
| #5  | Costumed           | ₃      | Favorite ₄        | Keep 2 per species                 |
| #6  | Shadow             | ₅      | Favorite ₅        | Keep 2 per species                 |
| #7  | XXS/XXL            | ₆      | Favorite ₆        | Keep 1 XXS + 1 XXL                 |
| #8  | Background         | ₇      | Favorite ₇        | Keep 2 per species                 |
| #9  | Gigantamax         | ₉      | Favorite ₉        | Keep 2 per species                 |
| #10 | Dynamax            | ₈      | Favorite ₈        | Keep 2 per species                 |
| #11 | Legendary Reserve  | ⇄      | (none)            | Keep top 10 (level+IV)             |
| #12 | Transfer Queue     | ⇄      | (none)            | Transfer at 2× candy events        |
| #13 | General Reserve    | ⇄      | (none)            | Keep top 2 (level+IV)              |
| #14 | Lucky Trade        | ⇄      | (none)            | Keep until aged 3+ years           |

**See**: STORAGE_STRATEGY_CORRECTED.md for full retention rules

---

## Usage Condition Priority

**PokeGenie applies generators in this priority order** (from PokeGenie documentation):

1. **Favorite** (₁-₉) - Highest priority
2. **Perfect IV** (100%)
3. **Has Second Charge Move**
4. **High IV** (≥ 90%)
5. **PvP IV** (≥ 97.5% or 98%)
6. **Trade** (default condition)
7. **Fully Evolved**
8. **Default** (•) - Lowest priority

**Example**: Shadow Metagross with 96% IV, Rank 15 ML, Favorite ₂

- Matches: Favorite ₂, High IV (96%)
- **Applied**: "High IV (₂)" (Favorite has highest priority)
- **Result**: `₂①●Metagr15⁹⁶②⁸A㈩`

---

## Related Files

- `STORAGE_STRATEGY_CORRECTED.md` - 14-category retention strategy
- `docs/reference/TAG_SYSTEM.md` - 43-tag system documentation
- `docs/reference/FAVORITE_QUERIES.md` - Search query strings
- `SUMMARY.md` - Project reorganization summary

---

_PokeGenie Name Generator Setup - Updated 2025-10-12_
