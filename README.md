# Indian Stock Market Data Analysis

A Python-based data analysis project that explores historical stock market data, evaluates investment performance, and compares risk and returns across five major Indian companies.

## Project Overview

This project analyses approximately five years of historical stock market data for:

- Reliance Industries
- Tata Consultancy Services (TCS)
- Infosys
- HDFC Bank
- ICICI Bank

The objective is to understand historical price movements, calculate investment returns, measure volatility, and compare risk-adjusted performance using Python.

## Tech Stack

- **Python** – Programming language
- **Pandas** – Data manipulation and analysis
- **NumPy** – Numerical computations
- **Matplotlib** – Data visualization
- **Seaborn** – Statistical visualization
- **yfinance** – Historical stock market data
- **Jupyter Notebook** – Interactive analysis environment

## Project Structure

```text
stock-market-analysis/
│
├── data/
│   ├── raw/
│   │   └── stock_data.csv
│   └── processed/
│       ├── cleaned_stock_data.csv
│       └── stock_analysis_report.csv
│
├── notebooks/
│   └── 01_data_collection.ipynb
│
├── src/
├── visualizations/
│   └── stock_performance_dashboard.png
│
├── requirements.txt
└── README.md
```

## Analysis Performed

### 1. Data Collection
- Retrieved approximately five years of historical stock data using Yahoo Finance.
- Collected Open, High, Low, Close and Volume data.

### 2. Data Cleaning
- Investigated missing and invalid records.
- Identified zero-volume observations.
- Created a separate cleaned dataset while preserving raw data.

### 3. Exploratory Data Analysis
- Examined historical closing prices.
- Visualized price movements and trends.
- Calculated daily percentage returns.

### 4. Risk and Return Analysis
Calculated:
- Mean daily return
- Daily return standard deviation
- Maximum and minimum daily returns
- Annualized volatility
- Approximate annualized mean return
- Sharpe Ratio

### 5. Investment Performance Analysis
- Simulated the growth of an initial ₹100 investment.
- Calculated cumulative returns.
- Calculated Compound Annual Growth Rate (CAGR).
- Compared historical investment performance.

## Key Findings

Based on the selected historical period:

- ICICI Bank recorded the highest CAGR among the five companies.
- ICICI Bank also had the lowest annualized volatility.
- Infosys recorded the highest annualized volatility.
- Infosys had the lowest cumulative investment performance in this sample.

## Visualizations

The project includes:
- Historical stock price charts
- Risk vs Return scatter plot
- Growth of ₹100 comparison
- CAGR vs Risk analysis
- Stock performance dashboard

## How to Run

1. Clone the repository.

```bash
git clone 
cd stock-market-analysis
```

2. Create and activate a virtual environment.

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies.

```bash
pip install -r requirements.txt
```

4. Launch Jupyter Notebook.

```bash
jupyter notebook
```

5. Open `notebooks/01_data_collection.ipynb` and run the cells.

## Data Source

Historical stock market data was retrieved using the Yahoo Finance Python library (`yfinance`).

## Disclaimer

This project is for educational and analytical purposes only. Historical performance does not guarantee future returns. The analysis excludes certain real-world investment costs and uses simplified assumptions for selected financial metrics.

---

**Author:** Pawan 
**Project:** Indian Stock Market Data Analysis  
**Language:** Python