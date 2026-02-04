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


# python
WaterA = [".", ".", ".", ".", ".", ".", ".", ".", ".", "."]
header = "   " + " ".join(f"{i+1:>2}" for i in range(len(WaterA)))
row = "A  " + " ".join(f"{cell:>2}" for cell in WaterA)
print(header)
print(row)
WaterB = [".", ".", ".", ".", ".", ".", ".", ".", ".", "."]
row = "B  " + " ".join(f"{cell:>2}" for cell in WaterB)
print(row)
WaterC = [".", ".", ".", ".", ".", ".", ".", ".", ".", "."]
row = "C  " + " ".join(f"{cell:>2}" for cell in WaterC)
print(row)
WaterD = [".", ".", ".", ".", ".", ".", ".", ".", ".", "."]
row = "D  " + " ".join(f"{cell:>2}" for cell in WaterD)
print(row)
WaterE = [".", ".", ".", ".", ".", ".", ".", ".", ".", "."]
row = "E  " + " ".join(f"{cell:>2}" for cell in WaterE)
print(row)
WaterF = [".", ".", ".", ".", ".", ".", ".", ".", ".", "."]
row = "F  " + " ".join(f"{cell:>2}" for cell in WaterF)
print(row)
WaterG = [".", ".", ".", ".", ".", ".", ".", ".", ".", "."]
row = "G  " + " ".join(f"{cell:>2}" for cell in WaterG)
print(row)
WaterH = [".", ".", ".", ".", ".", ".", ".", ".", ".", "."]
WaterH[5] = "X"
row = "H  " + " ".join(f"{cell:>2}" for cell in WaterH)

print(row)
WaterI = [".", ".", ".", ".", ".", ".", ".", ".", ".", "."]
row = "I  " + " ".join(f"{cell:>2}" for cell in WaterI)
print(row)
WaterJ = [".", ".", ".", ".", ".", ".", ".", ".", ".", "."]
row = "J  " + " ".join(f"{cell:>2}" for cell in WaterJ)

print(row)

# python
# 10x10 Grid als Liste von Listen
grid = [["." for _ in range(10)] for _ in range(10)]

# Änderungen vornehmen
grid[7][5] = "X"  # Row H (Index 7), Spalte 6 (Index 5)
grid[9][8] = "X"  # Row J (Index 9), Spalte 9 (Index 8)

# Ausgabe
header = "   " + " ".join(f"{i+1:>2}" for i in range(10))
print(header)

for r in range(10):
    letter = chr(ord("A") + r)
    row = letter + "  " + " ".join(f"{cell:>2}" for cell in grid[r])
    print(row)


""" python
Ziffern = ["." for _ in range(100)]  # 100 Punkte für 10x10 Grid

# Ausgabe
header = "   " + " ".join(f"{i+1:>2}" for i in range(10))
print(header)

for r in range(10):
    letter = chr(ord("A") + r)
    row = letter + "  " + " ".join(f"{Ziffern[r*10 + c]:>2}" for c in range(10))
    print(row)
    Ziffern[25] = "X"
    Ziffern[88] = "o"
"""