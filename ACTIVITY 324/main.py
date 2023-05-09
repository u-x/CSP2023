import matplotlib.pyplot as plt
import pandas
df = pandas.read_csv('honey.csv')

df['Value'] = df['Value'].str.replace(',', '')
df['Value'] = pandas.to_numeric(df['Value'], errors='coerce')
df.dropna(subset=['Value'], inplace=True)

print(df['Value'])

unique_states = df['State'].unique()

all_honey = []
all_states = []
hivol = 4522819.0
medvol = 1006464.0 + 1
  
# with grouping
for state in unique_states:
  honey_data = df[df['State'] == state].groupby('Year')['Value']
  sum_honey_data = honey_data.sum()
  # print (state, honey_data.sum())
  all_honey.append(sum_honey_data)
  all_states.append(state)

fig, ax = plt.subplots(1,3,figsize=(16,9))
fig.set_figheight(2.5)

anchor_x = 0.5
anchor_y = -0.4

for i in range(0, len(all_honey), 1):
  honey = all_honey[i]
  state = all_states[i]
  years = honey.keys()
  print(years)
  print(honey)
  if (sum(honey) > hivol):
    ax[0].plot(years, honey, label=state, linestyle="--", marker="o")
  elif (sum(honey) > medvol):
    ax[1].plot(years, honey, label=state, linestyle="--", marker="o")
  else:
    ax[2].plot(years, honey, label=state, linestyle="--", marker="o")

# large config
ax[0].set_title("Large Honey Producers")
ax[0].set_xlabel("Year")
ax[0].set_ylabel("Production Levels")
ax[0].legend(loc='center', fontsize='small', bbox_to_anchor=(anchor_x, anchor_y), ncol=3)
# medium config
ax[1].set_title("Medium Honey Producers")
ax[1].set_xlabel("Year")
ax[1].set_ylabel("Production Levels")
ax[1].legend(loc='center', fontsize='small', bbox_to_anchor=(anchor_x, anchor_y), ncol=3)
# small config
ax[2].set_title("Small Honey Producers")
ax[2].set_xlabel("Year")
ax[2].set_ylabel("Production Levels")
ax[2].legend(loc='center', fontsize='small', bbox_to_anchor=(anchor_x, anchor_y), ncol=3)

plt.tight_layout()
plt.show()

fig, ax = plt.subplots(1,2,figsize=(16,9))
fig.set_figheight(8)

unique_years = df['Year'].unique()

for state in unique_states:
  totals = df[df['State'] == state].groupby("Year")["Value"]
  avg_honey = totals.mean()
  ax[0].plot(avg_honey.keys(), avg_honey, label=state)

for year in unique_years:
  totals = df[df["Year"] == year].groupby("Year")["Value"]
  totals_sum = totals.sum()
  ax[1].bar(totals_sum.keys(), totals_sum, label=year)

ax[0].set_ylabel("Honey Production Average")
ax[0].set_xlabel("Years")
ax[0].set_title("State Averages")

ax[1].set_ylabel("Production")
ax[1].set_xlabel("Years")
ax[1].set_title("USA Total Production")
plt.tight_layout()
plt.show()