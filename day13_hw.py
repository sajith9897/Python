import os

filename = "students.txt"

if os.path.exists(filename):
    print("Existing student names:")
    with open(filename, "r") as file:
        existing_names = file.read()
        print(existing_names)
else:
    print("No existing student records found.")


n = int(input("How many student names do you want to add? "))


with open(filename, "a") as file:
    for i in range(n):
        name = input(f"Enter student name {i + 1}: ")
        file.write(name + "\n")

print("\nUpdated student list:")
with open(filename, "r") as file:
    print(file.read())