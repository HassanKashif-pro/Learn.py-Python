import os
import time

Listofwork = []

def prettyPrint():
    os.system("clear")  # start by clearing the screen
    print("ToDo List Manager: ")  # print the title of my program
    print()  # print a blank line
    for idx, item in enumerate(Listofwork, 1):  # use enumerate to access list items along with their indices
        print(f"{idx}. {item}")
    time.sleep(1)

while True:
    print("ToDo List Manager: ")  # print the title of my program
    print("")
    print("Do you want to view, add, remove, or edit the todo list?:\n")
    menu = input("1. Add List\n2. Remove List\n3. Show view\n4. Get edit\n> ")

    if menu == "1":
        email = input("Add > ")
        Listofwork.append(email)
    elif menu == "2":
        email = input("Remove > ")
        confirming = input("Are you sure about that (yes/no)?: ").lower()
        if confirming == "yes":
            if email in Listofwork:
                Listofwork.remove(email)
        elif confirming == "no":
            print("Cancelled.")
        else:
            print("Invalid input. Operation cancelled.")
        prettyPrint()
    elif menu == "3":
        prettyPrint()
    elif menu == "4":
        number_list = int(input("Which string do you want to edit?: "))  # Convert input to int
        if 1 <= number_list <= len(Listofwork):  # Check if the entered index is valid
            replace_with = input("What do you want to replace it with?: ")
            Listofwork[number_list - 1] = replace_with  # Modify the list item at the specified index
        else:
            print("Invalid index.")
        time.sleep(1)

    time.sleep(1)
    os.system("clear")
