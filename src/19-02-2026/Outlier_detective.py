import numpy as np
import pandas as pd

# Sample dataset
data = {
    "Student": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"],
    "Marks": [65, 70, 72, 68, 75, 80, 78, 74, 69, 200]
}

df = pd.DataFrame(data)

# Calculate Mean (μ) and Standard Deviation (σ)
mean = df["Marks"].mean()
std = df["Marks"].std()

# Create z_score column
df["z_score"] = (df["Marks"] - mean) / std

# Identify statistical outliers (|Z| > 3)
outliers = df[np.abs(df["z_score"]) > 3]

# Output
print("Dataset with Z-Scores:")
print(df)

print("\nStatistical Outliers (|Z| > 3):")
print(outliers)
