import os, time

mokedex = {}

def prettyPrint():
  print("Name\tType\tHP\tMP\t")
for key, value in mokedex.items():
    print(f"""{key:^12}|{value["type"]:^10}|{value["hp"]:^6}|{value["mp"]:^6}""")

while True: 
    print("Moke Beast Full-on Moke Dex")
    print()
    print("Add your Beast")
    name = input("Name > ").capitalize()
    type = input("Type > ").capitalize()
    HP = int(input("HP > "))
    MP = int(input("MP > "))
    mokedex[name] = {"type >": type, "HP":HP, "MP":MP}
    print()
    print("-----------")

