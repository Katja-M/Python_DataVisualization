from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.palettes import Dark2_5 as palette
import pickle

output_file('multiline.html')

with open(r'C:\Users\Katja\PythonCodingTraining\DataVisualization\data-viz\bokeh\prog-langs-popularity.pickle', 'rb') as file:
    data = pickle.load(file)

languages, ranking = zip(*data)

fig = figure(x_axis_label = 'year', y_axis_label = 'rank', title = 'Ranking')

for i in range(len(languages)):
    years, ranks = zip(*ranking[i])
    # with legend and color for each programming language
    fig.line(years, ranks, line_width = 2, legend_label = languages[i], color = palette[i])

#Create interactive legend
fig.legend.click_policy = 'hide'

show(fig)