
def clean_table(weekly_data):
    for index, row in weekly_data.iterrows():
        name = row['Player']
        position = row['Pos']
        
        cleaned_position = get_clean_position(name, position)
        if position != cleaned_position:
            weekly_data.at[index, 'Pos'] = cleaned_position

def get_clean_position(name, position):
    if str(position) == 'nan' or str(position) == '0':
        if name == 'Jonathan Quinn': 
            return "QB"
        elif name == "Chad Johnson":
            return "WR"
        elif name == "Tytus Howard":
            return "OT"
        elif name == "Tremon Smith":
            return "CB"
        elif name == "Devaroe Lawrence":
            return "DT"
        elif name == "Kevan Barlow":
            return "RB" 
        elif name == "Justin McCareins":
            return "WR" 
        elif name == "Randy Fasani":
            return "QB" 
        elif name == "Ty Johnson":
            return "RB" 
        elif name == "Az-Zahir Hakim":
            return "WR" 
        elif name == "Sean Ryan":
            return "TE" 
        elif name == "Reagan Maui'a":
            return "FB" 
        elif name == "Terry Jones":
            return "TE" 
        elif name == "Benny Snell Jr.":
            return "RB"
        elif name == "Teyo Johnson":
            return "TE" 
        elif name == "Desmond Clark":
            return "TE" 
        elif name == "Mike Anderson":
            return "RB" 
        elif name == "Darren McFadden":
            return "RB" 
        elif name == "Andre' Davis":
            return "WR" 
        elif name == "Quincy Williams":
            return "LB" 
        elif name == "David Dunn":
            return "WR" 
        elif name == "Kolby Smith":
            return "RB" 
        elif name == "Brad Smith":
            return "WR" 
        elif name == "Devale Ellis":
            return "WR"
        elif name == "Tony Carter":
            return "CB" 
        elif name == "Brian Calhoun":
            return "RB" 
        elif name == "Musa Smith":
            return "RB" 
        elif name == "Jalen Thompson":
            return "S" 
        elif name == "Virgil Green":
            return "TE" 
        elif name == "James Davis":
            return "RB" 
        elif name == "Michael Davis":
            return "CB" 
        elif name == "Tae Crowder":
            return "LB" 
        elif name == "Aaron Dobson":
            return "WR"
        elif name == "Andre Johnson":
            return "WR" 
        elif name == "Wayne Gallman":
            return "RB"
        else: 
            print(f"Missing cleaning mapping for name={name}, using original position")
            return position
    else:
        return position