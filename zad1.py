import time 

#Uzytkownik podaje dowolny plik tekstowy, oczywiscie z zalozeniem ze jest w tym samym folderze co program, jesli nie musialby podac cala sciezke
sciezka=raw_input("Podaj nazwe pliku do analizowania (wraz z rozszerzeniem!): ")

plik=open(str(sciezka),"r")
tekst=[] #plik wejsciowy czysto po odczytaniu
for linia in plik:
   linijka=linia.split(" ")
   tekst.append(linijka)
plik.close()

zn=0 #flaga do znakow interpunkcyjnych i zalamania linii
tekst2=[]   #tekst bez znakow interpunkcyjnych i zalamania linii, tworzony w ponizszej petli, ponadto usuwa wielkie litery
for i in xrange(0,len(tekst)):
    for slowo in tekst[i]:
        for znak in slowo:
            if znak==".":
                zn=1
            elif znak==",":
                zn=2
            elif znak=="\n":
                zn=3
        if zn==1:
            tekst2.append(str(slowo).replace(".","").lower())
        elif zn==2:
            tekst2.append(str(slowo).replace(",","").lower())
        elif zn==3:
            tekst2.append(str(slowo).replace("\n","").lower())
        else:
            tekst2.append(str(slowo).lower())

#Zbior slow unikalnych z wykluczeniem pustych miejsc i spacji jako slow
unikalne=set(tekst2)
unikalne.discard("")
unikalne.discard(" ")

wynik=[] #wynikowa lista, ktora zawiera krotki z nazwa slowa i iloscia jego wystepowania w tekscie
for element in unikalne:
    krotka=(element,tekst2.count(element))
    wynik.append(krotka)

#Zapisanie do pliku
plik=open("statystyki.txt","a")
plik.writelines("\nSTATYSTYKI dla pliku tekstowego, stan na " + time.strftime("%H:%M dnia:%d.%m.%Y")+"\n")
for krotka in wynik:
    if krotka[1]!=1:
        plik.writelines( "Slowo '" +str(krotka[0]) + "' wystepuje "+ str(krotka[1])+ " razy.\n")
    else:
        plik.writelines( "Slowo '" +str(krotka[0]) + "' wystepuje "+ str(krotka[1])+ " raz.\n")
plik.close()

print "Statystyki przeprowadzono i dopisano do pliku 'statystyki.txt'."