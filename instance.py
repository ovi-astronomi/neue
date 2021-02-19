from classes import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

die = Die(16)

tally = []

# roll the dice 10 times:
for roll_count in range(1000):
    x = die.roll()
    tally.append(x)

print(tally)

frequencies = []
for value in range(1, die.num_sides+1):
    frequency = tally.count(value)
    frequencies.append(frequency)
print(frequencies)

#visualise using plotly
x_values = list(range(1, die.num_sides+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Tally'}
y_axis_config = {'title': 'Frequency of result'}
my_layout = Layout(title= 'results of rolling a D16 1000 times.',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d16.html')