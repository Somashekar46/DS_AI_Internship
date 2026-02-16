import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the dataset
df = pd.read_csv("housing_data_500.csv")

# ----------------------------
# Histogram with KDE
# ----------------------------
plt.figure(figsize=(8,5))
sns.histplot(df["Price"], kde=True)

plt.title("Distribution of Housing Prices")
plt.xlabel("Price")
plt.ylabel("Frequency")

plt.show()

# ----------------------------
# Skewness and Kurtosis
# ----------------------------
print("Skewness:", df["Price"].skew())
print("Kurtosis:", df["Price"].kurt())

# ----------------------------
# Count Plot for City
# ----------------------------
plt.figure(figsize=(8,5))
sns.countplot(x=df["City"])

plt.title("Count of Houses by City")
plt.xlabel("City")
plt.ylabel("Count")

plt.show()
