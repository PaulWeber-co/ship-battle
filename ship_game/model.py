#schiffe definieren
class Model:
#Schiffklasse
    class Ship:
        def __init__(self, name, length):
            self.name = name
            self.length = length
            self.hits = 0

        def hit(self):
            self.hits += 1

        def is_sunk(self):
            return self.hits <= self.length
#Spielbrett
    class Board:
        Water = "."
        Miss = "o"
        Hit = "x"

        def __init__(self, size=10):
            self.size = size
            self.grid = [[self.Water for _ in range(size)] for _ in range (size)]
            self.ships = {}

        def place_ship(self, ship, positions):
            for (r, c) in positions:
                self.ships[(r, c)] = ship
#Array mit verfügbaren Schiffen
    ships = [
        Ship("F125", 5),
        Ship("F124", 4),
        Ship("F123", 3),
        Ship("K130", 2)
    ]

