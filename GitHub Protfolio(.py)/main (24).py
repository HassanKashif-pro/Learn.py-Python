import random, os, time

def generate_character():
    print("⚔ Character Builder ⚔")
    print("")
    name = input("Name Your Legend:\n")
    print("")
    character_type = input("Character Type (Human, Elf, Wizard, Orc, etc.):\n")
    return name, character_type

def generate_health():
    dice_rolls = [random.randint(1, 6) for _ in range(4)]
    health = sum(dice_rolls) * 10
    return health

def generate_strength():
    dice_rolls = [random.randint(1, 6) for _ in range(4)]
    strength = sum(dice_rolls) * 5
    return strength

def show_character_stats(name, character_type, health, strength):
    print(f"\n{name}\nCharacter Type: {character_type}\nHEALTH: {health}\nSTRENGTH: {strength}")
    print("May your name go down in Legend...")

def main():
    os.system("clear")
    while True:
        name, character_type = generate_character()
        health = generate_health()
        strength = generate_strength()
        show_character_stats(name, character_type, health, strength)

        play_again = input("\nDo you want to create another character? (y/n): ").lower()
        if play_again != 'y':
            print("Thank you for playing!")
            break
        os.system("clear")
        time.sleep(1)

if __name__ == "__main__":
    main()
