import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = {
    "SquareFootage": [800, 1000, 1200, 1500, 1800, 2000, 2200, 2500, 5000],
    "TotalRooms": [4, 5, 6, 7, 8, 9, 10, 11, 20],
    "Bedrooms": [2, 2, 3, 3, 3, 4, 4, 4, 6],
    "Price": [150000, 180000, 210000, 260000, 300000, 330000, 360000, 420000, 1000000]
}
df = pd.DataFrame(data)
corr_matrix = df.corr()
print("Correlation Matrix:\n", corr_matrix)
plt.figure()
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
high_corr = corr_matrix[(corr_matrix > 0.8) & (corr_matrix < 1.0)]
print("\nHighly Correlated Features:\n", high_corr)
plt.figure()
sns.boxplot(y=df["Price"])
plt.title("Boxplot of Price")
plt.show()
Q1 = df["Price"].quantile(0.25)
Q3 = df["Price"].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
outliers = df[(df["Price"] < lower_bound) | (df["Price"] > upper_bound)]
print("\nOutliers in Price column:")
print(outliers)
