from csv import DictReader
from datetime import datetime, timedelta


def solve(input_file: str):
    cereal = 0
    milk = []
    for line in DictReader(input_file.splitlines()):
        today = datetime(
            int(line["date"].split("-")[0]),
            int(line["date"].split("-")[1]),
            int(line["date"].split("-")[2]),
        )
        cereal += int(line["cereal"])
        if sum(m for m, _ in milk) >= 100 and cereal >= 100:
            milk[0][0] -= 100
            cereal -= 100
        if len(milk) > 0 and (milk[0][0] <= 0 or milk[0][1] <= today):
            milk = milk[1:]
        if line["milk"] != "0":
            milk.append([int(line["milk"]), today + timedelta(5)])
    return sum(m for m, _ in milk) + cereal
