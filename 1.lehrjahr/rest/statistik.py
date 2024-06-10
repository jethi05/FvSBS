import matplotlib.pyplot as plt

# Beispiel-Daten
categories = ['Kategorie A', 'Kategorie B', 'Kategorie C', 'Kategorie D']
values = [25, 40, 30, 45]

# Erstellen des Balkendiagramms
plt.bar(categories, values, color='blue')

# Hinzufügen von Titeln und Beschriftungen
plt.title('Beispiel-Balkendiagramm')
plt.xlabel('Kategorien')
plt.ylabel('Werte')

# Anzeigen des Diagramms
plt.show()

