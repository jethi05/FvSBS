#!/usr/bin/python3
'''Suche Mac-Adresse in Array'''
def SucheMAC(macAdressen, gesucht):
    return macAdressen in gesucht
liste = ["A5","B6","C8"]
print("ist True: " + str(SucheMAC(liste,("C8"))))
print("ist False: " + str(SucheMAC(liste,"F0")))
