#Hallo Welt ausgeben
#print("Hallo Welt")

#Mit Scanner Namen einlesen und begrüßen
#print("Wie heißt du?")
#name = input()
#print("Hallo " + name)

#Random Nummer ausgeben (1-6)
import random
#print(random.randrange(1,7))

def calcPoss():
    i = 1
    while i <= 6:
        j = 1
        while j <= 6:
            wert = i + j
            print("Würfel1:", i, "Würfel2:", j, "-> Summe", wert)
            j += 1
        i += 1

import random


import random

def diceThrow():
    def roll_die():
        print("6, 10 oder 12")
        würfelart = input()
        try:
            sides = int(würfelart)
        except ValueError:
            print("Ungültige Eingabe.")
            return None

        if sides in (6, 10, 12):
            return random.randrange(1, sides + 1)
        else:
            print("Bitte nur 6, 10 oder 12 angeben")
            return None

    print("Welcher Würfel soll als erstes geworfen werden?")
    w1 = roll_die()
    if w1 is None:
        return

    print("Welcher Würfel für den zweiten Wurf?")
    w2 = roll_die()
    if w2 is None:
        return

    summe = w1 + w2

    print("Wette: Was ist das Endergebnis?")
    wette = input()
    try:
        wette = int(wette)
    except ValueError:
        print("Ungültige Eingabe für die Wette.")
        return

    if wette == summe:
        print("Glückwunsch")
    else:
        print("Falsch, Pech gehabt")

    print("Erster Wurf:", w1, "Zweiter Wurf:", w2, "Summe:", summe)


print("Möchtest du alle Möglichkeiten sehen (drücke 1) oder den Würfel direkt werfen? (drücke 2)")

ent = input()

if ent == "1":
    calcPoss()

elif ent == "2":
    diceThrow()


#Welcher Teil macht was? Zwei print Statements um User zur Eingabe zu bewegen. 2x Berechnung der random Number je nach Würfelart (kann man auch als 1 Statement programmieren). Ausgabe der Werte und bildung der Summe.
#Hilfsmethoden implementieren
#Aufgabe 6 siehe oben

#Einfaches Würfelprogramm (Google)
result = random.randint(1, 6)
print("You rolled", {result})

