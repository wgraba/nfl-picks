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

# TODO
- [ ] Move to `rich` python package instead of `tabulate`
