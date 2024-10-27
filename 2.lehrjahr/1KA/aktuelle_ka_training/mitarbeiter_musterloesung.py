# Aufgabe 1
def lies_datei_als_liste(dateiname):
    """
    Liest den Inhalt einer Datei ein, entfernt unnötigen Whitespace
    und gibt eine Liste der Zeilen zurück.
    """
    with open(dateiname, "r") as datei:
        inhalt = datei.read().strip().split("\n")
    return inhalt

# Beispielaufruf für Aufgabe 1
mitarbeiter = lies_datei_als_liste("mitarbeiter.csv")

# Aufgabe 2
def extrahiere_mitarbeiter(mitarbeiter_liste):
    """
    Extrahiert die Namen der Mitarbeiter aus der gegebenen Liste und gibt sie
    als einen String zurück, bei dem die Namen durch Komma und Leerzeichen getrennt sind.
    """
    namen = []
    for eintrag in mitarbeiter_liste[1:]:  # Überspringe die Kopfzeile
        teile = eintrag.split(";")
        namen.append(teile[1])  # Füge den Namen zur Liste hinzu
    return ", ".join(namen)

# Beispielaufruf für Aufgabe 2
namen_string = extrahiere_mitarbeiter(mitarbeiter)

# Aufgabe 3
def berechne_durchschnittsgehalt(mitarbeiter_liste, abteilung):
    """
    Berechnet das durchschnittliche Gehalt aller Mitarbeiter in einer bestimmten Abteilung.
    """
    summe = 0
    anzahl = 0
    for eintrag in mitarbeiter_liste[1:]:  # Überspringe die Kopfzeile
        teile = eintrag.split(";")
        if teile[2] == abteilung:  # Überprüfe, ob die Abteilung übereinstimmt
            summe += float(teile[3])  # Addiere das Gehalt zur Summe
            anzahl += 1  # Erhöhe den Zähler für die Anzahl der Mitarbeiter
    if anzahl > 0:
        return summe / anzahl
    else:
        return 0  # Falls keine Mitarbeiter in der Abteilung sind, gib 0 zurück

# Beispielaufruf für Aufgabe 3
durchschnitt_it = berechne_durchschnittsgehalt(mitarbeiter, "IT")

# Aufgabe 4
def erhoehe_gehalt_teilzeit(mitarbeiter_liste):
    """
    Erhöht das Gehalt aller Teilzeit-Mitarbeiter um 10% und gibt eine aktualisierte
    Liste zurück, in der die neuen Gehälter enthalten sind.
    """
    aktualisierte_liste = []
    for eintrag in mitarbeiter_liste:  # Schließe die Kopfzeile mit ein
        teile = eintrag.split(";")
        if len(teile) == 6 and teile[5].strip().lower() == "ja":  # Prüfe, ob der Mitarbeiter Teilzeit arbeitet
            gehalt = float(teile[3]) * 1.10  # Erhöhe das Gehalt um 10%
            teile[3] = str(gehalt)  # Aktualisiere das Gehalt in der Liste
        aktualisierte_liste.append(";".join(teile))  # Füge den Eintrag zur aktualisierten Liste hinzu
    return aktualisierte_liste

# Beispielaufruf für Aufgabe 4
aktualisierte_mitarbeiter = erhoehe_gehalt_teilzeit(mitarbeiter)

# Aufgabe 5

mitarbeiterliste = lies_datei_als_liste("mitarbeiter.csv")
bericht = extrahiere_mitarbeiter(mitarbeiterliste) + "\n\n"
bericht += f"Durchschnittsgehalt IT: {berechne_durchschnittsgehalt(mitarbeiterliste, 'IT')}\n\n"
bericht += "Aktualisierte Gehälter:\n" + "\n".join(erhoehe_gehalt_teilzeit(mitarbeiterliste))

with open("gehaltsbericht.txt", "w") as datei:
    datei.write(bericht)
