#!/usr/bin/python3
'''Dieses Programm dient dazu, die Personen pro KM^2 je Bundesland Wohnen'''
ERSTE_ZEILE = True
with open("bundeslaender.csv", "r", encoding="utf8") as file:
    lines = file.readlines()
with open("bundeslaender_erweitert.csv", "w", encoding="utf8") as end_file:
    for line in lines:
        line = line.strip().split(",")
        if ERSTE_ZEILE:
            line.append("Einwohner je qKM")
            ERSTE_ZEILE = False
        else:
            einwohner_je_qkm = int(line[1]) / int(line[2])
            line.append(str(einwohner_je_qkm))
        end_file.write(",".join(line) + "\n")
print("Done")
