from datetime import datetime


def solve_17(file: str) -> str:

    streak_by_team: dict[str, datetime] = {}
    longest_streak: tuple[str, datetime, datetime] = ("", datetime.min, datetime.min)

    _, *scores = file.splitlines()

    for line in scores:
        date, team1, team2, score1, score2, _, _, _, _ = line.split(",")
        y, m, d = map(int, date.split("-"))
        date = datetime(y, m, d)
        for team, score in [(team1, score1), (team2, score2)]:
            if score != "0" and team in streak_by_team:
                _, lds, lde = longest_streak
                if lde - lds < date - streak_by_team[team]:
                    longest_streak = team, streak_by_team[team], date
                streak_by_team.pop(team)
            if score == "0" and team not in streak_by_team:
                streak_by_team[team] = date

    team, date_start, date_end = longest_streak
    return f"{team} {date_start.strftime('%Y%m%d')} {date_end.strftime('%Y%m%d')}"
