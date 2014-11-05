menu={"Spaghetti":10, "Pizza":21.50, "Ziemniaczki":5.00,"Klopsiki":10.50,
      "Ryz":5, "Zupa":6.90,"Woda":2, "Kanapka":1,"Tost":2,"Parowka":3.5}

def koszt(zamowienie):
    koszt=0
    for danie in zamowienie:
        if danie in menu:
            koszt=koszt+menu[danie]
    return "Koszt zamowienia to: " + str(round(koszt+0.05*koszt,2)) + "zl."

print koszt(["Ryz","Zupa","Kanapka"])