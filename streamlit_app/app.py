import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Supply Chain Demand Forecasting", page_icon="📦", layout="wide"
)

st.title("📦 Supply Chain Demand Forecasting Dashboard")
st.markdown("---")


st.write("""
    Welcome to the Supply Chain Demand Forecasting Dashboard.

    This dashboard provides insights into:

    • Historical Sales
    • Forecasted Demand
    • Model Performance
    • Inventory Planning
    """)

clean_df = pd.read_csv("data/processed/clean_sales.csv", parse_dates=["date"])

forecast_df = pd.read_csv("data/processed/future_forecast.csv", parse_dates=["date"])

anomaly_df = pd.read_csv("data/processed/anomaly_detection.csv")

total_sales = clean_df["sales"].sum()

average_sales = clean_df["sales"].mean()

max_sales = clean_df["sales"].max()

forecast_total = forecast_df["forecast_sales"].sum()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Sales", f"{total_sales:,.0f}")

col2.metric("Average Daily Sales", f"{average_sales:.2f}")

col3.metric("Maximum Daily Sales", f"{max_sales:.0f}")

col4.metric("90-Day Forecast", f"{forecast_total:.0f}")

st.subheader("📈 Historical Sales")

fig = px.line(clean_df, x="date", y="sales", title="Historical Daily Sales")

st.plotly_chart(fig, use_container_width=True)

st.subheader("🔮 Future Demand Forecast")

forecast_fig = px.line(
    forecast_df, x="date", y="forecast_sales", title="90-Day Demand Forecast"
)

st.plotly_chart(forecast_fig, use_container_width=True)

st.subheader("Forecast Table")

st.dataframe(forecast_df, use_container_width=True)

st.subheader("Detected Anomalies")

anomalies = anomaly_df[anomaly_df["iforest_anomaly"] == True]

st.dataframe(anomalies, use_container_width=True)

# import pandas as pd

# df = pd.read_csv("data/processed/anomaly_detection.csv")
# print(df.columns.tolist())
