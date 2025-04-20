def load_players(filename):
    player_dict = {}
    with open(filename, 'r') as file:
        for line in file:
            name, avg = line.strip().split()
            player_dict[name] = float(avg)
    return player_dict

def print_players(player_dict):
    print(f"{'Player Name':<15} {'Batting Average':<15}")
    print("-" * 30)
    for name, avg in player_dict.items():
        print(f"{name:<15} {avg:<.3f}")

def lookup_players(player_dict):
    while True:
        search_name = input("\nEnter a player's last name to look up (or type 'exit' to quit): ").strip()
        if search_name.lower() == 'exit':
            print("Goodbye!")
            break
        elif search_name in player_dict:
            print(f"{search_name} has a batting average of {player_dict[search_name]:.3f}")
        else:
            print(f"{search_name} not found in player list.")

filename = 'players.txt'
players = load_players(filename)
print_players(players)
lookup_players(players)