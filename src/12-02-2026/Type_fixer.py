import pandas as pd
data = {
    "Price": ["$100.50", "$250.00", "$75.25", "$300.10"],
    "Date": ["2026-01-01", "2026-01-05", "2026-01-10", "2026-01-15"]
}
df = pd.DataFrame(data)
print("Before Conversion:\n")
print(df.dtypes)
df["Price"] = df["Price"].str.replace("$", "", regex=False).astype(float)
df["Date"] = pd.to_datetime(df["Date"])
print("\nAfter Conversion:\n")
print(df.dtypes)
print("\nAverage Price:", df["Price"].mean())
print("Earliest Date:", df["Date"].min())
