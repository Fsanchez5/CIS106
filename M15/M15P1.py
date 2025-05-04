
class Employee:
    default_bonus_rate = 0.1  

    def __init__(self, first, last, pay):
        self._first = first
        self._last = last
        self._pay = self._validate_pay(pay)
        self._email = f"{first.lower()}.{last.lower()}@company.com"

    def _validate_pay(self, pay):
        if pay < 0:
            raise ValueError("Pay must be a non-negative number.")
        return pay

    def fullname(self):
        return f"{self._first} {self._last}"

    def calculate_bonus(self, rate=None):
        if rate is None:
            rate = self.default_bonus_rate
        if not (0 <= rate <= 1):
            raise ValueError("Bonus rate must be between 0 and 1.")
        return round(self._pay * rate, 2)

    def __str__(self):
        return f"{self.fullname()} - {self._email}"

class Manager(Employee):
    def long_term_bonus(self):
        
        return round(self._pay * 0.4, 2)

emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Test", "User", 60000)

mgr_1 = Manager("Fernanda", "Sanchez", 90000)
mgr_2 = Manager("Dylan", "Bernal", 120000)

print(emp_1)
print(f"Short-term Bonus: ${emp_1.calculate_bonus(0.3)}\n")

print(emp_2)
print(f"Short-term Bonus: ${emp_2.calculate_bonus(0.2)}\n")

print(mgr_1)
print(f"Short-term Bonus: ${mgr_1.calculate_bonus(0.25)}")
print(f"Long-term Bonus: ${mgr_1.long_term_bonus()}\n")

print(mgr_2)
print(f"Short-term Bonus: ${mgr_2.calculate_bonus(0.15)}")
print(f"Long-term Bonus: ${mgr_2.long_term_bonus()}")
