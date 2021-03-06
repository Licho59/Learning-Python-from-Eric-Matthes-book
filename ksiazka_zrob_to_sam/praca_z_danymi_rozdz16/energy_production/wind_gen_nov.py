import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'C:\\Users\\Leszek\\Documents\\python_scripts\\python_tutorial\\ksiazka_zrob_to_sam\\Data analysis\\energy_production\\2017_10_wind.csv'
with open(filename) as f:
    reader = csv.reader(f, delimiter=';')
    header_row = next(reader)
    #print(header_row)
    # Formating input data and converting it to dictionary;
    data = {}
    for row in reader:
        current_date = datetime.strptime(
            row[0], '%Y%m%d').strftime('%Y-%m-%d')
        for k in row:
            if "," in k:
                row[row.index(k)] = k.replace(",", ".")
        if current_date not in data:
            val = []
            val.append(float(row[2]))
            data[current_date] = val
        else:
            val.append(float(row[2]))

day_gen = {}
for key in data:
    day_gen[key] = int(sum(data[key]))  # Daily global generation

low_gen, high_gen = [], []  # Everydaymaximum and minimum generation
for key in data:
    low_gen.append(min(data[key]))
    high_gen.append(max(data[key]))

# Visualisation of results
dates = day_gen.keys()
day_wind_prod = day_gen.values()

fig = plt.figure(dpi=128, figsize=(12,8))
#plt.plot(dates, day_wind_prod, c='blue', alpha=0.5)
plt.plot(dates, low_gen, c='red', alpha=0.5)
plt.plot(dates, high_gen, c='yellow', alpha=0.5)
plt.fill_between(dates, low_gen, high_gen, facecolor='grey', alpha=0.1)
plt.title('Wind generation in October_2017', fontsize=10)
plt.xlabel('', fontsize=10)
fig.autofmt_xdate()
plt.ylabel('Generation(MWh)', fontsize=10)
plt.tick_params(axis='both', which='major', labelsize=6)
plt.show()