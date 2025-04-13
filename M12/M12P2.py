last_names = ["Sanchez", "Sosa", "Bernal", "Cisneros", "Rodriguez", 
  "Chavez", "Garcia", "Perez", "Gomez", "Bonilla"]
names = ["Fernanda", "Alexxa", "Dylan", "Mariana", "Paula", "Blanca", "Andres", "Julian", "Rebecca", "Paige"]
exam_scores = [60, 92, 75, 85, 90, 70, 55, 89, 99, 91]
# Function to display names with scores
def display_names_and_scores(names, scores):
    print("Names and Scores:")
    for i in range(len(names)):
        print(f"{names[i]} - Score: {scores[i]}")
    print()
# Function to display names and scores in reverse
def display_names_and_scores_reverse(names, scores):
    print("Names and Scores (Reversed):")
    for i in range(len(names)-1, -1, -1):
        print(f"{names[i]} - Score: {scores[i]}")
    print()
# Main code
display_names_and_scores(names, exam_scores)
display_names_and_scores_reverse(names, exam_scores)