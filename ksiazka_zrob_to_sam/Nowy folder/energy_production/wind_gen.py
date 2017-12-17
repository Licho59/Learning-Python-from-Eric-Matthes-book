import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = '2017_10_wind.csv'
with open(filename) as f:
    reader = csv.reader(f, delimiter=';')
    header_row = next(reader)
    #print(header_row)
    # Formating input data and converting it to dictionary;
    data = {}
    for row in reader:
        for k in row:
            if "," in k:
                row[row.index(k)] = k.replace(",", ".")
        if row[0] not in data:
            val = []
            val.append(float(row[2]))
            data[row[0]] = val
            current_date = datetime.strptime(row[0], '%Y%m%d').strftime('%Y-%m-%d')
            data[current_date] = data.pop(row[0])
        else:
            val.append(float(row[2]))
# Daily global generation
day_gen = {}
for key in data:
    day_gen[key] = int(sum(data[key]))
    #all_day = day_gen[key] 
#print(day_gen)
# Hours of maximum and minimu generation
low_gen, high_gen = [], []
dates = day_gen.keys()
day_wind_prod = day_gen.values()
# Visualisation of results
fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, day_wind_prod, c='blue')
plt.title('Wind generation in October_2017', fontsize=10)
plt.xlabel('', fontsize=10)
fig.autofmt_xdate()
plt.ylabel('Generation(MWh)', fontsize=10)
plt.tick_params(axis='both', which='major', labelsize=6)
plt.show()