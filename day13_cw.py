item = input("Enter a new stationery item: ")

with open("items.txt", "a") as file:
    file.write(item + "\n")


with open("items.txt", "r") as file:
    print("\nList of Stationery Items:")

    items = file.read()
    print(items)