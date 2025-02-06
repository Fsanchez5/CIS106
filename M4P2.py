#input phase

purchase_price = float(input("Enter the purchase per share:"))
current_price = float(input("Enter the current stock price:"))
quantity = int(input("Enter the quantity of stock:"))

#process phase
value_change = (current_price - purchase_price) * quantity

#output phase
print(f"The value of the stock has changed by ${value_change: .2f}")
