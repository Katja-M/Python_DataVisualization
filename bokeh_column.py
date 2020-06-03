from bokeh.io import show
from bokeh.plotting import figure
import pickle

# load data
with open(r'C:\Users\Katja\PythonCodingTraining\DataVisualization\data-viz\bokeh\fruit-sales.pickle', 'rb') as file:
    data = pickle.load(file)

fruit, num_sold = zip(*data)

plot = figure(x_range = fruit, y_axis_label = 'Fruit sold (millions)', title = 'Fruit sold')
# Vbar means vertical bar
plot.vbar(x = fruit, top = num_sold, width = 0.9)

show(plot)
