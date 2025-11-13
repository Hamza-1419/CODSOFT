# CODSOFT Python Internship
# Task 2 - To-Do List Program

tasks = []  # empty list to store all tasks

def show_menu():
    print("\n=== TO-DO LIST MENU ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Choose an option (1-4): ").strip()

    if choice == '1':
        task = input("Enter your task: ").strip()
        if task:
            tasks.append(task)
            print(f"✅ Task '{task}' added successfully!")
        else:
            print("⚠️ Empty task not added.")

    elif choice == '2':
        if not tasks:
            print("📭 No tasks in the list.")
        else:
            print("\nYour Tasks:")
            for i, t in enumerate(tasks, start=1):
                print(f"{i}. {t}")

    elif choice == '3':
        if not tasks:
            print("Nothing to delete.")
        else:
            try:
                num = int(input("Enter task number to delete: "))
                if 1 <= num <= len(tasks):
                    removed = tasks.pop(num - 1)
                    print(f"🗑️ Removed task: {removed}")
                else:
                    print("⚠️ Invalid task number.")
            except ValueError:
                print("⚠️ Please enter a valid number.")

    elif choice == '4':
        print("👋 Exiting... Have a productive day!")
        break

    else:
        print("⚠️ Invalid choice. Please select 1–4.")