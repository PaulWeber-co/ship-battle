# python
class Model:
    class Ship:
        def __init__(self, name, length):
            self.name = name
            self.length = length
            self.hits = 0

        def hit(self):
            self.hits += 1

        def is_sunk(self):
            return self.hits >= self.length

    def __init__(self):
        self.grid = [["." for _ in range(10)] for _ in range(10)]
        self.ships = [
            self.Ship("F125", 5),
            self.Ship("F124", 4),
            self.Ship("F123", 3),
            self.Ship("K130", 2)
        ]

    def display_grid(self):

        header = "   " + " ".join(f"{i + 1:>2}" for i in range(10))
        print(header)

        for r in range(10):
            letter = chr(ord("A") + r)
            row = letter + "  " + " ".join(f"{cell:>2}" for cell in self.grid[r])
            print(row)

    def place_ship(self):

        print("In welche Zeile möchtest du das Schiff setzen? (A-J)")
        y = ord(input().upper()) - ord("A")
        print("In welche Spalte möchtest du das Schiff setzen? (1-10)")
        x = int(input()) - 1

        self.grid[y][x] = "X"
