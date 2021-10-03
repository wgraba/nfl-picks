# Purpose
Create picks for NFL confidence pool with minimum effort.

[sportsdata.io](https://sportsdata.io) is used to get stats. Calculations are
done using stats to determine winning team and confidence in terms of points.

Only ["unscrambled"](https://sportsdata.io/developers/faq#scrambled-data) 
(available in the API free trial) simple stats are used. More thoughtful 
predictions using additional stats require a subscription.

# Requirements
* Python 3.6+
* Packages in `requirements.txt`

# Usage
* Install dependent packages - `pip install -r requirements.txt`
* See `python makepicks.py --help` for usage info.

Will respond with -
```
                 2021 Week 4 Picks                 
┏━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━┳━━━━━━━━┓
┃ Home Team ┃ Away Team ┃ Score ┃ Winner ┃ Points ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━╇━━━━━━━━┩
│ GB        │ PIT       │ 1     │ GB     │ 1      │
│ DAL       │ CAR       │ 2     │ CAR    │ 2      │
│ LAR       │ ARI       │ 5     │ ARI    │ 3      │
│ CHI       │ DET       │ 11    │ CHI    │ 4      │
│ LAC       │ LV        │ 11    │ LV     │ 5      │
│ NE        │ TB        │ 12    │ TB     │ 6      │
│ SF        │ SEA       │ 16    │ SF     │ 7      │
│ PHI       │ KC        │ 21    │ KC     │ 8      │
│ ATL       │ WAS       │ 29    │ WAS    │ 9      │
│ MIN       │ CLE       │ 31    │ CLE    │ 10     │
│ NYJ       │ TEN       │ 31    │ TEN    │ 11     │
│ MIA       │ IND       │ 33    │ IND    │ 12     │
│ NO        │ NYG       │ 37    │ NO     │ 13     │
│ DEN       │ BAL       │ 53    │ DEN    │ 14     │
│ CIN       │ JAX       │ 58    │ CIN    │ 15     │
│ BUF       │ HOU       │ 139   │ BUF    │ 16     │
└───────────┴───────────┴───────┴────────┴────────┘
```

A higher `Score` means a greater confidence.

# Calculations
The `Score` is determined by the thought that teams that score more
than their opponents tend to win games more often 🤔.

This is very simplistic -
* An entire season of stats (partial if currents season) is used
* Determine difference between home team points and points against
* Determine difference between away team points and points against
* Whichever potins differential is greater is the winning team
  * The `Score` is calculated by the difference of winning team's points 
    differential and the losing team's points differential

# TODO
- [x] Move to `rich` python package instead of `tabulate`
- [ ] Consider verbose logging of stats and calculations
