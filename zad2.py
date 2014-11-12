# -*- coding: utf-8 -*-

menu = {}
klucze=[]
wartosci=[]

plik=open("menu.txt","r")
tekst=[] #plik wejsciowy czysto po odczytaniu
for linia in plik:
   linijka=linia.split(":")
   klucze.append(str(linijka[0]))
   wartosci.append(float(linijka[1]))
plik.close()

menu=dict(zip(klucze,wartosci))
print "Wczytane menu z pliku menu.txt to: "
print menu


def koszt(zamowienie):
    niema=[]
    koszt=0
    for danie in zamowienie:
        if danie in menu:
            koszt=koszt+menu[danie]
        else:
            niema.append(danie)
    if len(niema)==0:
        return "Koszt zamowienia to: " + str(round(koszt+0.05*koszt,2)) + "zl."
    elif len(niema)==len(zamowienie):
        return "Zadnego z Twoich dan nie ma w menu."
    else:
        return "Elemety: "+ str(niema) +" nie istnieja w menu. Koszt pozostalego zamowienia to: "+ str(round(koszt+0.05*koszt,2)) + "zl."

print "\n Dla zamówienia, które jest w pełni w menu funkcja zwraca: "
print koszt(["Ryz","Zupa","Kanapka"])

print "\n Dla zamówienia, które jest częściowo w menu funkcja zwraca: "
print koszt(["Ryz","Zupa","Kanapka", "Kabaczek", "Kaszanka", "Klopsiki"])

print "\n Dla zamówienia, które nie ma wcale w menu funkcja zwraca:"
print koszt(["Kaszanka","Kabaczek"])
