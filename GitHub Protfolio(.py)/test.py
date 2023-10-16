import random

def rollDice(side):
    result = random.randint(1, side)
    return result
    print(result)
    rollDice()