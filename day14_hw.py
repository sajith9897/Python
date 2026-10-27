import random
import math

names = input("Enter customer names separated by commas: ")

name_list = []

for name in names.split(","):
    name = name.strip()

    if name:
        name_list.append(name)

unique_names = list(dict.fromkeys(name_list))

total_participants = len(unique_names)

if total_participants < 2:
    print("At least 2 unique participants are required!")

else:

    random.shuffle(unique_names)

    winners = random.sample(unique_names, 2)

    print("\n===== LUCKY DRAW RESULTS =====")

    for index, winner in enumerate(winners, start=1):
        print(f"Winner {index}: {winner}")
        print(f"Reversed name: {winner[::-1]}")

    print("\nTotal unique participants:", total_participants)

    result = round(math.sqrt(total_participants))

    print("Rounded square root:", result)