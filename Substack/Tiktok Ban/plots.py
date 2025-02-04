import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 
import time
from pytrends.request import TrendReq

# Initialize Pytrends with geo set to 'US'
pytrends = TrendReq(hl='en-US', tz=360, retries=3, backoff_factor=0.1)
kw_list = ["Rednote"]  
timeframe = "2024-12-01 2025-01-31"
pytrends.build_payload(kw_list, cat=0, timeframe=timeframe, geo='US')
time.sleep(5)
data = pytrends.interest_over_time().reset_index()
max_interest_row = data.loc[data['Rednote'].idxmax()]
plt.figure(figsize=(12, 6))
sns.lineplot(data=data, x="date", y="Rednote", marker="o", color="#9333ea")
plt.title("Google Trends {Dec 1st 2024 - Jan 31 2025}: Rednote", fontsize = 14, loc = 'left')
plt.xlabel("Date")
plt.ylabel("Interest Level")
plt.xticks(rotation=45)
plt.grid(False)
sns.despine(bottom = True, left = True)
plt.xticks([])
plt.yticks([])
plt.gca().tick_params(axis='y', length=0)
plt.xlabel("")
plt.ylabel("")
plt.annotate(f"Peak Interest on {max_interest_row['date'].strftime('%Y-%m-%d')}", 
             xy=(max_interest_row['date'], max_interest_row['Rednote']), 
             xytext=(max_interest_row['date'], max_interest_row['Rednote'] + 10),
             arrowprops=dict(facecolor='black', shrink=0.05))
plt.show()

kw_list = ["Learn Mandarin","Learn Chinese"] 
pytrends.build_payload(kw_list, cat=0, timeframe=timeframe, geo='US')
time.sleep(5)
data = pytrends.interest_over_time().reset_index()

data.drop(columns = 'isPartial',inplace = True)
data.rename(columns = {'Learn Mandarin':'Mandarin','Learn Chinese':'Chinese'},inplace = True)
data['date'] = pd.to_datetime(data['date'])
df_plot = data.melt(id_vars='date', value_vars=['Mandarin', 'Chinese'], var_name='Search Term', value_name='Value')
plt.figure(figsize=(10, 6))
sns.lineplot(data=df_plot, x='date', y='Value', hue='Search Term')
plt.title('Learn Mandarin and Learn Chinese Search Interest (Dec 1st 2024 to Jan 31st 2025)',loc = 'left',fontsize = 14, pad = 10)
plt.xlabel("Date")
plt.xticks([])
plt.gca().tick_params(axis='y', length=0)
plt.xlabel("")
plt.ylabel("")
plt.grid(False)
sns.despine(bottom  = 'True', left = 'True')
plt.tight_layout()
plt.show()

sensor_data_report = pd.read_csv('data.csv')
plt.figure(figsize=(10, 6))
sns.barplot(data = sensor_data_report,y=platforms, x=ad_spend_share, color = '#9333ea')
# plt.xlabel("Share of US Digital Ad Spend (%)")
# plt.ylabel("Social Media Platform")
plt.xticks([])
plt.title("Share of US Digital Ad Spend on Social Media Platforms (2024)",loc = 'left',fontsize = 14, pad = 10)
plt.text(40,8.2, "Data : Sensor Tower", ha='right', va='center', fontsize=10, color='gray')
plt.xlim(0, 40)  # Adjust the x-axis range for clarity
for index, value in enumerate(ad_spend_share):
    plt.text(value + 0.25, index, f"{value}%", va='center')
sns.despine(left = True, bottom = True)
ax = plt.gca()
ax.tick_params(axis='x', length=0)  
ax.tick_params(axis='y', length=0)  
plt.show()

highlight_platform = "TikTok"

highlight_mask = data['Platform'] == highlight_platform
gray_mask = data['Platform'] != highlight_platform

# Gray bars for all platforms except TikTok
sns.barplot(data = sensor_data_report,
    x='Platform', 
    y='Hours/Day (Millions)', 
    hue='Quarter', 
    data=data[gray_mask], 
    palette={'Quarter 1 : 2024': 'gray', 'Quarter 4 : 2024': 'gray'},
    alpha=0.7,  
    edgecolor='white',
    linewidth=1
)

# Highlighted Bars for TikTok
sns.barplot(data = sensor_data_report, 
    x='Platform', 
    y='Hours/Day (Millions)', 
    hue='Quarter', 
    data=data[highlight_mask], 
    palette={'Quarter 1 : 2024': '#9333ea', 'Quarter 4 : 2024': '#9333ea'},
    edgecolor='white',
    linewidth=1
)

plt.title("Time Spent on Short-Form Video Platforms : Q1 and Q4 2024", fontsize=14, loc='left', pad=10)
plt.text(-0.5, 90, "• United States  • Millions of Hours per day • Data : Sensor Tower", fontsize=10, color='gray')

# Remove ticker marks and legend
ax = plt.gca()
ax.tick_params(axis='x', length=0)  
ax.tick_params(axis='y', length=0)  
ax.get_legend().remove()
ax.set_xlabel("")
ax.set_ylabel("")

plt.tight_layout()
sns.despine(left=True, bottom=True)
plt.show()

fig, ax = plt.subplots(figsize=(10, 6))

colors = ['#9333ea' if platform == 'TikTok' else 'gray' for platform in platforms]
alphas = [1 if platform == 'TikTok' else 0.5 for platform in platforms] 

for platform, spend, color, alpha in zip(platforms, spending, colors, alphas):
    ax.bar(platform, spend, color=color, alpha=alpha)

ax.set_title("Consumer Spend on Social Media Apps, Millions (US, 2024)", 
             fontsize=14, loc='left', pad=10)
# Subtitle
fig.text(0.125, 0.86,"TikTok brought in ~$1.7bn which is more than Instagram, Facebook, YouTube, and Snapchat combined" ,fontsize=10, color='gray', ha='left')

# Remove ticker marks
ax.tick_params(axis='x', length=0)  
ax.tick_params(axis='y', length=0)  

sns.despine(bottom=True, left=True)
plt.show()

plt.barh(data = data_sorted, advertisers, growth_rates, color='#9333ea')
plt.title("Top Ten Advertisers on TikTok (2024)", loc='left', fontsize = 14, pad = 10)
plt.text(0.19, 0.98, "• Year-on-Year Growth 23-24 • Data : Adweek", ha='center', va='bottom', fontsize=10, color='gray', transform=plt.gca().transAxes)

for i, v in enumerate(sorted_growth_rates):
    plt.text(v + 2, i, f'{v}%', va='center')

sns.despine(bottom=True, left=True)

plt.tight_layout()
ax = plt.gca()
ax.tick_params(axis='x', length=0)  
ax.tick_params(axis='y', length=0)
plt.xticks([])
plt.show()
