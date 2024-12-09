# Installation and Import
import pandas as pd

# Creating a Series
series = pd.Series([10, 20, 30, 40])
print("\nSeries:\n", series)

# Accessing Data from Series
print("Access Element by Index:", series[1])

# Basic Series Functions
print("\nSum of Series:", series.sum())
print("Mean of Series:", series.mean())
print("Maximum Value in Series:", series.max())

# Creating a DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "San Francisco", "Los Angeles"]
}
df = pd.DataFrame(data)
print("\nDataFrame:\n", df)

# Accessing Data from DataFrame
print("\nAccess Column:\n", df["Name"])
print("Access Row:\n", df.iloc[1])  # Access row by index

# Basic DataFrame Functions
print("\nDataFrame Description:\n", df.describe())
print("DataFrame Shape:", df.shape)
print("DataFrame Head:\n", df.head())
