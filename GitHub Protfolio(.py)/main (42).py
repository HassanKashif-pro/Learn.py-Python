import random,os

# Generate a list of unique random numbers for the Bingo card
random_numbers = random.sample(range(1, 91), 8)  # Generate 8 unique numbers

# Fill the remaining cell with "BINGO"
center_cell = "BINGO"

# Shuffle the list to ensure randomness
random.shuffle(random_numbers)

# Create the Bingo card layout
My2DList = [[random_numbers.pop(), random_numbers.pop(), random_numbers.pop()],
            [random_numbers.pop(), center_cell, random_numbers.pop()],
            [random_numbers.pop(), random_numbers.pop(), random_numbers.pop()]
           ]

# Calculate the maximum length of any element in the list (including "BINGO")
max_length = max(len(str(number)) for row in My2DList for number in row)

# Print the Bingo card with aligned spacing
for row in My2DList:
    for element in row:
        # Format each element to have a fixed width
        formatted_element = str(element).center(max_length)
        print(formatted_element, end=" | ")  # Adjust the spacing as needed
    print()

# Bingo number input and marking
while True:
    next_number = input("Next Number: ")
    if next_number == "":
        break
    next_number = int(next_number)
    
    # Mark the number as "X" if it exists in the card
    marked = False
    for row in My2DList:
        for i in range(len(row)):
            if row[i] == next_number:
                row[i] = "X"
                marked = True
                break
                
    os.system("clear")
    if marked:
        # Print the updated Bingo card with marked number
        for row in My2DList:
            for element in row:
                formatted_element = str(element).center(max_length)
                print(formatted_element, end=" | ")
    else:
        print(f"Number {next_number} is not on the Bingo card.")
