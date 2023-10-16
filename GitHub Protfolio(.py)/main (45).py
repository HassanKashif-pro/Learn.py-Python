f = open("python.txt", "a+")

while True:
    print("HIGH SCORE TABLE")
    print()
    initial = input("INITIAL> ").upper()
    SCORE = int(input("SCORE> "))
    print("")
    
    f.write(f"{initial}\t{SCORE}\n")  # Write the initial and score to the file
    
    print("ADDED!")
    another = input("Add Another? (y/n): ").strip().capitalize()
    
    if another != "Y":
        break
f.close()  # Close the file when done
