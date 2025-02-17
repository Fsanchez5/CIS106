#input phase
num_books = int(input("Enter the number of books to order:"))
cost_per_book = float(input("Enter the cost per book:"))

#process phase
order_total = num_books * cost_per_book

if order_total > 50.00:
    shipping_charge = 0.00

else:
    shipping_charge = 25.00

#output phase
print("Order Total: ${:.2f}".format(order_total))
print("Shipping Charge: ${:.2f}".format(shipping_charge))
    
