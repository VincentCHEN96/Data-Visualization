import pygal

from die import Die

die_1 = Die(8)
die_2 = Die(8)

results = []
for i in range(100000):
    results.append(die_1.roll()+die_2.roll())
print(results)

frequency = []
for i in range(2, die_1.num_sides+die_2.num_sides+1):
    frequency.append(results.count(i))
print(frequency)
hist = pygal.Bar()
hist.title = "Result of Rolling (D8 + D8) 100000 Times"
hist.x_labels = [str(i) for i in range(2, die_1.num_sides+die_2.num_sides+1)]
hist.x_title= "Result"
hist.y_title = "Frequency of Results"
hist.add("D8 + D8", frequency)
hist.render_to_file('dice_visual.svg')