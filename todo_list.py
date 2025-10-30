# todo_list.py
# Simple command-line To-Do List application

def show_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    print()

def main():
    tasks = []
    while True:
        print("To-Do List Options:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter choice (1-4): ")

        if choice == "1":
            task = input("Enter task: ")
            tasks.append(task)
            print("Task added!\n")
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            show_tasks(tasks)
            try:
                index = int(input("Enter task number to remove: "))
                removed = tasks.pop(index - 1)
                print(f"Removed: {removed}\n")
            except (ValueError, IndexError):
                print("Invalid task number!\n")
        elif choice == "4":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice!\n")

if __name__ == "__main__":
    main()
