import matplotlib.pyplot as plt

'''input_values = list(range(1, 6))
cube_values = [x**3 for x in input_values]''' # wersja I

input_values = list(range(1, 5001))
cube_values = [x**3 for x in input_values] # wersja II
plt.plot(input_values, cube_values, linewidth=3)

plt.title("Sześciany liczb", fontsize=20)
plt.xlabel("Wartość", fontsize=16)
plt.ylabel("Sześcian wartości", fontsize=16)

plt.tick_params(axis='both', labelsize=16)

plt.show()