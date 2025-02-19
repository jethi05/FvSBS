#!/usr/bin/python3
def primzahltester(n):
    t = 0
    i = 1
    while i <= n:
        if n % 2 == 0:
            t += 1
        i += 1
    if t == 2:
        print(f"{n} ist keine Primzahl")
    else:
        print(f"{n} ist eine Primzahl")
primzahltester(3)
