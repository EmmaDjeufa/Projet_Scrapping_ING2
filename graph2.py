import pandas as pd
import matplotlib.pyplot as plt


# Read CSV file
csv_loader = pd.read_csv('./result7.csv')

# Group values by column name
# You can use the first grouped_values or the second, just uncomment one and comment the other

#grouped_values = csv_loader.groupby('National Administrator')['For issuance to not new entrants'].sum().plot(kind='pie', xlabel="Country", ylabel="Allocations to Stationary Installations")
#grouped_values = csv_loader.groupby('EU ETS Phase')['For issuance to not new entrants'].sum().plot(kind='pie', xlabel="Phase", ylabel="Allocations to Stationary Installations")

grouped_values = csv_loader.groupby('National Administrator')['For issuance to not new entrants'].sum().plot(kind='pie', autopct='%1.0f%%', pctdistance=1.1, labeldistance=1.2)
#grouped_values = csv_loader.groupby('EU ETS Phase')['For issuance to not new entrants'].sum().plot(kind='pie', autopct='%1.0f%%', pctdistance=1.1, labeldistance=1.2)
# Configuration to show the plot
plt.ticklabel_format(style='plain', axis='y')

# Show the plot
plt.show()

