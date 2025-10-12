# Pokemon GO - Useful Search Queries

**Last Updated**: 2025-10-11

---

## Category 14: Lucky Trade Candidates (1-3 years old)

### Basic Search (Age only)

```
age364-&!age1095-
```

### Complete Search (Exclude Categories 1-13)

**In-Game Search**:

```
age364-&!age1095-&!shiny&!costume&!shadow&!@special&!legendary&!mythical&!ultra beasts&!xxs&!xxl&!background&!gigantamax&!dynamax
```

**Explanation**:

- `age364-` = 364+ days old (1+ years)
- `!age1095-` = NOT 1,095+ days old (exclude 3+ years)
- `!shiny` = Exclude Category 4 (Shiny)
- `!costume` = Exclude Category 5 (Costumed)
- `!shadow` = Exclude Category 6 (Shadow)
- `!@special` = Exclude Pokemon with special moves (bonus slots)
- `!legendary` = Exclude Category 11 (Legendary Reserve)
- `!mythical` = Exclude Category 12 (Mythical transfer queue)
- `!ultra beasts` = Exclude Category 11/12 (Ultra Beasts) - **CORRECTED**
- `!xxs` = Exclude Category 7 (XXS Pokemon)
- `!xxl` = Exclude Category 7 (XXL Pokemon)
- `!background` = Exclude Category 8 (Special backgrounds)
- `!gigantamax` = Exclude Category 9 (Gigantamax)
- `!dynamax` = Exclude Category 10 (Dynamax)

**Note**: This now excludes Categories 4-10! You only need to manually verify:

- Categories 1-3: Check if they're top-ranked for any league (use PokeGenie/IV4U or your tags: `great`, `ultra`, `little`)
- Category 13: Check if they're top 2 by level+IV for their species

### Simplified Approach (Tag-Based)

**Recommended**: Use your existing tags for easier filtering

**Your Current Tags**:

- `great` = Category 1 GL (Great League)
- `ultra` = Category 1 UL (Ultra League)
- `little` = Category 2 (Little League)
- `transfer` = Categories 11, 13, 14 (Pokemon ready to transfer/trade)

**Search for Category 14** (Lucky Trade Candidates):

```
age364-&!age1095-&!great&!ultra&!little&!shiny&!costume&!shadow&!legendary&!mythical&!ultra beasts&!xxs&!xxl&!background&!gigantamax&!dynamax
```

Or if you add a `keep` tag for Category 13 top 2:

```
age364-&!age1095-&!great&!ultra&!little&!keep&!shiny&!costume&!shadow&!legendary&!mythical&!ultra beasts&!xxs&!xxl&!background&!gigantamax&!dynamax
```

---

## Other Useful Searches

### Category 12: Transfer Queue (Tagged as "home")

```
home
```

**Your Setup**: You tag Pokemon waiting for 2× transfer events as `home`

### Special Move Pokemon

```
@special
```

**Use**: Identify Pokemon with legacy/Community Day/Elite TM moves

### Size Extremes (XXS/XXL)

```
xxs,xxl
```

### PvP IV Check (Great League example)

```
cp-1500&0*,1*,2*
```

Then use PokeGenie to check exact ranks

### Legendary + Mythical + Ultra Beasts

```
legendary,mythical,ultra beasts
```

### High IV (Traditional)

```
4*
```

**Note**: This is NOT the same as PvP IV rank

### Recent Catches (Last 7 days)

```
age0-7
```

### Ready for Lucky Trade (3+ years)

```
age1095-
```

---

## Category-Specific Searches

### Category 1-3: PvP Candidates

```
cp-1500 | cp501-2500 | cp2501-
```

Then check ranks in PokeGenie/IV4U

### Category 4: Shiny

```
shiny
```

### Category 5: Costumed

```
costume
```

### Category 6: Shadow

```
shadow
```

### Category 7: Size Tracking

```
xxs | xxl
```

### Category 11-12: Legendary/Mythical/Ultra Beast

```
legendary | mythical | ultra beasts
```

---

## Advanced Filtering

### Duplicates to Transfer (After Organizing)

```
age0-7&!great&!ultra&!little&!master&!keep&!shiny&!shadow&!costume&!legendary&!mythical&!ultra beasts&!xxs&!xxl&!background&!gigantamax&!dynamax&!@special
```

**Note**: Uses your actual tags (`great`, `ultra`, `little`) + recommended tags (`master`, `keep`) + built-in queries for special variants

### Community Day Cleanup

```
shiny&age0-1&<species_name>
```

Example: `shiny&age0-1&charmander`

### Purification Candidates (Non-Meta Shadows)

```
shadow&!great&!ultra&!little&!master&!keep&!legendary
```

Then manually verify which are non-meta for raids/PvP

---

## Tag System Recommendations

### Your Current Tags (Confirmed)

- `great` = Category 1 GL (Great League PvP)
- `ultra` = Category 1 UL (Ultra League PvP)
- `little` = Category 2 (Little League PvP)
- `home` = Category 12 (Transfer queue for 2× candy events)
- `transfer` = Categories 11, 13, 14 (Pokemon ready to transfer/trade)

### Recommended Additional Tags

- `master` = Category 3 (Master League PvP) - to match your GL/UL/LL tagging pattern
- `keep` = Category 13 (Top 2 per species for living dex)
- `raid` = Category 11 (Raid attackers) - to separate from legendary collectors
- `power` = Need to power up
- `tm` = Need to TM moves

**Note**:

- `lucky` and `evolve` are **reserved query strings** in Pokemon GO - don't use as tags
- Categories 4-10 (shiny, costume, shadow, xxs, xxl, background, gigantamax, dynamax) don't need tags since they have built-in search queries

---

## PokeGenie Integration

### Export to PokeGenie

1. Use PokeGenie's auto-scan feature (you already have this enabled)
2. PokeGenie will automatically detect:
   - PvP IV ranks for all leagues
   - Special moves (@special)
   - IV percentages

### Check Ranks in Bulk

1. Scan Pokemon with PokeGenie
2. Filter by league in PokeGenie app:
   - Great League: Rank ≤10, ≤25, ≤50, etc.
   - Ultra League: Rank ≤10, ≤25, ≤50, etc.
   - Little League: Rank ≤10, ≤25, ≤50, etc.

### Check Master League Ranks

1. Use IV4U website: https://iv4u.lima-city.de/en
2. Input Pokemon stats
3. Check Master League rank (15/15/15 = rank #1)

---

## Quick Decision Searches

### "Should I keep this catch?"

1. Check if shiny/costume/shadow: `shiny | costume | shadow`
2. Check if special move: `@special`
3. Check if size extreme: `xxs | xxl`
4. Check if special background: `background`
5. Check if Gigantamax/Dynamax: `gigantamax | dynamax`
6. Check if legendary: `legendary | mythical | ultra beasts`
7. If none of above, check PvP ranks in PokeGenie

### "What can I transfer now?"

```
age0-7&!great&!ultra&!little&!master&!keep&!shiny&!shadow&!costume&!legendary&!mythical&!ultra beasts&!@special&!xxs&!xxl&!background&!gigantamax&!dynamax
```

This query excludes all categories! Only catches from the last 7 days that don't qualify for ANY category will show up.

---

_Search queries optimized for Pokemon GO (2025-10-11)_
