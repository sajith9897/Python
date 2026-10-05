rice = 45
sugar = 40
oil = 130

rice_bought = 3
sugar_bought = 2.5
oil_bought = 1.8

rice_total = rice * rice_bought
sugar_total = sugar * sugar_bought
oil_total = oil * oil_bought

final_total =  rice_total + sugar_total + oil_total

final_total_integer = int(final_total)

final_total_string = str(final_total)

import random

delivery_charge = random.randint(45,110)

final_bill = final_total + delivery_charge


print ("Rice Total:", rice_total)
print ("Sugar Total:", sugar_total)
print ("Oil Total:", oil_total)

print ("Total:", final_total)

print("Total as integer:", final_total_integer)
print("Total as string:", final_total_string)

print("Delivery Charges:", delivery_charge)

print("Final Bill:", final_bill)
