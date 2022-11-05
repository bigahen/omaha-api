
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


# Special rules for duplicate names 

"""
Tony Carter 
    year > 2001 = new player 

Chris Johnson 
    year > 2005 = new player 

Dexter Jackson
    year > 2003 = new player

Levi Brown 
    year > 2008 = new player

Jimmy Smith
    year > 2005 = new player

Marvin Jones 
    year > 2001 = new player 

Josh Norman
    year > 2003 = new player

Chris Davis
    year > 2008 = new player

Kyle Williams 
    year > 2013 = new player

D.J. Moore
    year > 2012 = new player
    
Chris Jones
    TODO - pull all the data and figure this one out lol

Michael Thomas
    TODO - pull all data and confirm, but I believe not NOR player is a seperate person 

Josh Harris
    year > 2014 = new player

Quincy Wilson
    year > 2006 = new player

Nick Williams
    year > 2018 = new player

Josh Allen
    TODO - figure this one out but probably it will be QB vs DE

Daniel Thomas
    year > 2014 = new player

Kenny Moore
    year > 2010 = new player

John Simon
    year > 2003 = new player

Brandon Jones
    year > 2009 = new player

Brandon Williams
    TODO - multiple, figure this one out 

Kendall Lamm
    year > 2015 = new player

Kyle Nelson
    year > 2013 = new player

Austin Johnson 
    year > 2015 = new player

Greg Little
    year > 2014 = new player

Nick Harris
    year > 2011 = new player

Lamar Jackson
    RAV vs NYJ

J.R. Reed
    year > 2007 = new player

Tony Brown
    WAS vs CIN

Bobby Brown
    year > 2000 new player 

"""