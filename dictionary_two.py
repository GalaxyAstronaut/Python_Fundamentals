states = {"Florida": "Sunshine State",
          "Georgia": "Peach State",
          "New York": "Empire State"}

for i in range(3):
    for state in states:
        print(state + " is the " + states[state])
    print("-" * 40)


letters = {"z": "Zebra",
           "r": "Romeo",
           "t": "Tea",
           "m": "Mars"}


while True:
    value = input("Input a word ")
    if value == "quit":
        break
    description = letters.get(value)
    print(description)


letters = {"z": "Zebra",
           "r": "Romeo",
           "t": "Tea",
           "m": "Mars"}


letters_keys = letters.keys()
print(letters_keys)
print(letters.values())

letters["s"] = "Song"
print(letters)

letters["s"] = "snake"
print(letters)
