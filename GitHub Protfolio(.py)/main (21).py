import random

def dice():
    print("Infinity Dice 🎲")
    while True:
        dice_number = int(input("How many sides?: "))
        myNumber = random.randint(1, dice_number) 
        print("You rolled " + str(myNumber))
        print("")
        again_roll = input("Roll again (yes/no)?: ").lower()
        if again_roll == "no":
            break

# Call the dice function
dice()
