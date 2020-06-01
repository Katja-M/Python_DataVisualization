import matplotlib.pyplot as plt
import pickle

# load data
with open(r'C:\Users\Katja\PythonCodingTraining\DataVisualization\data-viz\matplotlib\prog-langs-popularity.pickle', 'rb') as file:
    data = pickle.load(file)

# split into two lists
languages, rankings = zip(*data)
# The popularity of a coding language is a function of time
# Hence, a line chart is a good chart

# Building a single line plot

# 1. Get the Java years and ranks
# by splitting Java data into two lists
java_years, java_ranks = zip(*rankings[0])
print(java_years)
print(java_ranks)

plt.plot(java_years, java_ranks)
# Without the following line, the years will be shown as decimals
plt.xticks(java_years)
plt.ylabel('Ranking')
plt.xlabel('Years')
plt.title('Java Ranking')
plt.show()