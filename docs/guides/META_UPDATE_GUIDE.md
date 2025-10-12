# Pokemon GO Meta Update Guide

**Last Updated**: 2025-10-12
**Meta Database Location**: `meta/` directory

---

## 📊 Current Meta Data

### Meta Database Files

- **`meta/great-league-meta.json`** - Great League (CP ≤1500) top 30 rankings
- **`meta/ultra-league-meta.json`** - Ultra League (CP ≤2500) top 30 rankings
- **`meta/little-league-meta.json`** - Little League (CP ≤500) top 30 rankings

Each file contains:

- League info and CP cap
- Last updated date
- Top 20 and Top 30 Pokemon with scores
- Source URL for manual verification
- Notes about the league

---

## 🔄 Update Schedule

### When to Update Meta Data

| Frequency                | Trigger                   | Action                              |
| ------------------------ | ------------------------- | ----------------------------------- |
| **Monthly**              | First week of month       | Check for changes, update if needed |
| **After Move Rebalance** | Niantic announces changes | Update immediately                  |
| **New Season**           | Every ~3 months           | Always update                       |
| **New Cup Rotation**     | Little League cups change | Update Little League only           |
| **New Pokemon Release**  | Major legendary/mythical  | Check impact, update if in top 30   |

### Update Priority

1. **Critical** (Update immediately):

   - Official move rebalance announced
   - New season starts
   - You notice current stored Pokemon underperforming

2. **High** (Update within 1 week):

   - Monthly scheduled check
   - New legendary released
   - Little League cup changes

3. **Medium** (Update within 1 month):
   - Community feedback about meta shift
   - Tournament results show new trends

---

## 🤖 Automated Update Process

### Step 1: Fetch Latest Data from PvPoke

Use Claude Code to run the update script:

```bash
# Request Claude to run these WebFetch commands:
# 1. https://pvpoke.com/data/rankings/all/overall/rankings-1500.json
# 2. https://pvpoke.com/data/rankings/all/overall/rankings-2500.json
# 3. https://pvpoke.com/data/rankings/little/overall/rankings-500.json
```

### Step 2: Update JSON Files

Claude will:

1. Parse the JSON data
2. Extract top 30 Pokemon
3. Update `meta/*-meta.json` files
4. Update `last_updated` field

### Step 3: Compare Changes

Claude will generate a changelog showing:

- Pokemon that entered top 20
- Pokemon that dropped out of top 20
- Significant rank changes (±5 positions)

### Step 4: Update Strategy Files

If top 20 changed, Claude will update:

- `STRATEGY_MODERATE_PVP.md` - Top 20 meta lists
- `STRATEGY_REVISIONS_FINAL.md` - Top 20 meta lists
- `STORAGE_STRATEGY_CORRECTED.md` - If needed

---

## 📋 Manual Update Process

### Quick Check (5 minutes)

**Goal**: Verify if update is needed

1. **Visit PvPoke Rankings**:

   - Great League: https://pvpoke.com/rankings/all/1500/overall/
   - Ultra League: https://pvpoke.com/rankings/all/2500/overall/
   - Little League: https://pvpoke.com/rankings/little/500/overall/

2. **Compare Top 10**:

   - Look at top 10 Pokemon on PvPoke
   - Compare to your `meta/*-meta.json` files
   - If 3+ Pokemon are different → update needed

3. **Decision**:

   - **No significant changes**: Skip update
   - **3+ changes in top 20**: Request Claude to update

### Detailed Update (15-30 minutes)

**Goal**: Full meta refresh

1. **Request Claude to update**:

   ```
   Please update the meta data from PvPoke for all three leagues
   (Great, Ultra, Little). Generate a changelog showing what changed.
   ```

2. **Review changelog**:

   - Check which Pokemon entered/left top 20
   - Assess impact on your stored Pokemon

3. **Update retention decisions**:

   - If you have Pokemon that dropped out of meta: Consider transferring
   - If new Pokemon entered meta: Start catching/trading for them

---

## 🎯 Meta-Relevant Species Definition

**"Meta-relevant species"** = Pokemon in **top 20** of current meta rankings

### Why Top 20?

- **Top 10**: Core meta (always keep rank ≤50)
- **Top 11-20**: Common meta (keep rank ≤50 for PvP players)
- **Top 21-50**: Fringe meta (rank ≤10 sufficient)
- **Below 50**: Off-meta (only keep rank ≤10 for favorites)

### How to Use in Retention Decisions

**Example from STRATEGY_MODERATE_PVP.md**:

| Rank Range  | Top 20 Meta Species | Other Species |
| ----------- | ------------------- | ------------- |
| Rank ≤10    | Keep 2              | Keep 2        |
| Rank 11-50  | Keep 1              | Keep 1        |
| Rank 51-100 | Keep 1              | Transfer      |
| Rank 101+   | Transfer            | Transfer      |

**Key**: Rank 51-100 gets special treatment ONLY if species is in top 20 meta

---

## 📊 Current Meta Summary (2025-10-12)

### Great League Top 20

**Current meta-relevant species** (keep rank ≤100):

1. Dragonair (Shadow)
2. Corviknight
3. Altaria
4. Dusknoir (Shadow)
5. Clodsire
6. Dusknoir
7. Empoleon
8. Azumarill
9. Marowak (Shadow)
10. Corsola (Galarian)
11. Cradily
12. Gastrodon
13. Zweilous (Shadow)
14. Malamar
15. Primeape
16. Regidrago
17. Drapion (Shadow)
18. Jellicent
19. Golisopod
20. Hakamo-o

**Comparison to Previous List** (from strategy files):

- ❌ **Dropped out**: Medicham, Skarmory, Talonflame, Lickitung, Shadow Nidoqueen, Shadow Walrein, Shadow Swampert, Trevenant, Sableye, Registeel, Cresselia, Bastiodon, Vigoroth, Diggersby, Shadow Gligar, Charjabug, Lanturn
- ✅ **New entries**: Dragonair (Shadow), Corviknight, Clodsire, Empoleon, Marowak (Shadow), Corsola (Galarian), Cradily, Gastrodon, Zweilous (Shadow), Malamar, Primeape, Regidrago, Drapion (Shadow), Golisopod, Hakamo-o

**⚠️ MAJOR META SHIFT DETECTED** - Only 3 Pokemon remain from previous list (Altaria, Azumarill, Jellicent)

### Ultra League Top 20

**Current meta-relevant species** (keep rank ≤100):

1. Bellibolt
2. Lapras
3. Corviknight
4. Lapras (Shadow)
5. Empoleon
6. Florges
7. Empoleon (Shadow)
8. Moltres (Galarian)
9. Jellicent
10. Forretress
11. Gastrodon
12. Virizion
13. Feraligatr
14. Feraligatr (Shadow)
15. Zygarde (Complete Forme)
16. Kyurem
17. Malamar (Shadow)
18. Cresselia
19. Crustle
20. Dusknoir

**Comparison to Previous List**:

- ❌ **Dropped out**: Registeel, Talonflame, Trevenant, Shadow Nidoqueen, Shadow Swampert, Giratina (Altered), Shadow Machamp, Cobalion, Shadow Walrein, Tapu Fini, Swampert, Umbreon, Scrafty, Pidgeot, Mandibuzz, Steelix, Greedent
- ✅ **New entries**: Bellibolt, Lapras, Corviknight, Empoleon, Florges, Moltres (Galarian), Forretress, Gastrodon, Virizion, Feraligatr, Zygarde, Kyurem, Malamar (Shadow), Crustle, Dusknoir

**⚠️ MAJOR META SHIFT DETECTED** - Only 2 Pokemon remain from previous list (Cresselia, Jellicent)

### Little League Top 20

**Current meta-relevant species** (keep rank ≤50):

1. Ducklett
2. Bronzor
3. Wynaut
4. Eevee
5. Seel
6. Zigzagoon (Galarian)
7. Vullaby
8. Gligar
9. Lickitung
10. Deino
11. Wooper (Shadow)
12. Wooper
13. Barboach (Shadow)
14. Stunky (Shadow)
15. Vulpix (Alolan)
16. Cubone (Shadow)
17. Pawniard
18. Wooper (Paldean)
19. Ledyba (Shadow)
20. Wailmer

**Note**: Little League meta is cup-specific. This is the "Open Little League" meta. Actual cup meta varies significantly.

---

## 🚨 What Changed Since Original Strategy?

### Impact on Your Storage

**Original Strategy (Early 2025)** assumed these were top meta:

- GL: Medicham, Skarmory, Talonflame, Lickitung, Bastiodon, Registeel
- UL: Registeel, Talonflame, Trevenant, Giratina (Altered), Cobalion

**Current Meta (2025-10-12)** shows MAJOR shift:

- GL: Dragonair (Shadow), Corviknight, Clodsire, Empoleon, Regidrago
- UL: Bellibolt, Lapras, Corviknight, Florges, Virizion

### Action Items

1. **Review your tagged Pokemon**:

   - Check if your `great`/`ultra` tagged Pokemon are still in top 30
   - Consider transferring Pokemon no longer in top 50

2. **Update catch priorities**:

   - Focus on catching/trading for current top 20 species
   - Especially: Corviknight, Clodsire, Bellibolt, Lapras

3. **Adjust retention rules**:

   - Old meta Pokemon (Medicham, Skarmory, etc.): Reduce to rank ≤10 only
   - New meta Pokemon (Corviknight, Clodsire, etc.): Keep rank ≤50-100

---

## 🛠️ Resources

### Primary Resources

1. **PvPoke Rankings** (Most Reliable)

   - Great League: https://pvpoke.com/rankings/all/1500/overall/
   - Ultra League: https://pvpoke.com/rankings/all/2500/overall/
   - Little League: https://pvpoke.com/rankings/little/500/overall/
   - **API Endpoints**:
     - GL: https://pvpoke.com/data/rankings/all/overall/rankings-1500.json
     - UL: https://pvpoke.com/data/rankings/all/overall/rankings-2500.json
     - LL: https://pvpoke.com/data/rankings/little/overall/rankings-500.json

2. **Pokemon GO Hub**

   - URL: https://pokemongohub.net/
   - Best for: Move rebalance announcements, meta analysis

### Note on Inaccessible Resources

- ❌ **GO Stadium** (https://www.gostadium.gg/) - Cannot access
- ❌ **Silph Arena** (https://silph.gg/) - Cannot access

**Workaround**: Use PvPoke as primary source. It aggregates data from multiple sources including tournament play.

---

## 📝 Update Log Template

When updating, document changes:

```markdown
## Meta Update - YYYY-MM-DD

### Great League

- **Entered Top 20**: [Pokemon list]
- **Dropped from Top 20**: [Pokemon list]
- **Significant rank changes**: [Pokemon with ±5 rank change]

### Ultra League

- **Entered Top 20**: [Pokemon list]
- **Dropped from Top 20**: [Pokemon list]
- **Significant rank changes**: [Pokemon with ±5 rank change]

### Little League

- **Entered Top 20**: [Pokemon list]
- **Dropped from Top 20**: [Pokemon list]
- **Cup format**: [Current cup name]

### Action Items

- [ ] Update strategy files
- [ ] Review stored Pokemon
- [ ] Update catch priorities
```

---

## 🤖 Claude Code Update Command

**To request meta update**:

```
Please update the Pokemon GO meta data:
1. Fetch latest rankings from PvPoke for all three leagues
2. Update meta/*.json files
3. Generate changelog comparing to previous version
4. Update top 20 lists in strategy files if changed
5. Recommend any storage adjustments based on meta shift
```

**Claude will**:

1. Fetch JSON from PvPoke API
2. Parse and update meta files
3. Compare with previous version
4. Show what changed
5. Update strategy documents
6. Recommend actions

---

## 📅 Next Update

**Recommended**: 2025-11-12 (monthly check)

**Or sooner if**:

- Move rebalance announced
- New season starts
- Major tournament meta shift
- You notice performance issues

---

_Meta update system created 2025-10-12. Database files in `meta/` directory._
