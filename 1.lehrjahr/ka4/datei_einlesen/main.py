#!/usr/bin/python3

erste_zeile = 1
with open("bundeslaender.csv", "r") as file:
    lines = file.readlines()  # Read all lines into a list

with open("bundeslaender_erweitert.csv", "w") as end_file:
    for line in lines:
        line = line.strip().split(",")  # Split the line into a list
        if erste_zeile == 1:
            line.append("Einwohner je qKM")
            erste_zeile = 0
        else:
            einwohner_je_qkm = int(line[1]) / int(line[2])
            line.append(str(einwohner_je_qkm))
        end_file.write(",".join(line) + "\n")  # Join the list back into a string and write to the file
print("Done")

