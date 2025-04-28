class Employee:
  def __init__(self, first, last, pay):
      self.first = first
      self.last = last
      self.pay = pay
      self.email = first + '.' + last + '@company.com'

  def fullname(self):
      return '{} {}'.format(self.first, self.last)

  def calculate_bonus(self, rate):
      bonus = self.pay * rate
      return bonus

emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Test", "User", 60000)

print(emp_1.fullname())

bonus_rate = 0.3
bonus = emp_1.calculate_bonus(bonus_rate)
print(f"Bonus for {emp_1.fullname()} at rate {bonus_rate*100}% is: ${bonus}")

