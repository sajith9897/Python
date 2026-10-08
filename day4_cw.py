fruits = ["apple", "orange", "grapes"]
vegetables = ["carrot", "cucmber", "spinach"]
beverage = ["cola", "sprite", "pepsi"]

fruits.append("banana")
print(fruits)

vegetables.insert (1,"tomato")
print(vegetables)

del beverage[-1]
print(beverage)

inventory = [fruits, vegetables, beverage]
print (inventory)

print(fruits[:2])

print(vegetables[-1])

fruit_length = [len(y) for y in fruits]
print (fruit_length)

print("water" in beverage)

items = (fruits[0], vegetables[0], beverage[0])
print(items)