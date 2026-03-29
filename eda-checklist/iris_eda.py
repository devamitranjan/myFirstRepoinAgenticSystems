import pandas as pd
import plotly.express as px
from pathlib import Path

DATASET_URL = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"


def load_dataset(url: str = DATASET_URL) -> pd.DataFrame:
    """
    Load the Iris dataset.

    Observation: The provided dataset is a classic Iris CSV with these columns:
    sepal_length, sepal_width, petal_length, petal_width, species
    """
    return pd.read_csv(url)


def inspect_structure(df: pd.DataFrame) -> None:
    # Observation: After loading, always validate the shape and quick sanity-check the first rows.
    print("=== Dataset Loaded Successfully ===")
    print(f"Shape: {df.shape}")
    print("\n=== First 5 Rows ===")
    print(df.head())

    print("\n=== Column Data Types (Structure) ===")
    print(df.dtypes)


def check_missing_values_and_info(df: pd.DataFrame) -> None:
    print("\n=== Dataset Info (df.info) ===")
    df.info()

    print("\n=== Missing Values (per column) ===")
    print(df.isnull().sum())

    # Observation: The classic Iris dataset has no missing values.


def feature_distribution_by_species(df: pd.DataFrame, feature: str = "petal_length") -> None:
    print(f"\n=== Distribution Stats for `{feature}` by Species ===")
    print(df.groupby("species")[feature].describe())

    fig = px.histogram(
        df,
        x=feature,
        color="species",
        barmode="overlay",
        nbins=25,
        opacity=0.65,
        title=f"{feature} Distribution by Species",
        hover_data=[c for c in df.columns if c != feature and c != "species"],
    )
    fig.write_html(OUT_DIR / "iris_petal_length_distribution.html")

    # Observation: Petal length is highly discriminative between setosa and the other two species.


def identify_outliers_iqr(df: pd.DataFrame) -> None:
    """
    Identify possible outliers using the IQR rule.

    Outliers can be visually inspected via box plots and also computed using:
      lower_bound = Q1 - 1.5 * IQR
      upper_bound = Q3 + 1.5 * IQR
    """
    numeric_cols = [c for c in df.columns if c != "species"]
    outlier_rows = []

    for col in numeric_cols:
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1

        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr

        mask = (df[col] < lower) | (df[col] > upper)
        if mask.any():
            sample = df.loc[mask, ["species", col]].head(5)
            outlier_rows.append((col, int(mask.sum()), sample))

    print("\n=== Outlier Candidates (IQR rule) ===")
    if not outlier_rows:
        print("No IQR outliers detected in numeric columns.")
    else:
        for col, count, sample in outlier_rows:
            print(f"- {col}: {count} potential outlier rows")
            print(sample.to_string(index=False))

    # Visual check: box plots make outliers immediately apparent.
    fig = px.box(
        df,
        x="species",
        y=numeric_cols,
        points="outliers",
        title="Box Plots by Species (Outliers Highlighted)",
    )
    fig.write_html(OUT_DIR / "iris_boxplots_outliers.html")


def analyze_relationships(df: pd.DataFrame) -> None:
    # Example requested in the question: petal_length vs petal_width
    corr = df[["petal_length", "petal_width"]].corr().iloc[0, 1]
    print(f"\n=== Relationship: petal_length vs petal_width (Overall Correlation) ===\n{corr:.4f}")

    for sp, sub in df.groupby("species"):
        c = sub[["petal_length", "petal_width"]].corr().iloc[0, 1]
        print(f"- {sp}: correlation = {c:.4f}")

    fig_scatter = px.scatter(
        df,
        x="petal_length",
        y="petal_width",
        color="species",
        title="Petal Length vs Petal Width (Colored by Species)",
        hover_data=["sepal_length", "sepal_width"],
    )
    fig_scatter.write_html(OUT_DIR / "iris_petal_length_vs_petal_width.html")

    # Observation: petal_length and petal_width increase together, and the three species form distinct clusters.


def insights_by_species(df: pd.DataFrame) -> None:
    print("\n=== Species Insights (Mean by Species) ===")
    numeric_cols = [c for c in df.columns if c != "species"]
    print(df.groupby("species")[numeric_cols].mean(numeric_only=True).round(3))

    # Observation: setosa has much smaller petal dimensions than versicolor/virginica.
    # Observation: virginica tends to have larger petal dimensions among the three.


def run_eda(df: pd.DataFrame) -> None:
    inspect_structure(df)
    check_missing_values_and_info(df)
    insights_by_species(df)
    feature_distribution_by_species(df, feature="petal_length")
    identify_outliers_iqr(df)
    analyze_relationships(df)


def main() -> None:
    df = load_dataset()
    run_eda(df)

    print("\n=== Visualization Files Generated ===")
    print(f"- {(OUT_DIR / 'iris_petal_length_distribution.html').name}")
    print(f"- {(OUT_DIR / 'iris_boxplots_outliers.html').name}")
    print(f"- {(OUT_DIR / 'iris_petal_length_vs_petal_width.html').name}")


OUT_DIR = Path(__file__).resolve().parent

if __name__ == "__main__":
    main()

