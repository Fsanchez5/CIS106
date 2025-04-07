def calculate_sales_report(sales):

    if sales > 100000:
        commission = sales * 0.10  
    else:
        commission = sales * 0.05 

    next_year_target = sales * 0.05

   
    return commission, next_year_target

last_name = input("Enter the salesperson's last name: ")
sales = float(input("Enter the total sales: $"))

commission, next_year_target = calculate_sales_report(sales)

print("\nSales Report:")
print(f"Salesperson's Last Name: {last_name}")
print(f"Commission: ${commission:.2f}")
print(f"Next Year's Target: ${next_year_target:.2f}")