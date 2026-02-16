import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = {
    "Price": [120000, 150000, 180000, 200000, 220000, 250000,
              300000, 350000, 400000, 450000, 500000, 800000],
    "City": ["Mumbai", "Delhi", "Mumbai", "Chennai", "Delhi",
             "Mumbai", "Chennai", "Delhi", "Mumbai",
             "Chennai", "Mumbai", "Delhi"]
}
df = pd.DataFrame(data)
plt.figure()
sns.histplot(df["Price"], kde=True)
plt.title("Distribution of Housing Prices")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.show()
skewness = df["Price"].skew()
kurtosis = df["Price"].kurt()
print("Skewness:", skewness)
print("Kurtosis:", kurtosis)
plt.figure()
sns.countplot(x=df["City"])
plt.title("Count of Houses by City")
plt.xlabel("City")
plt.ylabel("Count")
plt.show()
