def calculate_scores(score1, score2, score3, handicap):
    average_score = (score1 + score2 + score3) / 3

    average_score_with_handicap = average_score + handicap

    return average_score, average_score_with_handicap
    
last_name = input("Enter the bowler's last name: ")
score1 = int(input("Enter the first game score: "))
score2 = int(input("Enter the second game score: "))
score3 = int(input("Enter the third game score: "))
handicap = int(input("Enter the bowler's handicap: "))

average_score, average_score_with_handicap = calculate_scores(score1, score2, score3, handicap)

print("\nBowler's Summary:")
print(f"Last Name: {last_name}")
print(f"Average Score: {average_score:.2f}")
print(f"Average Score with Handicap: {average_score_with_handicap:.2f}")