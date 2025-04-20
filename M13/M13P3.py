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

filename = 'players.txt' 
players = load_players(filename)
print_players(players)