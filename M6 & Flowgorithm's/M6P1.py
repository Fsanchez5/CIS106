quantity = int(input("Enter the quantity of widgets:"))

if quantity > 10000:
  price = 10
elif quantity >= 5000:
  price = 20
else:
  price = 30

extended_price = quantity * price
tax = extended_price * 0.07
total = extended_price + tax

print(f"Quantity: {quantity}")
print(f"Price per widget: ${price}")
print(f"Extended price: ${extended_price:.2f}")
print(f"Tax (7%): ${tax:.2f}")
print(f"Total: ${total:.2f}")
  