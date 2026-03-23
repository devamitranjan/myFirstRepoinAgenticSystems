import pandas as pd
import plotly.express as px


def create_training_loss_dataframe() -> pd.DataFrame:
    """Create a simple training-loss dataset for epochs 1-10."""
    epochs = list(range(1, 11))
    training_loss = [1.00, 0.82, 0.68, 0.58, 0.50, 0.47, 0.45, 0.44, 0.43, 0.43]

    return pd.DataFrame({"Epoch": epochs, "Training Loss": training_loss})


def plot_training_loss(df: pd.DataFrame) -> None:
    """Plot interactive Loss vs Epoch line chart with annotation."""
    fig = px.line(
        df,
        x="Epoch",
        y="Training Loss",
        markers=True,
        title="Training Loss Over Epochs",
        labels={"Epoch": "Epoch", "Training Loss": "Loss"},
    )

    fig.add_annotation(
        x=8,
        y=0.44,
        text="Loss starts to stabilize",
        showarrow=True,
        arrowhead=2,
        ax=40,
        ay=-40,
    )

    fig.show()


def main() -> None:
    df = create_training_loss_dataframe()
    plot_training_loss(df)

if __name__ == "__main__":
    main()
