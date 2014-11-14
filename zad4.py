#Zestaw klas modelujacych fragment rzeczywistosci: SWIAT ZWIERZAT
#zrodlo informacji: http://pl.wikipedia.org/wiki/Zwierz%C4%99ta
from __builtin__ import True

#Krolestwo zwierzat
class Zwierzeta:
    def __init__(self,nazwa):
        self.nazwa=nazwa
    def jedz(self):
        return "Zjadlem"
    def oddychaj(self):
        return "Oddycham"
    def daj_glos(self):
        return "Dzwiek"
    def get_gatunek(self):
        return self.gatunek
    def set_gatunek(self,wartosc):
        self.gatunek=wartosc
    def get_srodowisko_naturalne(self):
        return self.srodowisko
    def set_srodowisko_naturalne(self,wartosc):
        self.srodowisko=wartosc 
    pass

#Glowny podzial krolestwa
class Bezkregowce(Zwierzeta):
    kregoslup = False
    czaszka=False
    def daj_glos(self):
        return "Nie umiem"
    pass

class Kregowce(Zwierzeta):
    kregoslup=True
    czaszka = True
    skora=True
    pass

#Podzial kregowcow
class Ssaki(Kregowce):
    mam_futerko=True
    pass
class Gady(Kregowce):
    def daj_glos(self):
        return "Nie umiem"
    pass
class Plazy(Kregowce):
    def daj_glos(self):
        return "Nie umiem"
    pass
class Ptaki(Kregowce):
    def daj_glos(self):
        return "Cwir cwir"
    def get_nielot(self):
        return self.nielot
    def set_nielot(self,wartosc):
        self.nielot=wartosc 
    def lataj(self):
        if self.nielot==True:
            return "Nie umiem latac"
        else: 
            return "Umiem latac i lece"
    pass
class Ryby(Kregowce):
    skrzela=True
    def daj_glos(self):
        return "Plum"
    def plywaj(self):
        return "Umiem plywac"
    pass

#Wybrane bezkregowce
class Mieczaki(Bezkregowce):
    def pelzaj(self):
        return "Jestem mieczakiem i sobie pelzne"
    pass
class Owady(Bezkregowce):
    def dokuczaj(self):
        return "Jestem owadem i denerwuje ludzi"
    pass
class Gabki(Bezkregowce):
    def zyj(self):
        return "Jestem gabka i jestem prymitywnym typem zwierzecia :("
    pass
    pass

#Poszczegolni przedstawiciele kregowcow i bezkregowcow
class Kot(Ssaki):
    def daj_glos(self):
        return "Miau!"
    pass
class Pies(Ssaki):
    def daj_glos(self):
        return "Hau!"
    pass
class Kotopies(Kot,Pies):
    def co_ty_jestes(self):
        return "Jestem kot-pies dlatego robie Miau, jakbym byl pies-kot robilbym Hau"
    pass
class Slimak(Mieczaki):
    gatunek="slimak"
    muszla=True
    czulki=True
    pass
class Komar(Owady):
    gatunek = "komar"
    def ssij_krew(self):
        return "Mniam mniam ale dobra"
    def lataj(self):
        return "Umiem latac"
    pass

#Rozne przyklady wykorzystania stworzonych klas
kot = Kot("Filemon")
waz = Gady("waz")
fred=Kotopies("fred")
print "Kot "+kot.nazwa+ " robi "+kot.daj_glos()
print "A waz robi "+ waz.daj_glos()
kot.set_gatunek("syjamski")
print "Gatunek kota to: " + kot.get_gatunek()
gabka=Gabki("panGabka")
if gabka.kregoslup==False:
    print gabka.nazwa + " nie ma kregoslupa"
else:
    print gabka.nazwa + " ma kregoslup"
if kot.kregoslup==False:
    print kot.nazwa + " nie ma kregoslupa"
else:
    print kot.nazwa + " ma kregoslup"
ptak = Ptaki("bociek")
ptak.set_nielot(False)
kiwi = Ptaki("kiwi")
kiwi.set_nielot(True)
print kiwi.nazwa + " mowi: " + kiwi.lataj()
print ptak.nazwa + " mowi: " + ptak.lataj()
slimol = Slimak("Henryk")
print "Slimak imieniem " + slimol.nazwa + " ma gatunek " + slimol.get_gatunek()
stefan=Komar("Stefan")
print stefan.nazwa + " to " + stefan.get_gatunek() + " i umie tylko mowic: " + stefan.dokuczaj()