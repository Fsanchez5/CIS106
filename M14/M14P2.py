class Student:
    def __init__(self, first_name, last_name, district_code, enrolled_credits):
        self.first_name = first_name
        self.last_name = last_name
        self.district_code = district_code.upper()
        self.enrolled_credits = enrolled_credits

    def compute_tuition(self):
        if self.district_code == 'I':
            rate_per_credit = 250.00
        else:
            rate_per_credit = 500.00
        return self.enrolled_credits * rate_per_credit

    def display_info(self):
        tuition = self.compute_tuition()
        print(f"Student: {self.first_name} {self.last_name}")
        print(f"District Code: {self.district_code}")
        print(f"Enrolled Credits: {self.enrolled_credits}")
        print(f"Tuition Owed: ${tuition:.2f}")


# Test the Student class
student1 = Student("Fernanda", "Sanchez", "I", 12)
student2 = Student("Dylan", "Bernal", "O", 15)

student1.display_info()
print("-" * 30)
student2.display_info()