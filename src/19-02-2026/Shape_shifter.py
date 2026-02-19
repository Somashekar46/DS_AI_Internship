import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
np.random.seed(42)
heights = np.random.normal(loc=170, scale=10, size=500)
incomes = np.random.exponential(scale=50000, size=500)
scores = 100 - np.random.exponential(scale=10, size=500)
df = pd.DataFrame({
    "Heights": heights,
    "Incomes": incomes,
    "Scores": scores
})
def plot_distribution(data, title):
    plt.figure()
    
    plt.hist(data, bins=30, density=True)

    pd.Series(data).plot(kind='kde')
    mean = np.mean(data)
    median = np.median(data)
    
    plt.axvline(mean)
    plt.axvline(median)
    
    plt.title(title)
    plt.xlabel("Value")
    plt.ylabel("Density")
    
    print(f"{title}")
    print(f"Mean: {mean:.2f}")
    print(f"Median: {median:.2f}")
    print("----------------------")
    
    plt.show()

plot_distribution(df["Heights"], "Normal Distribution (Heights)")
plot_distribution(df["Incomes"], "Right-Skewed Distribution (Incomes)")
plot_distribution(df["Scores"], "Left-Skewed Distribution (Scores)")
