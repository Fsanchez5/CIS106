def get_pay_rate(job_code):
    rates = {'L': 25, 'A': 30, 'J': 50}
    return rates.get(job_code.upper(), 0)  

def calculate_gross_pay(hours_worked, pay_rate):
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        return (40 * pay_rate) + (overtime_hours * pay_rate * 1.5)
    return hours_worked * pay_rate

def main():
    total_gross_pay = 0.0
    while True:
        try:
            last_name = input("Enter employee's last name (or 'stop' to end): ")
            if last_name.lower() == 'stop':
                break
            job_code = input("Enter job code (L, A, J): ")
            hours_worked = float(input("Enter hours worked: "))
            pay_rate = get_pay_rate(job_code)
            if pay_rate == 0:
                print("Invalid job code. Please enter L, A, or J.")
                continue
            gross_pay = calculate_gross_pay(hours_worked, pay_rate)
            print(f"Employee: {last_name}, Gross Pay: ${gross_pay:.2f}")
            total_gross_pay += gross_pay
        except ValueError:
            print("Invalid input. Please enter numerical values for hours worked.")

    print(f"Total gross pay for all employees: ${total_gross_pay:.2f}")
