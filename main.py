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