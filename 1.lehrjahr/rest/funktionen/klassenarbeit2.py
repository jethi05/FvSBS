#!/usr/bin/python3
def carsharing():
    fahrzeugklasse = input("Bitte geben sie ihre Fahrzeugklasse ein\n>>").lower() # in wiefern wäre es ohne Fehlerabwährung richtig?
    gefahrene_km = float(input("Bitte geben sie die gefahrenen Kilometer ein\n>>")) #<- float oder int
    gefahrene_std = float(input("Bitte geben sie die gesamte Zeit ein\n>>"))
    if fahrzeugklasse == "s":
        km_preis = 0.36
        std_preis = 2.05
    elif fahrzeugklasse == "m":
        km_preis = 0.37
        std_preis = 2.15
    elif fahrzeugklasse == "l":
        km_preis = 0.39
        std_preis = 2.35
    else:
        print("Sie haben falsche Daten eingegeben")
        carsharing()
   if gefahrene_std >= 12:
        gesamtkosten = (12 * std_preis + ((gefahrene_km - 12) * (std_preis * 0.95)) + gefahrene_km * km_preis
    else:
        gesamtkosten = (km_preis * gefahrene_km + std_preis * gefahrene_std)
if __name__=="__main__":
    carsharing()
