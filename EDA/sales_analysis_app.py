import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from dowhy import CausalModel
import networkx as nx

df = pd.read_excel('Sales Analysis.xlsx')
df.rename(columns = {"Sales ('000, USD)":"Sales"}, inplace=True)

# Title for Streamlit App
st.title("Sales Data Analysis and Causal Inference")

# Display data preview
st.header("Data Preview")
st.write(df.head())

# EDA: Displaying key metrics
st.header("Exploratory Data Analysis")

# 1. Total Sales
total_sales = df["Sales"].sum()

# 2. Sales by Region
sales_by_region = df.groupby('Region')["Sales"].sum().sort_values(ascending=False)

# 3. Sales by Product
sales_by_product = df.groupby('Product')["Sales"].sum().sort_values(ascending=False)

# 4. Number of Orders by Customer
orders_by_customer = df['Customer Name'].value_counts().head(10)

# 5. Average Sales per Order
average_sales_per_order = df["Sales"].mean()

# 6. Sales by Origin
sales_by_origin = df.groupby('Origin')["Sales"].sum().sort_values(ascending=False)

# 7. Percentage of Refunded Orders
refund_percentage = df['Refunded'].mean() * 100

# 8. Time taken from Registration to Purchase
df['Time to Purchase (days)'] = (df['Purchased At'] - df['Registered At']).dt.days
average_time_to_purchase = df['Time to Purchase (days)'].mean()

# 9. Sales distribution over time (Registered At)
sales_over_time = df.groupby(df['Registered At'].dt.date)["Sales"].sum()

# 10. Correlation between Refunds and Sales Amount
refund_sales_correlation = df['Refunded'].astype(int).corr(df["Sales"])

# Display metrics
st.write(f"**Total Sales (in '000 USD):** {total_sales}")
st.write(f"**Average Sales per Order:** {average_sales_per_order}")
st.write(f"**Refund Percentage:** {refund_percentage}%")
st.write(f"**Average Time to Purchase (days):** {average_time_to_purchase} days")

# Display Sales by Region
st.subheader("Sales by Region")
st.bar_chart(sales_by_region)

# Display Sales by Product
st.subheader("Sales by Product")
st.bar_chart(sales_by_product)

# Display Top 10 Customers by Orders
st.subheader("Top 10 Customers by Orders")
st.write(orders_by_customer)

# Display Sales by Origin
st.subheader("Sales by Origin")
st.bar_chart(sales_by_origin)

# Display Sales over Time
st.subheader("Sales Over Time")
st.line_chart(sales_over_time)

# Correlation Analysis
st.header("Correlation Analysis")

# Correlation Matrix
correlation_matrix = df.corr(numeric_only=True)

# Plot Correlation Matrix
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, fmt=".2f", ax=ax)
ax.set_title('Correlation Matrix')
st.pyplot(fig)

# Causal Inference
# st.header("Causal Inference")

# Define the causal model
# model = CausalModel(
#     data=df,
#     treatment='Some_Treatment_Variable',  # replace with your treatment variable
#     outcome='Sales',
#     graph='digraph { Some_Treatment_Variable -> Sales; Some_Confounder -> Sales; Some_Treatment_Variable -> Some_Confounder; }'  # replace with your causal graph
# )

# Render the causal model graph
# st.subheader("Causal Model Graph")
# fig, ax = plt.subplots(figsize=(10, 8))
# model.view_model(layout='dot')
# st.pyplot(fig)

# Identify the effect
# identified_estimand = model.identify_effect()
# st.write("Identified Estimand:")
# st.write(identified_estimand)

# Estimate the effect
# causal_estimate = model.estimate_effect(identified_estimand, method_name="backdoor.linear_regression")
# st.write("Causal Estimate:")
# st.write(causal_estimate)

# Refutation using placebo treatment
# refutation = model.refute_estimate(identified_estimand, causal_estimate, method_name="placebo_treatment_refuter")
# st.write("Refutation Summary:")
# st.write(refutation)

# Display results
# st.write("**Estimated Causal Effect:**", causal_estimate.value)
# st.write("**Refutation (Placebo Treatment):**", refutation)
