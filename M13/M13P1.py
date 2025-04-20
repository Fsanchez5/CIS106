students = {
  "Dylan": 90,
  "Fernanda": 95,
  "Alexxa": 71,
  "Mariana": 83,
  "Bianca": 86
}

print(f"{'Student Name':<15} {'Grade':<5}")
print("-" * 22)

total = 0

for name, grade in students.items():
  print(f"{name:<15} {grade:<5}")
  total += grade

average = total / len(students)
print("-" * 22)
print(f"{'Class Average':<15} {average:.2f}")