# Simple User Management System
# Manages user records with file handling

import os

FILENAME = "users.txt"

def create_file():
    """Create the users file if it doesn't exist"""
    if not os.path.exists(FILENAME):
        with open(FILENAME, 'w') as file:
            file.write("")

def add_user():
    """Add a new user"""
    print("\n--- Add New User ---")
    name = input("Enter name: ")
    email = input("Enter email: ")
    phone = input("Enter phone: ")
    
    with open(FILENAME, 'a') as file:
        file.write(f"{name},{email},{phone}\n")
    
    print(f"✓ User '{name}' added successfully!")

def view_users():
    """View all users"""
    print("\n" + "="*60)
    print("                    ALL USERS")
    print("="*60)
    
    if os.path.getsize(FILENAME) == 0:
        print("\nNo users found. Add some users first!")
        return
    
    with open(FILENAME, 'r') as file:
        lines = file.readlines()
        
    if len(lines) == 0:
        print("\nNo users found.")
    else:
        print(f"\nTotal Users: {len(lines)}\n")
        print(f"{'No.':<5} {'Name':<20} {'Email':<25} {'Phone':<15}")
        print("-" * 60)
        
        for i, line in enumerate(lines, 1):
            data = line.strip().split(',')
            if len(data) == 3:
                name, email, phone = data
                print(f"{i:<5} {name:<20} {email:<25} {phone:<15}")

def search_user():
    """Search for a user by name"""
    print("\n--- Search User ---")
    search_name = input("Enter name to search: ").lower()
    
    with open(FILENAME, 'r') as file:
        lines = file.readlines()
    
    found = False
    print("\n" + "-"*60)
    
    for line in lines:
        data = line.strip().split(',')
        if len(data) == 3:
            name, email, phone = data
            if search_name in name.lower():
                print(f"Name: {name}")
                print(f"Email: {email}")
                print(f"Phone: {phone}")
                print("-"*60)
                found = True
    
    if not found:
        print("No user found with that name!")

def delete_user():
    """Delete a user"""
    view_users()
    
    if os.path.getsize(FILENAME) == 0:
        return
    
    try:
        user_num = int(input("\nEnter user number to delete: "))
        
        with open(FILENAME, 'r') as file:
            lines = file.readlines()
        
        if 1 <= user_num <= len(lines):
            deleted_user = lines[user_num - 1].strip().split(',')[0]
            lines.pop(user_num - 1)
            
            with open(FILENAME, 'w') as file:
                file.writelines(lines)
            
            print(f"✓ User '{deleted_user}' deleted successfully!")
        else:
            print("❌ Invalid user number!")
    
    except ValueError:
        print("❌ Please enter a valid number!")

def show_menu():
    """Display main menu"""
    print("\n" + "="*60)
    print("           USER MANAGEMENT SYSTEM")
    print("="*60)
    print("1. Add User")
    print("2. View All Users")
    print("3. Search User")
    print("4. Delete User")
    print("5. Exit")
    print("="*60)

def main():
    """Main program"""
    create_file()
    print("Welcome to User Management System!")
    
    while True:
        show_menu()
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '1':
            add_user()
        elif choice == '2':
            view_users()
        elif choice == '3':
            search_user()
        elif choice == '4':
            delete_user()
        elif choice == '5':
            print("\n✓ Thank you for using User Management System!")
            print("Goodbye!")
            break
        else:
            print("\n❌ Invalid choice! Please choose 1-5")

# Run the program
if __name__ == "__main__":
    main()