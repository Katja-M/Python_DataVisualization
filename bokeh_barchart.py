from bokeh.io import show, output_file
from bokeh.plotting import figure
import pickle

output_file('bar.html')

with open(r'C:\Users\Katja\PythonCodingTraining\DataVisualization\data-viz\bokeh\coding-exp-by-dev-type.pickle','rb') as file:
    data = pickle.load(file)

dev_types, years_exp = zip(*data)
data_source = {'dev_types': dev_types, 'years_exp': years_exp}

# Goal: tool tips: "years of experience: actual val"
# Tool tips require a data source
TOOLTIPS = [('years of experience','@years_exp')]
plot = figure(y_range = dev_types, x_axis_label = 'years', title = 'Coding Experience by Developer Type', tools = 'hover', tooltips = TOOLTIPS)
# set data source: looks up values in data source dictionary
plot.hbar(y = 'dev_types', right = 'years_exp', height = 0.9, source = data_source)
    # by putting values in quotes, Python looks at data_source for values

# Line of code without tool tips
# plot.hbar(y = dev_types, right = years_exp, height = 0.9)
show(plot)