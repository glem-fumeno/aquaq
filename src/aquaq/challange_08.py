def solve_08(file: str):
    _, *logs = file.splitlines()
    milk: list[int] = []
    expiry: list[int] = []
    cereal = 0
    for i, log in enumerate(logs):
        _, new_milk, new_cereal = log.split(",")
        cereal += int(new_cereal)

        if cereal >= 100 and len(milk) > 0:
            milk[0] -= 100
            cereal -= 100
        if len(milk) > 0 and (milk[0] <= 0 or expiry[0] <= i):
            milk = milk[1:]
            expiry = expiry[1:]
        if new_milk != "0":
            milk.append(int(new_milk))
            expiry.append(i + 5)
    print(sum(milk) + cereal)
