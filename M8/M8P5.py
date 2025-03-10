
def compute_tuition(district_code, credits):
   
    cost_per_credit = 250.00 if district_code == "I" else 500.00
    return credits * cost_per_credit

def process_student_data(filename):
   
    total_tuition = 0
    student_count = 0

    try:
        with open(filename, "r") as file:
            lines = file.readlines()

        print(f"{'Last Name':<10} {'Credits':<10} {'Tuition Owed':<15}")
        print("-" * 35)

        for i in range(0, len(lines), 3):  
            last_name = lines[i].strip()
            district_code = lines[i + 1].strip().upper()  
            credits = int(lines[i + 2].strip())
            tuition = compute_tuition(district_code, credits)

            print(f"{last_name:<10} {credits:<10} ${tuition:<15,.2f}")

            total_tuition += tuition
            student_count += 1

        print("\nTotal Tuition Owed: ${:,.2f}".format(total_tuition))
        print("Total Number of Students:", student_count)

    except FileNotFoundError:
        print("Error: File not found. Please make sure 'students.txt' exists.")
    except Exception as e:
        print(f"An error occurred: {e}")
