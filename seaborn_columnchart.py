# Plotting functionality is in pyplot
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
import os

print(os.getcwd())

# load data (rb = reading binary data)
# The r in front of the path tells python to interpret the string as a raw string
with open(r'C:\Users\Katja\PythonCodingTraining\DataVisualization\data-viz\matplotlib\fruit-sales.pickle', 'rb') as file:
    data = pickle.load(file)

print(data)

# Splitting a list of tuples into two lists
# The star in front of data is required for the splitting
fruit, num_sold = zip(*data)
# Seaborn works with lists
fruit = list(fruit)
num_sold = list(num_sold)

# In Seaborn, the coordinates do not have to be specified

# Create plot
axes = sns.barplot(x = fruit, y = num_sold)
axes.set_title('Fruit sold (2017)')
axes.set_ylabel('Number of fruits sold in millions')
plt.show()