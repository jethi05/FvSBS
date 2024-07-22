def calc_einwohner_pro_km(zeile: list[str]) -> str:
    return str(round(int(zeile[2]) / int(zeile[1]),2))

def calc_anteil_gesamtflaeche(zeile: list[str], gesamtflaeche:int) -> str:
    return str(round(int(zeile[1]) / gesamtflaeche,3))

def calc_anteil_bevoelkerung(zeile: list[str], gesamtbevoelkerung:int) -> str:
    return str(round(int(zeile[2]) / gesamtbevoelkerung,3))

def calc_bevoelkerungsdichte(einwohner_pro_km: float, gesamtdichte:int) -> str:
    if (einwohner_pro_km > gesamtdichte):
        return 'hoch'
    else:
        return 'gering'

def main():
    with open("./bundeslaender.csv", "r") as laenderdatei:
        csv = laenderdatei.read().split('\n')
    
    csv[0] += ',Einwohner/Km,Anteil an Gesamtfläche,Anteil an Gesamtbevölkerung,Bevölkerungsdichte'
    
    gesamtflaeche = 0
    gesamtbevoelkerung = 0
    
    for zeile in csv[1:]:
        zeile = zeile.split(',')
        gesamtflaeche += int(zeile[1])
        gesamtbevoelkerung += int(zeile[2])
        
    gesamtdichte = gesamtbevoelkerung /  gesamtflaeche
    
        
    for i in range(1,len(csv)):
        zeile = csv[i].split(',')
        
        einwohner_pro_km = calc_einwohner_pro_km(zeile)
        flaechenanteil = calc_anteil_gesamtflaeche(zeile, gesamtflaeche)
        bevoelkerungsanteil = calc_anteil_bevoelkerung(zeile, gesamtbevoelkerung)
        bevoelkerungsdichte = calc_bevoelkerungsdichte(float(einwohner_pro_km),gesamtdichte)
        
        zeile.append(einwohner_pro_km)
        zeile.append(flaechenanteil)
        zeile.append(bevoelkerungsanteil)
        zeile.append(bevoelkerungsdichte)
        
        csv[i] = ','.join(zeile)

    neu_csv = '\n'.join(csv)
    with open('bundeslaender_erweitert.csv','w') as datei_erweitert:
        datei_erweitert.write(neu_csv)
    print(neu_csv)
    
if __name__ == '__main__':
    main()
