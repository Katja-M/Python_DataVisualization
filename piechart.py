import matplotlib.pyplot as plt
import pickle

with open(r'C:\Users\Katja\PythonCodingTraining\DataVisualization\data-viz\matplotlib\devs-outside-time.pickle', 'rb') as file:
    data = pickle.load(file)

# split into two lists
time, responses = zip(*data)
# The pie chart makes sense here because the responses are given in percentages


# The argument splits the pie but there are no further information given
plt.pie(responses, labels = time, autopct = '%.2f%%')
# autopct: f stand for fraction; d for integer '%d%%'
# Force the x/y axes to have the same scale
plt.axis('equal')
plt.title('Daily Time Developers Spend Outside')
plt.show()

