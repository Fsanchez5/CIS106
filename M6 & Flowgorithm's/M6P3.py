principal = float(input("Enter the principal amount of the CD :"))
years = int(input("Enter the number of years the CD will mature :"))

if principal > 100000 and years == 5:
    interest_rate = 0.06  

elif 50000 <= principal <= 100000 and years == 10:
    interest_rate = 0.05

elif 50000 <= principal <= 100000 and years == 5:
    interest_rate = 0.04

else:
    interest_rate = 0.02

first_year_interest= principal * interest_rate

print(f"Principal Amount: ${principal:,.2f}")
print(f"Interest Rate: {interest_rate * 100:.2f}%")
print(f"First Year Interest: ${first_year_interest:,.2f}")