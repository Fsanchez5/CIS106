def calculate_gallons(length, width, height):
    wall_area = 2 * height * (length + width)  
    gallons = (wall_area / 50)
    return gallons

def get_room_data():
    room_data = {} 

    while True:
        room_name = input("\nEnter room name (or type 'done' to finish): ").strip()
        if room_name.lower() == 'done':
            break

        try:
            length = float(input(f"Enter length of {room_name} in feet: "))
            width = float(input(f"Enter width of {room_name} in feet: "))
            height = float(input(f"Enter height of {room_name} in feet: "))
        except ValueError:
            print("Invalid input! Please enter numeric values for dimensions.")
            continue

        gallons_needed = calculate_gallons(length, width, height)
        room_data[room_name] = gallons_needed

    return room_data

def print_paint_requirements(paint_dict):
    print("\nPaint Requirements:")
    print(f"{'Room Name':<15} {'Gallons Needed':<15}")
    print("-" * 30)
    for room, gallons in paint_dict.items():
        print(f"{room:<15} {gallons:<15}")

def main():
    print("Paint Calculator: Enter room dimensions to find gallons needed.")
    rooms_paint = get_room_data()
    print_paint_requirements(rooms_paint)

main()