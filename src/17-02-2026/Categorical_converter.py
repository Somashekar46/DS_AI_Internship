import pandas as pd
from sklearn.preprocessing import LabelEncoder
df = pd.DataFrame({
    "Transmission": ["Automatic", "Manual", "Manual", "Automatic"],
    "Color": ["Red", "Blue", "Green", "Red"]
})
print("Original Data:\n")
print(df)
label_encoder = LabelEncoder()
df["Transmission"] = label_encoder.fit_transform(df["Transmission"])
df = pd.get_dummies(df, columns=["Color"], drop_first=True)
print("\nEncoded Data:\n")
print(df)
print("\nData Types:\n")
print(df.dtypes)
