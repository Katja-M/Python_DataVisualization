import matplotlib.pyplot as plt
import pickle

# load data
with open(r'C:\Users\Katja\PythonCodingTraining\DataVisualization\data-viz\matplotlib\prog-langs-popularity.pickle', 'rb') as file:
    data = pickle.load(file)

# split into two lists
languages, rankings = zip(*data)
# The popularity of a coding language is a function of time
# Hence, a line chart is a good chart

# Building a multi line plot

# Iterate over all of the language and call 'plot' on their data
for i in range(len(languages)):
    # for each language, split their data into years and rankings lists
    years, ranks = zip(*rankings[i])
    plt.plot(years, ranks)


plt.xlabel('Year')
plt.ylabel('Ranking')
plt.title('Rankings of programming languages')
# Adding legend in order to explain different colouring
# The order is retained because the order of the languages and values was not change when the 
# zip function was used
plt.legend(languages)
plt.show()