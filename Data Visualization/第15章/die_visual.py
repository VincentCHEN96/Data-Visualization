import pygal

from 第15章.die import Die


die = Die()

results = []
for i in range(100):
    results.append(die.roll())
print(results)

frequency = []
for i in range(1, die.num_sides+1):
    frequency.append(results.count(i))
print(frequency)
hist = pygal.Bar()
hist.title = "Result of Rolling One D6 100 Times"
hist.x_labels = [str(i) for i in range(1, die.num_sides+1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6', frequency)
hist.render_to_file('die_visual.svg')