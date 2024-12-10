# Installation and Import
import numpy as np

# Creating Arrays
one_d_array = np.array([1, 2, 3, 4])
print("\nOne-dimensional Array:", one_d_array)

n_d_array = np.array([[1, 2, 3], [4, 5, 6]])
print("N-dimensional Array:\n", n_d_array)

# Indexing and Slicing
print("\nIndexing Example:", one_d_array[2])  # Accessing element at index 2
print("Slicing Example:", one_d_array[1:3])  # Accessing elements from index 1 to 2

# Boolean Indexing
print("\nBoolean Indexing Example:", one_d_array[one_d_array > 2])

# Adding, Removing, and Sorting Arrays
array = np.array([3, 1, 4, 1, 5])
sorted_array = np.sort(array)
print("\nSorted Array:", sorted_array)

# Basic Array Operations
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

print("\nArray Addition:", array1 + array2)
print("Array Subtraction:", array1 - array2)
print("Array Multiplication:", array1 * array2)
print("Array Division:", array1 / array2)

# Working with Matrices
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

print("\nMatrix Addition:\n", matrix1 + matrix2)
print("Matrix Multiplication:\n", np.dot(matrix1, matrix2))

