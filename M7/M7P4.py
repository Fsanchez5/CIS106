
response = input("Do you want to enter employee data? (Yes/No): ").strip().lower()


total_gross_pay = 0
employee_count = 0


while response == "yes":
   
    last_name = input("Enter employee's last name: ")
    hours_worked = float(input("Enter hours worked: "))
    pay_rate = float(input("Enter hourly pay rate: "))


    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        gross_pay = (40 * pay_rate) + (overtime_hours * pay_rate * 1.5)
    else:
        gross_pay = hours_worked * pay_rate

   
    print(f"{last_name}'s Gross Pay: ${gross_pay:.2f}")

  
    total_gross_pay += gross_pay
    employee_count += 1

 
    response = input("Do you want to enter another employee? (Yes/No): ").strip().lower()


if employee_count > 0:
    average_pay = total_gross_pay / employee_count
    print(f"\nTotal Employees: {employee_count}")
    print(f"Total Gross Pay: ${total_gross_pay:.2f}")
    print(f"Average Pay: ${average_pay:.2f}")
else:
    print("\nNo employee data was entered.")