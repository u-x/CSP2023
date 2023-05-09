# a322_electricity_trends.py
# This program uses the pandas module to load a 3-dimensional data sheet into a pandas DataFrame object
# Then it will use the matplotlib module to plot comparative line graphs 

import matplotlib.pyplot as plt
import pandas as pd
import random

# choose countries of interest
my_countries = ['Sierra Leone', "Malawi", "Somalia", "South Sudan", "Central African Republic"]

# Load in the data with read_csv()
df = pd.read_csv("elec_access_data.csv", header=0)    # header=0 means there is a header in row 0

# get a list unique countries
unique_countries = df['Entity'].unique()

print(unique_countries)

# Plot the data on a line graph
for c in unique_countries:
  if c in my_countries:
    
    # match country to one of our we want to look at and get a list of years
    years = df[df['Entity'] == c]['Year']

    # match country to one of our we want to look at and get a list of electriciy values
    sum_elec = df[df['Entity'] == c]['Access']
    line_styles = ['-.', ':', '--', '-']
    markers = ["o", "v", "^", "<", ">", "8", "s", "X", "P", "d", "D", "H", "h", "*", "p"]
    plt.plot(years, sum_elec, label=c, marker=markers[random.randint(0, len(markers) - 1)], linestyle=line_styles[random.randint(0, len(line_styles) - 1)])


plt.ylabel('Percentage of Country Population')
plt.xlabel('Year')
plt.title('Percent of Population with Access to Electricity')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.tight_layout()
plt.show()
