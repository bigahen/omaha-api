# Master file to orchestrate processing of data and uploading to RDS

from load_weekly_data import load_weekly_data

class NFLPlayer:
    def __init__(self, name: str, position: str) -> None:
        self.name = name
        self.position = position
    
    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, NFLPlayer):
            return self.name == __o.name
        return False

if __name__ == "__main__":
    weekly_data = load_weekly_data()
    print(weekly_data)

    # Iterate over list and check if any duplicates exist
    duplicate_players = {}
    player_to_position = {}
    all_positions = set()
    for index, row in weekly_data.iterrows():
        name = row['Player']
        position = row['Pos']
        all_positions.add(position)
        player = NFLPlayer(name, position)
        if name in player_to_position and player_to_position[name] != position:
            if name not in duplicate_players:
                positions = [position, player_to_position[name]]
                print(f"Found a duplicate for player named {name} and positions {positions}")
                duplicate_players[name] = positions
            else: 
                current_duplicate_positions = duplicate_players[name]
                if position not in current_duplicate_positions:
                    print(f"Found a new duplicate for player named {name} and position {position}")
                    current_duplicate_positions.append(position)
        else:
            player_to_position[name] = position
    print(duplicate_players)
    print(all_positions)

