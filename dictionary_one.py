group_call = {
    "Marcus": "The OG",
    "Bert": "The Fire Cadet",
    "Corran": "The TFT monkaS",
    "Franky": "The Second Support",
    "Chimmey": "The TFT",
    "Timmy": "The Job"
}
#
# while True:
#     friend = input("Please input a boy name: ")
#     if friend == "quit":
#         break
#     description = group_call.get(friend, "There is no " + friend + " in the group.")
#     print(description)

# for boy in group_call:
#     print(group_call[boy])
#
#
# for i in range(5):
#     for lol in group_call:
#         print(lol + " is a " + group_call[lol])
#     print('-' * 40)

# ordered_keys = list(group_call.keys())
# ordered_keys.sort()
ordered_keys = sorted(list(group_call.keys()))
for f in ordered_keys:
    print(f + " - " + group_call[f])
