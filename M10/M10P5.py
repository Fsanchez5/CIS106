def calculate_assessed_value(county, market_value):
    if county == "Cook":
        assessed_value_percent = 0.90
    elif county == "DuPage":
        assessed_value_percent = 0.80
    elif county == "McHenry":
        assessed_value_percent = 0.75
    elif county == "Kane":
        assessed_value_percent = 0.60
    else:
        assessed_value_percent = 0.70  

    assessed_value = market_value * assessed_value_percent
    return assessed_value

total_market_value = 0
total_assessed_value = 0

while True:
    user_input = input("Do you want to enter home data? (Yes/No): ").strip().lower()

    if user_input == "no":
        print("Exiting the program.")
        break  

    elif user_input == "yes":
       
        county = input("Enter the county (e.g., Cook, DuPage, McHenry, Kane): ").strip()
        market_value = float(input("Enter the market value of the home: ").strip())
        assessed_value = calculate_assessed_value(county, market_value)

        total_market_value += market_value
        total_assessed_value += assessed_value

        print(f"Assessed value for the home in {county}: ${assessed_value:.2f}")

    else:
        print("Invalid input. Please enter 'Yes' or 'No'.")
print(f"\nTotal market value of all homes: ${total_market_value:.2f}")
print(f"Total assessed value of all homes: ${total_assessed_value:.2f}")