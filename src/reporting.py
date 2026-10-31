import pandas as pd
from pathlib import Path


def save_stock_report(
    report: pd.DataFrame,
    output_path: str = "data/processed/stock_analysis_report.csv"
) -> None:
    """
    Save the final stock analysis report as a CSV file.
    """

    report_path = Path(output_path)

    # Create the output directory if it doesn't exist
    report_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    # Save report
    report.to_csv(report_path, index=True)

    print(f"Report saved successfully: {report_path.resolve()}")