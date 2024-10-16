tasks = []

def add_task():
    task = input("Enter a task: ")
    tasks.append({"task": task, "done": False})

def view_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        for idx, task in enumerate(tasks, start=1):
            status = "Done" if task["done"] else "Pending"
            print(f"{idx}. {task['task']} - {status}")

def mark_done():
    view_tasks()
    task_num = int(input("Enter task number to mark as done: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks[task_num]["done"] = True
    else:
        print("Invalid task number!")

def main():
    while True:
        print("\nTO-DO LIST")
        print("\n1. Add Task.\n2. View Tasks.\n3. Mark Task as Done.\n4. Exit.")
        choice = input("Choose an option: ")
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            mark_done()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
