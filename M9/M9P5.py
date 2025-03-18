def calculate_tuition(credit_hours, district_code):
    rates = {'I': 250, 'O': 550}
    return credit_hours * rates.get(district_code.upper(), 0)  

def main():
    total_tuition = 0.0
    while True:
        try:
            last_name = input("Enter student's last name (or 'stop' to end): ")
            if last_name.lower() == 'stop':
                break
            credit_hours = int(input("Enter credit hours: "))
            district_code = input("Enter district code (I for In-District, O for Out-of-District): ")
            tuition = calculate_tuition(credit_hours, district_code)
            if tuition == 0:
                print("Invalid district code. Please enter I or O.")
                continue
            print(f"Student: {last_name}, Tuition Owed: ${tuition:.2f}")
            total_tuition += tuition
        except ValueError:
            print("Invalid input. Please enter numerical values for credit hours.")

    print(f"Total tuition owed for all students: ${total_tuition:.2f}")