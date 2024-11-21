#!/usr/bin/python3
'''
Aufgabe Hitzetage
Thiersch
'''

'''Aufgabe 1'''
def berechne_mittelwert(string):
    liste = string.strip().split(";")
    return sum(liste)/len(liste)

with open("hitzetage.txt", "r", encoding="utf8") as file:
    lines = file.readlines()
with open("neu_hitzetage.txt", "w", encoding="utf8") as new_file:
# als erstes neue Spalte für Mittelwert einfügen
    for first_line in lines[0:1]:
        ''' Hier wird der Ersten Zeile der Mittelwert hinzugefügt'''
        # first_line um Mittelwert erweitern
        first_line = first_line.strip() + "Mittelwert;\n"
        print(first_line)
    for line in lines[1:]:
        print(berechne_mittelwert(line))
