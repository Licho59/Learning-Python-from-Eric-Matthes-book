import csv
from datetime import datetime

from matplotlib import pyplot as plt

# Pobranie z pliku dat oraz najwyższych i najniższych temperatur w poszczególnych dniach.
filename = 'C:\\Users\\Leszek\\Documents\\python_scripts\\python_tutorial\\ksiazka_zrob_to_sam\\rozdz_16_pob_danych\death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'Brak danych')
        else:    
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
    
# Dane wykresu.
fig = plt.figure(dpi=90, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5) # alpha = przeźroczystość koloru
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Formatowanie wykresu.
plt.title('Najwyższa i najniższa temperatura dnia - 2014\nDolina Śmierci, Kalifornia', fontsize=14)
plt.xlabel('', fontsize=12)
fig.autofmt_xdate() # wyświetlanie etykiet ukośnie(aby się nie nakładały).
plt.ylabel('Temperatura (F)', fontsize=12)
plt.tick_params(axis='both', which='major', labelsize=10)

#print(highs)
plt.show()