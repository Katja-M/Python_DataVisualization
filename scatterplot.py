import matplotlib.pyplot as plt
import pickle

with open(r'C:\Users\Katja\PythonCodingTraining\DataVisualization\data-viz\matplotlib\iris.pickle', 'rb') as file:
    iris = pickle.load(file)

print(iris)

# Extract the first column from the data table
sepal_length = iris['data'][:,0]
    # [:,0]: all of the rows but only the first column in each row
sepal_width = iris['data'][:,1]

classes = iris['target']
print(classes)

# Arguments correspond to x and y axes
plt.scatter(sepal_length, sepal_width, c = classes)
    # c ...colours the points based on the class their belong to
plt.xlabel('Sepal length (cm)')
plt.ylabel('Sepal width (cm)')
plt.title('Iris data: Sepal length vs. width')
plt.show()