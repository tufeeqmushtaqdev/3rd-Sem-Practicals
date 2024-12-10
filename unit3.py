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

