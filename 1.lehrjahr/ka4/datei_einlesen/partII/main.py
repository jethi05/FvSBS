#!/usr/bin/python3
'''Dieses Programm dient dazu, die Personen pro KM^2 je Bundesland Wohnen'''
ERSTE_ZEILE = True
with open("bundeslaender.csv", "r", encoding="utf8") as file:
    lines = file.readlines()
with open("bundeslaender_erweitert.csv", "w", encoding="utf8") as end_file:
    end_file.write("Bundesland,Fläche,Einwohner,Einwohner je qKM,Gesamflaeche,Anteil an Gesamtbevölekerung,Bevölkerungsdichte\n")
    #ine = line.strip().split(",")
    gesammt_flaeche = 0
    gesammt_befoelkerung = 0
    for line in lines[1:]:
        line = line.strip().split(",")
        gesammt_flaeche+=int(line[1])
        gesammt_befoelkerung+=int(line[2])
    print(f"Gesammtbevölkerung {gesammt_befoelkerung}")
    print(f"Gesammtgläche {gesammt_flaeche}")
    for line in lines[1:]:
        line = line.strip().split(",")
        einwohner_je_qkm = int(line[2]) / int(line[1])
        line.append(str(round(einwohner_je_qkm, 1)))
        anteil_gesammtflaeche = 100 / gesammt_flaeche *  int(line[1])
        line.append(str(round(anteil_gesammtflaeche, 1)))
        anteil_befoelkerung = 100 / gesammt_flaeche * int(line[2])
        line.append(str(round(anteil_befoelkerung, 1)))
        befoelkerungsdichte = int(line[1]) / int(line[2])
        line.append(str(round(befoelkerungsdichte, 4)))
        end_file.write(",".join(line) + "\n")
print("Done")
