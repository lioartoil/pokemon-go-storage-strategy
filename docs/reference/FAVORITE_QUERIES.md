<!-- cSpell: ignore Xfer -->

# Pokemon GO - Favorite Search Queries (Quick Reference)

**Date**: 2025-10-12
**Tag System**: PascalCase (43 tags)
**Name Limit**: ≤12 characters (Pokemon GO favorite limit)

---

## Daily Workflow (5 queries)

| #   | Name           | Query                                                                                              | Purpose                         |
| --- | -------------- | -------------------------------------------------------------------------------------------------- | ------------------------------- |
| 1   | `New Catches`  | `!#`                                                                                               | Untagged Pokemon needing review |
| 2   | `Review`       | `#Review`                                                                                          | Duplicates/ranks to recheck     |
| 3   | `Review-Spec`  | `#Review&!legendary&!mythical&!ultra beasts`                                                       | Non-legendary review queue      |
| 4   | `Review-Leg`   | `#Review&legendary,mythical,ultra beasts`                                                          | Legendary review queue          |
| 5   | `Untagged-Spc` | `!#&legendary,mythical,ultra beasts,xxs,xxl,costume,shiny,shadow,4*,dynamax,gigantamax,background` | Special Pokemon without tags    |

---

## Resources (4 queries)

| #   | Name       | Query           | Purpose                  |
| --- | ---------- | --------------- | ------------------------ |
| 6   | `Buddy`    | `#CurrentBuddy` | Currently active buddy   |
| 7   | `PowerUp`  | `#PowerUp`      | Needs power-up           |
| 8   | `TM`       | `#TM`           | Needs move changes       |
| 9   | `Training` | `#InTraining`   | Active power-up projects |

---

## Transfer & Trade (8 queries)

| #   | Name          | Query                                                                                                                        | Purpose                              |
| --- | ------------- | ---------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ |
| 10  | `Xfer-Now`    | `#Transfer&!#Home`                                                                                                           | Immediate transfer                   |
| 11  | `Xfer-Event`  | `#Home`                                                                                                                      | Event transfer (2× candy)            |
| 12  | `Xfer-All`    | `#Transfer,#Home`                                                                                                            | All transfer candidates              |
| 13  | `Trade`       | `#Trade`                                                                                                                     | General trading queue                |
| 14  | `Lucky Trade` | `#LuckyTrade`                                                                                                                | Lucky friend trades                  |
| 15  | `Lucky-New`   | `age364-&!#Trade&!#Kept&!#Home&!traded&!legendary&!mythical&!ultra beasts&!shiny&!costume&!shadow&!xxs&!xxl&!background&!4*` | Auto-find lucky candidates (1+ year) |
| 16  | `HOME`        | `#Home&mythical`                                                                                                             | Mythicals for Pokemon HOME           |
| 17  | `HOME-New`    | `#Transfer&!#Home&mythical&151,251,385,386,491,492,494,647,648,649,718,719,720,802,893`                                      | Mythicals needing HOME tag           |

---

## Collections (3 queries)

| #   | Name         | Query                                                                                                    | Purpose                             |
| --- | ------------ | -------------------------------------------------------------------------------------------------------- | ----------------------------------- |
| 18  | `Specials`   | `shiny,legendary,mythical,ultra beasts,costume,shadow,xxs,xxl,background,4*,@special,dynamax,gigantamax` | All special Pokemon                 |
| 19  | `Spec-Trade` | `shiny,legendary,ultra beasts&!traded&!#Kept`                                                            | Special trade candidates (shiny/legendary/UB) |
| 20  | `Kept`       | `#Kept`                                                                                                  | Permanent collection                |

---

## Mega Evolution (3 queries)

| #   | Name       | Query                           | Purpose                    |
| --- | ---------- | ------------------------------- | -------------------------- |
| 21  | `Mega-1st` | `megaevolve&#Rank1&mega0&#Mega` | Best IVs, not mega evolved |
| 22  | `Mega-Lvl` | `megaevolve&#Rank1&mega1&#Mega` | Best IVs, mega level 1     |
| 23  | `Mega`     | `megaevolve&#Mega`              | All mega candidates        |

---

## PvP Ranks (6 queries)

| #   | Name          | Query                          | Purpose                   |
| --- | ------------- | ------------------------------ | ------------------------- |
| 24  | `GL-Top`      | `#Great&#Rank1,#Rank2,#Rank3`  | Great League top 3        |
| 25  | `UL-Top`      | `#Ultra&#Rank1,#Rank2,#Rank3`  | Ultra League top 3        |
| 26  | `LL-Top`      | `#Little&#Rank1,#Rank2,#Rank3` | Little League top 3       |
| 27  | `Global-Best` | `#First,#Second,#Third`        | Trophy Pokemon (#1-3 IVs) |
| 28  | `Raid`        | `#Attackers`                   | Raid attackers            |
| 29  | `Defense`     | `#Def1,#Def2,#Def2.5`          | Gym defenders             |

---

## Evolution (4 queries)

| #   | Name           | Query             | Purpose                  |
| --- | -------------- | ----------------- | ------------------------ |
| 30  | `Evo-Special`  | `#SpecialEvolve`  | Special evolution method |
| 31  | `Evo-Item`     | `#ItemEvolve`     | Needs evolution item     |
| 32  | `Evo-Location` | `#LocationEvolve` | Needs location           |
| 33  | `Evo-Time`     | `#TimeEvolve`     | Needs time/weather       |

---

## Buddy System (5 queries)

| #   | Name          | Query                   | Purpose                 |
| --- | ------------- | ----------------------- | ----------------------- |
| 34  | `Buddy-1km`   | `#Buddy1Km&#NeedCandy`  | 1km buddy candy claims  |
| 35  | `Buddy-3km`   | `#Buddy3Km&#NeedCandy`  | 3km buddy candy claims  |
| 36  | `Buddy-5km`   | `#Buddy5Km&#NeedCandy`  | 5km buddy candy claims  |
| 37  | `Buddy-20km`  | `#Buddy20Km&#NeedCandy` | 20km buddy candy claims |
| 38  | `Claim Candy` | `#NeedCandy`            | All candy claimable     |

---

## Form Variants (2 queries)

| #   | Name   | Query   | Purpose        |
| --- | ------ | ------- | -------------- |
| 39  | `Var1` | `#Var1` | Form variant 1 |
| 40  | `Var2` | `#Var2` | Form variant 2 |

---

## Top 10 Recommended (for limited favorite slots)

| Priority | Name           | Query                                                                                              | Why                 |
| -------- | -------------- | -------------------------------------------------------------------------------------------------- | ------------------- |
| 1        | `New Catches`  | `!#`                                                                                               | Daily workflow      |
| 2        | `Review`       | `#Review`                                                                                          | Weekly cleanup      |
| 3        | `Xfer-All`     | `#Transfer,#Home`                                                                                  | Transfer pipeline   |
| 4        | `PowerUp`      | `#PowerUp`                                                                                         | Resource management |
| 5        | `Buddy`        | `#CurrentBuddy`                                                                                    | Quick buddy access  |
| 6        | `Lucky Trade`  | `#LuckyTrade`                                                                                      | Lucky friends       |
| 7        | `Trade`        | `#Trade`                                                                                           | General trading     |
| 8        | `Global-Best`  | `#First,#Second,#Third`                                                                            | Trophy Pokemon      |
| 9        | `GL-Top`       | `#Great&#Rank1,#Rank2,#Rank3`                                                                      | Best GL Pokemon     |
| 10       | `Untagged-Spc` | `!#&legendary,mythical,ultra beasts,xxs,xxl,costume,shiny,shadow,4*,dynamax,gigantamax,background` | Special Pokemon QA  |

---

## Quick Copy-Paste (All 40 Queries)

```
1. New Catches: !#
2. Review: #Review
3. Review-Spec: #Review&!legendary&!mythical&!ultra beasts
4. Review-Leg: #Review&legendary,mythical,ultra beasts
5. Untagged-Spc: !#&legendary,mythical,ultra beasts,xxs,xxl,costume,shiny,shadow,4*,dynamax,gigantamax,background
6. Buddy: #CurrentBuddy
7. PowerUp: #PowerUp
8. TM: #TM
9. Training: #InTraining
10. Xfer-Now: #Transfer&!#Home
11. Xfer-Event: #Home
12. Xfer-All: #Transfer,#Home
13. Trade: #Trade
14. Lucky Trade: #LuckyTrade
15. Lucky-New: age364-&!#Trade&!#Kept&!#Home&!traded&!legendary&!mythical&!ultra beasts&!shiny&!costume&!shadow&!xxs&!xxl&!background&!4*
16. HOME: #Home&mythical
17. HOME-New: #Transfer&!#Home&mythical&151,251,385,386,491,492,494,647,648,649,718,719,720,802,893
18. Specials: shiny,legendary,mythical,ultra beasts,costume,shadow,xxs,xxl,background,4*,@special,dynamax,gigantamax
19. Spec-Trade: shiny,legendary,ultra beasts&!traded&!#Kept
20. Kept: #Kept
21. Mega-1st: megaevolve&#Rank1&mega0&#Mega
22. Mega-Lvl: megaevolve&#Rank1&mega1&#Mega
23. Mega: megaevolve&#Mega
24. GL-Top: #Great&#Rank1,#Rank2,#Rank3
25. UL-Top: #Ultra&#Rank1,#Rank2,#Rank3
26. LL-Top: #Little&#Rank1,#Rank2,#Rank3
27. Global-Best: #First,#Second,#Third
28. Raid: #Attackers
29. Defense: #Def1,#Def2,#Def2.5
30. Evo-Special: #SpecialEvolve
31. Evo-Item: #ItemEvolve
32. Evo-Location: #LocationEvolve
33. Evo-Time: #TimeEvolve
34. Buddy-1km: #Buddy1Km&#NeedCandy
35. Buddy-3km: #Buddy3Km&#NeedCandy
36. Buddy-5km: #Buddy5Km&#NeedCandy
37. Buddy-20km: #Buddy20Km&#NeedCandy
38. Claim Candy: #NeedCandy
39. Var1: #Var1
40. Var2: #Var2
```

---

## Name Changes (Old → New)

**Character limit fixes** (>12 chars):

| Old Name               | New Name       | Length      |
| ---------------------- | -------------- | ----------- |
| `Special Review`       | `Review-Spec`  | 11 chars ✅ |
| `Legendary Review`     | `Review-Leg`   | 10 chars ✅ |
| `Active Buddy`         | `Buddy`        | 5 chars ✅  |
| `Power-Up Queue`       | `PowerUp`      | 7 chars ✅  |
| `TM Queue`             | `TM`           | 2 chars ✅  |
| `Training Projects`    | `Training`     | 8 chars ✅  |
| `Transfer Now`         | `Xfer-Now`     | 8 chars ✅  |
| `Event Transfer`       | `Xfer-Event`   | 10 chars ✅ |
| `All Transfers`        | `Xfer-All`     | 8 chars ✅  |
| `Trade Queue`          | `Trade`        | 5 chars ✅  |
| `Lucky Trades`         | `Lucky Trade`  | 11 chars ✅ |
| `New Lucky Candidates` | `Lucky-New`    | 9 chars ✅  |
| `HOME Queue`           | `HOME`         | 4 chars ✅  |
| `New HOME Candidates`  | `HOME-New`     | 8 chars ✅  |
| `All Specials`         | `Specials`     | 8 chars ✅  |
| `Untagged Specials`    | `Untagged-Spc` | 12 chars ✅ |
| `Kept Pokemon`         | `Kept`         | 4 chars ✅  |
| `Mega First Evolve`    | `Mega-1st`     | 8 chars ✅  |
| `Mega Level Up`        | `Mega-Lvl`     | 8 chars ✅  |
| `Mega Candidates`      | `Mega`         | 4 chars ✅  |
| `GL Top Ranks`         | `GL-Top`       | 6 chars ✅  |
| `UL Top Ranks`         | `UL-Top`       | 6 chars ✅  |
| `LL Top Ranks`         | `LL-Top`       | 6 chars ✅  |
| `Global Best`          | `Global-Best`  | 11 chars ✅ |
| `Raid Teams`           | `Raid`         | 4 chars ✅  |
| `Gym Defense`          | `Defense`      | 7 chars ✅  |
| `Special Evolve`       | `Evo-Special`  | 11 chars ✅ |
| `Item Evolve`          | `Evo-Item`     | 8 chars ✅  |
| `Location Evolve`      | `Evo-Location` | 12 chars ✅ |
| `Time Evolve`          | `Evo-Time`     | 8 chars ✅  |
| `Buddy 1km`            | `Buddy-1km`    | 9 chars ✅  |
| `Buddy 3km`            | `Buddy-3km`    | 9 chars ✅  |
| `Buddy 5km`            | `Buddy-5km`    | 9 chars ✅  |
| `Buddy 20km`           | `Buddy-20km`   | 10 chars ✅ |
| `Variant 1`            | `Var1`         | 4 chars ✅  |
| `Variant 2`            | `Var2`         | 4 chars ✅  |

**Tag updates**:

| Old Tag         | New Tag         | Change                |
| --------------- | --------------- | --------------------- |
| `#currentbuddy` | `#CurrentBuddy` | PascalCase            |
| `#power up`     | `#PowerUp`      | PascalCase            |
| `#waiting`      | `#Review`       | Renamed               |
| `#to trade`     | `#Trade`        | Simplified            |
| `#kept`         | `#Kept`         | PascalCase            |
| `#home`         | `#Home`         | PascalCase            |
| `#luckies`      | N/A             | Deleted (use `lucky`) |
| `rank1`         | `#Rank1`        | Added `#`             |
| `mega`          | `#Mega`         | Added `#`             |
| `#buddy1km`     | `#Buddy1Km`     | PascalCase            |
| `#buddy3km`     | `#Buddy3Km`     | PascalCase            |
| `#buddy5km`     | `#Buddy5Km`     | PascalCase            |
| `#buddy20km`    | `#Buddy20Km`    | PascalCase            |
| `#var1`         | `#Var1`         | PascalCase            |
| `#var2`         | `#Var2`         | PascalCase            |

---

_Favorite Queries - Condensed Quick Reference - Updated 2025-10-12_
