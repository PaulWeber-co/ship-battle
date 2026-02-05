class Model:
    class Ship:
        def __init__(self, name, length):
            self.name = name
            self.length = length
            self.hits = 0
            self.positions = []

        def hit(self):
            self.hits = self.hits + 1

        def is_sunk(self):
            return self.hits >= self.length

    def __init__(self):
        self.ship_list = [
            self.Ship("F125", 5),
            self.Ship("F124", 4),
            self.Ship("F123", 3),
            self.Ship("K130", 2)
        ]
        self.grid1 = [["." for _ in range(10)] for _ in range(10)]
        self.grid2 = [["." for _ in range(10)] for _ in range(10)]
        self.ships_p1 = [self.Ship(s.name, s.length) for s in self.ship_list]
        self.ships_p2 = [self.Ship(s.name, s.length) for s in self.ship_list]

    def get_grid(self, player):
        if player == 1:
            return self.grid1
        return self.grid2

    def get_ships(self, player):
        if player == 1:
            return self.ships_p1
        return self.ships_p2

    def display_grid(self, player=1, show_ships=True):
        grid = self.get_grid(player)
        print(f"Spieler {player} Board:")
        print("   " + "".join(f"{i + 1:>2}" for i in range(10)))

        for r in range(10):
            letter = chr(ord("A") + r)
            row = letter + "  "
            for c in grid[r]:
                if not show_ships and c == "X":
                    row = row + " ."
                else:
                    row = row + " " + c
            print(row)

    def parse_position(self, pos):
        pos = pos.strip().upper()
        if len(pos) < 2:
            return None, None
        y = ord(pos[0]) - ord("A")
        try:
            x = int(pos[1:]) - 1
            if y < 0 or y > 9 or x < 0 or x > 9:
                return None, None
            return y, x
        except:
            return None, None

    def place_ship(self, player=1):
        grid = self.get_grid(player)
        ships = self.get_ships(player)

        for ship in ships:
            while True:
                pos = input(f"[Spieler {player}] {ship.name} (Länge {ship.length}): ")
                y, x = self.parse_position(pos)

                if y is None or x is None:
                    print("Ungültig. Format: A1")
                    continue

                if x + ship.length > 10:
                    print("Schiff passt nicht. Zu nah am Rand.")
                    continue

                frei = True
                for i in range(ship.length):
                    if grid[y][x + i] != ".":
                        frei = False

                if not frei:
                    print("Überlappung. Wähle andere Position.")
                    continue

                for i in range(ship.length):
                    grid[y][x + i] = "X"
                    ship.positions.append((y, x + i))

                print(f"{ship.name} platziert bei {chr(ord('A') + y)}{x + 1}.")
                break

    def take_shot(self, player, pos):
        if player == 1:
            target_grid = self.grid2
            target_ships = self.ships_p2
        else:
            target_grid = self.grid1
            target_ships = self.ships_p1

        y, x = self.parse_position(pos)
        if y is None or x is None:
            return "invalid"

        if target_grid[y][x] == "H" or target_grid[y][x] == "o":
            return "already"

        if target_grid[y][x] == "X":
            target_grid[y][x] = "H"
            ship = None
            for s in target_ships:
                if (y, x) in s.positions:
                    ship = ship.hit()

            if ship.is_sunk():
                alle_versenkt = True
                for s in target_ships:
                    if not s.is_sunk():
                        alle_versenkt = False
                if alle_versenkt:
                    return f"win:{ship.name}"
                return f"sunk:{ship.name}"
            return "hit"
        else:
            target_grid[y][x] = "o"
            return "miss"