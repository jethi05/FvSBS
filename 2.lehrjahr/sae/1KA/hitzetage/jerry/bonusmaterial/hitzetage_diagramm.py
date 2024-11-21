import matplotlib.pyplot as plt
import numpy as np

data = np.genfromtxt('hitzetage.txt', delimiter=';', skip_header=1)

# Daten für Brandenburg/Berlin extrahieren
jahre = data[:, 0]
hitzetage_brb = data[:, 1]

# Balkendiagramm
plt.figure(figsize=(10, 5))
plt.bar(jahre, hitzetage_brb, label='Hitzetage Brandenburg/Berlin', color='skyblue')

# Trendlinie berechnen und plotten
z = np.polyfit(jahre, hitzetage_brb, 1)
p = np.poly1d(z)
plt.plot(jahre, p(jahre), linestyle='--', label='Trend', color='red')

# Beschriften und Darstellung anpassen
plt.xlabel('Jahr')
plt.ylabel('Anzahl der Hitzetage')
plt.title('Anzahl der Hitzetage in Brandenburg/Berlin (1951-2023)')
plt.legend()
plt.grid(True)

# Anzeigen
plt.show()