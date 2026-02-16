# Raid Attacker Retention Counts - Exact Recommendations

**Last Updated**: 2026-02-16
**Data Source**: GamePress Comprehensive DPS/TDO Spreadsheet (2025-10-12), GamePress Tier List (2026-02), PokemonGOHub DB
**User Priority**: Collecting > Raids > Trading >>> PvP (minimal)

---

## How to Use This Guide

This document provides **exact recommended counts** for each top raid attacker, calculated using the ER-based tier methodology below. Every count is reproducible from the formula.

---

## Count Tier Methodology

### Maximum Count: 6

Pokemon GO raids use a **team of 6 Pokemon**. In practice, most trainers use mixed-species teams (3-4 species per team), group raids rarely require re-lobby, and storage is limited. One full team (6 copies) is the practical maximum for any single species.

### Step 1: Base Count from Estimator Rating (ER)

ER is a composite metric combining DPS (damage output) and TDO (survivability).

| ER Range  | Tier | Base Count | Description        |
| --------- | ---- | ---------- | ------------------ |
| ≥ 60      | S    | 6          | Elite dominant     |
| 55 – 59.9 | A    | 5          | Top-tier performer |
| 50 – 54.9 | B    | 4          | Strong reliable    |
| 45 – 49.9 | C    | 3          | Solid depth        |
| 40 – 44.9 | D    | 2          | Niche backup       |
| < 40      | E    | 1          | Budget replaceable |

**Missing ER proxy** (for Pokemon without GamePress ER data):

- Within-type DPS rank #1-2 → treat as Tier A (base 5)
- DPS rank #3-5 → treat as Tier B (base 4)
- DPS rank #6-10 → treat as Tier C (base 3)

### Step 2: Modifiers

| Modifier     | Effect | Condition                                                       |
| ------------ | ------ | --------------------------------------------------------------- |
| Dual-type    | +1     | Rank #1-5 in TWO or more types                                  |
| Legendary/UB | +1     | Legendary, Mythical, or Ultra Beast (limited raid availability) |
| Accessible   | -1     | Common spawn or easily evolved (Machop, Eevee, Roselia, Weedle) |
| Glass cannon | -1     | TDO < 300                                                       |

### Step 3: Hard Caps & Overrides

| Rule            | Effect                                                |
| --------------- | ----------------------------------------------------- |
| Maximum         | 6 (one full raid team)                                |
| Minimum         | 1                                                     |
| Account-limited | = account limit (Eternatus: 1, Keldeo: 1, Diancie: 1) |
| Giovanni-only   | "keep all" + note practical range                     |

### Step 4: Mega/Primal Merge

- Mega/Primal forms merge with their base form (same physical Pokemon)
- Use the BEST ER between forms for tier calculation
- Entry format: `Species: count (Mega)` or `Species: count (Primal)`
- Shadow forms remain separate entries (different Pokemon)

---

## Quick Reference Table

| Pokemon                 | Count | ER    | Types Covered        | Tier Calc                       |
| ----------------------- | ----- | ----- | -------------------- | ------------------------------- |
| **Rayquaza** (Mega)     | **6** | 81.15 | Dragon, Flying       | S(6)+legend+dual→cap6           |
| **Groudon** (Primal)    | **6** | 64.29 | Ground               | S(6)+legend→cap6                |
| **Kyogre** (Primal)     | **6** | 64.38 | Water                | S(6)+legend→cap6                |
| **Shadow Mewtwo**       | **6** | 63.29 | Psychic              | S(6), Giovanni: keep all        |
| **Garchomp** (Mega)     | **6** | 61.11 | Dragon, Ground       | S(6)+dual                       |
| **Shadow Salamence**    | **6** | 54.31 | Dragon, Flying       | B(4)+legend+dual                |
| **Shadow Metagross**    | **6** | 55.59 | Psychic, Steel       | A(5)+dual                       |
| **Shadow Moltres**      | **6** | 51.93 | Fire, Flying         | B(4)+legend+dual, Giovanni      |
| **Shadow Regigigas**    | **6** | 56.54 | Normal               | A(5)+legend, Giovanni           |
| **Tyranitar** (Mega)    | **6** | 58.91 | Rock, Dark           | A(5)+dual                       |
| **Heracross** (Mega)    | **6** | 55.06 | Bug, Fighting        | A(5)+dual                       |
| **Blaziken** (Mega)     | **6** | 57.78 | Fire, Fighting       | A(5)+dual                       |
| **Lucario** (Mega)      | **6** | 58.07 | Fighting, Steel      | A(5)+dual                       |
| **Kyurem (White)**      | **6** | —     | Ice, Dragon          | proxy A(5)+legend               |
| **Kyurem (Black)**      | **6** | —     | Ice, Dragon          | proxy A(5)+legend               |
| **Zacian (Crowned)**    | **6** | —     | Steel, Fairy         | proxy A(5)+legend+dual→cap6     |
| **Zamazenta (Crowned)** | **6** | —     | Steel                | proxy A(5)+legend               |
| **Dawn Wings Necrozma** | **6** | —     | Ghost, Psychic       | proxy A(5)+legend               |
| **Dusk Mane Necrozma**  | **6** | —     | Steel, Psychic       | proxy B(4)+legend+dual          |
| Mewtwo                  | 5     | 54.57 | Psychic              | B(4)+legend                     |
| Shadow Groudon          | 5     | 54.66 | Ground               | B(4)+legend, Giovanni           |
| Shadow Kyogre           | 5     | 54.76 | Water                | B(4)+legend, Giovanni           |
| Palkia (Origin)         | 5     | 54.48 | Dragon, Water        | B(4)+legend                     |
| Dialga (Origin)         | 5     | 54.37 | Dragon, Steel        | B(4)+legend                     |
| Shadow Tyranitar        | 5     | 53.64 | Rock, Dark           | B(4)+dual                       |
| Yveltal                 | 5     | 50.29 | Dark, Flying         | B(4)+legend                     |
| Hoopa (Unbound)         | 5     | 50.16 | Dark, Ghost, Psychic | B(4)+mythical                   |
| Reshiram                | 5     | 51.79 | Fire, Dragon         | B(4)+legend                     |
| Shadow Heatran          | 5     | ~50   | Fire, Steel          | B(4)+legend, Giovanni           |
| Shadow Latios           | 5     | 51.67 | Dragon, Psychic      | B(4)+legend                     |
| Shadow Chandelure       | 5     | 51.49 | Fire, Ghost          | B(4)+dual                       |
| Gengar (Mega)           | 5     | 57.59 | Ghost, Poison        | A(5)+dual-accessible            |
| Metagross (Mega)        | 5     | 58.01 | Psychic, Steel       | A(5)                            |
| Swampert (Mega)         | 5     | 55.62 | Water, Ground        | A(5)                            |
| Regieleki               | 5     | —     | Electric             | proxy A(5)+legend-glass         |
| Terrakion               | 5     | 51.02 | Rock, Fighting       | B(4)+legend                     |
| Kartana                 | 5     | 48.09 | Grass, Steel         | C(3)+UB+dual                    |
| Shadow Dragonite        | 4     | 52.70 | Dragon, Flying       | B(4)                            |
| Zekrom                  | 4     | 49.85 | Electric, Dragon     | C(3)+legend                     |
| Shadow Garchomp         | 4     | 53.95 | Dragon, Ground       | B(4)                            |
| Shadow Rampardos        | 4     | 50.05 | Rock                 | B(4)                            |
| Shadow Rhyperior        | 4     | 51.67 | Rock, Ground         | B(4)                            |
| Landorus (Therian)      | 4     | 47.71 | Ground, Flying       | C(3)+legend                     |
| Shadow Blaziken         | 4     | 48.61 | Fire, Fighting       | C(3)+dual                       |
| Kyurem (regular)        | 4     | 46.93 | Ice, Dragon          | C(3)+legend                     |
| Shadow Gengar           | 4     | 48.42 | Ghost, Poison        | C(3)+dual                       |
| Lunala                  | 4     | —     | Ghost, Psychic       | proxy C(3)+legend               |
| Blacephalon             | 4     | —     | Fire, Ghost          | proxy C(3)+UB                   |
| Shadow Raikou           | 4     | 48.96 | Electric             | C(3)+legend, Giovanni           |
| Shadow Zapdos           | 4     | 47.94 | Electric, Flying     | C(3)+legend, Giovanni           |
| Xurkitree               | 4     | 47.99 | Electric             | C(3)+UB                         |
| Shadow Excadrill        | 4     | 48.66 | Ground, Steel        | C(3)+dual                       |
| Shadow Weavile          | 4     | 46.95 | Ice, Dark            | C(3)+dual                       |
| Regigigas               | 4     | 49.00 | Normal               | C(3)+legend                     |
| Palkia                  | 4     | 47.39 | Water, Dragon        | C(3)+legend                     |
| Dialga                  | 4     | —     | Steel, Dragon        | C(3)+legend                     |
| Sceptile (Mega)         | 4     | 56.25 | Grass                | A(5)-accessible                 |
| Salamence (Mega)        | 4     | 56.03 | Dragon, Flying       | A(5)-accessible                 |
| Alakazam (Mega)         | 4     | 56.96 | Psychic              | A(5)-accessible                 |
| Shadow Honchkrow        | 3     | 48.91 | Dark, Flying         | C(3)+dual-accessible            |
| Xerneas                 | 3     | 44.41 | Fairy                | D(2)+legend                     |
| Shadow Mamoswine        | 3     | 49.62 | Ice, Ground          | C(3)                            |
| Shadow Electivire       | 3     | 47.32 | Electric             | C(3)                            |
| Shadow Magnezone        | 3     | 46.11 | Electric, Steel      | C(3)                            |
| Shadow Swampert         | 3     | 47.10 | Water, Ground        | C(3)                            |
| Shadow Darmanitan       | 3     | 49.08 | Fire, Ice            | C(3)                            |
| Gardevoir (Mega)        | 3     | 53.93 | Fairy, Psychic       | B(4)-accessible                 |
| Heatran                 | 3     | ~42   | Fire, Steel          | D(2)+legend                     |
| Pheromosa               | 3     | 42.89 | Bug, Fighting        | D(2)+UB                         |
| Shadow Darkrai          | 3     | —     | Dark                 | D(2)+mythical, Giovanni         |
| Shadow Gardevoir        | 2     | 44.85 | Fairy, Psychic       | D(2)                            |
| Shadow Staraptor        | 2     | 48.24 | Normal, Flying       | C(3)-accessible                 |
| Shadow Alakazam         | 2     | 47.53 | Psychic              | C(3)-accessible                 |
| Shadow Machamp          | 2     | 47.05 | Fighting             | C(3)-accessible                 |
| Shadow Conkeldurr       | 2     | —     | Fighting             | D(2)                            |
| Shadow Toxicroak        | 2     | 41.01 | Poison, Fighting     | D(2)                            |
| Shadow Tangrowth        | 2     | 44.06 | Grass                | D(2)                            |
| Rampardos               | 2     | 42.94 | Rock                 | D(2)                            |
| Volcarona               | 2     | 44.46 | Bug, Fire            | D(2)                            |
| Hydreigon               | 2     | —     | Dark, Dragon         | D(2)                            |
| Beedrill (Mega)         | 2     | 46.35 | Bug                  | C(3)-accessible                 |
| Shadow Palkia           | 2     | —     | Dragon, Water        | Giovanni: keep all              |
| Shadow Dialga           | 2     | —     | Steel, Dragon        | Giovanni: keep all              |
| Eternatus               | 1     | —     | Dragon, Poison       | Account-limited (1 per account) |
| Keldeo (Resolute)       | 1     | —     | Fighting, Water      | Account-limited                 |
| Diancie (Mega)          | 1     | —     | Rock, Fairy          | Account-limited                 |
| Deoxys (Attack)         | 1     | 38.45 | Psychic              | E(1)+mythical-glass             |
| Charizard (Mega)        | 1     | —     | Fire, Flying         | D(2)-accessible                 |
| Pinsir (Mega)           | 1     | 44.98 | Bug                  | D(2)-accessible                 |
| Scizor (Mega)           | 1     | 41.86 | Bug, Steel           | D(2)-accessible                 |

---

## Detailed Breakdowns by Type

### Bug Type

| Pokemon          | Count | Rank | ER    | Notes                         |
| ---------------- | ----- | ---- | ----- | ----------------------------- |
| Heracross (Mega) | 6     | #1   | 55.06 | Also #4 Fighting, dual-type   |
| Pheromosa        | 3     | #2   | 42.89 | Ultra Beast, also #6 Fighting |
| Beedrill (Mega)  | 2     | #3   | 46.35 | Weedle is common spawn        |
| Pinsir (Mega)    | 1     | #4   | 44.98 | Accessible                    |
| Volcarona        | 2     | #5   | 44.46 | Also Fire-type                |
| Scizor (Mega)    | 1     | #7   | 41.86 | Also Steel-type               |

**Bug Raid Frequency**: Low (rare raid type)

---

### Dark Type

| Pokemon          | Count | Rank | ER    | Notes                             |
| ---------------- | ----- | ---- | ----- | --------------------------------- |
| Shadow Honchkrow | 3     | #1   | 48.91 | Also #4 Flying, accessible shadow |
| Shadow Tyranitar | 5     | #3   | 53.64 | Also #2 Rock, dual coverage       |
| Tyranitar (Mega) | 6     | #4   | 58.91 | Also #3 Rock, dual coverage       |
| Shadow Weavile   | 4     | #5   | 46.95 | Also #2 Ice, dual coverage        |
| Hoopa (Unbound)  | 5     | #6   | 50.16 | Also Ghost/Psychic, mythical      |
| Shadow Darkrai   | 3     | —    | —     | Mythical shadow, Giovanni         |
| Yveltal          | 5     | #9   | 50.29 | Legendary, excellent bulk         |
| Hydreigon        | 2     | #10+ | —     | Pseudo-legendary                  |

**Dark Raid Frequency**: Medium (Psychic/Ghost bosses common)

---

### Dragon Type

| Pokemon          | Count | Rank | ER    | Notes                            |
| ---------------- | ----- | ---- | ----- | -------------------------------- |
| Eternatus        | 1     | #1   | —     | 1 per account (Special Research) |
| Rayquaza (Mega)  | 6     | #2   | 81.15 | Also #1 Flying, dominates        |
| Shadow Salamence | 6     | #3   | 54.31 | Also #3 Flying, dual coverage    |
| Garchomp (Mega)  | 6     | #4   | 61.11 | Also #2 Ground, dual coverage    |
| Shadow Dragonite | 4     | #5   | 52.70 | Also #7 Flying                   |
| Shadow Garchomp  | 4     | #6   | 53.95 | Also #4 Ground                   |
| Shadow Latios    | 5     | #8   | 51.67 | Also Psychic, legendary          |
| Palkia (Origin)  | 5     | #9   | 54.48 | Also #3 Water, legendary         |
| Dialga (Origin)  | 5     | #10  | 54.37 | Also #6 Steel, legendary         |
| Salamence (Mega) | 4     | #10+ | 56.03 | Accessible                       |
| Palkia           | 4     | #10+ | 47.39 | Regular forme                    |
| Dialga           | 4     | #10+ | —     | Regular forme                    |

**Dragon Raid Frequency**: High (Dragon bosses very common)

---

### Electric Type

| Pokemon           | Count | Rank | ER    | Notes                              |
| ----------------- | ----- | ---- | ----- | ---------------------------------- |
| Shadow Electivire | 3     | #1   | 47.32 | Accessible evolution               |
| Regieleki         | 5     | #2   | —     | Glass cannon (TDO: 250), legendary |
| Shadow Raikou     | 4     | #3   | 48.96 | Shadow legendary, Giovanni         |
| Xurkitree         | 4     | #4   | 47.99 | Ultra Beast                        |
| Shadow Zapdos     | 4     | #5   | 47.94 | Also Flying, Giovanni              |
| Shadow Magnezone  | 3     | #7   | 46.11 | Also Steel                         |
| Zekrom            | 4     | #9   | 49.85 | Also Dragon, legendary             |

**Electric Raid Frequency**: Medium (Water/Flying bosses)

---

### Fairy Type

| Pokemon          | Count | Rank | ER    | Notes                     |
| ---------------- | ----- | ---- | ----- | ------------------------- |
| Gardevoir (Mega) | 3     | #1   | 53.93 | Also Psychic, accessible  |
| Zacian (Crowned) | 6     | #2   | —     | Also #1 Steel, legendary  |
| Shadow Gardevoir | 2     | #3   | 44.85 | Also Psychic              |
| Xerneas          | 3     | #8   | 44.41 | Legendary, excellent bulk |

**Fairy Raid Frequency**: Medium (Dragon/Dark/Fighting bosses)

---

### Fighting Type

| Pokemon           | Count | Rank | ER    | Notes                       |
| ----------------- | ----- | ---- | ----- | --------------------------- |
| Lucario (Mega)    | 6     | #1   | 58.07 | Also #1 Steel, dual Mega    |
| Blaziken (Mega)   | 6     | #2   | 57.78 | Also #1 Fire, dual Mega     |
| Keldeo (Resolute) | 1     | #3   | —     | Account-limited             |
| Shadow Blaziken   | 4     | #4   | 48.61 | Also #4 Fire, dual coverage |
| Heracross (Mega)  | 6     | #5   | 55.06 | Also #1 Bug, dual coverage  |
| Pheromosa         | 3     | #6   | 42.89 | Ultra Beast                 |
| Shadow Machamp    | 2     | #8   | 47.05 | Very accessible shadow      |
| Terrakion         | 5     | #9   | 51.02 | Also #5 Rock, legendary     |
| Shadow Conkeldurr | 2     | #10+ | —     | Accessible shadow           |

**Fighting Raid Frequency**: High (Normal/Dark/Steel/Ice/Rock bosses common)

---

### Fire Type

| Pokemon           | Count | Rank | ER    | Notes                        |
| ----------------- | ----- | ---- | ----- | ---------------------------- |
| Blaziken (Mega)   | 6     | #1   | 57.78 | Also #2 Fighting, dual Mega  |
| Charizard (Mega)  | 1     | #2   | —     | Accessible                   |
| Shadow Chandelure | 5     | #3   | 51.49 | Also #2 Ghost, dual coverage |
| Shadow Darmanitan | 3     | #4   | 49.08 | Also Ice-type                |
| Shadow Blaziken   | 4     | #5   | 48.61 | Also #3 Fighting             |
| Shadow Moltres    | 6     | #6   | 51.93 | Also #5 Flying, Giovanni     |
| Shadow Heatran    | 5     | #7   | ~50   | Also Steel, Giovanni         |
| Blacephalon       | 4     | #8   | —     | Ultra Beast, also Ghost      |
| Reshiram          | 5     | #9   | 51.79 | Also Dragon, legendary       |
| Heatran           | 3     | #10+ | ~42   | Also Steel, legendary        |

**Fire Raid Frequency**: Medium-High (Grass/Bug/Steel/Ice bosses)

---

### Flying Type

| Pokemon          | Count | Rank | ER    | Notes                         |
| ---------------- | ----- | ---- | ----- | ----------------------------- |
| Rayquaza (Mega)  | 6     | #1   | 81.15 | Also #2 Dragon, dominates     |
| Shadow Salamence | 6     | #3   | 54.31 | Also #3 Dragon, dual coverage |
| Shadow Honchkrow | 3     | #4   | 48.91 | Also #1 Dark, accessible      |
| Shadow Moltres   | 6     | #5   | 51.93 | Also #5 Fire, Giovanni        |
| Shadow Staraptor | 2     | #6   | 48.24 | Also Normal, accessible       |
| Shadow Dragonite | 4     | #7   | 52.70 | Also #5 Dragon                |
| Shadow Zapdos    | 4     | #9   | 47.94 | Also #5 Electric, Giovanni    |

**Flying Raid Frequency**: Medium (Fighting/Bug/Grass bosses)

---

### Ghost Type

| Pokemon             | Count | Rank | ER    | Notes                       |
| ------------------- | ----- | ---- | ----- | --------------------------- |
| Dawn Wings Necrozma | 6     | #1   | —     | Legendary fusion, dominates |
| Gengar (Mega)       | 5     | #2   | 57.59 | Also #1 Poison, accessible  |
| Shadow Chandelure   | 5     | #3   | 51.49 | Also #2 Fire, dual coverage |
| Shadow Gengar       | 4     | #4   | 48.42 | Also #2 Poison              |
| Blacephalon         | 4     | #5   | —     | Ultra Beast, also Fire      |
| Hoopa (Unbound)     | 5     | #6   | 50.16 | Also Dark, mythical         |
| Lunala              | 4     | #7   | —     | Also Psychic, legendary     |

**Ghost Raid Frequency**: Medium (Psychic bosses)

---

### Grass Type

| Pokemon          | Count | Rank | ER    | Notes                      |
| ---------------- | ----- | ---- | ----- | -------------------------- |
| Sceptile (Mega)  | 4     | #1   | 56.25 | Accessible                 |
| Kartana          | 5     | #2   | 48.09 | Also #5 Steel, Ultra Beast |
| Shadow Tangrowth | 2     | #8   | 44.06 | Accessible shadow          |

**Grass Raid Frequency**: Medium-High (Water/Ground/Rock bosses)

---

### Ground Type

| Pokemon            | Count | Rank | ER    | Notes                         |
| ------------------ | ----- | ---- | ----- | ----------------------------- |
| Groudon (Primal)   | 6     | #1   | 64.29 | Massive ER, Primal evolution  |
| Garchomp (Mega)    | 6     | #2   | 61.11 | Also #4 Dragon, dual coverage |
| Shadow Groudon     | 5     | #3   | 54.66 | Shadow legendary, Giovanni    |
| Shadow Garchomp    | 4     | #4   | 53.95 | Also #6 Dragon                |
| Shadow Excadrill   | 4     | #5   | 48.66 | Also #3 Steel, dual coverage  |
| Shadow Mamoswine   | 3     | #6   | 49.62 | Also #1 Ice                   |
| Swampert (Mega)    | 5     | #7   | 55.62 | Also #4 Water                 |
| Shadow Rhyperior   | 4     | #8   | 51.67 | Also #4 Rock                  |
| Shadow Swampert    | 3     | #9   | 47.10 | Also Water                    |
| Landorus (Therian) | 4     | #10  | 47.71 | Legendary                     |

**Ground Raid Frequency**: High (Electric/Fire/Poison/Rock/Steel bosses)

---

### Ice Type

| Pokemon          | Count | Rank | ER    | Notes                       |
| ---------------- | ----- | ---- | ----- | --------------------------- |
| Kyurem (White)   | 6     | #1   | —     | Legendary forme, Dragon/Ice |
| Kyurem (Black)   | 6     | #2   | —     | Legendary forme, Dragon/Ice |
| Shadow Mamoswine | 3     | #3   | 49.62 | Also #6 Ground              |
| Shadow Weavile   | 4     | #4   | 46.95 | Also #5 Dark, dual coverage |
| Kyurem (regular) | 4     | #5+  | 46.93 | Regular forme, legendary    |

**Ice Raid Frequency**: High (Dragon/Flying/Grass/Ground bosses common)

---

### Normal Type

| Pokemon          | Count | Rank | ER    | Notes                      |
| ---------------- | ----- | ---- | ----- | -------------------------- |
| Shadow Regigigas | 6     | #1   | 56.54 | Shadow legendary, Giovanni |
| Shadow Staraptor | 2     | #2   | 48.24 | Also Flying, accessible    |
| Regigigas        | 4     | #7   | 49.00 | Legendary                  |

**Normal Raid Frequency**: Very Low (almost never needed)

---

### Poison Type

| Pokemon          | Count | Rank | ER    | Notes                          |
| ---------------- | ----- | ---- | ----- | ------------------------------ |
| Eternatus        | 1     | #1   | —     | Also #1 Dragon (1 per account) |
| Gengar (Mega)    | 5     | #2   | 57.59 | Also #1 Ghost, accessible      |
| Shadow Gengar    | 4     | #3   | 48.42 | Also #3 Ghost                  |
| Shadow Toxicroak | 2     | #5   | 41.01 | Also Fighting                  |

**Poison Raid Frequency**: Low (Fairy bosses uncommon)

---

### Psychic Type

| Pokemon          | Count | Rank | ER    | Notes                        |
| ---------------- | ----- | ---- | ----- | ---------------------------- |
| Shadow Mewtwo    | 6     | #1   | 63.29 | Dominates type, Giovanni     |
| Alakazam (Mega)  | 4     | #2   | 56.96 | Accessible                   |
| Deoxys (Attack)  | 1     | #3   | 38.45 | Glass cannon (TDO: 171.8)    |
| Shadow Metagross | 6     | #4   | 55.59 | Also #2 Steel, dual coverage |
| Shadow Alakazam  | 2     | #5   | 47.53 | Accessible shadow            |
| Mewtwo           | 5     | #6   | 54.57 | Legendary                    |
| Shadow Latios    | 5     | #10  | 51.67 | Also Dragon, legendary       |

**Psychic Raid Frequency**: Medium-High (Fighting/Poison bosses)

---

### Rock Type

| Pokemon          | Count | Rank | ER    | Notes                       |
| ---------------- | ----- | ---- | ----- | --------------------------- |
| Diancie (Mega)   | 1     | #1   | —     | Mythical (1 per account)    |
| Shadow Rampardos | 4     | #2   | 50.05 | Glass cannon, high DPS      |
| Shadow Tyranitar | 5     | #3   | 53.64 | Also #3 Dark, dual coverage |
| Tyranitar (Mega) | 6     | #4   | 58.91 | Also #4 Dark, excellent ER  |
| Shadow Rhyperior | 4     | #5   | 51.67 | Also #8 Ground              |
| Terrakion        | 5     | #6   | 51.02 | Also #9 Fighting, legendary |
| Rampardos        | 2     | #7   | 42.94 | Glass cannon, non-shadow    |

**Rock Raid Frequency**: High (Fire/Flying/Bug/Ice bosses)

---

### Steel Type

| Pokemon             | Count | Rank | ER    | Notes                          |
| ------------------- | ----- | ---- | ----- | ------------------------------ |
| Zacian (Crowned)    | 6     | #1   | —     | Also #2 Fairy, legendary       |
| Zamazenta (Crowned) | 6     | #2   | —     | Highest Steel TDO              |
| Dusk Mane Necrozma  | 6     | #3   | —     | Legendary fusion               |
| Lucario (Mega)      | 6     | #4   | 58.07 | Also #1 Fighting               |
| Shadow Metagross    | 6     | #5   | 55.59 | Also #4 Psychic, dual coverage |
| Shadow Dialga       | 2     | #6   | —     | Giovanni-limited               |
| Shadow Excadrill    | 4     | #7   | 48.66 | Also #5 Ground, dual coverage  |
| Metagross (Mega)    | 5     | #8   | 58.01 | Excellent ER                   |
| Kartana             | 5     | #9   | 48.09 | Also #2 Grass, Ultra Beast     |
| Dialga (Origin)     | 5     | #10  | 54.37 | Also Dragon, legendary         |
| Shadow Heatran      | 5     | #10+ | ~50   | Also Fire, Giovanni            |
| Shadow Magnezone    | 3     | #10+ | 46.11 | Also Electric                  |

**Steel Raid Frequency**: Medium (Fairy/Ice/Rock bosses)

---

### Water Type

| Pokemon         | Count | Rank | ER    | Notes                        |
| --------------- | ----- | ---- | ----- | ---------------------------- |
| Kyogre (Primal) | 6     | #1   | 64.38 | Massive ER, Primal evolution |
| Shadow Kyogre   | 5     | #2   | 54.76 | Shadow legendary, Giovanni   |
| Palkia (Origin) | 5     | #3   | 54.48 | Also #9 Dragon, legendary    |
| Swampert (Mega) | 5     | #4   | 55.62 | Also #7 Ground               |
| Shadow Swampert | 3     | #6   | 47.10 | Also Ground                  |
| Palkia          | 4     | #10  | 47.39 | Regular forme, legendary     |

**Water Raid Frequency**: Medium-High (Fire/Ground/Rock bosses)

---

## Special Cases & Exceptions

### Account-Limited Pokemon (Keep ALL)

| Pokemon               | Max Copies | Count | Notes                       |
| --------------------- | ---------- | ----- | --------------------------- |
| **Eternatus**         | 1          | 1     | #1 Dragon, #1 Poison        |
| **Keldeo (Resolute)** | 1          | 1     | #3 Fighting (best non-Mega) |
| **Diancie** (Mega)    | 1          | 1     | #1 Rock (Mega), Mythical    |

### Giovanni-Only (Keep ALL You Have)

| Pokemon              | Count | Practical Range | Notes                     |
| -------------------- | ----- | --------------- | ------------------------- |
| **Shadow Mewtwo**    | 6     | 3-5 copies      | #1 Psychic, irreplaceable |
| **Shadow Regigigas** | 6     | 2-4 copies      | #1 Normal                 |
| **Shadow Moltres**   | 6     | 2-4 copies      | #5 Fire, #5 Flying        |
| **Shadow Groudon**   | 5     | 1-3 copies      | #3 Ground                 |
| **Shadow Kyogre**    | 5     | 1-3 copies      | #2 Water                  |
| **Shadow Heatran**   | 5     | 1-3 copies      | #7 Fire, #10+ Steel       |
| **Shadow Latios**    | 5     | 1-3 copies      | #8 Dragon, #10 Psychic    |
| **Shadow Raikou**    | 4     | 1-3 copies      | #3 Electric               |
| **Shadow Zapdos**    | 4     | 1-3 copies      | #5 Electric, #9 Flying    |
| **Shadow Darkrai**   | 3     | 1-2 copies      | Mythical shadow           |
| **Shadow Dialga**    | 2     | 0-1 copies      | #6 Steel (May 2025)       |
| **Shadow Palkia**    | 2     | 0-1 copies      | #5 Dragon (early 2025)    |

---

## Summary by Count Tier

### Tier S: Keep 6 (19 species)

- Rayquaza (Mega), Groudon (Primal), Kyogre (Primal), Garchomp (Mega)
- Shadow Mewtwo, Shadow Salamence, Shadow Metagross, Shadow Moltres, Shadow Regigigas
- Tyranitar (Mega), Heracross (Mega), Blaziken (Mega), Lucario (Mega)
- Kyurem White, Kyurem Black, Zacian, Zamazenta, Dawn Wings Necrozma, Dusk Mane Necrozma

### Tier A: Keep 5 (18 species)

- Mewtwo, Palkia Origin, Dialga Origin, Reshiram, Yveltal, Hoopa Unbound, Terrakion
- Shadow Groudon, Shadow Kyogre, Shadow Tyranitar, Shadow Heatran, Shadow Latios, Shadow Chandelure
- Gengar (Mega), Metagross (Mega), Swampert (Mega)
- Regieleki, Kartana

### Tier B: Keep 4 (22 species)

- Zekrom, Kyurem, Lunala, Blacephalon, Landorus Therian, Regigigas, Palkia, Dialga, Xurkitree
- Shadow Dragonite, Shadow Garchomp, Shadow Rampardos, Shadow Rhyperior, Shadow Blaziken
- Shadow Gengar, Shadow Raikou, Shadow Zapdos, Shadow Excadrill, Shadow Weavile
- Sceptile (Mega), Salamence (Mega), Alakazam (Mega)

### Tier C: Keep 3 (11 species)

- Xerneas, Heatran, Pheromosa
- Shadow Honchkrow, Shadow Mamoswine, Shadow Electivire, Shadow Magnezone
- Shadow Swampert, Shadow Darmanitan, Shadow Darkrai
- Gardevoir (Mega)

### Tier D: Keep 2 (13 species)

- Rampardos, Volcarona, Hydreigon
- Shadow Gardevoir, Shadow Staraptor, Shadow Alakazam, Shadow Machamp
- Shadow Conkeldurr, Shadow Toxicroak, Shadow Tangrowth
- Shadow Palkia, Shadow Dialga
- Beedrill (Mega)

### Tier E: Keep 1 (7 species)

- Eternatus, Keldeo, Diancie (Mega) — account-limited
- Deoxys Attack — glass cannon mythical
- Charizard (Mega), Pinsir (Mega), Scizor (Mega) — accessible Megas

### Not Tracked (keep 0-1 as needed)

Accessible alternatives not worth dedicated storage. Replace from wild catches as needed:

- Togekiss, Primarina, Granbull, Shadow Granbull, Glaceon
- Mamoswine, Weavile, Electivire, Dragonite, Espeon
- Chandelure, Roserade, Shadow Venusaur, Staraptor, Shadow Scizor

---

## Usage Notes

1. **Prioritize shadows**: Shadow Pokemon get +20% attack bonus, making them superior even with lower IVs
2. **Keep high IV shadows**: NEVER transfer Shadow Mewtwo, Shadow Salamence, or other rare shadows
3. **Mega evolution**: Merged entries include both Mega and non-Mega copies. You can only have 1 Mega active, but keep extras for non-Mega raid use
4. **Transfer priority**: When reducing storage, transfer from lowest tier first (Not Tracked → E → D → C)
5. **Update frequency**: Revisit this list after major game updates or new Pokemon releases
6. **Total recommended**: ~358 copies across 90 tracked species (down from ~530 across 110 entries)

---

_Last Updated: 2026-02-16 | Methodology: ER-based tiers with explicit modifiers (GitHub Issue #1 recalibration)_
