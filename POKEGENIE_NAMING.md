# PokeGenie Name Generator - Improved Setup

**Date**: 2025-10-12
**Purpose**: Align PokeGenie naming with updated tag system (43 tags, PascalCase)

---

## Current Setup Issues

### 1. **Misaligned with Tag System**
- Uses Favorite ₁, ₂, ₃, ₄ but your tags are `#Rank1`, `#Rank2`, `#Rank3`, not Favorite numbers
- Missing alignment with `#Trade`, `#LuckyTrade`, `#Kept` tags

### 2. **Trade Category Confusion**
- "Trade (⇄)" and "Trage (₁)" both use same format but different triggers
- "Trade" uses condition: Average IV <= 50% and Level >= 30 (lucky trade candidates)
- "Trage" uses Favorite ₁ (should align with PvP ranks)

### 3. **Duplicate Conditions**
- "PVP IV (PvP)" and "PVP IV (₂)" generate same format
- "High IV (IV)", "High IV (2)", "High IV (₃)" generate same format

### 4. **Missing Categories**
- No naming for `#Transfer`, `#Home`, `#PowerUp`, `#TM`, `#InTraining`
- No naming for `#Attackers` (raid attackers)
- No naming for `#Def1`, `#Def2`, `#Def2.5` (gym defenders)
- No naming for `#Mega` candidates

---

## Recommended Improved Setup

### Strategy: Align with Your Tag System

**Map PokeGenie Favorites to Your Tags:**
- Favorite ₁ = `#Rank1` (Your #1 best for species/league) - **PvP focused**
- Favorite ₂ = `#Rank2` (Your #2 best for species/league) - **PvP focused**
- Favorite ₃ = `#Rank3` (Your #3 best for species/league) - **PvP focused**
- Favorite ₄ = `#Kept` (Permanent collection) - **Living dex/trophies**
- Favorite ₅ = `#Trade` (General trading queue) - **Trade candidates**
- Favorite ₆ = `#LuckyTrade` (Lucky friend trades) - **Lucky trade candidates**
- Favorite ₇ = `#Attackers` (Raid attackers) - **Raid teams**
- Favorite ₈ = `#PowerUp` (Needs power-up) - **Resource queue**

---

## Improved Name Generators

### 1. **PvP Rank 1** (Favorite ₁)
**Format**: `₁{League}{Evo Stage}{Sha/Pur}{Name Fill Tgt}{Rank #}{Attack Rating}{Attack2 Rating}{Legacy}`
**Example**: `₁Ⓖ①Ch1921aa㈩` or `₁Ⓤ②Venu1484A`
**Condition**: Favorite ₁
**Purpose**: Your best PvP IV for each species/league (#Rank1)

**Improvements**:
- ✅ Keep as-is, perfectly aligned with #Rank1 tag

---

### 2. **PvP Rank 2** (Favorite ₂)
**Format**: `₂{League}{Evo Stage}{Sha/Pur}{Name Fill Tgt}{Rank #}{Attack Rating}{Attack2 Rating}{Legacy}`
**Example**: `₂Ⓖ①Ch0584aa㈩` or `₂Ⓤ②Venu0238A`
**Condition**: Favorite ₂
**Purpose**: Your 2nd best PvP IV for each species/league (#Rank2)

**Changes**:
- Changed prefix from ₂ (currently used for High IV) → Use unique prefix
- **Recommended prefix**: `⒉` or keep `₂` but change High IV to `Ⓗ`

---

### 3. **PvP Rank 3** (Favorite ₃)
**Format**: `₃{League}{Evo Stage}{Sha/Pur}{Name Fill Tgt}{Rank #}{Attack Rating}{Attack2 Rating}{Legacy}`
**Example**: `₃Ⓖ①Ch0912aa㈩` or `₃Ⓤ②Venu0456A`
**Condition**: Favorite ₃
**Purpose**: Your 3rd best PvP IV for each species/league (#Rank3)

**Changes**:
- Changed prefix from ₃ (currently used for Kept) → Use unique prefix
- **Recommended prefix**: `⒊` or keep `₃` but change Kept to `Ⓚ`

---

### 4. **Kept / Permanent Collection** (Favorite ₄)
**Format**: `Ⓚ{Evo Stage}{IV Avg}{Level}{Shadow}{Name Fill Tgt}{Legacy}`
**Example**: `Ⓚ①⁸²⑳½Charm㈩` or `Ⓚ②⁷⁶⑳Venusau`
**Condition**: Favorite ₄
**Purpose**: Permanent collection - living dex, trophies (#Kept)

**Changes**:
- Changed prefix: `₃` → `Ⓚ` (K = Kept)
- Removed redundant info (no need for PvP rank for kept Pokemon)

---

### 5. **General Trade Queue** (Favorite ₅)
**Format**: `Ⓣ{Level}{IV Avg}{Evo Stage}{Sha/Pur}{Name Fill Tgt}{Legacy}`
**Example**: `Ⓣ⑳⁴⁵①Charm㈩` or `Ⓣ⑳⁵⁸②Venusau`
**Condition**: Favorite ₅
**Purpose**: General trading queue (#Trade)

**Changes**:
- Changed prefix: `⇄` → `Ⓣ` (T = Trade)
- **Old condition**: Average IV <= 50% and Level >= 30 (too restrictive)
- **New condition**: Favorite ₅ (manually tagged as #Trade)

---

### 6. **Lucky Trade Candidates** (Favorite ₆)
**Format**: `Ⓛ{Age}{IV Avg}{Evo Stage}{Sha/Pur}{Name Fill Tgt}{Legacy}`
**Example**: `Ⓛ⁴⁵⁰⁶⁷①Charm㈩` or `Ⓛ⁸⁰⁰⁵⁴②Venusau`
**Condition**: Favorite ₆
**Purpose**: Lucky trade candidates (#LuckyTrade)

**Changes**:
- **New format**: Added `{Age}` field (days old)
- Prefix: `Ⓛ` (L = Lucky)
- Shows age for lucky trade planning (1+ year = 365+ days)

---

### 7. **Raid Attackers** (Favorite ₇)
**Format**: `Ⓐ{Evo Stage}{IV Avg}{Level}{Shadow}{Name Fill Tgt}{Attack Rating}{Attack2 Rating}{Legacy}`
**Example**: `Ⓐ②⁹⁶⑳½Metagr⁸A㈩` or `Ⓐ③¹⁰⁰⑳Rayqua⁸⁸`
**Condition**: Favorite ₇
**Purpose**: Raid attackers (#Attackers)

**Changes**:
- Changed prefix: `₇` (currently Default) → `Ⓐ` (A = Attackers)
- Added Attack ratings (important for raids)
- Shows shadow status (shadows are better for raids)

---

### 8. **Power-Up Queue** (Favorite ₈)
**Format**: `Ⓟ{Evo Stage}{IV Avg}{Level}{Shadow}{Name Fill Tgt}{Candy Cost}{Dust Cost}{Legacy}`
**Example**: `Ⓟ②⁹⁶⑳½Metagr③④` or `Ⓟ③¹⁰⁰⑳Rayqua⑤⑧`
**Condition**: Favorite ₈
**Purpose**: Pokemon needing power-up (#PowerUp)

**Changes**:
- Prefix: `Ⓟ` (P = PowerUp)
- Added candy/dust cost indicators (helps planning)
- Shows current level to track progress

---

### 9. **High IV (Non-PvP)** (Condition: Average IV >= 90%)
**Format**: `Ⓗ{Evo Stage}{IV Avg}{Level}{Shadow}{Name Fill Tgt}{Gender}{Legacy}`
**Example**: `Ⓗ①⁹⁶⑳½Ch♀㈩` or `Ⓗ②¹⁰⁰⑳Venusa♂`
**Condition**: Average IV >= 90%
**Purpose**: High IV Pokemon (raid attackers, gym defenders, hundos)

**Changes**:
- Changed prefix: `₂` → `Ⓗ` (H = High IV)
- Simplified: removed PvP rank (not relevant for high IV)
- Added gender (useful for living dex)

---

### 10. **Default** (Fallback)
**Format**: `•{Evo Stage}{IV Avg}{Level}{Shadow}{Name Fill Tgt}{Gender}{Legacy}`
**Example**: `•①⁶⁷⑮½Ch♀㈩` or `•②⁵⁴⑫Venusa♂`
**Condition**: Default (no other conditions match)
**Purpose**: Everything else (review candidates, duplicates)

**Changes**:
- Changed prefix: `₇` → `•` (bullet point, neutral)
- Keep minimal info for quick review

---

## Summary: Prefix Legend

| Prefix | Favorite # | Tag           | Purpose                  |
| ------ | ---------- | ------------- | ------------------------ |
| `₁`    | ₁          | `#Rank1`      | PvP Rank 1 (best owned)  |
| `⒉`    | ₂          | `#Rank2`      | PvP Rank 2 (2nd best)    |
| `⒊`    | ₃          | `#Rank3`      | PvP Rank 3 (3rd best)    |
| `Ⓚ`    | ₄          | `#Kept`       | Permanent collection     |
| `Ⓣ`    | ₅          | `#Trade`      | General trading queue    |
| `Ⓛ`    | ₆          | `#LuckyTrade` | Lucky trade candidates   |
| `Ⓐ`    | ₇          | `#Attackers`  | Raid attackers           |
| `Ⓟ`    | ₈          | `#PowerUp`    | Power-up queue           |
| `Ⓗ`    | (IV check) | (none)        | High IV (90%+)           |
| `•`    | Default    | (none)        | Default/review           |

---

## Implementation Steps

1. **In PokeGenie Settings → Name Generator**:
   - Update each generator with new formats above
   - Map Favorite ₁-₈ to match your tag system

2. **Workflow**:
   - Scan Pokemon with PokeGenie
   - Favorite them based on purpose (₁ = best PvP, ₄ = kept, ₅ = trade, etc.)
   - Batch rename using PokeGenie

3. **In Pokemon GO**:
   - Tag Pokemon after renaming: `#Rank1`, `#Kept`, `#Trade`, etc.
   - Use favorite queries to find tagged Pokemon

---

## Alternative: Simpler Setup (If Current is Too Complex)

If you want to simplify, consider:

**Option A: Tag-First Approach**
- Tag Pokemon in-game first (`#Rank1`, `#Trade`, etc.)
- Use PokeGenie only for IV/rank info
- Simpler names: `Ⓖ①1921` (GL Stage1 Rank1921)

**Option B: Condition-Based Only**
- Remove Favorite conditions entirely
- Use only automatic conditions:
  - PvP: Average PvP Rank % >= 95%
  - High IV: Average IV >= 90%
  - Trade: Average IV <= 60% AND Level >= 30
  - Default: Everything else

---

## Recommended Next Steps

1. **Test new setup** with 10-20 Pokemon first
2. **Verify alignment** with your tag system
3. **Adjust prefixes** if Unicode symbols don't display well
4. **Document** your final setup for reference

---

_PokeGenie Name Generator Setup - Updated 2025-10-12_
