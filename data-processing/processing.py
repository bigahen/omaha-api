# Master file to orchestrate processing of data and uploading to RDS

from load_weekly_data import load_weekly_data, load_weekly_data_from_file
from data_positions import DEFENSIVE_POSITIONS, OFFENSIVE_POSITIONS, OFFENSIVE_LINE_POSITIONS, OTHER_POSITIONS, SPECIAL_TEAMS_POSITIONS

class NFLPlayer:
    def __init__(self, name: str, position: str, team_abr: str) -> None:
        self.name = name
        self.position = position
        self.team_abr = team_abr
    
    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, NFLPlayer):
            return self.name == __o.name
        return False
    
    def get_generic_position(self):
        return get_generic_position_mapping(self.position)

def get_generic_position_mapping(actual_pos: str):
    if actual_pos in DEFENSIVE_POSITIONS:
        return "DEF/OL"
    elif actual_pos in OFFENSIVE_POSITIONS:
        return "OFF"
    elif actual_pos in OFFENSIVE_LINE_POSITIONS:
        return "DEF/OL"
    elif actual_pos in SPECIAL_TEAMS_POSITIONS:
        return "SPEC"
    elif str(actual_pos) in OTHER_POSITIONS: # sometimes NaN is getting passed in here
        return "OTHER"
    else:
        print(f"Postion mapping for {actual_pos} is missing!")
        return "OTHER_MISSING"

if __name__ == "__main__":
    weekly_data = load_weekly_data()
    # print(weekly_data)

    # Iterate over list and check if any duplicates exist
    duplicate_players = {}
    player_name_to_nflplayer = {}
    unmapped_players = set()
    for index, row in weekly_data.iterrows():
        name = row['Player']
        position = row['Pos']
        team = row['Tm']
        player = NFLPlayer(name, position, team)
        if player.get_generic_position() == "OTHER":
            print(f"Player named {name} played weird position {position}")
            unmapped_players.add((name, position))

        if name in player_name_to_nflplayer:
            nflplayer = player_name_to_nflplayer[name]
            if player.get_generic_position() != nflplayer.get_generic_position() and player.team_abr != nflplayer.team_abr:
                if name not in duplicate_players:
                    positions = [player.get_generic_position(), nflplayer.get_generic_position()]
                    duplicate_players[name] = positions
                else: 
                    current_duplicate_positions = duplicate_players[name]
                    if player.get_generic_position() not in current_duplicate_positions:
                        current_duplicate_positions.append(player.get_generic_position())
                        print(f"Found a new duplicate for player named {name} and position {current_duplicate_positions}")
        else:
            player_name_to_nflplayer[name] = player
    print(len(duplicate_players))
    print(duplicate_players)
    print(f"Unmapped Players={unmapped_players}")

