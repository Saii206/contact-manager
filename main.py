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