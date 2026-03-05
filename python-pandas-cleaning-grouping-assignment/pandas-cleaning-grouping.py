import pandas as pd
import numpy as np


if __name__ == "__main__":
    # Creating sample dataset
    data = {
        "Employee": [
            "Amit", "Neha", "Rahul", "Sneha",
            "Vikram", "Priya", "Arjun", "Divya"
        ],
        "Department": [
            "IT", "HR", "IT", "Finance",
            "HR", "Finance", "IT", "HR"
        ],
        "Salary": [
            600000, 500000, np.nan, 700000,
            520000, np.nan, 650000, 480000
        ],
        "Temporary_Notes": [
            "On probation", "Contract",
            "Pending docs", "Verified",
            "Intern", "New joiner",
            "On leave", "Temporary role"
        ]
    }

    # Create DataFrame
    df = pd.DataFrame(data)

    print("Original DataFrame:")
    print(df)
    print("\nMissing values per column:")
    print(df.isna().sum())

    # Fill missing Salary values with mean salary
    mean_salary = df["Salary"].mean()
    df["Salary"] = df["Salary"].fillna(mean_salary)

    print("\nDataFrame after filling missing Salary with mean:")
    print(df)

    # Drop Temporary_Notes column
    df = df.drop(columns=["Temporary_Notes"])

    # Rename Salary to Annual_Salary
    df = df.rename(columns={"Salary": "Annual_Salary"})

    # Group by Department and compute mean salary and employee count
    summary = df.groupby("Department").agg(
        Mean_Annual_Salary=("Annual_Salary", "mean"),
        Employee_Count=("Employee", "count")
    ).reset_index()

    print("\nFinal summary table (by Department):")
    print(summary)