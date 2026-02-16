import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = {
    "SquareFootage": [800, 1000, 1200, 1400, 1600, 1800, 2000, 2200],
    "Price": [150000, 180000, 210000, 240000, 270000, 300000, 330000, 360000],
    "Location": ["Urban", "Urban", "Suburban", "Suburban", "Suburban", "Urban", "Urban", "Suburban"]
}
df = pd.DataFrame(data)
plt.figure()
sns.scatterplot(x="SquareFootage", y="Price", data=df)
plt.title("Relationship between Square Footage and Price")
plt.xlabel("Square Footage")
plt.ylabel("Price")
plt.show()
plt.figure()
sns.boxplot(x="Location", y="Price", data=df)
plt.title("Price Distribution by Location")
plt.xlabel("Location")
plt.ylabel("Price")
plt.show()
correlation = df["SquareFootage"].corr(df["Price"])
print("Correlation:", correlation)
