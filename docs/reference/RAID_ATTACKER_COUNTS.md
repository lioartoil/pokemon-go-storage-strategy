# Raid Attacker Retention Counts - Exact Recommendations

**Last Updated**: 2026-02-21
**Data Sources**: PokeBase DPS Calculator (2026-02-21), PokemonGOHub DB (2026-02-21), PvPoke ML Rankings (2026-02-21), GamePress (2025-10-12 fallback)
**User Priority**: Collecting > Raids > Trading >>> PvP (minimal)

---

## How to Use This Guide

This document provides **exact recommended counts** for each top raid attacker, calculated using the ER-based tier methodology below. Every count is reproducible from the formula.

---

## Count Tier Methodology

### Maximum Count: 6

Pokemon GO raids use a **team of 6 Pokemon**. In practice, most trainers use mixed-species teams (3-4 species per team), group raids rarely require re-lobby, and storage is limited. One full team (6 copies) is the practical maximum for any single species.

### Step 1: Base Count from Estimator Rating (ER)

ER is a composite metric combining DPS (damage output) and TDO (survivability). Source: PokeBase DPS Calculator (primary), GamePress (fallback).

| ER Range  | Tier | Base Count | Description        |
| --------- | ---- | ---------- | ------------------ |
| ≥ 60      | S    | 6          | Elite dominant     |
| 55 – 59.9 | A    | 5          | Top-tier performer |
| 50 – 54.9 | B    | 4          | Strong reliable    |
| 45 – 49.9 | C    | 3          | Solid depth        |
| 40 – 44.9 | D    | 2          | Niche backup       |
| < 40      | E    | 1          | Budget replaceable |

### Step 2: Modifiers

| Modifier     | Effect | Condition                                                       |
| ------------ | ------ | --------------------------------------------------------------- |
| Dual-type    | +1     | Rank #1-5 in TWO or more types (PokemonGOHub top-5)             |
| Legendary/UB | +1     | Legendary, Mythical, or Ultra Beast (limited raid availability) |
| ML PvP       | +1     | PvPoke Master League rank ≤ 50 (dual-use value)                 |
| Accessible   | -1     | Common spawn or easily evolved (Machop, Eevee, Roselia, Weedle) |
| Glass cannon | -1     | TDO < 300                                                       |

### Step 3: Hard Caps & Overrides

| Rule            | Effect                                                |
| --------------- | ----------------------------------------------------- |
| Maximum         | 6 (one full raid team)                                |
| Minimum         | 1                                                     |
| Account-limited | = account limit (Eternatus: 2, Keldeo: 2, Diancie: 2) |
| Giovanni-only   | "keep all" + note practical range                     |

### Step 4: Mega/Primal Merge

- Mega/Primal forms merge with their base form (same physical Pokemon)
- Use the BEST ER between forms for tier calculation
- Entry format: `Species: count (Mega)` or `Species: count (Primal)`
- Shadow forms remain separate entries (different Pokemon)

---

## Quick Reference Table

| Pokemon                 | Count | ER    | PvP | Types Covered        | Tier Calc                        |
| ----------------------- | ----- | ----- | --- | -------------------- | -------------------------------- |
| **Rayquaza** (Mega)     | **6** | 73.98 |     | Dragon, Flying       | S(6)+dual+legend→cap6            |
| **Shadow Regigigas**    | **6** | 69.09 |     | Normal               | S(6)+legend, Giovanni            |
| **Zamazenta (Crowned)** | **6** | 63.84 | #5  | Steel                | S(6)+legend+pvp→cap6             |
| **Zacian (Crowned)**    | **6** | 63.64 | #1  | Steel, Fairy         | S(6)+legend+pvp→cap6             |
| **Dawn Wings Necrozma** | **6** | 63.07 | #18 | Ghost, Psychic       | S(6)+legend+pvp→cap6             |
| **Dusk Mane Necrozma**  | **6** | 63.07 | #21 | Steel, Psychic       | S(6)+legend+pvp→cap6             |
| **Kyurem (Black)**      | **6** | 60.56 | #11 | Ice, Dragon          | S(6)+legend+pvp→cap6             |
| **Regigigas**           | **6** | 59.64 |     | Normal               | A(5)+legend                      |
| **Garchomp** (Mega)     | **6** | 58.60 |     | Dragon, Ground       | A(5)+dual                        |
| **Blaziken** (Mega)     | **6** | 58.40 |     | Fire, Fighting       | A(5)+dual                        |
| **Shadow Mewtwo**       | **6** | 58.23 |     | Psychic              | A(5)+dual+legend, Giovanni       |
| **Kyogre** (Primal)     | **6** | 57.74 | #23 | Water                | A(5)+dual+legend+pvp→cap6        |
| **Groudon** (Primal)    | **6** | 57.56 | #20 | Ground               | A(5)+legend+pvp→cap6             |
| **Metagross** (Mega)    | **6** | 55.68 | #3  | Psychic, Steel       | A(5)+pvp                         |
| **Kyurem (White)**      | **6** | 54.19 | #6  | Ice, Dragon          | B(4)+legend+pvp                  |
| **Dialga (Origin)**     | **6** | 52.31 | #7  | Dragon, Steel        | B(4)+legend+pvp                  |
| **Shadow Dialga**       | **6** | 51.41 | #27 | Steel, Dragon        | B(4)+legend+pvp, Giovanni        |
| **Shadow Palkia**       | **6** | 50.92 | #14 | Dragon, Water        | B(4)+legend+pvp, Giovanni        |
| **Palkia (Origin)**     | **6** | 50.21 | #2  | Dragon, Water        | B(4)+legend+pvp                  |
| Lucario (Mega)          | 5     | 59.31 |     | Fighting, Steel      | A(5)                             |
| Shadow Metagross        | 5     | 53.29 | #12 | Psychic, Steel       | B(4)+pvp                         |
| Tyranitar (Mega)        | 5     | 52.57 |     | Rock, Dark           | B(4)+dual                        |
| Shadow Garchomp         | 5     | 52.00 |     | Dragon, Ground       | B(4)+dual                        |
| Blacephalon             | 5     | 51.15 |     | Fire, Ghost          | B(4)+legend                      |
| Regieleki               | 5     | 50.97 |     | Electric             | B(4)+legend                      |
| Mewtwo                  | 5     | 50.28 |     | Psychic              | B(4)+legend                      |
| Shadow Groudon          | 5     | 49.16 | #46 | Ground               | C(3)+legend+pvp, Giovanni        |
| Reshiram                | 5     | 47.46 | #8  | Fire, Dragon         | C(3)+legend+pvp                  |
| Yveltal                 | 5     | 46.10 | #17 | Dark, Flying         | C(3)+legend+pvp                  |
| Landorus (Therian)      | 5     | 45.69 | #43 | Ground, Flying       | C(3)+legend+pvp                  |
| Zekrom                  | 5     | 45.60 | #10 | Electric, Dragon     | C(3)+legend+pvp                  |
| Salamence (Mega)        | 4     | 57.43 |     | Dragon, Flying       | A(5)-access                      |
| Shadow Salamence        | 4     | 56.14 |     | Dragon, Flying       | A(5)-access                      |
| Gengar (Mega)           | 4     | 52.21 |     | Ghost, Poison        | B(4)+dual-access                 |
| Alakazam (Mega)         | 4     | 52.18 |     | Psychic              | B(4)+dual-access                 |
| Shadow Latios           | 4     | 49.89 | #24 | Dragon, Psychic      | C(3)+pvp                         |
| Heracross (Mega)        | 4     | 49.29 |     | Bug, Fighting        | C(3)+dual                        |
| Shadow Kyogre           | 4     | 49.23 |     | Water                | C(3)+legend, Giovanni            |
| Shadow Heatran          | 4     | 48.54 |     | Fire, Steel          | C(3)+legend, Giovanni            |
| Shadow Tyranitar        | 4     | 47.89 | #41 | Rock, Dark           | C(3)+pvp                         |
| Shadow Moltres          | 4     | 47.51 |     | Fire, Flying         | C(3)+legend, Giovanni            |
| Shadow Raikou           | 4     | 47.17 |     | Electric             | C(3)+legend, Giovanni            |
| Shadow Darkrai          | 4     | 46.06 |     | Dark                 | C(3)+legend, Giovanni            |
| Hoopa (Unbound)         | 4     | 46.00 |     | Dark, Ghost, Psychic | C(3)+legend                      |
| Terrakion               | 4     | 45.98 |     | Rock, Fighting       | C(3)+legend                      |
| Dialga                  | 4     | 44.83 | #32 | Steel, Dragon        | D(2)+legend+pvp                  |
| Palkia                  | 4     | 44.32 | #25 | Water, Dragon        | D(2)+legend+pvp                  |
| Lunala                  | 4     | 44.18 | #9  | Ghost, Psychic       | D(2)+legend+pvp                  |
| Kyurem (regular)        | 4     | 43.20 | #44 | Ice, Dragon          | D(2)+legend+pvp                  |
| Xerneas                 | 4     | 40.96 | #4  | Fairy                | D(2)+legend+pvp                  |
| Charizard (Mega)        | 3     | 54.03 |     | Fire, Flying         | B(4)-access                      |
| Sceptile (Mega)         | 3     | 53.14 |     | Grass                | B(4)-access                      |
| Gardevoir (Mega)        | 3     | 49.43 |     | Fairy, Psychic       | C(3)+dual-access                 |
| Shadow Blaziken         | 3     | 49.42 |     | Fire, Fighting       | C(3)                             |
| Shadow Dragonite        | 3     | 48.71 | #45 | Dragon, Flying       | C(3)+pvp-access                  |
| Shadow Rhyperior        | 3     | 47.30 |     | Rock, Ground         | C(3)                             |
| Shadow Chandelure       | 3     | 46.99 |     | Fire, Ghost          | C(3)                             |
| Shadow Darmanitan       | 3     | 45.33 |     | Fire, Ice            | C(3)                             |
| Xurkitree               | 3     | 43.88 |     | Electric             | D(2)+legend                      |
| Kartana                 | 3     | 43.52 |     | Grass, Steel         | D(2)+legend                      |
| Shadow Zapdos           | 3     | 43.25 |     | Electric, Flying     | D(2)+legend, Giovanni            |
| Heatran                 | 3     | 41.93 |     | Fire, Steel          | D(2)+legend                      |
| Swampert (Mega)         | 2     | 49.78 |     | Water, Ground        | C(3)-access                      |
| Shadow Staraptor        | 2     | 46.21 |     | Normal, Flying       | C(3)-access                      |
| Shadow Rampardos        | 2     | 44.97 |     | Rock                 | D(2)                             |
| Shadow Excadrill        | 2     | 44.79 |     | Ground, Steel        | D(2)                             |
| Shadow Mamoswine        | 2     | 44.50 |     | Ice, Ground          | D(2)                             |
| Shadow Electivire       | 2     | 44.14 |     | Electric             | D(2)                             |
| Beedrill (Mega)         | 2     | 42.71 |     | Bug                  | D(2)+dual-access                 |
| Shadow Weavile          | 2     | 42.60 |     | Ice, Dark            | D(2)                             |
| Shadow Magnezone        | 2     | 42.22 |     | Electric, Steel      | D(2)                             |
| Shadow Tangrowth        | 2     | 41.26 |     | Grass                | D(2)                             |
| Volcarona               | 2     | 41.08 |     | Bug, Fire            | D(2)                             |
| Hydreigon               | 2     | 40.85 |     | Dark, Dragon         | D(2)                             |
| Eternatus               | 2     | 67.53 | #15 | Dragon, Poison       | Account-limited (normal + shiny) |
| Keldeo (Resolute)       | 2     | 54.17 | #49 | Fighting, Water      | Account-limited (normal + shiny) |
| Diancie (Mega)          | 2     | 45.44 |     | Rock, Fairy          | Account-limited (normal + shiny) |
| Shadow Conkeldurr       | 1     | 44.91 |     | Fighting             | D(2)-access                      |
| Shadow Honchkrow        | 1     | 44.85 |     | Dark, Flying         | D(2)-access                      |
| Shadow Gengar           | 1     | 43.93 |     | Ghost, Poison        | D(2)-access                      |
| Shadow Alakazam         | 1     | 43.56 |     | Psychic              | D(2)-access                      |
| Shadow Swampert         | 1     | 42.19 |     | Water, Ground        | D(2)-access                      |
| Pinsir (Mega)           | 1     | 42.17 |     | Bug                  | D(2)-access                      |
| Shadow Machamp          | 1     | 42.03 |     | Fighting             | D(2)-access                      |
| Shadow Gardevoir        | 1     | 41.13 |     | Fairy, Psychic       | D(2)-access                      |
| Scizor (Mega)           | 1     | 40.00 |     | Bug, Steel           | D(2)-access                      |
| Rampardos               | 1     | 38.59 |     | Rock                 | E(1)                             |
| Pheromosa               | 1     | 38.55 |     | Bug, Fighting        | E(1)+legend-glass                |
| Shadow Toxicroak        | 1     | 36.64 |     | Poison, Fighting     | E(1)-access→cap1                 |
| Deoxys (Attack)         | 1     | 34.96 |     | Psychic              | E(1)+legend-glass                |

---

## Detailed Breakdowns by Type

### Bug Type

| Pokemon          | Count | Rank | ER    | Notes                     |
| ---------------- | ----- | ---- | ----- | ------------------------- |
| Heracross (Mega) | 4     | #1   | 49.29 | Also Fighting, dual-type  |
| Pheromosa        | 1     | #2   | 38.55 | Ultra Beast, glass cannon |
| Beedrill (Mega)  | 2     | #3   | 42.71 | Weedle is common spawn    |
| Pinsir (Mega)    | 1     | #4   | 42.17 | Accessible                |
| Volcarona        | 2     | #5   | 41.08 | Also Fire-type            |
| Scizor (Mega)    | 1     | #7   | 40.00 | Also Steel-type           |

**Bug Raid Frequency**: Low (rare raid type)

---

### Dark Type

| Pokemon          | Count | Rank | ER    | Notes                             |
| ---------------- | ----- | ---- | ----- | --------------------------------- |
| Shadow Honchkrow | 1     | #1   | 44.85 | Also Flying, accessible shadow    |
| Shadow Tyranitar | 4     | #3   | 47.89 | Also Rock, dual coverage, PvP #41 |
| Tyranitar (Mega) | 5     | #4   | 52.57 | Also Rock, dual coverage          |
| Shadow Weavile   | 2     | #5   | 42.60 | Also Ice                          |
| Hoopa (Unbound)  | 4     | #6   | 46.00 | Also Ghost/Psychic, mythical      |
| Shadow Darkrai   | 4     | —    | 46.06 | Mythical shadow, Giovanni         |
| Yveltal          | 5     | #9   | 46.10 | Legendary, PvP #17                |
| Hydreigon        | 2     | #10+ | 40.85 | Pseudo-legendary                  |

**Dark Raid Frequency**: Medium (Psychic/Ghost bosses common)

---

### Dragon Type

| Pokemon          | Count | Rank | ER    | Notes                            |
| ---------------- | ----- | ---- | ----- | -------------------------------- |
| Eternatus        | 2     | #1   | 67.53 | Account-limited (normal + shiny) |
| Rayquaza (Mega)  | 6     | #2   | 73.98 | Also #1 Flying, dominates        |
| Shadow Salamence | 4     | #3   | 56.14 | Also Flying, accessible          |
| Garchomp (Mega)  | 6     | #4   | 58.60 | Also Ground, dual coverage       |
| Shadow Dragonite | 3     | #5   | 48.71 | Also Flying, PvP #45             |
| Shadow Garchomp  | 5     | #6   | 52.00 | Also Ground, dual coverage       |
| Shadow Latios    | 4     | #8   | 49.89 | Also Psychic, PvP #24            |
| Palkia (Origin)  | 6     | #9   | 50.21 | Also Water, PvP #2               |
| Dialga (Origin)  | 6     | #10  | 52.31 | Also Steel, PvP #7               |
| Salamence (Mega) | 4     | #10+ | 57.43 | Accessible                       |
| Palkia           | 4     | #10+ | 44.32 | Regular forme, PvP #25           |
| Dialga           | 4     | #10+ | 44.83 | Regular forme, PvP #32           |

**Dragon Raid Frequency**: High (Dragon bosses very common)

---

### Electric Type

| Pokemon           | Count | Rank | ER    | Notes                      |
| ----------------- | ----- | ---- | ----- | -------------------------- |
| Shadow Electivire | 2     | #1   | 44.14 | Accessible evolution       |
| Regieleki         | 5     | #2   | 50.97 | Legendary                  |
| Shadow Raikou     | 4     | #3   | 47.17 | Shadow legendary, Giovanni |
| Xurkitree         | 3     | #4   | 43.88 | Ultra Beast                |
| Shadow Zapdos     | 3     | #5   | 43.25 | Also Flying, Giovanni      |
| Shadow Magnezone  | 2     | #7   | 42.22 | Also Steel                 |
| Zekrom            | 5     | #9   | 45.60 | Also Dragon, PvP #10       |

**Electric Raid Frequency**: Medium (Water/Flying bosses)

---

### Fairy Type

| Pokemon          | Count | Rank | ER    | Notes                    |
| ---------------- | ----- | ---- | ----- | ------------------------ |
| Gardevoir (Mega) | 3     | #1   | 49.43 | Also Psychic, accessible |
| Zacian (Crowned) | 6     | #2   | 63.64 | Also #1 Steel, PvP #1    |
| Shadow Gardevoir | 1     | #3   | 41.13 | Also Psychic, accessible |
| Xerneas          | 4     | #8   | 40.96 | Legendary, PvP #4        |

**Fairy Raid Frequency**: Medium (Dragon/Dark/Fighting bosses)

---

### Fighting Type

| Pokemon           | Count | Rank | ER    | Notes                      |
| ----------------- | ----- | ---- | ----- | -------------------------- |
| Lucario (Mega)    | 5     | #1   | 59.31 | Also Steel                 |
| Blaziken (Mega)   | 6     | #2   | 58.40 | Also Fire, dual Mega       |
| Keldeo (Resolute) | 2     | #3   | 54.17 | Account-limited, PvP #49   |
| Shadow Blaziken   | 3     | #4   | 49.42 | Also Fire                  |
| Heracross (Mega)  | 4     | #5   | 49.29 | Also #1 Bug, dual coverage |
| Pheromosa         | 1     | #6   | 38.55 | Ultra Beast, glass cannon  |
| Shadow Machamp    | 1     | #8   | 42.03 | Very accessible shadow     |
| Terrakion         | 4     | #9   | 45.98 | Also Rock, legendary       |
| Shadow Conkeldurr | 1     | #10+ | 44.91 | Accessible shadow          |

**Fighting Raid Frequency**: High (Normal/Dark/Steel/Ice/Rock bosses common)

---

### Fire Type

| Pokemon           | Count | Rank | ER    | Notes                    |
| ----------------- | ----- | ---- | ----- | ------------------------ |
| Blaziken (Mega)   | 6     | #1   | 58.40 | Also Fighting, dual Mega |
| Charizard (Mega)  | 3     | #2   | 54.03 | Accessible               |
| Shadow Chandelure | 3     | #3   | 46.99 | Also Ghost               |
| Shadow Darmanitan | 3     | #4   | 45.33 | Also Ice-type            |
| Shadow Blaziken   | 3     | #5   | 49.42 | Also Fighting            |
| Shadow Moltres    | 4     | #6   | 47.51 | Also Flying, Giovanni    |
| Shadow Heatran    | 4     | #7   | 48.54 | Also Steel, Giovanni     |
| Blacephalon       | 5     | #8   | 51.15 | Ultra Beast, also Ghost  |
| Reshiram          | 5     | #9   | 47.46 | Also Dragon, PvP #8      |
| Heatran           | 3     | #10+ | 41.93 | Also Steel, legendary    |

**Fire Raid Frequency**: Medium-High (Grass/Bug/Steel/Ice bosses)

---

### Flying Type

| Pokemon          | Count | Rank | ER    | Notes                   |
| ---------------- | ----- | ---- | ----- | ----------------------- |
| Rayquaza (Mega)  | 6     | #1   | 73.98 | Also Dragon, dominates  |
| Shadow Salamence | 4     | #3   | 56.14 | Also Dragon, accessible |
| Shadow Honchkrow | 1     | #4   | 44.85 | Also Dark, accessible   |
| Shadow Moltres   | 4     | #5   | 47.51 | Also Fire, Giovanni     |
| Shadow Staraptor | 2     | #6   | 46.21 | Also Normal, accessible |
| Shadow Dragonite | 3     | #7   | 48.71 | Also Dragon, PvP #45    |
| Shadow Zapdos    | 3     | #9   | 43.25 | Also Electric, Giovanni |

**Flying Raid Frequency**: Medium (Fighting/Bug/Grass bosses)

---

### Ghost Type

| Pokemon             | Count | Rank | ER    | Notes                   |
| ------------------- | ----- | ---- | ----- | ----------------------- |
| Dawn Wings Necrozma | 6     | #1   | 63.07 | Legendary, PvP #18      |
| Gengar (Mega)       | 4     | #2   | 52.21 | Also Poison, accessible |
| Shadow Chandelure   | 3     | #3   | 46.99 | Also Fire               |
| Shadow Gengar       | 1     | #4   | 43.93 | Also Poison, accessible |
| Blacephalon         | 5     | #5   | 51.15 | Ultra Beast, also Fire  |
| Hoopa (Unbound)     | 4     | #6   | 46.00 | Also Dark, mythical     |
| Lunala              | 4     | #7   | 44.18 | Also Psychic, PvP #9    |

**Ghost Raid Frequency**: Medium (Psychic bosses)

---

### Grass Type

| Pokemon          | Count | Rank | ER    | Notes                   |
| ---------------- | ----- | ---- | ----- | ----------------------- |
| Sceptile (Mega)  | 3     | #1   | 53.14 | Accessible              |
| Kartana          | 3     | #2   | 43.52 | Also Steel, Ultra Beast |
| Shadow Tangrowth | 2     | #8   | 41.26 | Accessible shadow       |

**Grass Raid Frequency**: Medium-High (Water/Ground/Rock bosses)

---

### Ground Type

| Pokemon            | Count | Rank | ER    | Notes                      |
| ------------------ | ----- | ---- | ----- | -------------------------- |
| Groudon (Primal)   | 6     | #1   | 57.56 | Primal evolution, PvP #20  |
| Garchomp (Mega)    | 6     | #2   | 58.60 | Also Dragon, dual coverage |
| Shadow Groudon     | 5     | #3   | 49.16 | Shadow legendary, PvP #46  |
| Shadow Garchomp    | 5     | #4   | 52.00 | Also Dragon, dual coverage |
| Shadow Excadrill   | 2     | #5   | 44.79 | Also Steel                 |
| Shadow Mamoswine   | 2     | #6   | 44.50 | Also Ice                   |
| Swampert (Mega)    | 2     | #7   | 49.78 | Also Water, accessible     |
| Shadow Rhyperior   | 3     | #8   | 47.30 | Also Rock                  |
| Shadow Swampert    | 1     | #9   | 42.19 | Also Water, accessible     |
| Landorus (Therian) | 5     | #10  | 45.69 | Legendary, PvP #43         |

**Ground Raid Frequency**: High (Electric/Fire/Poison/Rock/Steel bosses)

---

### Ice Type

| Pokemon          | Count | Rank | ER    | Notes                  |
| ---------------- | ----- | ---- | ----- | ---------------------- |
| Kyurem (White)   | 6     | #1   | 54.19 | Legendary, PvP #6      |
| Kyurem (Black)   | 6     | #2   | 60.56 | Legendary, PvP #11     |
| Shadow Mamoswine | 2     | #3   | 44.50 | Also Ground            |
| Shadow Weavile   | 2     | #4   | 42.60 | Also Dark              |
| Kyurem (regular) | 4     | #5+  | 43.20 | Regular forme, PvP #44 |

**Ice Raid Frequency**: High (Dragon/Flying/Grass/Ground bosses common)

---

### Normal Type

| Pokemon          | Count | Rank | ER    | Notes                      |
| ---------------- | ----- | ---- | ----- | -------------------------- |
| Shadow Regigigas | 6     | #1   | 69.09 | Shadow legendary, Giovanni |
| Shadow Staraptor | 2     | #2   | 46.21 | Also Flying, accessible    |
| Regigigas        | 6     | #7   | 59.64 | Legendary                  |

**Normal Raid Frequency**: Very Low (almost never needed)

---

### Poison Type

| Pokemon          | Count | Rank | ER    | Notes                           |
| ---------------- | ----- | ---- | ----- | ------------------------------- |
| Eternatus        | 2     | #1   | 67.53 | Also #1 Dragon (normal + shiny) |
| Gengar (Mega)    | 4     | #2   | 52.21 | Also Ghost, accessible          |
| Shadow Gengar    | 1     | #3   | 43.93 | Also Ghost, accessible          |
| Shadow Toxicroak | 1     | #5   | 36.64 | Also Fighting, accessible       |

**Poison Raid Frequency**: Low (Fairy bosses uncommon)

---

### Psychic Type

| Pokemon          | Count | Rank | ER    | Notes                    |
| ---------------- | ----- | ---- | ----- | ------------------------ |
| Shadow Mewtwo    | 6     | #1   | 58.23 | Dominates type, Giovanni |
| Alakazam (Mega)  | 4     | #2   | 52.18 | Accessible               |
| Deoxys (Attack)  | 1     | #3   | 34.96 | Glass cannon             |
| Shadow Metagross | 5     | #4   | 53.29 | Also Steel, PvP #12      |
| Shadow Alakazam  | 1     | #5   | 43.56 | Accessible shadow        |
| Mewtwo           | 5     | #6   | 50.28 | Legendary                |
| Shadow Latios    | 4     | #10  | 49.89 | Also Dragon, PvP #24     |

**Psychic Raid Frequency**: Medium-High (Fighting/Poison bosses)

---

### Rock Type

| Pokemon          | Count | Rank | ER    | Notes                     |
| ---------------- | ----- | ---- | ----- | ------------------------- |
| Diancie (Mega)   | 2     | #1   | 45.44 | Mythical (normal + shiny) |
| Shadow Rampardos | 2     | #2   | 44.97 | Glass cannon, high DPS    |
| Shadow Tyranitar | 4     | #3   | 47.89 | Also Dark, PvP #41        |
| Tyranitar (Mega) | 5     | #4   | 52.57 | Also Dark, dual coverage  |
| Shadow Rhyperior | 3     | #5   | 47.30 | Also Ground               |
| Terrakion        | 4     | #6   | 45.98 | Also Fighting, legendary  |
| Rampardos        | 1     | #7   | 38.59 | Glass cannon, non-shadow  |

**Rock Raid Frequency**: High (Fire/Flying/Bug/Ice bosses)

---

### Steel Type

| Pokemon             | Count | Rank | ER    | Notes                     |
| ------------------- | ----- | ---- | ----- | ------------------------- |
| Zacian (Crowned)    | 6     | #1   | 63.64 | Also Fairy, PvP #1        |
| Zamazenta (Crowned) | 6     | #2   | 63.84 | Highest Steel TDO, PvP #5 |
| Dusk Mane Necrozma  | 6     | #3   | 63.07 | Legendary, PvP #21        |
| Lucario (Mega)      | 5     | #4   | 59.31 | Also Fighting             |
| Shadow Metagross    | 5     | #5   | 53.29 | Also Psychic, PvP #12     |
| Shadow Dialga       | 6     | #6   | 51.41 | Giovanni, PvP #27         |
| Shadow Excadrill    | 2     | #7   | 44.79 | Also Ground               |
| Metagross (Mega)    | 6     | #8   | 55.68 | PvP #3                    |
| Kartana             | 3     | #9   | 43.52 | Also Grass, Ultra Beast   |
| Dialga (Origin)     | 6     | #10  | 52.31 | Also Dragon, PvP #7       |
| Shadow Heatran      | 4     | #10+ | 48.54 | Also Fire, Giovanni       |
| Shadow Magnezone    | 2     | #10+ | 42.22 | Also Electric             |

**Steel Raid Frequency**: Medium (Fairy/Ice/Rock bosses)

---

### Water Type

| Pokemon         | Count | Rank | ER    | Notes                      |
| --------------- | ----- | ---- | ----- | -------------------------- |
| Kyogre (Primal) | 6     | #1   | 57.74 | Primal evolution, PvP #23  |
| Shadow Kyogre   | 4     | #2   | 49.23 | Shadow legendary, Giovanni |
| Palkia (Origin) | 6     | #3   | 50.21 | Also Dragon, PvP #2        |
| Swampert (Mega) | 2     | #4   | 49.78 | Also Ground, accessible    |
| Shadow Swampert | 1     | #6   | 42.19 | Also Ground, accessible    |
| Palkia          | 4     | #10  | 44.32 | Regular forme, PvP #25     |

**Water Raid Frequency**: Medium-High (Fire/Ground/Rock bosses)

---

## Special Cases & Exceptions

### Account-Limited Pokemon (Keep ALL)

| Pokemon               | Max Copies | Count | Notes                       |
| --------------------- | ---------- | ----- | --------------------------- |
| **Eternatus**         | 2          | 2     | #1 Dragon, #1 Poison        |
| **Keldeo (Resolute)** | 2          | 2     | #3 Fighting (best non-Mega) |
| **Diancie** (Mega)    | 2          | 2     | #1 Rock (Mega), Mythical    |

### Giovanni-Only (Keep ALL You Have)

| Pokemon              | Count | Practical Range | Notes                     |
| -------------------- | ----- | --------------- | ------------------------- |
| **Shadow Mewtwo**    | 6     | 3-5 copies      | #1 Psychic, irreplaceable |
| **Shadow Regigigas** | 6     | 2-4 copies      | #1 Normal                 |
| **Shadow Palkia**    | 6     | 1-3 copies      | Dragon/Water, PvP #14     |
| **Shadow Dialga**    | 6     | 1-3 copies      | Steel/Dragon, PvP #27     |
| **Shadow Groudon**   | 5     | 1-3 copies      | #3 Ground, PvP #46        |
| **Shadow Kyogre**    | 4     | 1-3 copies      | #2 Water                  |
| **Shadow Moltres**   | 4     | 1-3 copies      | Fire, Flying              |
| **Shadow Heatran**   | 4     | 1-3 copies      | Fire, Steel               |
| **Shadow Latios**    | 4     | 1-3 copies      | Dragon, PvP #24           |
| **Shadow Raikou**    | 4     | 1-3 copies      | #3 Electric               |
| **Shadow Darkrai**   | 4     | 1-2 copies      | Mythical shadow           |
| **Shadow Zapdos**    | 3     | 1-2 copies      | Electric, Flying          |

---

## Summary by Count Tier

### Tier S: Keep 6 (19 species)

- Rayquaza (Mega), Shadow Regigigas, Zamazenta, Zacian, Dawn Wings Necrozma, Dusk Mane Necrozma
- Kyurem Black, Regigigas, Garchomp (Mega), Blaziken (Mega), Shadow Mewtwo
- Kyogre (Primal), Groudon (Primal), Metagross (Mega), Kyurem White
- Dialga Origin, Shadow Dialga, Shadow Palkia, Palkia Origin

### Tier A: Keep 5 (12 species)

- Lucario (Mega), Shadow Metagross, Tyranitar (Mega), Shadow Garchomp
- Blacephalon, Regieleki, Mewtwo
- Shadow Groudon, Reshiram, Yveltal, Landorus Therian, Zekrom

### Tier B: Keep 4 (19 species)

- Salamence (Mega), Shadow Salamence, Gengar (Mega), Alakazam (Mega)
- Shadow Latios, Heracross (Mega), Shadow Kyogre, Shadow Heatran
- Shadow Tyranitar, Shadow Moltres, Shadow Raikou, Shadow Darkrai
- Hoopa Unbound, Terrakion, Dialga, Palkia, Lunala, Kyurem, Xerneas

### Tier C: Keep 3 (12 species)

- Charizard (Mega), Sceptile (Mega), Gardevoir (Mega)
- Shadow Blaziken, Shadow Dragonite, Shadow Rhyperior, Shadow Chandelure, Shadow Darmanitan
- Xurkitree, Kartana, Shadow Zapdos, Heatran

### Tier D: Keep 2 (15 species)

- Swampert (Mega), Shadow Staraptor
- Shadow Rampardos, Shadow Excadrill, Shadow Mamoswine, Shadow Electivire
- Beedrill (Mega), Shadow Weavile, Shadow Magnezone, Shadow Tangrowth
- Volcarona, Hydreigon
- Eternatus, Keldeo, Diancie (Mega) — account-limited (normal + shiny)

### Tier E: Keep 1 (13 species)

- Shadow Conkeldurr, Shadow Honchkrow, Shadow Gengar, Shadow Alakazam
- Shadow Swampert, Pinsir (Mega), Shadow Machamp, Shadow Gardevoir, Scizor (Mega)
- Rampardos, Pheromosa, Shadow Toxicroak, Deoxys Attack

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
6. **Total recommended**: ~329 copies across 90 tracked species

---

_Last Updated: 2026-02-21 | Methodology: ER-based tiers with 5 modifiers (PokeBase + PokemonGOHub + PvPoke cross-reference)_
