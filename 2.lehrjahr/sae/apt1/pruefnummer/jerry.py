#!/usr/bin/python3
''' Zehn stellige Zahl, 1-9 werden mal deren Stelle'''
def pruefeNummer(liste):
    summe = 0
    stelle = 0
    for zahl in liste[0][:9:]:
        stelle += 1
        summe += int(zahl) * stelle
    return(summe%10 == int(liste[0][9]))
print(pruefeNummer(["5124897253"]))
