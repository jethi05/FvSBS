#!/usr/bin/python3
def gefahrene_laenge(pass_id):
    sum = 0
    with open("LogSkipass", "r") as file:
         for eintrag in file:
            if eintrag.split("|")[2] == pass_id:
                sum += int(eintrag.split("|")[5])
         return(f">>{sum}")
print(gefahrene_laenge("30201"))
