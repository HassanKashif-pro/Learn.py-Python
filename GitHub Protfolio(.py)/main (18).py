print("Math Game!")
print("")
multiple = int(input("Name your multiples: "))
print("")

correct = 0  # Initialize the score counter

for i in range(1, 11):
    user_input = input(f"{multiple} x {i} = ")
    print("")

    while user_input == "":
        print("Type your Answer")
        user_input = input(f"{multiple} x {i} = ")
        print("")

    if int(user_input) == multiple * i:
        print("Well Done 🤩")
        correct += 1  # Increase the score when the answer is correct
    else:
        print("Nope! The answer is", multiple * i)
        print("")
        print("---")
        print("")
print("")
print("Your score is", correct)
print("")
if correct == 10 :
 print("Wow your a genious 🤩😘🥰🤩")