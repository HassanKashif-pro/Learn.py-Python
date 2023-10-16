import random, os, time

def rollDice(side):
    result = random.randint(1, side)
    return result
  
def health():
    health = ((rollDice(6)*rollDice(12))/2) + 10
    return health
  
def strength():
    strength = ((rollDice(6)*rollDice(8))/2) + 12
    return strength

print("⚔️ 🛡️ BATTLE TIME ⚔️ 🛡️")
print("")
c1Name = input("Name Your Legend:\n")
c1Type = input("Character Type (Human, Elf, Wizard, Orc, etc.):\n")
print("")
c1Health = health()
c1Strength = strength()
print(c1Name)
print("Character Type:", str(c1Type))
print("HEALTH ❤️ :", c1Health)
print("STRENGTH 💪 :", c1Strength)
print("")      
print("Who is This legend Fighting?! 😱")
print("")      
c2Name = input("Name Your Legend:\n")
c2Type = input("Character Type (Human, Elf, Wizard, Orc, etc.):\n")
print("")
print(c2Name)
c2Health = health()
c2Strength = strength()
print("Character Type:", str(c2Type))
print("HEALTH ❤️ :", c2Health)
print("STRENGTH 💪 :", c1Strength)

round = 1
winner = None
while True:
    time.sleep(2)
    os.system("clear")
    print("⚔️ 🛡️ BATTLE TIME ⚔️ 🛡️")
    print("")  
    print("Battle Begins!")

    c1Dice = rollDice(6)
    c2Dice = rollDice(6)

    diffrence = abs(c1Strength - c2Strength) + 1 

    if c1Dice > c2Dice:
        c2Health -= diffrence
        if round == 1:
            print(c1Name, "wins the first blow")
        else:
            print(c1Name, "wins round", round)
    elif c2Dice > c1Dice:
        c1Health -= diffrence
        if round == 1:
            print(c2Name, "wins the first blow")
        else:
            print(c2Name, "wins round", round)      
    else:
        print("Their sword slash and they have a draw of round", round)

    print()
    print(c1Name)
    print("c1 HEALTH ❤️ :", c1Health)
    print("")      
    print(c2Name)
    print("c2 HEALTH ❤️ :", c2Health)
    print("")

    if c1Health <= 0:
        print(c1Name, "Has Died!")
        winner = c2Name
        break
    elif c2Health <= 0:
        print(c2Name, "Has Died!")
        winner = c1Name
        break
    else:
        print("And They're both standing for the next round")
        round += 1

time.sleep(3)
os.system("clear")
print("⚔️ 🛡️ BATTLE TIME ⚔️ 🛡️")
print("")
print(winner, "has won in", round, "rounds")
