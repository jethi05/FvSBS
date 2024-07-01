#!/usr/bin/pythn3
erste_zeile = 1
with open("bundeslaender.csv", "r") as file:
    file = file.read()
with open("bundeslaender_erweitert.csv", "w") as end_file:
    for line in file:
        line.split(",")
        print(line)
        if erste_zeile == 1:
            line.append("Einwohner je qKM")
            erste_zeile = 0
        else:
            line.append(f"{line[1]/line[2]}")
        end_file.write(line)
    file.close()
