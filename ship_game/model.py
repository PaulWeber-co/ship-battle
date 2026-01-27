#schiffe definieren
class Model:

    class Ship:
        def __init__(self, name, length):
            self.name = name
            self.length = length

    ships = [
        Ship("F125", 5),
        Ship("F124", 4),
        Ship("F123", 3),
        Ship("K130", 2)
    ]

