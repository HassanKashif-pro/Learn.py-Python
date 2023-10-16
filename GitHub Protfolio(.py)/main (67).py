from replit import db 

def add():
  newUsername = input("UserName: ")
  newPassword = input("Password: ")
  newPassword = hash(newPassword)
  db[newUsername] = newPassword

Login = input("1.Add user \n2.Login \n>")

print(db["key"])

