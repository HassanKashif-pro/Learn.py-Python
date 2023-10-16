print("G U E S S   T H E   N U M B E R")
print("")
print("One - Million")
print("")
number = 0
tries = 0

while number != 450:
    number = int(input("What is your guess? (Enter 0 to exit): "))

    if number == 0:
        print("Exiting the game.")
        break

    tries += 1

    if number == 450:
        print("Congratulations! You guessed the correct number.")
        print("It took you", tries, "tries.")
        break

    if 1 < number <= 500:
        print("Close!")
    elif 500 < number <= 1000:
        print("Very Close!")
    elif 1000 < number <= 3000:
        print("Lower!")
    elif 3000 < number <= 4000:
        print("You're too high, mate!")
    elif 4000 < number <= 5000:
        print("Are you high? I think you are, a lot!")
    else:
        print("Out of range!")

print("Game over.")
