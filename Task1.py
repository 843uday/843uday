import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv(r'C:\Users\uday\Desktop\python\population.csv')
data.head(266)
countries_to_plot = ['East Asia & Pacific', 'South Asia', 'Sub-Saharan Africa', 'Europe & Central Asia', 'Africa Eastern and Southern', 'Latin America & Caribbean','Africa Western and Central','Middle East & North Africa','Arab World','European Union','North America','Euro area','Russian Federation', 'World']

filtered_data = data[data['Country Name'].isin(countries_to_plot)]

plt.bar (filtered_data['Country Name'], filtered_data['2022'])
plt.xlabel ('Country Name')
plt.ylabel ('Population in 2022')
plt.title('Population of selected countries in 2022')
plt.xticks(rotation=45, ha='right') 
plt.show()

plt.bar (filtered_data['Country Name'], filtered_data['1960'])
plt.xlabel ('Country Name')
plt.ylabel ('Population in 1960')
plt.title('Population of selected countries in 1960')
plt.xticks(rotation=45, ha='right') 
plt.show()

plt.bar (filtered_data['Country Name'], filtered_data['2022'] - filtered_data['1960'] )
plt.xlabel ('Country Name')
plt.ylabel ('Population change')
plt.title('Change in population')
plt.xticks(rotation=45, ha='right') 
plt.show()
