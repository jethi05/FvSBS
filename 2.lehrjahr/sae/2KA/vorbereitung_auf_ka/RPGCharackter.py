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
    if o.berechne_kampfwert() > 300:
        print("---Legendärer Held")
    if s > i + 9 and s > g + 9:
        print("Krieger")
    elif i > s + 9 and i > g + 9:
        print("Magier")
    elif g > s + 9 and g > i + 9:
        print("Schurke")
    else:
        print("Abenteurer")

def erstelle_charackter(o_name, s, i, g):
    o_name.set_staerke(s)
    o_name.set_interlligenz(i)
    o_name.set_geschicklichkeit(g)
    analysiere_charakter(o_name)
    print(o_name.berechne_kampfwert())
a = RPGCharackter()
erstelle_charackter(a, 90, 30, 20)
b = RPGCharackter()
erstelle_charackter(b, 30, 90, 20)
c = RPGCharackter()
erstelle_charackter(c, 20, 30, 90)
d = RPGCharackter()
erstelle_charackter(d, 70, 60, 80)
e = RPGCharackter()
erstelle_charackter(e, 100, 100, 100)
f = RPGCharackter()
erstelle_charackter(f, 50, 70, 50)

