#!/usr/bin/python3
'''Suche Mac-Adresse in Array'''
def SucheMAC(array_mac_adresse, suchende_mac_adresse):
    return suchende_mac_adresse in array_mac_adresse
liste = ["192.168.178.1","192.168.178.2"]
print("ist True: " + str(SucheMAC(liste, "192.168.178.1")))
print("ist False: " + str(SucheMAC(liste, "192.168.178.3")))
