def calculate_total(quantity, price):
    total = quantity * price
    if total > 100000.00: 
        total *= 0.9
    return total

def main():
    total_extended_price = 0.0
    while True:
        try:
            quantity = int(input("Enter quantity (or 0 to stop): "))
            if quantity == 0:
                break
            price = float(input("Enter price per unit: "))
            total = calculate_total(quantity, price)
            print(f"Quantity: {quantity}, Price: ${price:.2f}, Total: ${total:.2f}")
            total_extended_price += total
        except ValueError:
            print("Invalid input. Please enter numerical values.")

    print(f"Total Extended Price: ${total_extended_price:.2f}")