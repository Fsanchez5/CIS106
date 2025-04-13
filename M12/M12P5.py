def load_players(filename):
    names = []
    averages = []

    with open(filename, 'r') as file:
        for line in file:
            name, avg = line.strip().split()
            names.append(name)
            averages.append(float(avg))

    return names, averages

def display_players(names, averages):
    print("\nPlayer List:")
    for i in range(len(names)):
        print(f"{names[i]} - Batting Average: {averages[i]:.3f}")
    print()

def search_player(names, averages, search_name):
    found = False
    for i in range(len(names)):
        if names[i].lower() == search_name.lower():
            print(f"{names[i]}'s Batting Average: {averages[i]:.3f}")
            found = True
            break
    if not found:
        print("Name not found.")

def main():
    filename = "players.txt"
    names, averages = load_players(filename)

    display_players(names, averages)

    while True:
        search_name = input("Enter a player's last name to search (or type 'exit' to quit): ")
        if search_name.lower() == "exit":
            print("Goodbye!")
            break
        search_player(names, averages, search_name)

main()
