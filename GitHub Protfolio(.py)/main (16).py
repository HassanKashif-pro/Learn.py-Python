print("Loan Calculator")
print("")

loan = float(input("Amount of loan you want to take: "))
apr = 5  # Annual Percentage Rate
years = 10

print("")
print(str(loan) + "$" + " over " + str(years) + " years at " + str(apr) + "% APR")
print("")

total_loan = loan  # Initialize total loan amount

for year in range(1, years+1):
    interest = round((apr / 100) * loan, 2)
    loan = round(loan + interest, 2)
    total_loan = round(loan + interest, 2)
    print("Year", year, "is ", str(loan) + "$")

print("\nTotal loan amount after", years, "years:", str(total_loan) + "$")
