import time
import pygal
from die import Die

# Utworzenie 3 kości do gry typu D6.
die_1, die_2, die_3 = Die(), Die(), Die()

N = 1
results = []
while N < 7:
    start = time.clock()
    for roll in range(10**N):
        result = die_1.roll() + die_2.roll() + die_3.roll()
        results.append(result)

    # Analiza wyników z użyciem wyrażenia generatora.
    max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
    frequencies = (results.count(value) for value in range(3, max_result + 1)) 
    print(list(frequencies))
    elapsed = time.clock() - start
    print('For 10 **', N, 'times done in ', elapsed)
    print('-' * 47)
    N += 1

# Visualize the results.
hist = pygal.Bar()
hist.title = "Results of rolling three D6 dice 1000 times."
hist.x_labels = [x for x in range(3, 19)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6 + D6', frequencies)
hist.render_to_file('dice_multiply.svg')