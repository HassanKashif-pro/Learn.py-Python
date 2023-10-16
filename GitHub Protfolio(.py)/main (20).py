def ID():
    name = "David"
    password = "David is cool"
    
    print("REPLIT LOGIN SYSTEM")
    print("")
    
    while True:
        input_name = input("What is your name: ")
        print("")
        input_password = input("What is your password: ")

        if input_name == name and input_password == password:
            print("")
            print("Login successful. Welcome, David!")
            break
        else:
            print("")
            print("Invalid name or password. Please try again.")
            print("")

ID()
