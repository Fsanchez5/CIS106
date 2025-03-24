def compute_forecast(month, sales):

    if month in ["Jan", "Feb", "Mar"]:
        return sales * 1.10
    elif month in ["Apr", "May", "Jun"]:
        return sales * 1.15
    elif month in ["Jul", "Aug", "Sep"]:
        return sales * 1.20
    elif month in ["Oct", "Nov", "Dec"]:
        return sales * 1.25
    else:
        return None

while True:
    user_input = input("Do you want to enter sales data? (Yes/No): ").lower()
    if user_input == "no":
        print("Exiting program.")
        break
    elif user_input == "yes":
        last_name = input("Enter your last name: ")
        month = input("Enter the month (e.g., Jan, Feb, Mar, etc.): ")
        sales = float(input("Enter the sales amount for this month: "))

        next_month_sales = compute_forecast(month, sales)

        if next_month_sales:
            print(f"{last_name}, the forecasted sales for next month are: ${next_month_sales:.2f}")
    else:
        print("Invalid input. Please enter 'Yes' or 'No'.")