print("30 Days Down - What do you think?")
print("")

for i in range(1, 31):
    Thoughts = input(f"Day {i}:".ljust(8))
    print("")
    print(f"{f'You thought Day {i} was {Thoughts}'.center(50)}")
    print("")