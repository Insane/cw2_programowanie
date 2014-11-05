import time

plik=open("plik.txt","r")

unikalne=set()
tekst=[]

tt=[]

for linia in plik:
   linijka=linia.split(" ")
   tt.append(linijka)

plik.close()
zn=0
   
tekst2=[]
wynik=[]
for i in xrange(0,len(tt)):
    for slowo in tt[i]:
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

unikalne=set(tekst2)
unikalne.discard("")
unikalne.discard(" ")


for element in unikalne:
    krotka=(element,tekst2.count(element))
    wynik.append(krotka)
   
plik=open("statystyki.txt","a")
plik.writelines("\nSTATYSTYKI dla pliku tekstowego, stan na: " + str(time.localtime())+"\n")
for krotka in wynik:
    if krotka[1]!=1:
        plik.writelines( "Slowo '" +str(krotka[0]) + "' wystepuje "+ str(krotka[1])+ " razy.\n")
    else:
        plik.writelines( "Slowo '" +str(krotka[0]) + "' wystepuje "+ str(krotka[1])+ " raz.\n")

plik.close()