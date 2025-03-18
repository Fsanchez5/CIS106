def calculate_batting_average(hits, at_bats):
    if at_bats == 0:
        return 0.0  
    return hits / at_bats

def main():
    player_count = 0
    while True:
        try:
            last_name = input("Enter player's last name (or 'stop' to end): ")
            if last_name.lower() == 'stop':
                break
            hits = int(input("Enter number of hits: "))
            at_bats = int(input("Enter number of at-bats: "))
            batting_average = calculate_batting_average(hits, at_bats)
            print(f"Player: {last_name}, Batting Average: {batting_average:.3f}")
            player_count += 1
        except ValueError:
            print("Invalid input. Please enter numerical values for hits and at-bats.")

    print(f"Total number of players entered: {player_count}")