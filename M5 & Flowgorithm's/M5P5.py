last_name = input("Enter your last name: ")
num_dependents = int(input("Enter the number of dependents: "))
gross_income = float(input("Enter your gross income: "))


adjusted_gross_income = gross_income - (num_dependents * 12000)

if adjusted_gross_income > 50000:
    tax_rate = 0.20
else:
  tax_rate = 0.10

income_tax = adjusted_gross_income * tax_rate

if income_tax <0:
  income_tax = 100

print("Last Name: {}".format(last_name))
print("Gross Income: ${:.2f}".format(gross_income))
print("Number of Dependents: {}".format(num_dependents))
print("Adjusted Gross Income: ${:.2f}".format(adjusted_gross_income))
print("Income Tax: ${:.2f}".format(income_tax))
  
  