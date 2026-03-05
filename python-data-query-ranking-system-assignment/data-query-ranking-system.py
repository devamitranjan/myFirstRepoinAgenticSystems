'''
Task: Build a Python program using Pandas that simulates querying and analyzing an AI dataset.

Your program must:

Create or load a sample dataset containing at least:

Name
Score
Passed (Boolean)
Category (e.g., "A", "B")
Perform the following operations:

Select a single column and print it
Select multiple columns and store them in a new DataFrame
Use iloc to retrieve the first three rows
Use loc after setting a meaningful index
Filter rows where Score > 85
Filter rows where Score > 85 and Passed is True
Sort the filtered result in descending order of Score
Chain at least one filtering and sorting operation together.

Print labeled outputs for clarity.

Requirements:

Use Boolean filtering correctly (&, |, ~)
Use parentheses for multiple conditions
Demonstrate both iloc and loc
Avoid modifying the original DataFrame unintentionally
Write clean, readable code
'''

import pandas as pd

if __name__ == "__main__":
    df = pd.DataFrame({
        "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
        "Score": [85, 88, 90, 82, 87],
        "Passed": [True, True, True, False, True],
        "Category": ["A", "B", "A", "B", "A"]
    })
    new_df = df[["Name", "Score"]].copy()
    df_indexed = new_df.set_index("Name")
    # Labeled: Select a single column
    print("\n--- Names ---")
    print(df["Name"])

    # Labeled: Select multiple columns into a new DataFrame
    print("\n--- Name and Score DataFrame (new_df) ---")
    print(new_df)

    # Labeled: Using iloc to retrieve the first three rows
    print("\n--- First three rows of new_df using iloc ---")
    print(new_df.iloc[:3])

    # Labeled: Using loc with Name as index
    print("\n--- Data for 'Charlie' using .loc with 'Name' as index ---")
    print(df_indexed.loc["Charlie"])

    # Labeled: Filter rows where Score > 85
    print("\n--- Rows where Score > 85 ---")
    filt_score = df["Score"] > 85
    print(df.loc[filt_score])

    # Labeled: Filter where Score > 85 and Passed is True
    print("\n--- Rows where Score > 85 AND Passed is True ---")
    filt_both = (df["Score"] > 85) & (df["Passed"])
    print(df.loc[filt_both])

    # Labeled: Sort the filtered result in descending order of Score
    print("\n--- Filtered (Score > 85 & Passed) sorted by Score descending ---")
    filtered_sorted = df.loc[filt_both].sort_values(by="Score", ascending=False)
    print(filtered_sorted)

    # Labeled: Chained filtering and sorting operation
    print("\n--- Chained: All with Category 'A', sorted by Score descending ---")
    print(df[df["Category"] == "A"].sort_values(by="Score", ascending=False))
