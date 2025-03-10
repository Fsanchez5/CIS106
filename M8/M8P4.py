
def process_items(filename):
  
    total_extended_price = 0
    order_count = 0

    try:
        with open(filename, "r") as file:
            lines = file.readlines()

        print(f"{'Item':<10} {'Quantity':<10} {'Price':<10} {'Extended Price':<15}")
        print("-" * 50)

        for i in range(0, len(lines), 3): 
            item = lines[i].strip()
            quantity = int(lines[i + 1].strip())
            price = float(lines[i + 2].strip())
            extended_price = quantity * price

            print(f"{item:<10} {quantity:<10} ${price:<10.2f} ${extended_price:<15,.2f}")

            total_extended_price += extended_price
            order_count += 1

       
        average_order = total_extended_price / order_count if order_count > 0 else 0

        print("\nTotal Extended Price: ${:,.2f}".format(total_extended_price))
        print("Total Number of Orders:", order_count)
        print("Average Order Value: ${:,.2f}".format(average_order))

    except FileNotFoundError:
        print("Error: File not found. Please make sure 'items.txt' exists.")
    except Exception as e:
        print(f"An error occurred: {e}")