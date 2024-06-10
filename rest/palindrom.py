#!usr/bin/env bash
# Aufgabe 19
# Wenn ein String ein Palindrom ist, gibt das Programm ```True``` aus. Sonst ```False```. Löse das Problem mit einer while-Schleife. Ein Palindrom klingt gleich, egal ob es vorwärts oder rückwärts gelesen wird. Beispiele: ehe, anna, kajak, rentner, reliefpfeiler. Bonus: Erweitere dein Programm so, dass es auch Satzpalindrome erkennen kann. Beispiele für Satzpalindrome: "anna hetzte hanna", "dreh mal am herd", "ein eis esse sie nie". Tipp: ```wort.replace('ae', 'ä')``` ersetzt alle 'ae' in Wort durch 'ä'.

# Dieses Zeile 6 wird immer benötigt
palindrom = "Dreh mal am Herd".replace(" ", "").lower()


# EIne Extrene Lösung, ohne while schleife
# Diese Lösung ist einfach unnötig, sie bringt keinen Vorteil
if palindrom == palindrom[::-1]:
    print("True")
else:
    print("False")


# eine extremere Lösung:
print(palindrom==palindrom[::-1])


# die Lösung mit der while Schleife
n = 0
while n < len(palindrom)/2:
    if palindrom[n] == palindrom[(n+1)*(-1)]:
        n += 1
    else:
        n = len(palindrom)+2
print(n < len(palindrom))
