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
age364-&!age1095-&!shiny&!costume&!shadow&!@special&!legendary&!mythical&!ultrabeast
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
- `!ultrabeast` = Exclude Category 11/12 (Ultra Beasts)

**Note**: This will still include some Pokemon from Categories 1-3, 7-10, 13. You'll need to manually verify:
- Categories 1-3: Check if they're top-ranked for any league (use PokeGenie/IV4U)
- Category 7: Check if they're your XXS/XXL record holders
- Category 8: Check if they have special backgrounds
- Category 9-10: Check if they're Gigantamax/Dynamax capable
- Category 13: Check if they're top 2 by level+IV for their species

### Simplified Approach (Tag-Based)

**Recommended**: Use in-game tags for easier filtering

1. **Tag your keepers** as you organize:
   - `keep1` = Categories 1-3 (PvP)
   - `keep2` = Categories 4-10 (Special variants)
   - `keep3` = Categories 11-13 (Reserves)

2. **Search for Category 14**:
```
age364-&!age1095-&!keep1&!keep2&!keep3
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
legendary,mythical,ultrabeast
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
legendary | mythical | ultrabeast
```

---

## Advanced Filtering

### Duplicates to Transfer (After Organizing)
```
age0-7&!keep1&!keep2&!keep3&!shiny&!shadow&!costume&!legendary&!mythical
```

### Community Day Cleanup
```
shiny&age0-1&<species_name>
```
Example: `shiny&age0-1&charmander`

### Purification Candidates (Non-Meta Shadows)
```
shadow&!keep1&!keep2&!keep3
```
Then manually verify which are non-meta

---

## Tag System Recommendations

### Organize by Category
- `keep1` = Categories 1-3 (PvP)
- `keep2` = Categories 4-10 (Special variants - shiny, costume, size, etc.)
- `keep3` = Categories 11-13 (Reserves - legendary, general)
- `home` = Category 12 (Transfer queue for 2× candy events) - **YOUR CURRENT TAG**
- `trade` = Category 14 (Lucky trade candidates 3+ years old)

### Organize by Action
- `evolve` = Ready to evolve
- `power` = Need to power up
- `tm` = Need to TM moves
- `lucky` = Lucky Pokemon (reduced power-up cost)

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
4. Check if legendary: `legendary | mythical | ultrabeast`
5. If none of above, check PvP ranks in PokeGenie

### "What can I transfer now?"
```
age0-7&!shiny&!shadow&!costume&!legendary&!mythical&!@special&!xxs&!xxl
```
Then manually verify they're not:
- Top 2 for their species (Category 13)
- Ranked for PvP (Categories 1-3)

---

*Search queries optimized for Pokemon GO (2025-10-11)*
