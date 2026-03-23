import numpy as np
import matplotlib.pyplot as plt


def generate_synthetic_training_loss(
    num_epochs: int = 10, *, seed: int = 42
) -> tuple[np.ndarray, np.ndarray]:
    """Generate epochs and synthetic (decreasing) training loss values."""
    rng = np.random.default_rng(seed)
    epochs = np.arange(1, num_epochs + 1)
    losses = 1.0 / np.sqrt(epochs) + rng.normal(0, 0.05, size=num_epochs)

    return epochs, losses




def plot_loss_vs_epoch_line(epochs: np.ndarray, losses: np.ndarray) -> None:
    """Line plot: Loss vs Epoch (with markers and grid)."""
    plt.figure(figsize=(8, 4))
    plt.plot(epochs, losses, marker="o")
    plt.title("Epoch vs Loss (Line Plot)")
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.grid(True, linestyle="--", alpha=0.4)
    plt.tight_layout()
    plt.show()


def plot_epoch_vs_loss_scatter(epochs: np.ndarray, losses: np.ndarray) -> None:
    """Scatter plot: Epoch vs Loss."""
    plt.figure(figsize=(8, 4))
    plt.scatter(epochs, losses, marker="o")
    plt.title("Epoch vs Loss (Scatter)")
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.grid(True, linestyle="--", alpha=0.4)
    plt.tight_layout()
    plt.show()


def plot_model_accuracies_bar() -> None:
    """Bar chart comparing accuracy of three models."""
    models = ["Model A", "Model B", "Model C"]
    accuracies = [0.85, 0.90, 0.88]

    plt.figure(figsize=(8, 4))
    bars = plt.bar(models, accuracies)
    plt.title("Model Accuracy Comparison")
    plt.xlabel("Models")
    plt.ylabel("Accuracy")
    plt.ylim(0, 1)
    plt.grid(True, axis="y", linestyle="--", alpha=0.4)

    # Add numeric labels above each bar.
    for bar, acc in zip(bars, accuracies):
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            acc + 0.01,
            f"{acc:.2f}",
            ha="center",
        )

    plt.tight_layout()
    plt.show()


def main() -> None:
    epochs, losses = generate_synthetic_training_loss(num_epochs=10, seed=42)
    plot_loss_vs_epoch_line(epochs, losses)
    plot_epoch_vs_loss_scatter(epochs, losses)
    plot_model_accuracies_bar()

if __name__ == "__main__":
    main()