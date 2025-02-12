# Lösung erklärt
Nur Linux spezifisch, nicht beachten
```
#!/usr/bin/python3
```
```
''' Zehn stellige Zahl, 1-9 werden mal deren Stelle'''
def pruefeNummer(liste):
```
Es wird Summe und Stelle definiert um keine For Schleife machen zu müssen, da dieses nur Länger wird
```
    summe = 0
    stelle = 0
```
In der `for`-Schleife wird die Liste auseinander genommen, in dem Array, der Liste, wird der erste Eintrag genommen, daher, dass die zehnte Stelle nur die Prüfsumme ist, wird diese nicht genommen, daher dass `[:9:]`
    for zahl in liste[0][:9:]:
        stelle += 1
        summe += int(zahl) * stelle
    return(summe%10 == int(liste[0][9]))
print(pruefeNummer(["5124897253"]))
```
meldet euch bei Fragen ;)
