#!/usr/bin/python3
''' soll methode LoginUeberpruefen entwickeln
Benutzernamen und PW
True False -> Daten nicht korrekt
es wird
0 date Korrekt
1 Benutzername existiert nicht
2 Passwort falsch'''
import random

def db_abfrage(username, password):
    return (random.randint(0,2))


def LoginUeberpruefen(user,name):
    if db_abfrage(user,name) != 0:
        print("Daten nicht korrekt")
    return db_abfrage(user,name) == 0
print(LoginUeberpruefen("j","j"))

# Aufgabe Sommer 2023 10 Min Zeit
