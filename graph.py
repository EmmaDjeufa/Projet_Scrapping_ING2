import pandas as pd
import matplotlib.pyplot as plt


# Read CSV file
csv_loader = pd.read_csv('./result.csv')

# Group values by column name
# You can use the first grouped_values or the second, just uncomment one and comment the other

grouped_values = csv_loader.groupby('National Administrator')['For issuance to not new entrants'].sum().plot(kind='bar', xlabel="Country", ylabel="Allocations to Stationary Installations")
#grouped_values = csv_loader.groupby('EU ETS Phase')['For issuance to not new entrants'].sum().plot(kind='bar', xlabel="Phase", ylabel="Allocations to Stationary Installations")


# Configuration to show the plot
plt.ticklabel_format(style='plain', axis='y')

# Show the plot
plt.show()
