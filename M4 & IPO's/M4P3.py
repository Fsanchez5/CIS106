#input phase
meal_total = float(input("Enter the total for the meal: "))

#process phase
tip_15 = meal_total * .15
tip_18 = meal_total * .18
tip_20 = meal_total * .20

total_15 = meal_total + tip_15
total_18 = meal_total + tip_18
total_20 = meal_total + tip_20

#output phase
print("With 15% Tip:")
print(f"Total: {meal_total: .2f}")
print(f"Tip: {tip_15: .2f}")
print(f"Total with Tip: {total_15: .2f}\n")

print("With 18% Tip:")
print(f"Total: {meal_total: .2f}")
print(f"Tip: {tip_18: .2f}")
print(f"Total with Tip: {total_18: .2f}\n")

print("With 20% Tip:")
print(f"Total: {meal_total: .2f}")
print(f"Tip: {tip_20: .2f}")
print(f"Total with Tip: {total_20: .2f}\n")



