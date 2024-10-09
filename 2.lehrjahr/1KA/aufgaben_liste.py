#!/usr/bin/python3
# Schreibe jeweils ein Programm.
# Aufgabe 1 Nutze die Listenmethoden aus help(list)

# Erstelle eine Liste namens obst, die die Elemente "Apfel", "Banane", "Pflaume" enthält.
obst = ["Apfel", "Bannane", "Pflaume" ]
# Füge die Elemente der Liste beeren = ["Stachelbeere", "Himbeere", "Heidelbeere"] ans Ende von obst.
beeren = ["Stachelbeere", "Himbeere", "Heidelbeere"]
obst += beeren
# Füge am Ende der Liste das Element "Mango" hinzu.
obst.append("Mango")
# Füge zwischen Banane und Pflaume das Element "Kirsche" ein.
obst.insert(2, "Kirsche")
# Ändere das zweite Element von "Banane" in "Birne".
obst[1]="Birne"
# Entferne das erste Element aus der Liste.
obst.pop(0)
# Nutze pop() um das letzte Element zu entfernen und auszugeben.
print(obst.pop())
# Gib den Index des Elements "Pflaume" auf der Konsole aus.
print(f"Index von Pflaume ist: {obst.index("Pflaume")}")
# Gib das größte Element auf der Konsole aus.
print(f"Größte Element aus Liste: {max(obst)}")
# Gib den Index des größten Elements auf der Konsole aus.
print(f" der Index des Größten Elements ist: {obst.index(max(obst))}")
# Wie viele Stellen ist das größte Element vom Kleinsten entfernt? Gib hierzu die Differenz der
# Indizes des größten und des kleinsten Elements als positive Zahl aus.
max_obst_index = int(obst.index(max(obst)))
min_obst_index = int(obst.index(min(obst)))
if max_obst_index > min_obst_index:
    digit = max_obst_index - min_obst_index
elif min_obst_index < min_obst_index:
    digit = min_obst_index - max_obst_index
else:
    digit = max_obst_index
print(f"The difference is {digit}")
# Gib die Liste auf der Konsole aus.
print(obst)
# Sortiere die Liste alphabetisch aufsteigend.
obst.sort()
print(obst)
# Gib die einzelnen Elemente der Liste zeiilenweise auf der Konsole aus (for-each-Schleife)
for r in obst:
    print(r)
# Aufgabe 2 Slicing

# Erstelle eine Liste zahlen die die Zahlen von 1 bis 100 enthält. Nutze hierzu for i in range()
# und füge jedes einzelne Element hinten an deine Liste.
nummern = []
for i in range(1,101,1):
    nummern.append(i)
# Gib die Anzahl der Elemente aus.
print(len(nummern))
# Nutze die Slicing-Notation liste[start:stop:step] für die folgenden Aufgaben
# https://stackoverflow.com/questions/509211/how-slicing-in-python-works

# Gib die gesamte Liste aus.
print(nummern[::])
# Gib die Liste bis zum vorletzten Element aus.
print(nummern[:-1:1])
# Gib die Liste bis zum fünften Element von Hinten aus.
print(nummern[:-5:1])
# Gib alle Elemente zwischen den Indizes 25 und 35 (inklusive) aus
print(nummern[24:35:1])
# Gib jedes zweite Element aus.
print(nummern[::2])
# Gib jedes fünfte Element bis zum Index 80 (exklusive) aus.
print(nummern[:79:5])
# Gib die Liste rückwärts aus.
print(nummern[::-1])

# Aufgabe 3 Listen durchlaufen

# Erstelle die Liste messwerte = [22.86, 20.39, 23.76, 21.34, 24.32]
messwerte = [22.86, 20.39, 23.76, 21.34, 24.32]
# Durchlaufe die Liste ein Mal und ermittle dabei minimum, maximum und summe.
# Nutze dabei NICHT die Funktionen min(), max(), sum().
# Gib Minimum, Maximum, Summe und Durchschnitt aus.
minimum = messwerte[0]
maximum = messwerte[0]
summe_zahlen = 0
for r in messwerte:
    if r > maximum:
        maximum = r
    elif r < minimum:
        minimum = r
    summe_zahlen += r
print(f"Minimum {minimum}\nMaximum {maximum}\nDurchschnitt {summe_zahlen/len(messwerte)}")
# Aufgabe 4 Listen und Strings

# Zerschneide den String "Schneider;Fischer;Seemann;Schmied;Müller" in eine Liste berufe.
# Sortiere die Liste berufe.
string = "Schneider;Fischer;Seemann;Schmied;Müller"
berufe = []
berufe = string.strip().split(";")
berufe.sort()
# Füge die Liste zu einem String mit dem Trennzeichen | zusammen.
string_mit_trennzeichen = "|".join(berufe)
# Aufgabe 4 Verschachtelte Listen

# Gegeben ist die verschachtelte Liste matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]].
# Schreibe eine Funktion, die die Summe aller Zahlen in der Matrix berechnet. Hierzu bekommt sie
# die Matrix als Parameter und liefert die Summe zurück.
<<<<<<< HEAD
liste = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
def summe_berechnen(matrix):
=======
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
 def calc_summe_matrix(matrix):
>>>>>>> 280edf8faff420ee2112a5f65137323cc656c092
    summe_matrix = 0
    for liste in matrix:
        for matrix_zahlen in liste:
            summe_matrix += matrix_zahlen
    return summe_matrix
<<<<<<< HEAD
print(summe_berechnen(liste))
=======
print(f"Ergebnis Matrix: {calc_summe_matrix(matrix)}")
>>>>>>> 280edf8faff420ee2112a5f65137323cc656c092
