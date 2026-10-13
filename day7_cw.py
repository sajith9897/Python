initial_items = ["milk", "bread", "eggs"]

def add_item(item):
    initial_items.append(item)

def remove_last_item():
    initial_items.pop()

display_item = lambda item: print("Item:", item)
for item in initial_items:
    display_item(item)

def count_characters(items):
    if len(items) == 0:
        return 0
    return len(items[0]) + count_characters(items[1:])


add_item("rice")
print (initial_items)

remove_last_item()


print("Updated Grocery List:", initial_items)
print("Total Characters:", count_characters(initial_items))