# Plotting functionality is in pyplot
import matplotlib.pyplot as plt
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

# The following list will help telling Python where to locate the bars
bar_coords = range(len(fruit))

# Create plot
# First argument are the x-axes coordinates, second y-axes coordinates
plt.bar(bar_coords, num_sold)
# Numbers on x-axis are replaced with fruit names
plt.xticks(bar_coords, fruit)
# Label y axis
plt.ylabel('Number of fruits sold in millions')
# Label the chart
plt.title('Fruit sold (2017)')
plt.show()