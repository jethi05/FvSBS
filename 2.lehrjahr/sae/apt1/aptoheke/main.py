#!/usr/bin/python3
def flugpreise(pnutzlast, pentfernung):
    preis_nutzlast=0
    if pentfernung <= 25 and pnutzlast <= 12:
        if pnutzlast <= 6:
            preis_nutzlast=3
        else:
            preis_nutzlast=7
        gesamtpreis = preis_nutzlast + pentfernung * 0.4
        return f"Gesamtpries des Transportes {gesamtpreis}"
    else:
        return "Mit diesen Angaben ist ein Drohnentransport nicht möglich"

print(flugpreise(13, 26))
