"""
from datetime import date
import json
import unicodedata


#Hilfsfunktionen
def reminder():
    heute = date.today()
    formattedDate = heute.strftime("%d.%m")
    geburtstag = False
    for d in personen:
        if d.bd == formattedDate:
            print("Heute hat jemand Geburtstag")
            geburtstag = True
    if not geburtstag:
        print("Heute hat keiner Geburtstag")

def addBirthday():
    print("Name eingeben")
    name = input()
    print("Geburtstag eingeben")
    bd = input()
    personen.append(Person(name, bd))
    print("\nGeburtstagsliste:")
    for p in personen:
        print(p.name,"->", p.bd)


def search():
    print("Nach welchem Namen soll gesucht werden?")
    n = input()
    n = n.lower()
    gefunden = False

    for p in personen:
        if p.name.lower() == n:
            print("Gefunden:", p.name, "hat am", p.bd, "Geburtstag")
            gefunden = True
    if not gefunden:
        print("Name nicht gefunden")

#wenn keine eingabe

class Person:
    def __init__(self, name, bd):
        self.name = name
        self.bd = bd
personen = [
        Person("paul", "13.01"),
        Person("lukas", "23.05"),
        Person("markus", "13.09"),
        Person("robert", "28.04")
]
#y = json.dumps(personen)
#print(y)

#Main
print("Wähle 1 um einen neuen Geburtstag hinzuzufügen (name, geburtstag), 2 um alle vorhandenen anzusehen, 3 um nach einem Namen zu suchen")
x = input()
reminder()
if x == "1":
    addBirthday()
elif x == "2":
    print("\nGeburtstagsliste:")
    for p in personen:
        print(p.name,"->", p.bd)
elif x == "3":
    search()
else:
   print("Bitte nur 1 oder 2 eingeben oder 3")

"""