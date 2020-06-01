import matplotlib.pyplot as plt
import pickle

# load data
with open(r'C:\Users\Katja\PythonCodingTraining\DataVisualization\data-viz\matplotlib\coding-exp-by-dev-type.pickle', 'rb') as file:
    data = pickle.load(file)

# Split into two lists
dev_types, years_exp = zip(*data)

bar_coords = range(len(dev_types))

# barh stands for horizontal bar chart
plt.barh(bar_coords, years_exp)
plt.xlabel('years')
plt.title('Years of Coding Experience by Developer Type')
plt.yticks(bar_coords, dev_types, fontsize = 8)
# The following function gets rid of any white space and condenses the function
plt.tight_layout()
plt.show()