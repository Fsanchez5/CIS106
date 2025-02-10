#input phase
first_name = input("Enter your first name: ")
steps_walked = int(input("Enter the number of steps walked in one day: "))

#process phase
calories_burned = steps_walked * 0.25

#output phase
print(f"{first_name},you burned {calories_burned:.2f} calories")