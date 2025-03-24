def compute_wall_square_footage(length, width, height):
    return 2 * length * height + 2 * width * height

def compute_gallons_needed(area):
    return area / 50

while True:
    user_input = input("Do you want to enter room dimensions? (Yes/No): ").lower()

    if user_input == "no":
        print("Exiting program.")
        break
    elif user_input == "yes":
        length = float(input("Enter the length of the room (in feet): "))
        width = float(input("Enter the width of the room (in feet): "))
        height = float(input("Enter the height of the room (in feet): "))

        
        wall_area = compute_wall_square_footage(length, width, height)
        gallons_for_walls = compute_gallons_needed(wall_area)

        ceiling_area = length * width
        gallons_for_ceiling_floor = compute_gallons_needed(ceiling_area)

        print(f"Gallons for walls: {gallons_for_walls:.2f}")
        print(f"Gallons for ceiling or floor: {gallons_for_ceiling_floor:.2f}")
    else:
        print("Invalid input. Please enter 'Yes' or 'No'.")