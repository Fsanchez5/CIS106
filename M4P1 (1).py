#input phase
  
exam1 = float(input("Enter exam 1 score: "))
exam2 = float(input("Enter exam 2 score: "))
weight1 = 0.6 # 60%
weight2 = 0.4 # 40%

#process phase
total_score = (exam1 * weight1) + (exam2 * weight2)

#output phase
print(f"Total weighted score: {total_score: .2f}")
