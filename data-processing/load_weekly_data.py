# File to load weekly data from local files into memory, update your relative path as needed
import os
import pandas as pd
import uuid
from clean_data import clean_table

RELATIVE_DATA_PATH = './../fantasydatapros-data/weekly/' # Relative data path for the weekly fantasy data folder

def load_all_tables():
    tables = []
    # Open all the files in each directory
    for root, dirs, files in os.walk(RELATIVE_DATA_PATH):
        for file in files:
            week = file.replace("week", "").replace(".csv", "")
            year = root.replace(RELATIVE_DATA_PATH, "")
            file_path = os.path.join(root, file)
            # print(f"Week {week}, Year {year} filepath={file_path}")

            table = pd.read_csv(file_path)

            # Add the week and year to the table
            table['week'] = week
            table['year'] = year

            # Add table to list
            tables.append(table)
    return tables

def load_weekly_data(): 
    tables = load_all_tables()
    full_table = pd.concat(tables, ignore_index=True)
    clean_table(full_table)
    return full_table

def load_weekly_data_from_file():
    return pd.read_csv(os.path.join("weekly_data.csv"))

def append_uuid(cleaned_table):
    uuids = dict()

    cleaned_table.insert(1, "player_id", "0")

    for index, row in cleaned_table.iterrows():
        name = row['Player']
        if name not in uuids:
            generated_uuid = str(uuid.uuid4())
            uuids[name] = generated_uuid
        cleaned_table.at[index, 'player_id'] = uuids[name]

if __name__ == "__main__":
    # If main, write it to a main csv file for testing
    combined_table = load_weekly_data()
    append_uuid(cleaned_table=combined_table)
    print(combined_table)
    combined_table.to_csv(os.path.join("weekly_data.csv"))