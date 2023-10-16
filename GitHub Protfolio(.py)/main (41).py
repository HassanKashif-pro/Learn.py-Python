import random

# Generate a list of unique random numbers for the Bingo card
random_numbers = random.sample(range(1, 91), 8)  # Generate 8 unique numbers

# Fill the remaining cell with "BINGO"
center_cell = "BINGO"

# Shuffle the list to ensure randomness
random.shuffle(random_numbers)

# Create the Bingo card layout
My2DList = [[random_numbers.pop(),"|", random_numbers.pop(),"|", random_numbers.pop()],
            [random_numbers.pop(),"|", center_cell,"|", random_numbers.pop()],
            [random_numbers.pop(),"|", random_numbers.pop(),"|", random_numbers.pop()]
           ]

# Calculate the maximum length of any element in the list (including "BINGO")
max_length = max(len(str(number)) for row in My2DList for number in row)
My2DList.sort()
# Print the Bingo card with aligned spacing
for row in My2DList:
    for element in row:
        # Format each element to have a fixed width
        formatted_element = str(element).center(max_length)
        print(formatted_element, end="  ")  # Adjust the spacing as needed
    print()
