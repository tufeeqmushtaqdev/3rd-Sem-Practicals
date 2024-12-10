# Installation and Import
import pandas as pd

#  Creating a Pandas Series
data = pd.Series([10, 20, 30, 40, 50])

#  Appending to a Pandas Series
new_data = data.append(pd.Series([60, 70]), ignore_index=True)
print("Appended Series:\n", new_data)

#  Sorting a Pandas Series
sorted_series = new_data.sort_values()
print("Sorted Series:\n", sorted_series)

#  Indexing in Pandas Series
print("Element at index 2:", data[2])  # Accessing the 3rd element

#  Slicing in Pandas Series
print("Sliced Series (index 1 to 3):\n", data[1:4])  # Elements from index 1 to 3

# Creating a Series
series = pd.Series([10, 20, 30, 40])
print("\nSeries:\n", series)

# Accessing Data from Series
print("Access Element by Index:", series[1])

# Basic Series Functions
print("\nSum of Series:", series.sum())
print("Mean of Series:", series.mean())
print("Maximum Value in Series:", series.max())

