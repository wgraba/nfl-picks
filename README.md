# Purpose
Create picks for NFL confidence pool with minimum effort.

[sportsdata.io](https://sportsdata.io) is used to get stats. Calculations are
done using stats to determine winning team and confidence in terms of points.

# Requirements
* Python 3.6+
* Packages in `requirements.txt`

# Usage
* Install dependent packages - `pip install -r requirements.txt`
* See `python makepicks.py --help` for usage info.

Will respond with -
```
Home Team    Away Team    Winner      Score
-----------  -----------  --------  -------
IND          SEA          IND             1
NO           GB           NO              5
TEN          ARI          TEN             9
BUF          PIT          BUF            22
NYG          DEN          NYG            46
WAS          LAC          WAS            48
ATL          PHI          ATL            66
CIN          MIN          MIN            68
LAR          CHI          LAR            74
NE           MIA          MIA            93
HOU          JAX          HOU           106
KC           CLE          KC            122
DET          SF           SF            128
CAR          NYJ          CAR           162
LV           BAL          BAL           209
TB           DAL          TB            215
```

A higher `Score` means a greater confidence.

# Calculations
The `Score` is determined by the though that teams that score more
than their opponents tend to win games more often 🤔.

This is very simplistic -
* An entire season of stats (partial if currents season) is used
* Determine difference between home team points and points against
* Determine difference between away team points and points against
* Whichever potins differential is greater is the winning team
  * The `Score` is calculated by the different of winning team's points 
    differential and the losing team's points differential

# TODO
- [ ] Move to `rich` python package instead of `tabulate`
