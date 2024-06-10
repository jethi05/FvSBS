#!/usr/bin/python3
# Caesar Verschlüsselung bauen

wort=input("Geben sie ein Wort zum Verschlüsseln ein \n>> ")
liste=[]
verschl_wert=int(input("Geben sie einen Verschlüsselungsfaktor ein \n>> "))
output=""

for buchstabe in wort:
    output += chr(ord(buchstabe)+verschl_wert)
print(output)

