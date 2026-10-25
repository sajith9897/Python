
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        task = input("Enter your task: ")

        if task.strip() == "":
            print("Task cannot be empty!")
        else:
            self.tasks.append({
                "task": task,
                "completed": False
            })
            print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("Your to-do list is empty!")
        else:
            print("\n--- YOUR TASKS ---")

            for index, task in enumerate(self.tasks, start=1):
                if task["completed"]:
                    status = "Completed"
                else:
                    status = "Pending"

                print(f"{index}. {task['task']} - {status}")

    def complete_task(self):
        self.view_tasks()

        if not self.tasks:
            return

        try:
            number = int(input("Enter task number to complete: "))

            if 1 <= number <= len(self.tasks):
                self.tasks[number - 1]["completed"] = True
                print("Task marked as completed!")
            else:
                print("Invalid task number!")

        except ValueError:
            print("Please enter a valid number!")

    def delete_task(self):
        self.view_tasks()

        if not self.tasks:
            return

        try:
            number = int(input("Enter task number to delete: "))

            if 1 <= number <= len(self.tasks):
                removed = self.tasks.pop(number - 1)
                print(f"Deleted task: {removed['task']}")
            else:
                print("Invalid task number!")

        except ValueError:
            print("Please enter a valid number!")


todo = ToDoList()

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        todo.add_task()
    elif choice == "2":
        todo.view_tasks()
    elif choice == "3":
        todo.complete_task()
    elif choice == "4":
        todo.delete_task()
    elif choice == "5":
        print("Thank you for using the To-Do List!")
        break
    else:
        print("Invalid choice! Please try again.")
