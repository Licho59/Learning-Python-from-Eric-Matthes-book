import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, c='red', edgecolor='none', s=40) # parametr s określa wielkość punktu na wykresie, 'c' to kolor, a 'edgecolor' dotyczy obwódki wyświetlanego punktu; wg modelu RGB (skala od 0 do 1) - np. c=(0, 0, 0.8) to w pobliżu niebieskiego
#plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors=None, s=40) #użyto mapy kolorów o nazwie Blues ze strony matplot

# Zdefiniowanie tytułu wykresu i etykiet osi.
plt.title("Kwadraty liczb", fontsize=24)
plt.xlabel("Wartość", fontsize=14)
plt.ylabel("Kwadraty wartości", fontsize=14)

# Zdefiniowanie wielkości etykiet.
plt.tick_params(axis='both', which='major', labelsize=14)

# Zdefiniowanie zakresu dla każdej osi.
plt.axis([0, 1100, 0, 1100000])

#plt.show() # wyświetla wykres
plt.savefig('scatter_squares_plot.png', bbox_inches='tight') #automatyczny zapis wykresu w tym samy folderze co skrypt, bbox_inches -opcjonalny