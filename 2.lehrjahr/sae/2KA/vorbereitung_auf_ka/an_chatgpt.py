#!/usr/bin/env python3
class RPGCharackter:
    def __init__(self):
        self.__staerke = 0
        self.__interlligenz = 0
        self.__geschicklichkeit = 0

    def set_staerke(self, staerke):
        if staerke >= 0:
            self.__staerke = staerke
    def set_interlligenz(self, interlligenz):
        if interlligenz >= 0:
            self.__interlligenz = interlligenz
    def set_geschicklichkeit(self, geschicklichkeit):
        if geschicklichkeit >= 0:
            self.__geschicklichkeit = geschicklichkeit

    def get_staerke(self):
        return self.__staerke
    def get_interlligenz(self):
        return self.__interlligenz
    def get_geschicklichkeit(self):
        return self.__geschicklichkeit

    def berechne_kampfwert(self):
        return self.__staerke + self.__interlligenz/2 + self.__geschicklichkeit*2

def analysiere_charakter(o):
    s = o.get_staerke()
    i = o.get_interlligenz()
    g = o.get_geschicklichkeit()
    if s > 300:
        print("Legendärer Held")
    if s > i + 10 and s > g + 10:
        print("Krieger")
    elif i > s + 10 and i > g + 10:
        print("Magier")
    elif g > s + 10 and g > i + 10:
        print("Schurke")
    else:
        print("Abenteurer")

def erstelle_charackter(o_name, s, i, g):
    o_name = RPGCharackter()
    o_name.set_staerke(s)
    o_name.set_interlligenz(i)
    o_name.set_geschicklichkeit(g)
erstelle_charackter(x, 90, 30, 20)
