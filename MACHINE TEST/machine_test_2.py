while True:
    try:
        num = int(input("Enter a number: "))

        for i in range(1, 11):
            print(num, "x", i, "=", num * i)

    except ValueError:
        print("Invalid input! Enter an integer.")

    choice = input("Do you want to continue? (yes/no): ")

    if choice == "no":
        print("Program Stopped")
        break
    
    elif choice != "yes":
        print("Invalid choice. Program Stopped.")
        break