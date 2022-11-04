# Master file to orchestrate processing of data and uploading to RDS

from load_weekly_data import load_weekly_data

if __name__ == "__main__":
    weekly_data = load_weekly_data()
    print(weekly_data)