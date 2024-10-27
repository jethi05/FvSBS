#!/usr/bin/python3
'''Dieses Programm dient dazu, die Personen pro KM^2 je Bundesland Wohnen'''
with open("bundeslaender.csv", "r", encoding="utf8") as file:
    lines = file.readlines()
with open("bundeslaender_erweitert.csv", "w", encoding="utf8") as end_file:
    end_file.write("Bundesland,Fläche,Einwohner,Einwohner je qKM\n")
    for line in lines[1:]:
        line = line.strip().split(",")
        einwohner_je_qkm = int(line[2]) / int(line[1])
        line.append(str(einwohner_je_qkm))
        end_file.write(",".join(line) + "\n")
print("Done")
