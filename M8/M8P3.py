
def calculate_bonus(salary):
  
  if salary >= 100000:
      rate = 0.20
  elif salary == 50000:
      rate = 0.15
  else:
      rate = 0.10
  return salary * rate

def process_employee_data(filename):
 
  total_bonus = 0
  employee_count = 0

  try:
      with open(filename, "r") as file:
          lines = file.readlines()

      print(f"{'Last Name':<10} {'Salary':<10} {'Bonus':<10}")
      print("-" * 30)

      for i in range(0, len(lines), 2): 
          last_name = lines[i].strip()
          salary = float(lines[i + 1].strip())
          bonus = calculate_bonus(salary)

          print(f"{last_name:<10} ${salary:,.2f}  ${bonus:,.2f}")

          total_bonus += bonus
          employee_count += 1

      print("\nTotal Bonuses Paid: ${:,.2f}".format(total_bonus))
      print("Total Employees Processed:", employee_count)

  except FileNotFoundError:
      print("Error: File not found. Please make sure 'employees.txt' exists.")
  except Exception as e:
      print(f"An error occurred: {e}")