def display_menu():
    print("\nTo-Do List")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

tasks = []

def add_task():
    task_description = input("Enter the task: ")
    tasks.append({"task": task_description, "done": False})
    print(f"Task '{task_description}' has been added successfully.")

def show_tasks():
    if not tasks:
        print("\nYour to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            status = "✓" if task["done"] else "✗"
            print(f"{i}. {task['task']} [{status}]")

def mark_task_done():
    show_tasks()
    if tasks:
        try:
            task_no = int(input("Enter the task number to mark as done: "))
            tasks[task_no - 1]["done"] = True
            print(f"Task '{tasks[task_no - 1]['task']}' marked as done.")
        except (IndexError, ValueError):
            print("Invalid task number. Please try again.")

def delete_task():
    show_tasks()
    if tasks:
        try:
            task_no = int(input("Enter the task number to delete: "))
            removed = tasks.pop(task_no - 1)
            print(f"Task '{removed['task']}' deleted successfully.")
        except (IndexError, ValueError):
            print("Invalid task number. Please try again.")

def main():
    print("Welcome to the To-Do List App!")
    while True:
        display_menu()
        try:
            choice = int(input("Choose an option: "))
            if choice == 1:
                add_task()
            elif choice == 2:
                show_tasks()
            elif choice == 3:
                mark_task_done()
            elif choice == 4:
                delete_task()
            elif choice == 5:
                print("Goodbye! Have a nice day!")
                break
            else:
                print("Invalid choice. Please select a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()

        
            

        
        
            




            



