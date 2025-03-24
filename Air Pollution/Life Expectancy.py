import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('Life Expectancy.csv')
df_sorted = df.sort_values(by='Life Expectancy', ascending=False)
top_2_countries = df_sorted.head(2)
bottom_country = df_sorted.tail(1)
selected_countries = pd.concat([top_2_countries, bottom_country])

# print(selected_countries)

plt.figure(figsize=(10, 6))
sns.set_style("white")
bar_color = '#007bff'
ax = sns.barplot(x='Country', y='Life Expectancy Gain', data=selected_countries, color=bar_color)

plt.title('Average Life Expectancy Gains if WHO Air Quality Guidelines Were Met', fontsize=14)
plt.xlabel('')  
plt.ylabel('')  
for i, v in enumerate(selected_countries['Life Expectancy Gain']):
    ax.text(i, v, f'+{v}', ha='center', va='bottom', fontsize=10)

sns.despine(left=True, bottom=True)
ax.set_yticks([])
plt.tight_layout()
plt.show()
