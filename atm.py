
def deposit(balance):
    amount = float(input("Enter deposit amount: "))

    if amount > 0:
        balance = balance + amount
        print("Deposit successful")
    else:
        print("Enter a valid amount")

    return balance


def withdraw(balance):
    amount = float(input("Enter withdrawal amount: "))

    if amount <= 0:
        print("Enter a valid amount")

    elif amount > balance:
        print("Insufficient balance")

    else:
        balance = balance - amount
        print("Withdrawal successful")

    return balance


def check_balance(balance):
    print("Current balance: ₹", balance)


balance = 1000

while True:
    print("\n===== ATM MENU =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        balance = deposit(balance)

    elif choice == "2":
        balance = withdraw(balance)

    elif choice == "3":
        check_balance(balance)

    elif choice == "4":
        print("Thank you for using our ATM!")
        break

    else:
        print("Invalid choice. Try again.")
