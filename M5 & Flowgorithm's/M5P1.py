#input phase
quantity = int(input("Enter the quantity of the item:"))

if quantity >= 1000:
    unit_price = 3.00
else:
    unit_price = 5.00

#process phase
extended_price = quantity * unit_price
tax = extended_price * 0.07
total_price = extended_price + tax

#output phase

print("Quantity: {}".format(quantity))
print("Unit Price: ${:.2f}".format(unit_price))
print("Extended Price: ${:.2f}".format(extended_price))
print("Tax (7%): ${:.2f}".format(tax))  
print("Total Price: ${:.2f}".format(total_price))
      



  






