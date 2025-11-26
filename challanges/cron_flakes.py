from datetime import datetime, timedelta


def solve(input_file: str):
    cereal = 0
    milk = []
    for line in input_file.splitlines():
        today_i, milk_i, cereal_i = line.split(",")
        today = datetime(
            int(today_i.split("-")[0]),
            int(today_i.split("-")[1]),
            int(today_i.split("-")[2]),
        )
        cereal += int(cereal_i)
        if sum(m for m, _ in milk) >= 100 and cereal >= 100:
            milk[0][0] -= 100
            cereal -= 100
        if len(milk) > 0 and (milk[0][0] <= 0 or milk[0][1] <= today):
            milk = milk[1:]
        if milk_i != "0":
            milk.append([int(milk_i), today + timedelta(5)])
    return sum(m for m, _ in milk) + cereal
