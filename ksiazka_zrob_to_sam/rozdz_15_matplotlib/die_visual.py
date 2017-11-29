import pygal
from die import Die

# Utworzenie kości do gry typu D6 i D10.
die_1 = Die()
die_2 = Die(10)

# Wykonanie pewnej liczby rzutów i umieszczenie wyników na liście.
results = []
for roll in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analiza wyników.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Wizualizacja wyników.
hist = pygal.Bar() # Utworzenie egzemplarza wykresu słupkowego.
hist.force_uri_protocol = 'http'

hist.title = "Wynik rzucania kośćmi D6 i D10 pięćdziesiąt tysięcy razy."
hist.x_labels = list(range(2, max_result +1)) # lista od 2 do 16
hist.x_title = "Wynik"
hist.y_title = "Częstotliwość występowania wartości"

hist.add('D6 + D10', frequencies)
hist.render_to_file('die_visual.svg')

print(frequencies)
#print(results)