import random

print("⚔ CHARACTER STAT GENERATOR ⚔")
print("")

def warriors():
    warrior_name = input("Name your warrior: ")
    dice6 = random.randint(1, 6)
    dice8 = random.randint(1, 8)
    health = dice6 * dice8
    print("Your warrior, " + warrior_name + ", has " + str(health) + " health.")

# Loop 4 times
for _ in range(4):
    warriors()
    print("")  # Add an empty line between each warrior's stats
   
