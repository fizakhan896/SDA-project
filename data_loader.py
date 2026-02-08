import pandas as pd
import json
import os

def load_config():
    with open("config.json", "r") as f:
        return json.load(f)

def load_data():
    try:
        file_path = os.path.join("data", "gdp_data_clean.csv")
        data = pd.read_csv(file_path)

        data.columns = data.columns.str.strip()
        print("COLUMNS FOUND:", list(data.columns))

        if data.empty:
            print("Data file is empty")

        # CLEANING (IMPORTANT)
        data = data.dropna(subset=["Value"])
        data["Year"] = data["Year"].astype(int)
        data["Value"] = data["Value"].astype(float)

        return data

    except Exception as e:
        raise Exception(f"Error loading data: {e}")

