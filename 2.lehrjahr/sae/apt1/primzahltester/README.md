```
def primzahltester(n):
    t = 0
    i = 1
```
t = Teilerzahl, i = Laufvariable, Schaue in der Schleife alle Werte zwischen 0 und der Zahl n an und probiere diese zu teilen. Wenn die Zahl nur durch 1 und sich selbst teilbar ist, dann ist es eine Primzahl, ist es öfters teilbar, ist es keine
```
    while i <= n:
        if n % 2 == 0:
            t += 1
        i += 1
    if t == 2:
        print(f"{n} ist keine Primzahl")
    else:
        print(f"{n} ist eine Primzahl")
primzahltester(3)
```
