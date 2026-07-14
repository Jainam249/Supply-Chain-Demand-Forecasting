# import streamlit as st
# import pandas as pd
# import plotly.express as px

# st.set_page_config(
#     page_title="Supply Chain Demand Forecasting", page_icon="📦", layout="wide"
# )

# st.title("📦 Supply Chain Demand Forecasting Dashboard")
# st.markdown("---")


# st.write("""
#     Welcome to the Supply Chain Demand Forecasting Dashboard.

#     This dashboard provides insights into:

#     • Historical Sales
#     • Forecasted Demand
#     • Model Performance
#     • Inventory Planning
#     """)

# # clean_df = pd.read_csv("data/processed/clean_sales.csv", parse_dates=["date"])

# # forecast_df = pd.read_csv("data/processed/future_forecast.csv", parse_dates=["date"])

# # anomaly_df = pd.read_csv("data/processed/anomaly_detection.csv")


# @st.cache_data
# def load_data():
#     clean = pd.read_csv("data/processed/clean_sales.csv", parse_dates=["date"])

#     forecast = pd.read_csv("data/processed/future_forecast.csv", parse_dates=["date"])

#     anomaly = pd.read_csv("data/processed/anomaly_detection.csv")

#     return clean, forecast, anomaly


# clean_df, forecast_df, anomaly_df = load_data()


# st.sidebar.title("Dashboard Filters")

# st.sidebar.markdown("---")

# stores = sorted(clean_df["store_id"].unique())

# selected_store = st.sidebar.selectbox("Select Store", stores)

# items = sorted(clean_df[clean_df["store_id"] == selected_store]["item_id"].unique())

# selected_item = st.sidebar.selectbox("Select Item", items)

# start_date = st.sidebar.date_input("Start Date", clean_df["date"].min())

# end_date = st.sidebar.date_input("End Date", clean_df["date"].max())

# filtered_df = clean_df[
#     (clean_df["store_id"] == selected_store)
#     & (clean_df["item_id"] == selected_item)
#     & (clean_df["date"] >= pd.to_datetime(start_date))
#     & (clean_df["date"] <= pd.to_datetime(end_date))
# ]

# if filtered_df.empty:
#     st.warning("No data available for the selected filters.")
#     st.stop()

# total_sales = filtered_df["sales"].sum()

# average_sales = filtered_df["sales"].mean()

# max_sales = filtered_df["sales"].max()

# forecast_total = forecast_df["forecast_sales"].sum()

# col1, col2, col3, col4 = st.columns(4)

# col1.metric("Total Sales", f"{total_sales:,.0f}")

# col2.metric("Average Daily Sales", f"{average_sales:.2f}")

# col3.metric("Maximum Daily Sales", f"{max_sales:.0f}")

# col4.metric("90-Day Forecast", f"{forecast_total:.0f}")

# st.subheader("📊 Sales Analysis")

# fig = px.line(
#     filtered_df,
#     x="date",
#     y="sales",
#     title=f"Sales Trend - Store {selected_store}, Item {selected_item}",
# )

# fig.update_traces(line_width=3)


# hist = px.histogram(filtered_df, x="sales", nbins=30, title="Distribution of Sales")


# col1, col2 = st.columns(2)

# with col1:
#     st.plotly_chart(fig, use_container_width=True, key="historical_sales_chart")

# with col2:
#     st.plotly_chart(hist, use_container_width=True, key="sales_distribution_chart")


# monthly_sales = (
#     filtered_df.set_index("date").resample("ME")["sales"].sum().reset_index()
# )

# monthly_fig = px.bar(monthly_sales, x="date", y="sales", title="Monthly Sales")

# st.plotly_chart(monthly_fig, use_container_width=True)

# st.info(f"""
#     Selected Store: {selected_store}

#     Selected Item: {selected_item}

#     Date Range:
#     {start_date} → {end_date}
#     """)

# st.subheader("🔮 Future Demand Forecast")

# forecast_fig = px.line(
#     forecast_df, x="date", y="forecast_sales", title="90-Day Demand Forecast"
# )

# st.plotly_chart(forecast_fig, use_container_width=True)

# st.subheader("Forecast Table")

# st.dataframe(forecast_df, use_container_width=True)

# st.subheader("Detected Anomalies")

# anomalies = anomaly_df[anomaly_df["iforest_anomaly"] == True]

# st.dataframe(anomalies, use_container_width=True)

# st.markdown("---")

# st.caption(
#     "Supply Chain Demand Forecasting Dashboard | "
#     "Built with Streamlit, Plotly, Pandas and ARIMA"
# )

# import pandas as pd

# clean_df = pd.read_csv("data/processed/clean_sales.csv")
# print(clean_df.columns.tolist())

# forecast_df = pd.read_csv("data/processed/future_forecast.csv")

# print(forecast_df.columns.tolist())


import streamlit as st
import pandas as pd
import plotly.express as px

# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="Supply Chain Demand Forecasting", page_icon="📦", layout="wide"
)


# =====================================================
# HEADER
# =====================================================

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


# =====================================================
# LOAD DATA (CACHED)
# =====================================================


@st.cache_data
def load_data():

    clean = pd.read_csv("data/processed/clean_sales.csv", parse_dates=["date"])

    forecast = pd.read_csv("data/processed/future_forecast.csv", parse_dates=["date"])

    anomaly = pd.read_csv("data/processed/anomaly_detection.csv")

    return clean, forecast, anomaly


clean_df, forecast_df, anomaly_df = load_data()


# =====================================================
# SIDEBAR FILTERS
# =====================================================

st.sidebar.title("Dashboard Filters")
st.sidebar.markdown("---")


stores = sorted(clean_df["store_id"].unique())

selected_store = st.sidebar.selectbox("Select Store", stores)


items = sorted(clean_df[clean_df["store_id"] == selected_store]["item_id"].unique())


selected_item = st.sidebar.selectbox("Select Item", items)


start_date = st.sidebar.date_input("Start Date", clean_df["date"].min())


end_date = st.sidebar.date_input("End Date", clean_df["date"].max())

forecast_days = st.sidebar.slider(
    "Forecast Horizon (Days)", min_value=30, max_value=180, value=90, step=30
)


# =====================================================
# FILTER DATASET
# =====================================================

filtered_df = clean_df[
    (clean_df["store_id"] == selected_store)
    & (clean_df["item_id"] == selected_item)
    & (clean_df["date"] >= pd.to_datetime(start_date))
    & (clean_df["date"] <= pd.to_datetime(end_date))
]


forecast_filtered = forecast_df.head(forecast_days)


anomaly_filtered = anomaly_df[
    (anomaly_df["store_id"] == selected_store)
    & (anomaly_df["item_id"] == selected_item)
    & (anomaly_df["iforest_anomaly"] == True)
]


# =====================================================
# EMPTY DATA CHECK
# =====================================================

if filtered_df.empty:

    st.warning("No data available for the selected filters.")

    st.stop()


# =====================================================
# FILTER SUMMARY
# =====================================================

st.info(f"""
    **Selected Store:** {selected_store}

    **Selected Item:** {selected_item}

    **Date Range:** {start_date} → {end_date}
    """)


# =====================================================
# KPI CARDS
# =====================================================

total_sales = filtered_df["sales"].sum()

average_sales = filtered_df["sales"].mean()

max_sales = filtered_df["sales"].max()

forecast_total = forecast_filtered["forecast_sales"].sum()


col1, col2, col3, col4 = st.columns(4)


col1.metric("Total Sales", f"{total_sales:,.0f}", delta=f"{average_sales:.1f} Avg/day")


col2.metric("Average Daily Sales", f"{average_sales:.2f}", delta="Daily")


col3.metric("Maximum Daily Sales", f"{max_sales:.0f}", delta="Peak")


col4.metric("90-Day Forecast", f"{forecast_total:,.0f}", delta="Future Demand")


# =====================================================
# DATASET SUMMARY
# =====================================================

st.subheader("📌 Dataset Summary")


summary1, summary2, summary3 = st.columns(3)


summary1.info(f"🏪 Stores: {clean_df['store_id'].nunique()}")


summary2.info(f"📦 Items: {clean_df['item_id'].nunique()}")


summary3.info(f"📄 Records: {len(clean_df):,}")


# =====================================================
# SALES ANALYSIS CHART
# =====================================================

st.subheader("📊 Sales Analysis")


sales_fig = px.line(
    filtered_df,
    x="date",
    y="sales",
    title=f"Sales Trend - Store {selected_store}, Item {selected_item}",
)

sales_fig.update_traces(line_width=3)


hist_fig = px.histogram(
    filtered_df, x="sales", nbins=30, title="Distribution of Daily Sales"
)


left_col, right_col = st.columns(2)


with left_col:

    st.plotly_chart(sales_fig, use_container_width=True, key="historical_sales")


with right_col:

    st.plotly_chart(hist_fig, use_container_width=True, key="sales_distribution")


# =====================================================
# MONTHLY SALES
# =====================================================

st.subheader("📅 Monthly Sales")


monthly_sales = (
    filtered_df.set_index("date").resample("ME")["sales"].sum().reset_index()
)


monthly_fig = px.bar(monthly_sales, x="date", y="sales", title="Monthly Sales")


st.plotly_chart(monthly_fig, use_container_width=True, key="monthly_sales")


# =====================================================
# FORECAST CHART
# =====================================================


st.subheader("🔮 Historical vs Forecast Demand")

if not forecast_filtered.empty:

    forecast_fig = px.line(
        forecast_filtered,
        x="date",
        y="forecast_sales",
        title=f"{forecast_days}-Day Demand Forecast",
    )

    forecast_fig.update_traces(name="Historical Sales", line_color="blue")

    forecast_fig.add_scatter(
        x=forecast_filtered["date"],
        y=forecast_filtered["forecast_sales"],
        mode="lines",
        name="Forecast",
        line=dict(color="red", dash="dash"),
    )

    st.plotly_chart(forecast_fig, use_container_width=True, key="forecast_chart")

else:

    st.warning("No forecast available for the selected store and item.")


# =====================================================
# FORECAST TABLE
# =====================================================

st.subheader("Forecast Table")


st.dataframe(forecast_filtered, use_container_width=True)

forecast_csv = forecast_filtered.to_csv(index=False).encode("utf-8")


st.download_button(
    label="📥 Download Forecast CSV",
    data=forecast_csv,
    file_name="future_forecast.csv",
    mime="text/csv",
)


# =====================================================
# ANOMALY TABLE
# =====================================================

st.subheader("🚨 Detected Anomalies")


if anomaly_filtered.empty:

    st.success("No anomalies detected for this selection.")

else:

    st.dataframe(anomaly_filtered, use_container_width=True)


# =====================================================
# ABOUT SECTION
# =====================================================

with st.expander("ℹ️ About this Project"):

    st.write("""
    This dashboard was developed for a Supply Chain
    Demand Forecasting project.

    Technologies Used:

    • Python

    • Pandas

    • Streamlit

    • Plotly

    • Scikit-learn

    • Statsmodels (ARIMA)

    Features:

    • Historical Sales Analysis

    • Demand Forecasting

    • Anomaly Detection

    • Interactive Filtering

    • Forecast Export
    """)


# =====================================================
# FOOTER
# =====================================================

st.markdown("---")


st.caption(
    "Supply Chain Demand Forecasting Dashboard | "
    "Built with Streamlit, Plotly, Pandas and ARIMA"
)
