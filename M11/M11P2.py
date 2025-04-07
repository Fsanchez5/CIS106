def calculate_scores(score1, score2, score3):
    total_points = score1 + score2 + score3

    average_score = total_points / 3

    return total_points, average_score

last_name = input("Enter the student's last name: ")
score1 = float(input("Enter the first exam score: "))
score2 = float(input("Enter the second exam score: "))
score3 = float(input("Enter the third exam score: "))

total_points, average_score = calculate_scores(score1, score2, score3)

print("\nStudent's Summary:")
print(f"Last Name: {last_name}")
print(f"Total Points: {total_points:.2f}")
print(f"Average Exam Score: {average_score:.2f}")