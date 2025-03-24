def calculate_ticket_price(miles):
  if miles >= 30:
      return 12  
  elif 20 <= miles <= 29:
      return 10  
  elif 10 <= miles <= 19:
      return 8  
  else:
      return 5  

total_ticket_price = 0

while True:
  user_input = input("Do you want to enter train data? (Yes/No): ").strip().lower()

  if user_input == "no":
      print("Exiting the program.")
      break  
  elif user_input == "yes":
      last_name = input("Enter your last name: ").strip()
      miles = int(input("Enter the miles from downtown Chicago: ").strip())

      ticket_price = calculate_ticket_price(miles)
      total_ticket_price += ticket_price

      print(f"{last_name}, your ticket price is: ${ticket_price}")
  else:
      print("Invalid input. Please enter 'Yes' or 'No'.")

print(f"\nTotal ticket price for all entries: ${total_ticket_price}")