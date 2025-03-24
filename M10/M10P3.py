def calculate_price(msrp, make, model, ev_code):
  
    if make == "Honda" and model == "Accord":
        discount = 0.10  
    elif make == "Toyota" and model == "Rav4":
        discount = 0.15  
    elif ev_code == "Y":
        discount = 0.30 
    else:
        discount = 0.05  

    discounted_price = msrp * (1 - discount)

    total_price = discounted_price * 1.07

    return total_price, msrp

total_msrp = 0
total_sales = 0

while True:
    user_input = input("Do you want to enter car data? (Yes/No): ").lower()

    if user_input == "no":
        print("Exiting the program.")
        break

    elif user_input == "yes":
        make = input("Enter the car make (e.g., Honda, Toyota): ").strip()
        model = input("Enter the car model (e.g., Accord, Rav4): ").strip()
        ev_code = input("Is this an electric vehicle? (Y/N): ").strip().upper()
        msrp = float(input("Enter the MSRP (price) of the car: ").strip())

        final_price, car_msrp = calculate_price(msrp, make, model, ev_code)

        total_msrp += car_msrp
        total_sales += final_price

        print(f"Total price for {make} {model}: ${final_price:.2f}")

    else:
        print("Please enter 'Yes' or 'No'.")

print(f"\nTotal MSRP of all cars: ${total_msrp:.2f}")
print(f"Total sales price (after discount and tax): ${total_sales:.2f}")