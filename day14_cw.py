import random
import math

names = input("Enter guest names separated by commas:")

name_list = [name.strip() for name in names.split(",") if name.strip()]

unique_names = list(dict.fromkeys(name_list))

if unique_names:
    selected_name = random.choice(unique_names)
    reversed_name = selected_name[::-1]
    total_names = len(unique_names)

    square_root = round(math.sqrt(total_names))

    print("\n----- BIRTHDAY NAME GAME -----")
    print("Unique guest names:", unique_names)
    print("Selected name:", selected_name)
    print("Reversed name:", reversed_name)
    print("Total unique names:", total_names)
    print("Rounded square root:", square_root)

else:
    print("Please enter at least one valid name!")              