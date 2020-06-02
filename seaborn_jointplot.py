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
classes = iris['target']

axes = sns.jointplot(sepal_length, sepal_width, kind = 'kde')
    # hue ...colours the points based on the class their belong to
    # kde...does not show the single points, but rather the distribution of points is coloured differently
axes.set_axis_labels('Sepal length (cm)', 'Sepal width (cm)')
plt.show()