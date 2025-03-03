response = input("Do you want to enter an order? (Yes/No): ").strip().lower()


total_discount = 0  


while response == "yes":
   
    quantity = int(input("Enter quantity of the item: "))
    price = float(input("Enter price per item: "))

  
    extended_price = quantity * price

  
    if extended_price > 10000:
        discount_rate = 0.25  
    else:
        discount_rate = 0.10  
    discount_amount = extended_price * discount_rate
    total_price = extended_price - discount_amount

   
    print(f"\nExtended Price: ${extended_price:.2f}")
    print(f"Discount Amount: ${discount_amount:.2f}")
    print(f"Total Price After Discount: ${total_price:.2f}\n")

   
    total_discount += discount_amount

    
    response = input("Do you want to enter another order? (Yes/No): ").strip().lower()


print(f"\nTotal Discount on All Orders: ${total_discount:.2f}")