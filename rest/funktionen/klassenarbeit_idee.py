import matplotlib.pyplot as plt

tag = 1
zombies = 1
menschen = 116033

zombies_list = [zombies]  # Liste für Zombie-Werte
tage_list = [tag]  # Liste für Tageswerte

while menschen >= zombies:
    zombies += zombies * 1.5
    tag += 1
    zombies_list.append(zombies)  # Zombie-Wert zur Liste hinzufügen
    tage_list.append(tag)  # Tageswert zur Liste hinzufügen

# Diagramm erstellen
plt.plot(tage_list, zombies_list, marker='o', linestyle='-')
plt.title('Zombie-Ausbreitung')
plt.xlabel('Tag')
plt.ylabel('Anzahl der Zombies')
plt.grid(True)
plt.show()

