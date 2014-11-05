# -*- coding: utf-8 -*-

from math import sqrt

class Zespolona:
    def __init__(self,a,b):
        self.r=a
        self.u=b
    def getR(self):
        return self.r
    def setR(self,r):
        self.r=r
    def getU(self):
        return self.u
    def setU(self,u):
        self.u=u
    def dodaj(self,liczba):
        return Zespolona(self.r+liczba.r,self.u+liczba.u)
    def odejmij(self,liczba):
        return Zespolona(self.r-liczba.r,self.u-liczba.u)
    def modul(self):
        return sqrt(self.r**2+self.u**2)
    def __str__(self):
        return str(self.r)+" + "+str(self.u)+"i"
    pass


z1=Zespolona(2,3)
z2=Zespolona(-1,4)

print "Liczba zespolona z1 to: "+str(z1) +", a liczba zespolona z2 to: " +str(z2)+"."
print "Dodawanie z1+z2 to z3 rowne: " + str(z1.dodaj(z2))+"."
print "Odejmowanie z1-z2 to z3 rowne: " + str(z1.odejmij(z2))+"."
print "Moduly liczb z1 i z2 to kolejno: %4.4f i %4.4f." %(z1.modul(),z2.modul())

