def main():
    '''Liest aus der Datei "./bundeslaender.csv", erweitert sie um Einwohner/Km
    und schreibt das Ergebnis in "./bundeslaender_erweitert.csv"
    '''
    with open("./bundeslaender.csv", "r") as laenderdatei:
        csv = laenderdatei.read().split('\n')

    index_flaeche = 1
    index_einwohner = 2
    csv[0] += ',Einwohner/Km'

    for i in range(1,len(csv)):
        zeile = csv[i].split(',')
        einwohner_pro_km = round(int(zeile[index_einwohner]) / int(zeile[index_flaeche]),2)
        zeile.append(str(einwohner_pro_km))
        csv[i] = ','.join(zeile)

    neu_csv = '\n'.join(csv)
    with open('bundeslaender_erweitert.csv','w') as datei_erweitert:
        datei_erweitert.write(neu_csv)
    print(neu_csv)
    
if __name__ == '__main__':
    main()
    
