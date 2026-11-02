while True:
    try:
        n = int(input("Enter number of rows: "))

        if n <= 0:
            print("Enter a positive number")
        else:
            for i in range(1, n + 1):
                print("*" * i)

    except ValueError:
        print("Invalid input! Enter an integer.")

    choice = input("Do you want to continue? (yes/no): ")

    if choice == "no":
        print("Program stopped")
        break

    elif choice != "yes":
        print("Invalid choice. Program stopped.")
        break

    else:
        continue