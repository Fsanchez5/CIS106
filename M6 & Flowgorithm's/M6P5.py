last_name = input("Enter employee's last name: ")
salary = float(input("Enter employee's salary: "))
job_level = int(input("Enter employee's job level: "))

if job_level >= 10:
    bonus_rate = 0.25
elif 5 <= job_level <= 9:
    bonus_rate = 0.20
else:
    bonus_rate = 0.10
  
bonus = salary * bonus_rate

print(f"Employee Last Name: {last_name}")
print(f"Bonus Rate: {bonus_rate * 100:.2f}%")
print(f"Bonus Amount: ${bonus:.2f}")


  
