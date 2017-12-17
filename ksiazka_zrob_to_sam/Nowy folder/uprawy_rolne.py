# Program przedstawia procentowy udział powierzchni rolnych poszczególnych krajów w 2016 r.

import csv      # moduł przetwarzający wiersze w pliku .csv

filename = 'C:\\Users\\Leszek\Documents\\python_scripts\\python_tutorial\\ksiazka_zrob_to_sam\\rozdz_16_pob_danych\\pow_upraw_rolnych.csv'
with open(filename) as f:
    reader = csv.reader(f)  # utworzenie obiektu przeglądarki
    header_row = next(reader)
    print(header_row)
