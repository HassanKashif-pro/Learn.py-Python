from replit import db
import datetime, os, time, random

def addTweet():
  time.sleep(1)
  os.system("clear")
  tweet = input("🐥 > ")
  timestamp = datetime.datetime.now()
  key = f"mes{timestamp}"
  db[key] = tweet
  time.sleep(1)
  os.system("clear")

def viewTweet():
  time.sleep(1)
  os.system("clear")
  matches = db.prefix("mes")
  matches = matches[::-1]
  counter = 0
  for i in matches:
    print(db[i])
    print()
    time.sleep(0.3)
    counter+=1
    if(counter%10==0):
      carryOn = input("Next 10?: ")
      if(carryOn.lower()=="no"):
        break

keys = db.keys()
print(keys)
if len(keys)<1 : 
  username = input("Username: ")
  password = input("Password: ")
  salt = random.randint(0,9999999)
  newPassword = f"{password}{salt}"
  password = hash(password)     
  db[username] = {"password": newPassword, "salt": salt}
else:
  print("Log in")
  username = input("Username > ")
  password = input("Password > ")
  if username not in keys:
    print("Username or password incorrect")
    exit()
  salt = db[username]["salt"]
  newPassword = hash(f"{password}{salt}")
  if db[username]["password"]!=newPassword:
    print("Username or password incorrect")
    exit()
while True:
  os.system("clear")
  menu = input("1: Add\n2: View\n> ")
  if menu == "1":
    addTweet()
  else:
    viewTweet()

