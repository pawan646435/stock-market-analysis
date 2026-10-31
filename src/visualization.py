import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


def create_stock_dashboard(
    report: pd.DataFrame,
    benchmark_cagr: float,
    output_path: str = "visualizations/stock_performance_dashboard.png"
) -> None:
    """
    Create a three-panel stock performance dashboard.

    Charts:
    1. CAGR comparison
    2. Annualized volatility comparison
    3. Sharpe Ratio comparison
    """

    # Sort stocks by CAGR
    report = report.sort_values("CAGR", ascending=False)

    # Create output directory
    
    PROJECT_ROOT = Path(__file__).resolve().parent.parent

    dashboard_path = Path(output_path)

    if not dashboard_path.is_absolute():
        dashboard_path = PROJECT_ROOT / dashboard_path

    # Create output directory
    dashboard_path.parent.mkdir(parents=True, exist_ok=True)

    # Create three charts
    fig, axes = plt.subplots(1, 4, figsize=(24, 6))

    # Chart 1: CAGR
    axes[0].bar(report.index, report["CAGR"])
    axes[0].set_title("CAGR Comparison")
    axes[0].set_ylabel("CAGR (%)")
    axes[0].tick_params(axis="x", rotation=45)
    axes[0].axhline(0, linewidth=0.8)

    # Chart 2: Annualized Volatility
    axes[1].bar(
        report.index,
        report["Annualized_Volatility"]
    )
    axes[1].set_title("Annualized Volatility")
    axes[1].set_ylabel("Volatility (%)")
    axes[1].tick_params(axis="x", rotation=45)

    # Chart 3: Sharpe Ratio
    axes[2].bar(report.index, report["Sharpe_Ratio"])
    axes[2].set_title("Risk-Adjusted Performance")
    axes[2].set_ylabel("Sharpe Ratio")
    axes[2].tick_params(axis="x", rotation=45)
    axes[2].axhline(0, linewidth=0.8)
    
    
        # Chart 4: Stock performance vs Nifty 50
    axes[3].bar(
        report.index,
        report["CAGR"],
        label="Stock CAGR"
    )

    axes[3].axhline(
        y=benchmark_cagr,
        linestyle="--",
        linewidth=2,
        label="Nifty 50 CAGR"
    )

    axes[3].set_title("Stock vs Nifty 50")
    axes[3].set_ylabel("CAGR (%)")
    axes[3].tick_params(axis="x", rotation=45)
    axes[3].legend()

    fig.suptitle(
        "Stock Market Performance Analysis",
        fontsize=16,
        fontweight="bold"
    )

    plt.tight_layout()
    plt.savefig(
        dashboard_path,
        dpi=300,
        bbox_inches="tight"
    )
    plt.show()
    plt.close()

    print(f"Dashboard saved: {dashboard_path.resolve()}")