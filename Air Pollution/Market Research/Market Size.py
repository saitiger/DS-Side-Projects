import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Data.csv")

# Stack the values
total_values = np.sum(df['market_size'], axis=1)
colors = ["#4B0082", "#8A2BE2", "#6495ED", "#87CEEB", "#DDA0DD", "#000000"]

# Plot the stacked bar chart
fig, ax = plt.subplots(figsize=(10, 6))
ax.stackplot(df['years'], df['categories'].T, labels=df['categories'], colors=colors)

# Labels and title
ax.set_title("U.S. Gas Detection Equipment Market\nSize, by Technology, 2020 - 2030 (USD Billion)", fontsize=14, fontweight="bold")
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Market Size (USD Billion)", fontsize=12)
ax.legend(loc="upper left", fontsize=10)

# CAGR annotation
ax.annotate("10.1%\nU.S. Market CAGR,\n2024 - 2030",
            xy=(2029, 3.5), xycoords='data',
            fontsize=12, fontweight='bold', color='#4B0082',
            bbox=dict(boxstyle="round,pad=0.3", edgecolor='#4B0082', facecolor='white'))

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Calculate total values
total_values = np.sum(values, axis=1)

# Plot bar chart of total market size over the years
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(years, total_values, color='#4B0082', label="Total Market Size")

# Labels and title
# ax.set_title("U.S. Gas Detection Equipment Market\nTotal Market Size, 2020 - 2030 (USD Billion)", fontsize=14, fontweight="bold")
# ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Market Size (USD Billion)", fontsize=12)
# ax.legend()
# plt.grid(axis='y', linestyle='--', alpha=0.7)
sns.despine()
plt.show()

# Filter data from 2024 onwards
start_index = np.where(years == 2024)[0][0]
years = years[start_index:]
values = values[start_index:]

total_values = np.sum(values, axis=1)

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(years, total_values, color='#dade85', label="Total Market Size")

ax.set_title("U.S. Gas Detection Equipment Market\nTotal Market Size, (USD Billion)", fontsize=14, fontweight="bold")
ax.set_ylabel("Market Size", fontsize=12)

sns.despine()
plt.show()

# Plot CAGR line
start_year, end_year = years[0], years[-1]
start_value, end_value = total_values[0], total_values[-1]
cagr = ((end_value / start_value) ** (1 / (end_year - start_year)) - 1) * 100
ax.plot(years, total_values[0] * (1 + 10.1 / 100) ** (years - start_year), linestyle='--', color='red', label="CAGR 10.1%")

# Annotation for CAGR
ax.annotate("CAGR 10.1%", xy=(2027, total_values[0] * (1 + 10.1 / 100) ** (2027 - start_year)), 
             xytext=(2023, total_values[-1] * 0.5), arrowprops=dict(arrowstyle='->', color='red'), color='red', fontsize=12)

# Labels and title
ax.set_title("U.S. Gas Detection Equipment Market\nTotal Market Size, 2020 - 2030 (USD Billion)", fontsize=14, fontweight="bold")
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Market Size (USD Billion)", fontsize=12)
ax.legend()

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
