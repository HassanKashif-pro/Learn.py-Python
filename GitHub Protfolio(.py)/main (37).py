"""import random

listOfWords = ["Serendipity", "Harmony", "Breeze", "Joyful", "Whisper", "Delight", "Sparkle", "Discover", "Soothe", "Cheerful"]
myWord = random.choice(listOfWords)
Lives = 6
print(myWord)
while Lives > 0:
    Letter_choice = input("Choose a Letter: ")
    if Letter_choice.lower() in myWord.lower():
        print("You found a letter")
        print()
      
    else:
        Lives -= 1
        print("Try Again")
        print(f"You have {Lives} lives remaining")
        print()

print("Game Over")
"""

import random
import os

listOfWords = ["Serendipity", "Harmony", "Breeze", "Joyful", "Whisper", "Delight", "Sparkle", "Discover", "Soothe", "Cheerful"]
myWord = random.choice(listOfWords).lower()
guessed_letters = set()
Lives = 6
Lives -= 1
print("Incorrect guess. You have", Lives, "lives remaining.")
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display

while Lives > 0:
    clear_screen()
    print("Current word:", display_word(myWord, guessed_letters))
    Letter_choice = input("Choose a Letter: ").lower()

    if Letter_choice in guessed_letters:
        print("You've already guessed that letter. Try again.")
    elif Letter_choice in myWord:
        guessed_letters.add(Letter_choice)
        if myWord == display_word(myWord, guessed_letters):
            clear_screen()
            print("Congratulations, you guessed the word:", myWord)
            break
    else:
        Lives -= 1
        clear_screen()
        print("Incorrect guess. You have", Lives, "lives remaining.")

    if Lives == 0:
        clear_screen()
        print("Sorry, you're out of lives. The word was:", myWord)

print("Game Over")
