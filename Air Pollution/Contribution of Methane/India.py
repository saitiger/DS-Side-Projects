import matplotlib.pyplot as plt
import seaborn as sns

# Color palette from the provided image
colors = ['#7BA5B3', '#F7A23F', '#E55634', '#3C5F74']

# Sector Data
sector_data = {
    'Energy': 73,
    'Agriculture': 16,
    'Industrial Processes': 8,
    'Waste': 3
}

# Pollutant Data
pollutant_data = {
    'CO2': 77,
    'CH4': 16,
    'N2O': 6,
    'F-Gases': 1
}

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

def create_pie_chart(ax, data, title):
    wedges, texts, autotexts = ax.pie(
        data.values(),
        labels=data.keys(),
        autopct='%1.1f%%',
        colors=colors,
        startangle=90,
        textprops={'color': 'white', 'fontweight': 'bold'}
    )

    plt.setp(autotexts, size=10)
    plt.setp(texts, size=10)

    ax.set_title(title, fontsize=14, fontweight='bold')

create_pie_chart(ax1, sector_data, 'Distribution of GHG Emissions in India by Sector')

create_pie_chart(ax2, pollutant_data, 'Distribution of GHG Emissions in India by Pollutant')
plt.tight_layout()
plt.show()
