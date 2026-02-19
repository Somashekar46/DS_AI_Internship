import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Create heavily skewed dataset (simulate income-like data)
np.random.seed(42)
data = np.random.exponential(scale=10, size=10000)

df = pd.DataFrame(data, columns=["Values"])

# Step 2: Take 1000 samples and calculate means
sample_means = []

for i in range(1000):
    sample = np.random.choice(df["Values"], size=30)
    sample_mean = np.mean(sample)
    sample_means.append(sample_mean)

sample_means = pd.DataFrame(sample_means, columns=["Sample_Mean"])

# Step 3: Print comparison
print("Original Data Mean:", df["Values"].mean())
print("Mean of Sample Means:", sample_means["Sample_Mean"].mean())

# Step 4: Plot original skewed data
plt.figure()
plt.hist(df["Values"], bins=50)
plt.title("Original Data Distribution (Skewed)")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# Step 5: Plot distribution of sample means
plt.figure()
plt.hist(sample_means["Sample_Mean"], bins=50)
plt.title("Distribution of Sample Means (Normal Bell Curve)")
plt.xlabel("Sample Mean")
plt.ylabel("Frequency")
plt.show()
