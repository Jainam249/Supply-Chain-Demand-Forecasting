# 📦 Supply Chain Analytics – Demand Forecasting & Anomaly Detection

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-yellow)
![Statsmodels](https://img.shields.io/badge/Statsmodels-Time%20Series-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

# 📖 Project Overview

This project was developed as part of the **Infotact Technical Internship Program**.

The objective of this project is to analyze historical retail sales data, detect anomalies, forecast future demand, and visualize insights through an interactive Streamlit dashboard.

The project demonstrates an end-to-end Data Analytics workflow including:

- Data Cleaning
- Exploratory Data Analysis
- Time Series Analysis
- Statistical Anomaly Detection
- Demand Forecasting
- Dashboard Development

---

# 🎯 Project Objectives

- Clean and preprocess raw sales data
- Perform exploratory data analysis
- Detect anomalies using statistical techniques
- Forecast future demand using ARIMA
- Evaluate forecasting performance
- Build an interactive dashboard
- Generate business insights for inventory planning

---

# 🛠 Technology Stack

| Category         | Tools               |
| ---------------- | ------------------- |
| Programming      | Python              |
| Data Analysis    | Pandas, NumPy       |
| Visualization    | Matplotlib, Plotly  |
| Machine Learning | Scikit-learn        |
| Time Series      | Statsmodels (ARIMA) |
| Dashboard        | Streamlit           |
| Version Control  | Git & GitHub        |

---

# 📁 Project Structure

```text
Supply-Chain-Demand-Forecasting/
│
├── data/
│   ├── raw/
│   │   └── retail_sales.csv
│   │
│   └── processed/
│       ├── clean_sales.csv
│       ├── anomaly_detection.csv
│       └── future_forecast.csv
│
├── notebooks/
│   ├── 01_data_preprocessing.ipynb
│   ├── 02_anomaly_detection.ipynb
│   └── 03_demand_forecasting.ipynb
│
├── src/
│   ├── preprocessing.py
│   ├── anomaly_detection.py
│   ├── forecasting.py
│   └── evaluation.py
│
├── streamlit_app/
│   ├── app.py
│   └── assets/
│
├── reports/
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# 📊 Project Workflow

```text
Raw Dataset
      │
      ▼
Data Cleaning
      │
      ▼
Exploratory Data Analysis
      │
      ▼
Time Series Decomposition
      │
      ▼
Anomaly Detection
      │
      ▼
Demand Forecasting
      │
      ▼
Model Evaluation
      │
      ▼
Future Forecast
      │
      ▼
Interactive Streamlit Dashboard
```

---

# 📚 Notebook Description

### 01_data_preprocessing.ipynb

- Import dataset
- Data inspection
- Missing value treatment
- Duplicate removal
- Datetime conversion
- Data cleaning
- Save cleaned dataset

---

### 02_anomaly_detection.ipynb

- Time series decomposition
- Z-Score anomaly detection
- IQR anomaly detection
- Isolation Forest
- Anomaly visualization
- Save anomaly dataset

---

### 03_demand_forecasting.ipynb

- Train/Test split
- Moving Average forecasting
- ARIMA forecasting
- Model evaluation
- RMSE
- MAE
- MAPE
- Future demand prediction

---

# 📦 Source Modules

### preprocessing.py

Reusable preprocessing functions.

### anomaly_detection.py

Contains:

- Z-Score Detection
- IQR Detection
- Isolation Forest

### forecasting.py

Contains:

- Train/Test Split
- Moving Average Forecast
- ARIMA Forecast
- Future Forecast Generation

### evaluation.py

Contains evaluation metrics including:

- RMSE
- MAE
- MAPE

---

# 📈 Dashboard Features

The Streamlit dashboard includes:

- KPI Cards
- Historical Sales Visualization
- Future Demand Forecast
- Sales Distribution
- Monthly Sales Trend
- Store Selection
- Item Selection
- Date Range Filter
- Forecast Table
- Detected Anomalies Table

---

# 📊 Results

The project successfully demonstrates:

- Cleaned retail sales dataset
- Statistical anomaly detection
- ARIMA demand forecasting
- Future sales prediction
- Interactive business dashboard

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/Jainam249/Supply-Chain-Demand-Forecasting.git
```

Go into the project directory

```bash
cd Supply-Chain-Demand-Forecasting
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Running the Notebooks

Launch Jupyter Notebook

```bash
jupyter notebook
```

Run notebooks in the following order:

1. 01_data_preprocessing.ipynb
2. 02_anomaly_detection.ipynb
3. 03_demand_forecasting.ipynb

---

# 💻 Running the Dashboard

```bash
streamlit run streamlit_app/app.py
```

---

# 📌 Future Improvements

- Prophet Forecasting
- LSTM Forecasting
- XGBoost Forecasting
- Real-Time Inventory Dashboard
- Docker Deployment
- Cloud Deployment (Render / Streamlit Cloud / Azure)

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push your branch.
5. Create a Pull Request.

---

# 👨‍💻 Author

**Jainam Shah**

GitHub:
https://github.com/Jainam249

---

# ⭐ Acknowledgements

This project was completed as part of the **Infotact Technical Internship Program** to demonstrate practical skills in:

- Data Analytics
- Time Series Forecasting
- Machine Learning
- Dashboard Development
- Business Intelligence

---

If you found this project useful, consider giving it a ⭐ on GitHub.
