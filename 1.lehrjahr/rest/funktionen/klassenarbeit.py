#!/usr/bin/python3
#Aufgabe 1
tag = 1
zombies = 1
menschen = 116033
while menschen >= zombies:
    zombies += zombies*1.5
    tag +=1
    print(f"Zombies: {zombies}   Menschen: {menschen} tag: {tag}")
