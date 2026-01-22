import pandas as pd

def load_data(path="data/raw.csv"):
    df = pd.read_csv(path)

    # Rename columns to standard names
    df = df.rename(columns={
        "Date": "date",
        "Temp": "value"
    })

    # Convert date column
    df["date"] = pd.to_datetime(df["date"])

    # Sort by date (VERY important for time series)
    df = df.sort_values("date")

    # Reset index
    df = df.reset_index(drop=True)

    return df
if __name__ == "__main__":
    df = load_data()
    print("Rows:", len(df))
    print(df.head())
    print(df.tail())


