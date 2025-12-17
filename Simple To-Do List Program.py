# Simple To-Do List Program
# Perfect for beginners

# List to store tasks
tasks = []

def show_menu():
    """Display the menu"""
    print("\n" + "="*35)
    print("       MY TO-DO LIST")
    print("="*35)
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Delete a task")
    print("4. Exit")
    print("="*35)

def add_task():
    """Add a new task"""
    task = input("\nEnter your task: ")
    tasks.append(task)
    print(f"✓ Task '{task}' added!")

def view_tasks():
    """Show all tasks"""
    if len(tasks) == 0:
        print("\nNo tasks yet! Add some tasks.")
    else:
        print("\nYour Tasks:")
        print("-" * 35)
        for i in range(len(tasks)):
            print(f"{i + 1}. {tasks[i]}")

def delete_task():
    """Delete a task"""
    view_tasks()
    if len(tasks) > 0:
        try:
            num = int(input("\nEnter task number to delete: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                print(f"✓ Task '{removed}' deleted!")
            else:
                print("Invalid number!")
        except:
            print("Please enter a valid number!")

# Main program
print("Welcome to your To-Do List!")

while True:
    show_menu()
    choice = input("\nChoose an option (1-4): ")
    
    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        delete_task()
    elif choice == '4':
        print("\nGoodbye! Have a productive day!")
        break
    else:
        print("\nInvalid choice! Please choose 1-4")