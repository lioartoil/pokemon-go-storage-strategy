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

- `₁G0Char84aa㈩` (GL Rank 84 - Category #1a)
- `₂0Char15⁹¹2A` (ML Rank 15, 91% IV, Lvl 2 - Category #2)
- `~2⁴⁵0Char㈩` (Transfer, Lvl 2, 45% IV - Categories #10-13)

---

## Name Generator Setup (15 Total)

### Core Generators (9 Current)

| #   | Name             | Prefix | Condition          | Favorite | Categories | Example         |
| --- | ---------------- | ------ | ------------------ | -------- | ---------- | --------------- |
| 1   | **Trade**        | ~      | Default            | (none)   | #10-13     | `~2⁴⁵0Char㈩`   |
| 2   | **PVP IV (PvP)** | ₁      | PvP Rank % ≥ 97.5% | (auto)   | #1a, #1b   | `₁G0Char84aa㈩` |
| 3   | **PVP IV (₁)**   | ₁      | Favorite ₁         | ₁        | #1a, #1b   | `₁U1Venu38A`    |
| 4   | **High IV (IV)** | ₂      | IV ≥ 90%           | (auto)   | Auto       | `₂0Cha8⁹⁶2½A`   |
| 5   | **High IV (2)**  | ₂      | Has 2nd move       | (auto)   | Auto       | `₂1Ve5⁹⁶2A`     |
| 6   | **High IV (₂)**  | ₂      | Favorite ₂         | ₂        | #2, Manual | `₂0Char15⁹¹2A`  |
| 7   | **Shiny (₃)**    | ₃      | Favorite ₃         | ₃        | #3         | `₃0⁸²2•Char㈩`  |
| 8   | **Costume (₄)**  | ₄      | Favorite ₄         | ₄        | #4         | `₄0⁷⁶2Char㈩`   |

**Note**: "Trade" is the **default generator** (no favorite assigned). It catches all Pokemon not matching other conditions or generators.

### New Generators to Add (6 Total)

| #   | Name               | Prefix | Favorite | Categories | Format                                               | Example        |
| --- | ------------------ | ------ | -------- | ---------- | ---------------------------------------------------- | -------------- |
| 9   | **Shadow (₅)**     | ₅      | ₅        | #5         | `₅{Stage}{IV}{Lvl}{•}{Name}{Leg}`                    | `₅0⁸²2•Char㈩` |
| 10  | **XXS/XXL (₆)**    | ₆      | ₆        | #6         | `₆{Stage}{IV}{Lvl}{Name}{Leg}`                       | `₆0⁷⁵2Char㈩`  |
| 11  | **Background (₇)** | ₇      | ₇        | #7         | `₇{Stage}{IV}{Lvl}{Name}{Leg}`                       | `₇0⁸²2Char㈩`  |
| 12  | **Dynamax (₈)**    | ₈      | ₈        | #8         | `₈{Stage}{•/°}{Name}{Rank}{IV}{Lvl}{Atk}{Atk2}{Leg}` | `₈0Char15⁹¹2A` |
| 13  | **Gigantamax (₉)** | ₉      | ₉        | #9         | `₉{Stage}{•/°}{Name}{Rank}{IV}{Lvl}{Atk}{Atk2}{Leg}` | `₉0Char15⁹¹2A` |

**Note**: Dynamax (₈) and Gigantamax (₉) use the same format as Category #2 (High IV format) but with their own favorite prefix symbols.

---

## Favorite → Category Mapping

| Favorite   | Prefix | Categories | Description                          |
| ---------- | ------ | ---------- | ------------------------------------ |
| (none)     | ~      | #10-13     | Transfer/Trade queue (default)       |
| ₁          | ₁      | #1a, #1b   | PvP IV override (GL/UL/LL)           |
| ₂          | ₂      | #2, Manual | Master League PvP + High IV override |
| ₃          | ₃      | #3         | Shiny Pokemon                        |
| ₄          | ₄      | #4         | Costumed Pokemon                     |
| ₅          | ₅      | #5         | Shadow Pokemon                       |
| ₆          | ₆      | #6         | XXS/XXL size extremes                |
| ₇          | ₇      | #7         | Background Pokemon                   |
| ₈          | ₈      | #8         | Dynamax Pokemon                      |
| ₉          | ₉      | #9         | Gigantamax Pokemon                   |
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
- **Default (Trade)**: Everything else → Prefix `~` (Transfer candidates)

---

## Format Details

### Common Formats

**PvP Format** (Categories #1a-1b):

```
₁{League}{Stage}{•/°}{Name}{Rank}{Atk}{Atk2}{Leg}
Example: ₁G0Char84aa㈩      (GL Rank 84, basic, no shadow)
Example: ₁U1°Venu38A        (UL Rank 38, stage 1, purified)
Example: ₁C0Pika25aa         (LL Rank 25, basic, no shadow)
```

**High IV / Master League Format** (Category #2, Dynamax, Gigantamax):

```
₂{Stage}{•/°}{Name}{Rank}{IV}{Lvl}{Atk}{Atk2}{Leg}
Example: ₂0Cha8⁹⁶2½A         (Basic, Rank 8, 96% IV, Lvl 2.5, auto-IV ≥90%)
Example: ₂1Ve5⁹⁶2A           (Stage 1, Rank 5, 96% IV, Lvl 2, has 2nd move)
Example: ₂0Char15⁹¹2A        (Basic, no shadow, ML Rank 15, 91% IV, Lvl 2)
Example: ₂1Ve38⁹⁶2A          (Stage 1, no shadow, ML Rank 38, 96% IV, Lvl 2)

Dynamax/Gigantamax (same format, different prefix):
Example: ₈0Char15⁹¹2A        (Dynamax, Rank 15, 91% IV, Lvl 2)
Example: ₉0Char15⁹¹2A        (Gigantamax, Rank 15, 91% IV, Lvl 2)
```

**Shiny / Costumed Format** (Categories #3-4):

```
₃{Stage}{IV}{Lvl}{•/°}{Name}{Leg}  or  ₄{Stage}{IV}{Lvl}{•/°}{Name}{Leg}
Example: ₃0⁸²2½•Char㈩   (Shiny, basic, 82% IV, Lvl 2.5, shadow)
Example: ₄1⁷⁶2Venu        (Costume, stage 1, 76% IV, Lvl 2, no shadow)
```

**Transfer Format** (Categories #10-13):

```
~{Lvl}{IV}{Stage}{•/°}{Name}{Leg}
Example: ~2⁴⁵0Char㈩      (Lvl 2, 45% IV, basic, no shadow)
Example: ~2½⁷⁶1•Venu      (Lvl 2.5, 76% IV, stage 1, shadow)
```

**Category-Specific Formats** (Shadow, XXS/XXL, Background):

```
₅{Stage}{IV}{Lvl}{•}{Name}{Leg}  (Shadow - always has •)
Example: ₅0⁸²2½•Char㈩

₆{Stage}{IV}{Lvl}{Name}{Leg}     (XXS/XXL - no size symbol needed)
Example: ₆0⁷⁵2Char㈩

₇{Stage}{IV}{Lvl}{Name}{Leg}     (Background)
Example: ₇0⁸²2Char㈩
```

---

## Symbol Legend

| Symbol                                      | Meaning                     | Symbol                       | Meaning         |
| ------------------------------------------- | --------------------------- | ---------------------------- | --------------- |
| `₁`, `₂`, `₃`, `₄`, `₅`, `₆`, `₇`, `₈`, `₉` | Favorite prefix             | `~`                          | Transfer/Trade  |
| `C`, `G`, `U`                               | League (Cup/Great/Ultra)    | `-`, `0`, `1`, `2`, `M`, `P` | Evolution stage |
| `•`                                         | Shadow                      | `°`                          | Purified        |
| `2`, `15`, `20`                               | Level (whole)               | `2½`, `15½`, `20½`             | Level (half)    |
| `⁸²`, `⁹⁶`, `¹⁰⁰`                           | IV percentage               | `84`, `38`, `15`             | PvP rank        |
| `⁸`, `A`, `a`                               | Attack/Defense rating       | `㈩`                         | Legacy move     |
| `♀`, `♂`                                    | Gender (rarely used)        |                              |                 |

**Evolution Stage**:

- `-` = Baby (e.g., Pichu, Riolu)
- `0` = Basic (e.g., Pikachu, Charmander)
- `1` = Stage 1 (e.g., Raichu, Charmeleon)
- `2` = Stage 2 (e.g., Charizard)
- `M` = Mega (e.g., Mega Charizard)
- `P` = Primal (e.g., Primal Kyogre, Primal Groudon)

**League Symbols**:

- `G` = Great League (CP ≤ 1,500)
- `U` = Ultra League (CP ≤ 2,500)
- `C` = Little League / Little Cup (CP ≤ 500)
- No symbol = Master League (unlimited CP)

**Level Format**:

- `2` = Level 2
- `2½` = Level 2.5 (half-level from power-up breakpoint)
- `15` = Level 15
- `15½` = Level 15.5
- `20` = Level 20
- `20½` = Level 20.5

**Note**: Half-levels (e.g., 2.5, 20.5) use `½` symbol and occur at power-up breakpoints. Shadow boost is NOT related to level format.

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

**Recommendation**: **Change to `PvP Rank % >= 97.55%`** (aligns with Rank ≤ 100)

**Note**: PokeGenie may only support certain decimal values. Use **97.55%** if available, otherwise **98%** (Rank ≤ 82, slightly more restrictive).

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
- "High IV (2)" - Auto (Has 2nd charge move)
- "High IV (₂)" - Manual (Favorite ₂ for Master League + high IV)

**Purpose**: Manually favorite Pokemon that don't meet auto-criteria but need same format.

**Use Case**: You have a Rank 150 Charmander that doesn't auto-trigger "PVP IV (PvP)", but you want PvP format for Great League. Manually favorite it as ₁ → gets `₁` prefix.

---

## Implementation Steps

### 1. Update Existing Conditions

In PokeGenie Settings → Name Generator:

| Generator        | Current          | Change To                                                |
| ---------------- | ---------------- | -------------------------------------------------------- |
| **PVP IV (PvP)** | PvP Rank % ≥ 95% | **PvP Rank % ≥ 97.55%** (or 98% if 97.55% not available) |
| **High IV (IV)** | IV ≥ 90%         | ✅ Keep as-is                                            |
| **Trade**        | Default          | ✅ Keep as-is                                            |

**Rename Generators** (align with Favorite numbers):

| Old Name        | New Name        | Favorite | Change    |
| --------------- | --------------- | -------- | --------- |
| **PVP IV (₂)**  | **PVP IV (₁)**  | ₁        | ✅ Rename |
| **High IV (₃)** | **High IV (₂)** | ₂        | ✅ Rename |
| **Kept (₄)**    | **Shiny (₃)**   | ₃        | ✅ Rename |

### 2. Add New Generators

Create 6 new generators with formats above:

- **Costume (₄)** with Favorite ₄ → Format: `₄{Stage}{IV}{Lvl}{•/°}{Name}{Leg}`
- **Shadow (₅)** with Favorite ₅ → Format: `₅{Stage}{IV}{Lvl}{•}{Name}{Leg}`
- **XXS/XXL (₆)** with Favorite ₆ → Format: `₆{Stage}{IV}{Lvl}{Name}{Leg}`
- **Background (₇)** with Favorite ₇ → Format: `₇{Stage}{IV}{Lvl}{Name}{Leg}`
- **Dynamax (₈)** with Favorite ₈ → Format: `₈{Stage}{•/°}{Name}{Rank}{IV}{Lvl}{Atk}{Atk2}{Leg}` (High IV format)
- **Gigantamax (₉)** with Favorite ₉ → Format: `₉{Stage}{•/°}{Name}{Rank}{IV}{Lvl}{Atk}{Atk2}{Leg}` (High IV format)

### 3. Test with 10-20 Pokemon

- Scan test Pokemon in PokeGenie
- Assign Favorites ₁-₉
- Verify names generate correctly
- Check that Dynamax/Gigantamax use High IV format with correct prefix

### 4. Update Tags in Pokemon GO

After renaming, tag Pokemon by prefix:

- Search "₁" → Review ranks, tag `#Great`, `#Ultra`, `#Little`, plus rank tags `#Rank1-3`, `#Rank4-20`, etc.
- Search "₂" → Review ranks, tag Master League ranks OR tag as high IV keepers
- Search "₃" → Tag `#Kept` (Shiny)
- Search "₄" → Tag `#Kept` (Costume)
- Search "₅" → Tag `#Kept` (Shadow)
- Search "₆" → Tag `#Kept` (XXS/XXL)
- Search "₇" → Tag `#Kept` (Background)
- Search "₈" → Tag `#Kept` (Dynamax)
- Search "₉" → Tag `#Kept` (Gigantamax)
- Search "~" → Tag `#Transfer`, `#Home`, `#Trade`, or `#LuckyTrade` based on retention category

---

## Category Reference

| Cat | Description        | Prefix | Favorite          | Retention                          |
| --- | ------------------ | ------ | ----------------- | ---------------------------------- |
| #1a | Great/Ultra League | ₁      | Auto (PvP ≥97.5%) | Keep 3 (Rank ≤10), 1 (Rank 11-100) |
| #1b | Little League      | ₁      | Auto (PvP ≥97.5%) | Keep 3 (Rank ≤10), 1 (Rank 11-100) |
| #2  | Master League      | ₂      | Favorite ₂        | Keep 3 (Rank ≤10), 1 (Rank 11-19)  |
| #3  | Shiny              | ₃      | Favorite ₃        | Keep 2 per species                 |
| #4  | Costumed           | ₄      | Favorite ₄        | Keep 2 per species                 |
| #5  | Shadow             | ₅      | Favorite ₅        | Keep 2 per species                 |
| #6  | XXS/XXL            | ₆      | Favorite ₆        | Keep 1 XXS + 1 XXL                 |
| #7  | Background         | ₇      | Favorite ₇        | Keep 2 per species                 |
| #8  | Dynamax            | ₈      | Favorite ₈        | Keep 2 per species                 |
| #9  | Gigantamax         | ₉      | Favorite ₉        | Keep 2 per species                 |
| #10 | Legendary Reserve  | ~      | (none)            | Keep top 10 (level+IV)             |
| #11 | Transfer Queue     | ~      | (none)            | Transfer at 2× candy events        |
| #12 | General Reserve    | ~      | (none)            | Keep top 2 (level+IV)              |
| #13 | Lucky Trade        | ~      | (none)            | Keep until aged 3+ years           |

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
- **Result**: `₂1•Metagr15⁹⁶2A㈩`

---

## Related Files

- `STORAGE_STRATEGY_CORRECTED.md` - 13-category retention strategy (with #1a/#1b subcategories)
- `docs/reference/TAG_SYSTEM.md` - 43-tag system documentation
- `docs/reference/FAVORITE_QUERIES.md` - Search query strings
- `SUMMARY.md` - Project reorganization summary

---

_PokeGenie Name Generator Setup - Updated 2025-10-13_
