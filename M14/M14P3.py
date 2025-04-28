class Student:
    tuition_rates = {
        'I': 250.00,  
        'O': 500.00,  
        'X': 800.00,  
        'G': 250.00   
    }

    def __init__(self, first_name, last_name, district_code, enrolled_credits):
        self.first_name = first_name
        self.last_name = last_name
        self.district_code = district_code.upper()
        self.enrolled_credits = enrolled_credits

    def compute_tuition(self):
        
        rate_per_credit = Student.tuition_rates.get(self.district_code, 500.00)
        return self.enrolled_credits * rate_per_credit

    def display_info(self):
        tuition = self.compute_tuition()
        print(f"Student: {self.first_name} {self.last_name}")
        print(f"District Code: {self.district_code}")
        print(f"Enrolled Credits: {self.enrolled_credits}")
        print(f"Tuition Owed: ${tuition:.2f}")
        print("-" * 40)

student1 = Student("Fernanda", "Sanchez", "I", 12)   
student2 = Student("Dylan", "Bernal", "O", 15)    
student3 = Student("Alexxa", "Sosa", "X", 9)   
student4 = Student("Mariana", "Cisneros", "G", 6)     

student1.display_info()
student2.display_info()
student3.display_info()
student4.display_info()