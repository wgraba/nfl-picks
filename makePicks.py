#!/usr/bin/env python3

import argparse
from argparse import ArgumentError
import requests
from tabulate import tabulate
import datetime


def find_stats(team: str, stats: list):
    for stat in stats:
        if stat["Team"] == team:
            return stat


def calc_score(home_team_stats: dict, away_team_stats: dict):
    home_team = home_team_stats["Team"]
    home_score = home_team_stats["Score"]
    home_score_against = home_team_stats["OpponentScore"]
    home_diff = home_score - home_score_against

    away_team = away_team_stats["Team"]
    away_score = away_team_stats["Score"]
    away_score_against = away_team_stats["OpponentScore"]
    away_diff = away_score - away_score_against

    if away_diff > home_diff:
        winner = away_team
        score = away_diff - home_diff

    else:
        winner = home_team
        score = home_diff - away_diff

    return winner, score


def data_sort(d):
    return d["Score"]


parser = argparse.ArgumentParser(
    description="Make statistic-based picks for confidence pools"
)
parser.add_argument("year", type=int, help="Season year")
parser.add_argument("week", type=int, help="Season week number")

cli_args = parser.parse_args()

if cli_args.week < 1 or cli_args.week > 17:
    raise ValueError(f"Invalid week - got {cli_args.week}; expected range [1, 17]")

if cli_args.year > datetime.datetime.today().year:
    raise ValueError(f"Expected the current year or less; got {cli_args.year}")

with open("sportsdataio.key", "r") as key_file:
    api_key = key_file.readline()

schedule_rsp = requests.get(
    f"https://api.sportsdata.io/v3/nfl/scores/json/ScoresByWeek/{cli_args.year}/{cli_args.week}",
    params={"key": api_key},
)
schedule_rsp.raise_for_status()
schedule = schedule_rsp.json()

team_stats_rsp = requests.get(
    f"https://api.sportsdata.io/v3/nfl/scores/json/TeamSeasonStats/{cli_args.year}",
    params={"key": api_key},
)
team_stats_rsp.raise_for_status
team_stats = team_stats_rsp.json()

data = []
for game in schedule:
    home_team = game["HomeTeam"]
    away_team = game["AwayTeam"]
    home_stats = find_stats(home_team, team_stats)
    away_stats = find_stats(away_team, team_stats)
    assert home_stats
    assert away_stats

    winner, score = calc_score(home_stats, away_stats)

    data += [
        {
            "Home Team": home_team,
            "Away Team": away_team,
            "Winner": winner,
            "Score": score,
        }
    ]

sorted_data = data.sort(key=data_sort)
print(tabulate(data, headers="keys"))
