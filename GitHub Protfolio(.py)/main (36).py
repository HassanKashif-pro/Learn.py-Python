Coloured_Words = ["b", "r", "y", "g", "o"]

User_Input = input("Write any sentence and see the magic: ")

for myString in User_Input:
    if myString.lower() == "b":
        print("\033[34m", end="")
    elif myString.lower() == "r":
        print("\033[31m", end="")
    elif myString.lower() == "y":
        print("\033[33m", end="")
    elif myString.lower() == "g":
        print("\033[32m", end="")
    elif myString.lower() == "o":
        print("\033[91m", end="")
    
    print(myString, end="")
    print("\033[0m", end="")

print()  # Print a newline after the loop
