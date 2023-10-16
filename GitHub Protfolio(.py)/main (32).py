import os, time
listOfEmail = []
def prettyPrint():
  os.system("clear") # start by clearing the screen
  print("listofEmail") # print the title of my program
  print() # print a blank line
  for email in listOfEmail: # use for loop to access list
    print(email)
  time.sleep(1)
while True:
  print("SPAMMER Inc.")
  menu = input("1. Add email\n2: Remove email\n3. Show emails\n4. Get SPAMMING\n> ")
  if menu == "1":
    email = input("Email > ")
    listOfEmail.append(email)
  elif menu =="2":
    email = input ("Email > ")
    if email in listOfEmail:
      listOfEmail.remove(email)
    prettyPrint()  
  time.sleep(1)
  os.system("clear")