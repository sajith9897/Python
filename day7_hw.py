inventory = []


def add_item(item):
    inventory.append(item)


def count_items(items):
    if not items:
        return 0

    return 1 + count_items(items[1:])


def main():
    add_item("dog food")
    add_item("cat toy")
    add_item("bird cage")
    add_item("fish tank")

    show_item = lambda item: print(f"Item in Stock: {item}")

    for item in inventory:
        show_item(item)

    total = count_items(inventory)
    print("Total number of items:", total)


main()