import time
import pygal
from die import Die

# Utworzenie 2 kości do gry typu D8.
die_1 = Die(8)
die_2 = Die(8)

# Wykonanie pewnej liczby rzutów i umieszczenie wyników na liście.
N = 1
results = []
while N < 8:
    start = time.clock()

    for roll in range(10**N):
        result = die_1.roll() + die_2.roll()
        results.append(result)

    # Analiza wyników.
    frequencies = []    
    max_result = die_1.num_sides + die_2.num_sides
    for value in range(2, max_result + 1):
        frequency = results.count(value)
        frequencies.append(frequency)
    print(frequencies)
    elapsed = time.clock() - start
    print('For 10 **', N, 'times done in ', elapsed)
    print('-' * 47)
    N += 1

# Wizualizacja wyników.
hist = pygal.Bar() # Utworzenie egzemplarza wykresu słupkowego.
hist.force_uri_protocol = 'http'

hist.title = "Wynik rzucania 2 kośćmi D8 dziesięć tysięcy razy."
hist.x_labels = list(range(2, max_result +1)) # lista od 2 do 16
hist.x_title = "Wynik"
hist.y_title = "Częstotliwość występowania wartości"

hist.add('D8 + D8', frequencies)
hist.render_to_file('die_visual.svg')

#print(frequencies)
#print(results)