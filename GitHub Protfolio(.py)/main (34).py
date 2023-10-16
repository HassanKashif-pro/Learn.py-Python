myName = []

while True:
    First_name = input("First Name: ").title().strip()
    Last_name = input("Last Name: ").capitalize().strip()
    print()
    Full_Name = f"{First_name} {Last_name}"  # Combine the first name and last name
    
    if Full_Name not in myName:  # Check if the full name is not already in the list
        myName.append(Full_Name)  # Add the full name to the list
        print(Full_Name)  # Print the full name
        print()
    else:
        print("Error: Duplicate Name")
        print()
