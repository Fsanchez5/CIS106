total = 0
tax = 0

def calculate_total_and_tax(quantity, unit_price):
    global total, tax  
 
    total = quantity * unit_price
    
    tax = total * 0.07

quantity = int(input("Enter the quantity of the item: "))
unit_price = float(input("Enter the unit price of the item: $"))

calculate_total_and_tax(quantity, unit_price)

print(f"\nTotal: ${total:.2f}")
print(f"Tax (7%): ${tax:.2f}")