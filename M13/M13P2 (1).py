students = {
  "Dylan": [90, 89, 93],
  "Fernanda": [95,87, 91],
  "Alexxa": [71, 80, 79],
  "Mariana": [83, 70, 81],
  "Bianca": [86, 90, 89]
}

def calculate_student_averages(student_dict):
  averages = []
  for name, grades in student_dict.items():
      avg = sum(grades) / len(grades)
      averages.append([name, avg])
  return averages

def calculate_class_grade_averages(student_dict):
  grade_totals = [0, 0, 0]
  num_students = len(student_dict)

  for grades in student_dict.values():
      for i in range(3):
          grade_totals[i] += grades[i]

  return [total / num_students for total in grade_totals]

student_averages = calculate_student_averages(students)

class_grade_averages = calculate_class_grade_averages(students)

print(f"{'Student Name':<15} {'Average Grade':<15}")
print("-" * 30)
for name, avg in student_averages:
  print(f"{name:<15} {avg:<.2f}")
print("-" * 30)

print("Class Average for Each Grade:")
print(f"{'Grade 1':<10} {'Grade 2':<10} {'Grade 3':<10}")
print(f"{class_grade_averages[0]:<10.2f} {class_grade_averages[1]:<10.2f} {class_grade_averages[2]:<10.2f}")