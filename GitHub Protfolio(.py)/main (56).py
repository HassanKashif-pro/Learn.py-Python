import time, os

def palindrome(word):
    if len(word) <= 1:
        return True
    if word[0] != word[-1]:
        return False
    return palindrome(word[1:-1])

print("🌟 Palindrome Checker 🌟")
print()
word = input("Input Word > ").lower().replace(" ", "")
print()
if palindrome(word):
    print("It's a palindrome!")
else:
    print("It's not a palindrome!")


time.sleep(1)
os.system("clear")
