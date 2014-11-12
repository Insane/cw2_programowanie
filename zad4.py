#Zestaw klas modelujacych fragment rzeczywistosci: SWIAT ZWIERZAT
#zrodlo informacji: http://pl.wikipedia.org/wiki/Zwierz%C4%99ta

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
    pass
class Strunowce(Zwierzeta):
    pass
class Kregowce(Zwierzeta):
    pass

class Ssaki(Kregowce):
    pass

class Gady(Kregowce):
    pass

class Plazy(Kregowce):
    pass
class Ptaki(Kregowce):
    pass
class Ryby(Kregowce):
    pass
class Mieczaki(Strunowce):
    pass
class Stawonogi(Strunowce):
    pass
class Gabki(Strunowce):
    pass

class Kot(Ssaki):
    def daj_glos(self):
        return "Miau!"
    pass
class Pies(Ssaki):
    def daj_glos(self):
        return "Hau!"
    pass

kot = Kot("Filemon")
waz = Gady("waz")
print "Kot "+kot.nazwa+ " robi "+kot.daj_glos()
print "A waz robi "+ waz.daj_glos()
kot.set_gatunek("syjamski")
print "Gatunek kota to: " + kot.get_gatunek()