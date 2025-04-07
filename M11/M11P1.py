def calculate_discount(quantity, price, discount_rate):
    total_price = quantity * price

    discount_amount = total_price * (discount_rate / 100)

    discounted_price = total_price - discount_amount

    return discount_amount, discounted_price

quantity = int(input("Enter the quantity: "))
price = float(input("Enter the price per item: "))
discount_rate = float(input("Enter the discount rate (in %): "))

discount_amount, discounted_price = calculate_discount(quantity, price, discount_rate)

print("\nSummary:")
print(f"Quantity: {quantity}")
print(f"Price per item: ${price:.2f}")
print(f"Discount rate: {discount_rate}%")
print(f"Discount amount: ${discount_amount:.2f}")
print(f"Discounted price: ${discounted_price:.2f}")