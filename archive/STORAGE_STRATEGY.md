# Pokemon GO Storage Strategy

**Current Utilization**: 10,184 / 10,500 (316 free slots, ~3% free)
**Last Updated**: 2025-10-11

---

## Overview

This document outlines the strategy for managing Pokemon storage in Pokemon GO. The goal is to maintain competitive Pokemon for various leagues while preserving special Pokemon for collecting and trading purposes.

## Core Principles

1. **Species Separation**: Mega, Shadow, Shiny, Costumed, and Background variants are treated as separate species
2. **IV Ranking**: Pokemon are evaluated based on their PvP IV rankings (optimal stat distributions for specific CP caps)
3. **Multi-Category Eligibility**: Pokemon may qualify for multiple categories (e.g., a shiny shadow with top IV ranks)
4. **League-Specific Optimization**: Different retention rules apply based on competitive league requirements

---

## Category Breakdown

### Category 1: Great & Ultra League Competitive Pokemon

**Total**: 1,370 Pokemon

**Criteria**:

- Great League: CP ≤ 1,500
- Ultra League: CP ≤ 2,500
- IV Rank ≤ 205 for each species

**Retention Rules**:

- Rank ≤ 10: Keep best **3** Pokemon per species
- Rank 11-205: Keep best **1** Pokemon per species
- Mega and Shadow forms counted as separate species

**Purpose**: Maintain competitive roster for Great and Ultra League PvP

---

### Category 2: Little League Competitive Pokemon

**Total**: 498 Pokemon

**Criteria**:

- Little League: CP ≤ 500
- Species must be in top 60th percentile (see `go/little-percentile-60.csv`)
- IV Rank thresholds vary by species percentile

**Retention Rules**:

- **All species**: If rank ≤ 19, keep according to rank rules below
- **60th+ percentile species**: If rank 20-205, keep according to rank rules below
- **<60th percentile species**: If rank 20-205, discard
- Rank ≤ 10: Keep best **3** Pokemon per species
- Rank 11-205 (60th+ percentile only): Keep best **1** Pokemon per species
- Mega and Shadow forms counted as separate species

**Purpose**: Specialized roster for Little League cups with focus on viable species

**Reference**: See `go/little-percentile-60.csv` for species viability rankings

---

### Category 3: Master League Competitive Pokemon

**Total**: 2,037 Pokemon

**Criteria**:

- Master League: Any CP (unlimited)
- IV Rank ≤ 19 for each species

**Retention Rules**:

**For Final Evolution & Mega Pokemon**:

- Rank ≤ 10: Keep best **3** Pokemon per species
- Rank 11-19: Keep **0** Pokemon if rank ≤ 10 already exists, otherwise keep **1**

**For Non-Final Evolution Pokemon**:

- Keep best **2** Pokemon per species

**Shadow Forms**: Counted as separate species

**Purpose**: High-IV Pokemon for Master League and raid battles

---

### Category 4: Shiny Pokemon

**Total**: 1,058 Pokemon

**Criteria**:

- Any Shiny Pokemon

**Retention Rules**:

- Keep best **2** IV-ranked Pokemon per species and form
- Shadow forms counted as separate species

**Purpose**: Collecting rare variants and trading value

---

### Category 5: Costumed Pokemon

**Total**: 324 Pokemon

**Criteria**:

- Any Pokemon with special costume/outfit

**Retention Rules**:

- Keep best **2** IV-ranked Pokemon per species, form, and costume combination
- Shadow forms counted as separate species

**Purpose**: Limited-time event collectibles

---

### Category 6: Shadow Pokemon

**Total**: 394 Pokemon

**Criteria**:

- Any Shadow Pokemon (including those not meeting competitive thresholds)

**Retention Rules**:

- Keep best **2** IV-ranked Pokemon per species

**Purpose**: Future purification, special moves, or potential PvP use

**Note**: Shadow Pokemon qualifying for competitive leagues (Categories 1-3) should also be counted here

---

### Category 7: Size Extremes (XXS & XXL)

**Total**: 1,058 Pokemon

**Criteria**:

- Smallest (XXS) or Largest (XXL) Pokemon owned for each species

**Retention Rules**:

- Keep **1** smallest (XXS) per species
- Keep **1** largest (XXL) per species

**Purpose**: Size collecting and potential future gameplay features

---

### Category 8: Background Pokemon

**Total**: 150 Pokemon

**Criteria**:

- Pokemon with special catch backgrounds (e.g., location-based, event-based)

**Retention Rules**:

- Keep best **2** IV-ranked Pokemon per species and background type

**Purpose**: Rare location/event markers

---

### Category 9: Gigantamax Pokemon

**Total**: 17 Pokemon

**Criteria**:

- Pokemon with Gigantamax capability

**Retention Rules**:

- Keep best **2** Pokemon per species

**Purpose**: Special battle mechanic availability

---

### Category 10: Dynamax Pokemon

**Total**: 45 Pokemon

**Criteria**:

- Pokemon with Dynamax capability

**Retention Rules**:

- Keep best **2** Pokemon per species

**Purpose**: Special battle mechanic availability

---

### Category 11: Legendary & Ultra Beast Reserve

**Total**: 643 Pokemon

**Criteria**:

- Legendary or Ultra Beast Pokemon
- Does NOT meet criteria for Categories 1-10

**Retention Rules**:

- Keep top **10** Pokemon per species, sorted by:
  1. Level (highest first)
  2. IV total (highest first)
- Shiny, Costumed, Background, Gigantamax, and Dynamax forms counted as separate species

**Purpose**: High-quality legendary Pokemon for potential future use or trading

---

### Category 12: Legendary/Mythical Transfer Queue

**Total**: 76 Pokemon

**Criteria**:

- Legendary Pokemon from Category 11 that didn't make top 10
- All Mythical Pokemon (generally cannot be traded)

**Retention Rules**:

- Keep ALL until 2× Candy transfer events

**Purpose**: Maximize candy gain during transfer bonus events

---

### Category 13: General Population Reserve

**Total**: 2,441 Pokemon

**Criteria**:

- Any Pokemon not meeting Categories 1-12

**Retention Rules**:

- Keep top **2** Pokemon per species, sorted by:
  1. Level (highest first)
  2. IV total (highest first)
- Shiny, Costumed, Background, Gigantamax, and Dynamax forms counted as separate species

**Purpose**: General backup and evolution fodder

---

### Category 14: Lucky Trade Candidates

**Total**: Unknown (not specified)

**Criteria**:

- Pokemon from Category 13 that didn't make top 2
- Age ≥ 364 days (will be kept until age ≥ 1,095 days / 3 years)

**Retention Rules**:

- Keep ALL until age reaches 3+ years
- Trade with friends for increased Lucky Pokemon chance

**Purpose**: Maximize Lucky Trade probability with aged Pokemon

---

## Storage Summary

| Category  | Description        | Count       | % of Total |
| --------- | ------------------ | ----------- | ---------- |
| 1         | Great/Ultra League | 1,370       | 13.5%      |
| 2         | Little League      | 498         | 4.9%       |
| 3         | Master League      | 2,037       | 20.0%      |
| 4         | Shiny              | 1,058       | 10.4%      |
| 5         | Costumed           | 324         | 3.2%       |
| 6         | Shadow             | 394         | 3.9%       |
| 7         | XXS/XXL            | 1,058       | 10.4%      |
| 8         | Background         | 150         | 1.5%       |
| 9         | Gigantamax         | 17          | 0.2%       |
| 10        | Dynamax            | 45          | 0.4%       |
| 11        | Legendary Reserve  | 643         | 6.3%       |
| 12        | Transfer Queue     | 76          | 0.7%       |
| 13        | General Reserve    | 2,441       | 24.0%      |
| 14        | Lucky Trade Queue  | TBD         | TBD        |
| **Total** |                    | **10,184+** | **~97%**   |

**Free Space**: 316 slots (~3%)

---

## Maintenance Procedures

### Daily Tasks

- Review and transfer Category 14 Pokemon that have aged 3+ years
- Transfer duplicate catches that don't meet any category criteria

### Weekly Tasks

- Audit Category 1-3 for duplicates when new Pokemon are caught
- Review Category 12 for upcoming 2× transfer candy events

### Event-Based Tasks

- During 2× Transfer Candy: Clear Category 12
- During Lucky Trade Events: Prioritize Category 14 trades
- After Community Day: Re-evaluate species viability in Category 2 (Little League)

### Monthly Tasks

- Verify IV rankings haven't shifted due to game balance changes
- Review and prune Category 13 for Pokemon that have aged enough for Category 14

---

## Open Questions / Considerations

1. **Overlap Handling**: How are Pokemon that qualify for multiple categories counted? (e.g., Shiny Shadow with rank #5 for Great League)

2. **Category 14 Count**: Current number of Lucky Trade candidates not specified

3. **Storage Pressure**: With only ~3% free space, consider whether categories need tightening

4. **PvP Activity Level**: Strategy assumes active PvP participation across all leagues

5. **Trading Frequency**: Category 14 assumes regular trading with friends for Lucky trades

---

## Notes

- IV Rankings are based on PvP stat distributions (not traditional IV percentage)
- Rankings assume level 50 capability where applicable
- Great League and Ultra League favor bulk (high DEF/HP, lower ATK)
- Master League favors high total stats (15/15/15 or near-perfect)
- Strategy prioritizes PvP competitive viability over raid/gym performance

---

## Related Files

- `pokedex.md` - Master Pokedex tracking
- `go/little-percentile-60.csv` - Little League species viability data
- `leagues/` - League-specific tracking by generation
