#!/usr/bin/python3
def primzahltester(n):
    t = 0
    i = 1
    while i <= n:
        print(n%2==0)
        if n % 2 == 0:
            t += 1
        i += 1
    if t == 2:
        print(f"{n} ist keine Primzahl")
    else:
        print(f"{n} ist eine Primzahl")
primzahltester(35)
#print(17%2==0)
#liste=[4,6,8,10,12,14,15,16]
#for entry in liste:
#    print(entry%2==0)
