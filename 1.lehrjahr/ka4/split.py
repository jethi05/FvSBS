zaehler = 0
ergebnis = []  # Initialisiere ergebnis als leere Liste
daten = "Giotta;Dennis;E1FS1;-Beeken;Pascal;E1FS1"
print(daten.split("-"))

# Erste Schleife trennt die einzelnen Menschen an dem Minus
for schueler in daten.split(";-"):
    ergebnis.append([])  # Füge eine leere Unterliste zu ergebnis hinzu
    # Jetzt wird am Semikolon getrennt um die einzelnen Werte zu bekommen
    for string in schueler.split(";"):
        ergebnis[zaehler].append(string)
    zaehler += 1

print(ergebnis)
