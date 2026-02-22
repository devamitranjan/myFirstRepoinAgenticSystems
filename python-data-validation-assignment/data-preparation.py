'''
Question: NumPy-Based Dataset Preparation Pipeline
Task: Build a Python program using NumPy that simulates a realistic AI-style data preparation pipeline.

Your program must:

Set a random seed for reproducibility.

Generate a 2D NumPy array representing a dataset with:

Rows as samples
Columns as features
Compute the mean and standard deviation per feature using axis-aware operations.

Normalize the dataset using broadcasting:

normalized = (data - mean) / std
Slice the normalized array to:

Extract the first 80% of samples as a training set
Extract the remaining samples as a test set
Modify a sliced value intentionally and observe its effect on the original array (to demonstrate view behavior).

Print:

Original data shape
Mean and standard deviation shapes
Training and test set shapes
A brief message explaining what changed due to slicing
Requirements:

Use NumPy vectorized operations only (no Python loops for math)
Use .shape, slicing, broadcasting, and random generation
Use clear variable names and clean structure
Demonstrate understanding of views vs copies
Sample Output (example):

Original data shape: (100, 3)
Mean shape: (3,)
Training data shape: (80, 3)
Test data shape: (20, 3)
Note: Modifying the slice affected the original array

'''



import numpy as np

def data_preparation_pipeline(data: np.ndarray): 
    mean = np.mean(data, axis= 0)
    print(f"Mean shape: {mean.shape}")
    std = np.std(data, axis = 0)
    normalized = (data - mean)/ std
    
    # print(f"Normalized Samples * Features {normalized}\n")

    split_index = len(normalized) * 80 // 100

    training_data = normalized[:split_index]
    print(f"Training data shape: {training_data.shape}")
    test_data = normalized[split_index:]
    print(f"Test data shape: {test_data.shape}")
    # print(normalized[0][0])
    training_data[0][0] = 0.1344556445
    print(f"Note: Modifying the slice affected the original array: {normalized[0][0]}")

    return training_data, test_data

  
if __name__ == "__main__":
    np.random.seed(42)
    shape = (5,3)
    rng = np.random.default_rng()
    random_floats = rng.random(shape)
    print(f"Original data shape: {shape}")
    data_preparation_pipeline(np.copy(random_floats))
