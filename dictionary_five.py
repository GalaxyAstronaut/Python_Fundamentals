locations = {
    0: "You are sitting in front of a computer learning Python",
    1: "You are standing beside a huge statue of a black amethyst dragon.",
    2: "You are at the crossroad of truth.",
    3: "You are inside a house with no windows.",
    4: "You are at a lake of fire.",
    5: "You are in the forbidden forest of solitude."
}

exits = [
    {"Q": 0},
    {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
    {"N": 5, "Q": 0},
    {"W": 1, "Q": 0},
    {"N": 1, "W": 2, "Q": 0},
    {"W": 2, "S": 1, "Q": 0}
]

loc = 1
while True:
    availableExits = ", ".join(exits[loc].keys())
    # for direction in exits[loc].keys():
    #     availableExits += direction + ", "

    print(locations[loc])

    if loc == 0:
        break

    direction = input("Available exits are " + availableExits).upper()
    print()
    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("You cannot go in that direction.")