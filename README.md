# 📈 Yahoo Finance Data Fetcher - Streamlit App

This is a **Streamlit web application** that allows users to fetch and explore historical stock data from **Yahoo Finance** by simply entering a stock ticker symbol (like `AAPL`, `TSLA`, or `MSFT`) and selecting a date range. The application retrieves the data using the `yfinance` Python library and provides useful tools to analyze, preview, and download the dataset.

---

## 🚀 Features

- 🎯 Enter any valid stock ticker symbol.
- 📆 Select a custom date range (default: 1900 to current date).
- 📥 Download historical data from Yahoo Finance.
- 🔎 View top, bottom, and random samples of data.
- 📊 Display:
  - Column names
  - Null values
  - Data types
  - Duplicate rows
- 💾 Download the cleaned dataset as a CSV file.

---

## 🔧 How to Run Locally
- First make new environment
- then:
```bash
pip install -r requirements.txt
```
```bash
streamlit run main.py
```
