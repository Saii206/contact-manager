def create_contact():
    name = input("Enter name: ")
    number = input("Enter number: ")

    with open("contacts.txt", "w") as file:
        file.write(f"{name} - {number}\n")

    print("Saved!")

def add_contact():
    name = input("Enter name: ")
    number = input("Enter number: ")

    with open("contacts.txt", "a") as file:
        file.write(f"{name} - {number}\n")

    print("Added!")

def view_contacts():
    with open("contacts.txt", "r") as file:
        for line in file:
            print(line.strip())

def update_contact():
    name = input("Enter name to update: ")
    new_number = input("Enter new number: ")

    lines = []

    with open("contacts.txt", "r") as file:
        for line in file:
            if name in line:
                lines.append(f"{name} - {new_number}\n")
            else:
                lines.append(line)

    with open("contacts.txt", "w") as file:
        file.writelines(lines)

    print("Updated!")      

def search_contact():
    name = input("Enter name to search: ")

    with open("contacts.txt", "r") as file:
        found = False
        for line in file:
            if name in line:
                print(line.strip())
                found = True

        if not found:
            print("Contact not found.")

def delete_contact():
    name = input("Enter name to delete: ")

    lines = []

    with open("contacts.txt", "r") as file:
        for line in file:
            if name not in line:
                lines.append(line)

    with open("contacts.txt", "w") as file:
        file.writelines(lines)

    print("Contact deleted!")

print("5. Search Contact")
print("6. Delete Contact") 

while True:
    print("\n1. Create Contact")
    print("2. Add Contact")
    print("3. View Contacts")
    print("4. Update Contact")
    print("5. Search Contact")
    print("6. Delete Contact")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        create_contact()
    elif choice == "2":
        add_contact()
    elif choice == "3":
        view_contacts()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        search_contact()
    elif choice == "6":
        delete_contact()
    elif choice == "7":
        break
    else:
        print("Invalid choice")