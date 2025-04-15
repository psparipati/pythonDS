import pandas as pd

population = pd.read_csv('https://www.kaggle.com/datasets/iamsouravbanerjee/world-population-dataset')
pd.set_option('display.max_rows', None)

# Look at the number of countries whose populations decreased from 2010 to 2020.
print((population['2010 Population'] > population['2020 Population']).sum())
print(population[population['2010 Population'] > population['2020 Population']].shape)
print(*list(population['Country/Territory'][population['2010 Population'] > population['2020 Population']]))
print("\n")

# Look at the number of countries who contributed to more than 1% of the world's population.
print((population['World Population Percentage'] > 1).sum())
print(population[population['World Population Percentage'] > 1].shape)
print(*list(population['Country/Territory'][population['World Population Percentage'] > 1]))
print("\n")

# Compute the arithmetic population density of each country and display in decreasing order.
population['2020 Population Density'] = population['2020 Population'] / population['Area (km²)']
print(population.sort_values(by='2020 Population Density', ascending=False)[['Country/Territory', '2020 Population Density']])
print("\n")