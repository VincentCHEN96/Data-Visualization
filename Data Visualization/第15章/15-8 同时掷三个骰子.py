import pygal

from 第15章.die import Die

die_1 = Die()
die_2 = Die()
die_3 = Die()

results = []
for i in range(1000):
    results.append(die_1.roll()+die_2.roll()+die_3.roll())
print(results)

frequency = []
for i in range(3, die_1.num_sides+die_2.num_sides+die_3.num_sides+1):
    frequency.append(results.count(i))
print(frequency)
hist = pygal.Bar()
hist.title = "Result of Rolling (D6 + D6 + D6) 1000 Times"
hist.x_labels = [str(i) for i in range(3, die_1.num_sides+die_2.num_sides+
                                       die_3.num_sides+1)]
hist.x_title= "Result"
hist.y_title = "Frequency of Results"
hist.add("D6 + D6 + D6", frequency)
hist.render_to_file('dice_visual.svg')