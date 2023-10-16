import os, time

Inventory = []

try:
    f = open("Inventory.txt", "r")
    Inventory = eval(f.read())
    f.close()
except:
    print("ERROR: No existing item list, using a blank list")

def add():
    time.sleep(1)
    os.system("clear")
    print("INVENTORY")
    print("=========")
    print()
    adding = input("What do you want to add: ").capitalize().strip()
    Inventory.append(adding)
    print(adding, "has been added to the inventory")

def remove():
    time.sleep(1)
    os.system("clear")
    print("INVENTORY")
    print("=========")
    print()
    removing = input("What do you want to remove: ")
    if removing in Inventory:
        Inventory.remove(removing)
        print(removing, "has been removed from the inventory")
    else:
        print(removing, "is not in the inventory")

def view():
    time.sleep(1)
    os.system("clear")
    print("INVENTORY")
    print("=========")
    print()
    item = input("Item to view in Inventory: ")
    for item in Inventory:
        print(f"{item} {Inventory.count(item)}")
        time.sleep(3) 
      
while True:
    time.sleep(1)
    os.system("clear")
    print("🌟RPG Inventory🌟")
    print()
    option = input("1: Add\n2: Remove\n3: View\n>")
    if option == "1":
        add()
    elif option == "2":
        remove()
    elif option == "3":
        view()
    else:
        print("Invalid option. Please choose 1, 2, or 3.")

    # Save the updated inventory to the file
    f = open("Inventory.txt", "w")
    f.write(str(Inventory))
    f.close()
