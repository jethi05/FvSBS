#!/usr/bin/env python3
#from math import sqrt

class Viereck:

    def __init__(self):
        self.__a:int = 0
        self.__b:int = 0
        self.__c:int = 0
        self.__d:int = 0

    def set_a(self, a):
        self.__a = a


    def set_b(self, b):
        self.__b = b

    def set_c(self, c):
        self.__c = c

    def set_d(self, d):
        self.__d = d

    def get_a(self):
        return self.__a

    def get_b(self):
        return self.__b

    def get_c(self):
        return self.__c

    def get_d(self):
        return self.__d

    def get_umfang(self):
        return(self.__a+self.__b+self.__c+self.__d)

v = Viereck()

v.set_a(3)
v.set_b(4)
v.set_c(3)
v.set_d(4)
print(v.get_umfang())

def analysiere_viereck(v):
    print(v.get_a()) 

analysiere_viereck(v)
