import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('health_issues.csv')

data = data.sort_values('Percentage', ascending=False).reset_index(drop=True)
plt.figure(figsize=(12, 8))

ax = sns.barplot(
    x='Percentage', 
    y='Health Issue', 
    data=data, 
    color='#a0b1c0',  
    orient='h'
)

for i, v in enumerate(data['Percentage']):
    ax.text(v + 0.5, i, f"{v}%", va='center', ha='left')

air_pollution_index = data[data['Health Issue'] == 'Air pollution'].index[0]
ax.patches[air_pollution_index].set_facecolor('#007bff')
ax.tick_params(axis='y', length=0)
ax.set_ylabel('')
ax.set_xticks([])
ax.set_xlabel('')

for spine in ax.spines.values():
    spine.set_visible(False)
plt.figtext(0.01, 0.97, "Share of U.S. respondents feeling very/rather worried about the following health-related issues", 
            fontsize=14, ha='left')
plt.figtext(0.01, 0.94, "2,074 U.S. respondents (18-80 y/o) surveyed Nov. 10-23, 2023. Multiple selections possible", 
            fontsize=10, ha='left', alpha=0.7)
plt.figtext(0.01, 0.91, "Source: Statista Consumer Insights", 
            fontsize=9, ha='left', alpha=0.7)
plt.xlim(0, 70)
plt.subplots_adjust(left=0.15, right=0.95, top=0.85, bottom=0.05)
plt.show()
