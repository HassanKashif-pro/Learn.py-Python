import csv

total = 0

with open("Day54Totals.csv") as file:
    reader = csv.DictReader(file)

    for row in reader:
        cost = float(row["Cost"])
        quantity = int(row["Quantity"])
        row_total = cost * quantity
        round(print(f"Cost: {cost}, Quantity: {quantity}, Row Total: {row_total}", 2))
        print(", ".join(row))
        total += row_total

round(print(f"Total: {total}"),2)
