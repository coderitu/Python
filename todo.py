# Create an empty list to store the items
todo_list = []

# Function to add items
def add_item(item):
    todo_list.append(item)
    print("Item added successfully!")

# Function to view items
def view_items():
    if len(todo_list) == 0:
        print("You have no items in your todo list")
    else:
        for item in todo_list:
            print(item)

# Function to remove items
def remove_item(item):
    if item in todo_list:
        todo_list.remove(item)
        print("Item removed successfully!")
    else:
        print("Item not found!")

# Driver code
while True:
    print("1. Add item")
    print("2. View items")
    print("3. Remove item")
    print("4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = input("Enter the item: ")
        add_item(item)
    elif choice == 2:
        view_items()
    elif choice == 3:
        item = input("Enter the item: ")
        remove_item(item)
    elif choice == 4:
        break
    else:
        print("Invalid choice!")