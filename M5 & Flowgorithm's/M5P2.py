#input phase
item = input("Enter the item (A or B):").strip().upper()
quantity = int(input("Enter the quantity:"))

if item == "A":
    unit_price = 10.00
else:
    unit_price = 20.00

#process phase
extended_price = unit_price * quantity

#output phase
print("Item {}".format(item))
print("Unit Price ${:.2f}".format(unit_price))
print("Extended Price ${:.2f}".format(extended_price))

