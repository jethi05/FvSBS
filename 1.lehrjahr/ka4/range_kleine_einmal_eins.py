#!/usr/bin/python3
# Gebe das ganze kleine einmal eins aus
for r_zahl in range(1,11):
    print(f"\n{r_zahl}er Reihe")
    for l_zahl in range(1,11):
        print(f"{l_zahl}\t*\t{r_zahl}\t=\t{l_zahl*r_zahl}")
