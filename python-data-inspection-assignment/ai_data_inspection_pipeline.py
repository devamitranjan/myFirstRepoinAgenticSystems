import pandas as pd

def load_csv(file_name: str)-> pd.DataFrame:
    try:
        column_names = ["Age", "Score", "Label"]
        df = pd.read_csv(file_name)
        return df.loc[:, column_names]
    except: 
        return pd.DataFrame(columns=column_names);

def print_output(df: pd.DataFrame)-> None:
    print(f"First 5 rows: \n {df.head()} \n")
    print(f"Last 5 rows: \n {df.tail()} \n")
    print(f"Structural Info: \n {df.info()} \n")
    print(f"Summary statistics: \n {df.describe()} \n")

def process_data(df: pd.DataFrame)-> None:
    age_column = df["Age"]
    print(f"Age Series: \n{age_column} \n")

    selected_columns_df = df[["Age", "Score"]]
    print(f"Selected Columns Dataframe: \n{selected_columns_df} \n")

    filtered_rows = df[df["Score"]> 80]
    print(f"Rows with Score > 80: \n{filtered_rows} \n")

if __name__==  "__main__":
    df = load_csv("employee.csv")
    print_output(df)
    process_data(df)


