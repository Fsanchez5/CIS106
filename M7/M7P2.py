#input phase

fixed_costs = float(input("Enter the fixed costs: "))
price_per_unit = float(input("Enter price per unit:"))
cost_per_unit = float(input("Enter cost per unit:"))

#process phase
break_even = fixed_costs / (price_per_unit - cost_per_unit)

#output phase
print(f"You need to sell {break_even:.2f} units to break even.")
