
import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv("data.csv")

# Create Revenue column
df["Revenue"] = df["Price"] * df["Quantity"]

# Title
st.title("📊 E-commerce Metrics Dashboard")

# Show data
st.subheader("Dataset")
st.write(df)

# KPIs
st.subheader("Key Metrics")
st.write("Total Revenue:", df["Revenue"].sum())
st.write("Total Orders:", df["OrderID"].count())
st.write("Total Customers:", df["CustomerID"].nunique())

import matplotlib.pyplot as plt

# Revenue by Product
st.subheader("Revenue by Product")
product_sales = df.groupby("Product")["Revenue"].sum()
st.bar_chart(product_sales)

# Sales over time
st.subheader("Sales Over Time")
df["Date"] = pd.to_datetime(df["Date"])
sales_time = df.groupby("Date")["Revenue"].sum()
st.line_chart(sales_time)

st.sidebar.header("Filters")

category = st.sidebar.selectbox("Select Category", df["Category"].unique())

(filtered_df) = df[df["Category"] == category]

from sklearn.cluster import KMeans

# Prepare data
customer_data = df.groupby("CustomerID")["Revenue"].sum().reset_index()

# Apply KMeans
kmeans = KMeans(n_clusters=3)
customer_data["Cluster"] = kmeans.fit_predict(customer_data[["Revenue"]])

st.subheader("Customer Segmentation")
st.write(customer_data)

st.metric("💰 Total Revenue", df["Revenue"].sum())
st.metric("🛒 Orders", df["OrderID"].count())
st.metric("👥 Customers", df["CustomerID"].nunique())

