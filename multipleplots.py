import matplotlib.pyplot as plt
import pickle

with open(r'C:\Users\Katja\PythonCodingTraining\DataVisualization\data-viz\matplotlib\iris.pickle', 'rb') as file:
    iris = pickle.load(file)

print(iris)

# Extract the first column from the data table
sepal_length = iris['data'][:,0]
    # [:,0]: all of the rows but only the first column in each row
sepal_width = iris['data'][:,1]
petal_length = iris['data'][:,2]
petal_width = iris['data'][:,3]
classes = iris['target']

# Fig provides access to the entire window
# Access refers to the individual grid
fig, axes = plt.subplots(2,2)
# Access top left grid
axes[0,0].scatter(sepal_length, sepal_width, c = classes)
axes[0,0].set_xlabel('Sepal length (cm)')
axes[0,0].set_ylabel('Sepal width (cm)')

# Fill grid in the first row second column
axes[0,1].scatter(petal_length, petal_width, c = classes)
axes[0,1].set_xlabel('Petal length (cm)')
axes[0,1].set_ylabel('Petal width (cm)')

axes[1,0].scatter(sepal_length, petal_length, c = classes)
axes[1,0].set_xlabel('Sepal_length (cm)')
axes[1,0].set_ylabel('Petal length (cm)')

# Fill grid in the first row second column
axes[1,1].scatter(sepal_width, petal_width, c = classes)
axes[1,1].set_xlabel('Sepal width (cm)')
axes[1,1].set_ylabel('Petal width (cm)')

fig.suptitle("Iris dataset")
plt.show()