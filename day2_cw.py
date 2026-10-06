header = """--- BOOKSTORE RECEIPT ---
------------------------"""

book1 = "Python Basics"
book1_price = 450

book2 = "Data Science Intro"
book2_price = 600

item1 = "{}\t\t{}".format (book1, book1_price)
item2 = "{}\t{}".format (book2, book2_price)

total = book1_price + book2_price
total_line = f"Total:\t\t\t{total}"

thankyou = "Thankyou for shopping"

receipt = (
    header +'\n'+'\n'
    +item1 +'\n'
    +item2 +'\n'
    +"------------------------"+'\n'
    +total_line +'\n'+'\n'
    +'\t'+thankyou
)

print(receipt.upper())