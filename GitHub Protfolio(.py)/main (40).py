def color_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

print("👾 MokéBeast - The Non-copyright Generic Beast Battle Game🤖")
print()

Beast_Name = input("Type your Beast Name: ")
print()

Beast_Type = input("Type your Beast Type (fire, water, wind, lightning, ghost, fairy): ").lower()
print()

Special_move = input("Input Your Beast's Special Move: ")
print()

Starter_Health = input("Input Your Beast's Health: ")
print()

Starter_Mp = input("Input Your Beast's MP: ")
print()

print()
Beast_Prepared = {
    "Beast Name": Beast_Name,
    "Beast Type": Beast_Type,
    "Special Move": Special_move,
    "Starter Health": Starter_Health,
    "Starter MP": Starter_Mp
}

type_colors = {
    "fire": "31",       # Red
    "water": "34",      # Blue
    "wind": "90",       # Grey
    "lightning": "33",  # Yellow
    "ghost": "30",      # Black
    "fairy": "95"       # Pink
}

attribute_colors = {
    "Starter Health": "32",  # Green
    "Starter MP": "34"       # Blue
}

if Beast_Type in type_colors:
    colored_type = color_text(Beast_Type, type_colors[Beast_Type])
    colored_name = color_text(Beast_Name, type_colors[Beast_Type]) 
    colored_attack = color_text(Special_move, type_colors[Beast_Type]) 
    Beast_Prepared["Beast Name"] = colored_name
    Beast_Prepared["Beast Type"] = colored_type
    Beast_Prepared["Special Move"] = colored_attack
for key, value in Beast_Prepared.items():
    if key in attribute_colors:
        colored_value = color_text(value, attribute_colors[key])
        print(f"{key}: {colored_value}")
    else:
        print(f"{key}: {value}")
