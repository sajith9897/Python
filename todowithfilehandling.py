import os

FILE_NAME = "tasks.txt"


def add_task():
    task = input("Enter your task: ").strip()

    if not task:
        print("Task cannot be empty!")
        return

    with open(FILE_NAME, "a") as file:
        file.write(task + "\n")

    print("Task added successfully!")


def view_tasks():
    if not os.path.exists(FILE_NAME):
        print("No tasks found!")
        return

    with open(FILE_NAME, "r") as file:
        tasks = file.readlines()

    if not tasks:
        print("Your To-Do List is empty!")
        return

    print("\n------ YOUR TO-DO LIST ------")

    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task.strip()}")


def delete_task():
    if not os.path.exists(FILE_NAME):
        print("No tasks available to delete!")
        return

    with open(FILE_NAME, "r") as file:
        tasks = file.readlines()

    if not tasks:
        print("Your To-Do List is empty!")
        return

    print("\n------ YOUR TO-DO LIST ------")

    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task.strip()}")

    try:
        task_number = int(input("Enter the task number to delete: "))

        if task_number < 1 or task_number > len(tasks):
            print("Invalid task number!")
            return

        removed_task = tasks.pop(task_number - 1)

        with open(FILE_NAME, "w") as file:
            file.writelines(tasks)

        print(f"Deleted task: {removed_task.strip()}")

    except ValueError:
        print("Please enter a valid number!")


def main():
    while True:
        print("\n====== TO-DO LIST APP ======")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            delete_task()

        elif choice == "4":
            print("Thank you for using the To-Do List!")
            break

        else:
            print("Invalid choice! Please select 1-4.")


main()