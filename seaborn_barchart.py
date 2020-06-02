# Plotting functionality is in pyplot
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
import os

import matplotlib.pyplot as plt
import pickle

# load data
with open(r'C:\Users\Katja\PythonCodingTraining\DataVisualization\data-viz\matplotlib\coding-exp-by-dev-type.pickle', 'rb') as file:
    data = pickle.load(file)

# Split into two lists
dev_types, years_exp = zip(*data)
dev_types = list(dev_types)
years_exp = list(years_exp)


axes = sns.barplot(x = years_exp, y = dev_types)
axes.set_xlabel('years')
axes.set_title('Years of Coding Experience by Developer Type')
# The following function gets rid of any white space and condenses the function
plt.tight_layout()
plt.show()