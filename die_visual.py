from die import Die
import pygal
# from datetime import datetime


die_1 = Die()
die_2 = Die()

# results = []
# num = [0, 0, 0, 0, 0, 0]
# print(datetime.now())
#
# for roll_num in range(1000):
#     result = die.roll()
#     results.append(result)
#     num[result-1] += 1
#
# print(datetime.now())
# print(num)


# 掷几次骰子，并将结果存储在一个列表中
results = []

for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
# 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()

hist.title = "Result of rolling one D6 1000 times."
print(frequencies)
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6+D6', frequencies)
hist.render_to_file('die_visual.svg')
