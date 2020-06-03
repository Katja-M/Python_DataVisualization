from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.layouts import row, column, gridplot
from bokeh.palettes import Dark2_5 as palette
import pickle

output_file('panning.html')

with open(r'C:\Users\Katja\PythonCodingTraining\DataVisualization\data-viz\bokeh\iris.pickle', 'rb') as file:
    iris = pickle.load(file)

sepal_length = iris['data'][:,0]
sepal_width = iris['data'][:,1]
petal_length = iris['data'][:,2]
petal_width = iris['data'][:,3]
classes = iris['target']

# separate data via class
setosa_sepal_length = sepal_length[classes == 0]
setosa_sepal_width = sepal_width[classes == 0]
setosa_petal_length = petal_length[classes == 0]
setosa_petal_width = petal_width[classes == 0]
versicolor_sepal_length = sepal_length[classes == 1]
versicolor_sepal_width = sepal_width[classes == 1]
versicolor_petal_length = petal_length[classes == 1]
versicolor_petal_width = petal_width[classes == 1]
virginica_sepal_length = sepal_length[classes == 2]
virginica_sepal_width = sepal_width[classes == 2]
virginica_petal_length = petal_length[classes == 2]
virginica_petal_width = petal_width[classes == 2]

# Creating multiple plots by creating multiple figures and then telling the show function 
# how to arrange these figures

fig1 = figure(x_axis_label = 'Sepal length (cm)', y_axis_label = 'Sepal width (cm)')
fig1.circle(setosa_sepal_length, setosa_sepal_width, color = palette[0], legend_label= 'setosa')
fig1.circle(versicolor_sepal_length, versicolor_sepal_width, color = palette[1], legend_label= 'versicolor')
fig1.circle(virginica_sepal_length, virginica_sepal_width, color = palette[2], legend_label= 'virginica')

fig3 = figure(x_axis_label = 'Sepal length (cm)', y_axis_label = 'Petal length (cm)', x_range = fig1.x_range)
fig3.circle(setosa_sepal_length, setosa_petal_length, color = palette[0], legend_label= 'setosa')
fig3.circle(versicolor_sepal_length, versicolor_petal_length, color = palette[1], legend_label= 'versicolor')
fig3.circle(virginica_sepal_length, virginica_petal_length, color = palette[2], legend_label= 'virginica')


show(column(fig1, fig3))