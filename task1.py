# Codsoft Internship (Task 1 as per document)
# To-Do List

def display_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks available.")
    else:
        print("\nCurrent Tasks:")
        for i in range(len(tasks)):
            status = "Done" if tasks[i]["status"] else "Pending"
            print(f"Task {i + 1}: {tasks[i]['title']} - {status}")

def add_task(tasks):
    title = input("Enter task title: ").strip()
    if title != "":
        task = {"title": title, "status": False}
        tasks.append(task)
        print("Task added")
    else:
        print("Enter non-empty task title: ")

def mark_task_complete(tasks):
    display_tasks(tasks)
    index_input = input("Enter task number to mark as complete: ")
    if index_input.isdigit():
        index = int(index_input) - 1
        if 0 <= index < len(tasks):
            tasks[index]["status"] = True
            print("Task marked complete")
        else:
            print("Task number does not exist")
    else:
        print("Please enter valid number")


tasks = []

while True:
    print("\n--- To-Do List ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Complete")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        display_tasks(tasks)
    elif choice == "2":
        add_task(tasks)
    elif choice == "3":
        mark_task_complete(tasks)
    elif choice == "4":
        print("Exiting application")
        break
    else:
        print("Invalid option. Please select 1-4")
