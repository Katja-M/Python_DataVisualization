import matplotlib.pyplot as plt
import seaborn as sns
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
sns.scatterplot(sepal_length, sepal_width, hue = classes, legend = False, ax= axes[0,0])
axes[0,0].set_xlabel('Sepal length (cm)')
axes[0,0].set_ylabel('Sepal width (cm)')

# Fill grid in the first row second column
sns.scatterplot(petal_length, petal_width, hue = classes, legend = False, ax= axes[0,1])
axes[0,1].set_xlabel('Petal length (cm)')
axes[0,1].set_ylabel('Petal width (cm)')

sns.scatterplot(sepal_length, petal_length, hue = classes, legend = False, ax= axes[1,0])
axes[1,0].set_xlabel('Sepal_length (cm)')
axes[1,0].set_ylabel('Petal length (cm)')

# Fill grid in the first row second column
sns.scatterplot(sepal_width, petal_width, hue = classes, legend = False, ax= axes[1,1])
axes[1,1].set_xlabel('Sepal width (cm)')
axes[1,1].set_ylabel('Petal width (cm)')

fig.suptitle("Iris dataset")
plt.show()