mid_meta_champions = {
    "Diana": {"Q": "Crescent Strike - Cooldown : 8 / 7.5 / 7 / 6.5 / 6",
              "W": "Pale Cascade - Cooldown: 15 / 13.5 / 12 / 10.5 / 9",
              "E": "Lunar Rush - Cooldown: 22 / 20 / 18 / 16 / 14",
              "R": "MoonFall - Cooldown: 100 / 90 / 80"
              },
    "Fizz": {"Q": "Urchin Strike - Cooldown: 8 / 7.5 / 7 / 6.5 / 6",
             "W": "Seastone Trident- Cooldown: 7 / 6.5 / 6 / 5.5 / 5",
             "E": "Playful - Cooldown: 16/ 14.5 / 13 / 11.5 / 10",
             "R": "Chum the Waters - Cooldown: 100 / 85 / 70"
    },
    "Ekko": {"Q": "TimeWinder - Cooldown: 9 / 8.5 / 8 / 7.5 / 7",
             "W": "Parallel Convergence - Cooldown : 22 / 20 / 18 / 16 / 14 ",
             "E": "Phase Dive - Cooldown - 9 / 8.5 / 8 / 7.5 / 7 ",
             "R": "ChronoBreak - Cooldown - 110 / 80 / 50"
    },
    "Katarina": {"Q": "Bouncing Blade - Cooldown : 11 / 10 / 9 / 8 / 7",
                 "W": "Preparation - Cooldown: 15 / 14 / 13 / 12 / 11 ",
                 "E": "Shunpo - Cooldown: 14 / 12.5 / 11 / 9.5 / 8",
                 "R": "Death Lotus - Cooldown: 90 / 60 / 45 "
    }

}

while True:
    champion_key = input("Please input a champion name: ")
    if champion_key == "quit":
        break
    description = mid_meta_champions.get(champion_key, "We don't have a " + champion_key)
    print(description)