tasks = []

def show_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        for i, task in enumerate(tasks, start=1):
            status = "✓" if task["done"] else "✗"
            print(f"{i}. [{status}] {task['name']}")

def add_task():
    name = input("Enter task: ")
    tasks.append({"name": name, "done": False})
    print("Task added!")

def mark_done():
    show_tasks()
    num = int(input("Enter task number to mark done: "))
    if 1 <= num <= len(tasks):
        tasks[num-1]["done"] = True
        print("Task marked as done!")

def delete_task():
    show_tasks()
    num = int(input("Enter task number to delete: "))
    if 1 <= num <= len(tasks):
        tasks.pop(num-1)
        print("Task deleted!")

def menu():
    while True:
        print("\n--- TO-DO LIST ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

menu()
