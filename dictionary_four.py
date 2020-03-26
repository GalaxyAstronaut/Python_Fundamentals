classes = {"Warlock": "Lose 2 Life",
           "Hunter": "Opponent loses 2 life",
           "Warrior": "Gain 2 armor"
           }

while True:
    choose_class = input("Please pick a class: ")
    if choose_class == "quit":
        break
    description = classes.get(choose_class, "We couldn't find " + choose_class)
    print(description)