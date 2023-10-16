import os

password = os.environ['password'] # Uses the os library to talk to the environment and get the secret password stored there.

userID = input("ID> ")
userPass = input("Password > ")

if userPass == hassan:
  print("Well done")
else:
  print("Better luck next time")