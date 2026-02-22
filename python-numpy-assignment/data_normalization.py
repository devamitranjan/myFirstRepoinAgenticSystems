'''
Question: NumPy-Based Data Normalization Pipeline
Task: Build a Python program using NumPy that simulates a small numerical preprocessing pipeline similar to those used in machine learning.

Your program must:

Create a NumPy array representing numeric data (e.g., feature values).

Compute:

Mean of the data
Standard deviation of the data
Normalize the data using the formula:

normalized = (data - mean) / std
Reshape the normalized data into a 2D array with a valid shape.

Print:

Original array
Mean and standard deviation
Normalized array
Reshaped array and its shape
Requirements:

Use NumPy array operations (no Python loops for math)
Use vectorized arithmetic
Use .shape and .reshape()
Write clean, readable code
Import NumPy properly
Sample Output (example):

Original data: [10 20 30 40]
Mean: 25.0
Standard Deviation: 11.18
Normalized data: [-1.34 -0.45  0.45  1.34]
Reshaped data shape: (2, 2)
'''

import numpy as np


def normalization_pipeline(data: np.ndarray):
    mean = np.mean(data)
    std = np.std(data)
    normalized = (data - mean) / std

    size = data.size
    rows = int(np.sqrt(size))
    cols = size // rows
    reshaped = normalized.reshape(rows, cols)

    return normalized, reshaped


if __name__ == "__main__":
    data = np.array([10, 20, 30, 40])

    mean = np.mean(data)
    std = np.std(data)
    normalized, reshaped = normalization_pipeline(data)

    print(f"Original data: {data}")
    print(f"Mean: {mean}")
    print(f"Standard Deviation: {std:.2f}")
    print(f"Normalized data: {normalized}")
    print(f"Reshaped data shape: {reshaped.shape}")
    print(f"Reshaped data:\n{reshaped}")
