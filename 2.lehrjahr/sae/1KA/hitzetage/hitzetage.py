#!/bin/python3
def berechne_mittelwert(werte):
    '''Nimmt eine Liste an Zahlen vom Datentyp String entgegen und gibt den Mittelwert als String zurück'''
    summe = 0
    for wert in werte:
        summe += float(wert)
    return str(round(summe / len(werte),2))

def berechne_median(werte):
    '''Nimmt eine Liste an Zahlen vom Datentyp String entgegen und gibt den Median als String zurück'''
    for i in range(len(werte)):
        werte[i] = float(werte[i])

    werte.sort()
    if len(werte) % 2:
        median = (werte[len(werte) // 2] + werte[len(werte)//2-1]) / 2
    else:
        median = werte[len(werte)//2]

    return str(median)

def main():
    # Datei öffnen
    filename = './hitzetage.txt'
    with open(filename, 'r') as file:
        text = file.read()
    
    # Tabelle erstellen
    lines = text.split(';\n')
    lines.pop()
    tabelle = []
    for line in lines:
        line = line.split(';') 
        tabelle.append(line)

    # Jahresmittel anfügen
    for zeile in tabelle[1:]:
        mittelwert = berechne_mittelwert(zeile[1:])
        zeile.append(mittelwert)
    
    # Ländermittel anfügen
    mittelwerte = ['Mittel']
    mediane = ['Median']
    for i in range(1,len(tabelle[0])):
        spaltenwerte = [tabelle[j][i] for j in range(1,len(tabelle))]
        mittelwerte.append(berechne_mittelwert(spaltenwerte))
        mediane.append(berechne_median(spaltenwerte))
    tabelle.append(mittelwerte)
    tabelle.append(mediane)

    # Quartil? bestimmen
    median = float(tabelle[-1][-1])
    tabelle[0].append('Quartil')
    for zeile in tabelle[1:]:
        jahresmittel = float(zeile[-1])
        if jahresmittel < median:
            zeile.append('unteres')
        elif jahresmittel > median:
            zeile.append('oberes')
        else:
            zeile.append('Median')
    
    # In hitzetage_erweitert.txt schreiben
    neuliste = [';'.join(zeile) for zeile in tabelle]
    neutext = ';\n'.join(neuliste)    
    with open('hitzetage_erweitert.txt', 'w') as file:
        file.write(neutext)

    

if __name__ == "__main__":
    main()
