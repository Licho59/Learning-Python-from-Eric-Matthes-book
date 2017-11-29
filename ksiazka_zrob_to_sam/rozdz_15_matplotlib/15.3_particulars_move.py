import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Tworzenie nowego błądzenia losowego, dopóki program pozostaje aktywny.
while True:
    # Przygotowanie danych błądzenia losowego i wyświetlenie punktów.
    rw = RandomWalk(50000)
    rw.fill_walk()

    # Określenie wielkości okna wykresu.
    plt.figure(figsize=(10, 6))
    
    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_values, rw.y_values, linewidth=1)

    # Podkreślenie pierwszego i ostatniego punktu błądzenia losowego.
    plt.scatter(0, 0, c='green', edgecolors='none', s=20)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=20)
    
    # Ukrycie osi.
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    
    plt.show()

    keep_running = input("Utworzyć kolejne błądzenie losowe? (y/n): ")
    if keep_running == 'n':
        break