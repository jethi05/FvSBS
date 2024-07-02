#!/usr/bin/python3
erste_zeile = True
with open("bundeslaender.csv", "r") as file:
    lines = file.readlines()
with open("bundeslaender_erweitert.csv", "w") as end_file:
    for line in lines:
        line = line.strip().split(",")
        if erste_zeile:
            line.append("Einwohner je qKM")
            erste_zeile = False
        else:
            einwohner_je_qkm = int(line[1]) / int(line[2])
            line.append(str(einwohner_je_qkm))
        end_file.write(",".join(line) + "\n")
print("Done")
