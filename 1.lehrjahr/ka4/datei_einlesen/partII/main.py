#!/usr/bin/python3
'''Dieses Programm dient dazu, die Personen pro KM^2 je Bundesland Wohnen'''
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
    for line in lines[1:]:
        line = line.strip().split(",")
        line.append(str(round(int(line[2]) / int(line[1]), 1)))
        line.append(str(round(100 / gesammt_flaeche *  int(line[1]), 1)))
        line.append(str(round(100 / gesammt_flaeche * int(line[2]), 1)))
        line.append(str(round(int(line[1]) / int(line[2]), 4)))
        end_file.write(",".join(line) + "\n")
print("Done")
