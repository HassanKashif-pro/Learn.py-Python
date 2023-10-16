import random

for i in range(10):
  myNumber = random.randint(1, 10000)
 # print(myNumber)
print("G U E S S   T H E   N U M B E R")
print("")
print("One - Million")
print("")
number = 0
tries = 0

while number != myNumber:
    number = int(input("What is your guess? (Enter 0 to exit): "))

    if number == 0:
        print("Exiting the game.")
        break

    tries += 1

    if number == myNumber:
        print("")
        print("Congratulations! You guessed the correct number.")
        print("")
        print("It took you", tries, "tries.")
        break

    if myNumber >= 1000 + number :
        print("Close!")
    elif myNumber >= 500 +number:
        print("Very Close!")
    elif myNumber <=  1000 + number:
        print("Lower!")
    elif myNumber <= 5000 +number:
        print("You're too high, mate!")
    elif myNumber < 10000 +number:
        print("Are you high? I think you are, a lot!")
    else:
        print("Out of range!")

print("Game over.")
