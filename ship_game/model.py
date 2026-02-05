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
        # Templates (für Anzeige / Erzeugung pro Spieler)
        self.ship_templates = [
            self.Ship("F125", 5),
            self.Ship("F124", 4),
            self.Ship("F123", 3),
            self.Ship("K130", 2)
        ]

        # Grids für Spieler 1 und 2
        self.grid1 = [["." for _ in range(10)] for _ in range(10)]
        self.grid2 = [["." for _ in range(10)] for _ in range(10)]

        # Schiffe pro Spieler (eigene Instanzen)
        self.ships_p1 = [self.Ship(s.name, s.length) for s in self.ship_templates]
        self.ships_p2 = [self.Ship(s.name, s.length) for s in self.ship_templates]

        # Mapping Position -> Ship-Objekt für schnellen Treffer-Check
        self.pos_to_ship_p1 = {}  # (y,x) -> Ship
        self.pos_to_ship_p2 = {}

    def display_grid(self, player=1, show_ships=True):
        """
        Zeigt das Grid des angegebenen Spielers an.
        Wenn show_ships=False werden eigene Schiffe ('X') verborgen (für Gegnersicht).
        """
        grid = self.grid1 if player == 1 else self.grid2
        header = "   " + " ".join(f"{i + 1:>2}" for i in range(10))
        print(f"Spieler {player} Board:")
        print(header)

        for r in range(10):
            letter = chr(ord("A") + r)
            def cell_repr(c):
                if not show_ships and c == "X":
                    return "."
                return c
            row = letter + "  " + " ".join(f"{cell_repr(cell):>2}" for cell in grid[r])
            print(row)

    def place_ship(self, player=1):
        """
        Platziert nacheinander alle Schiffe horizontal (nach rechts) für den angegebenen Spieler.
        player=1 -> grid1 / pos_to_ship_p1 / ships_p1
        player=2 -> grid2 / pos_to_ship_p2 / ships_p2
        """
        grid = self.grid1 if player == 1 else self.grid2
        pos_map = self.pos_to_ship_p1 if player == 1 else self.pos_to_ship_p2
        ships = self.ships_p1 if player == 1 else self.ships_p2

        rows = len(grid)
        cols = len(grid[0]) if rows > 0 else 0

        for ship in ships:
            while True:
                pos = input(f"[Spieler {player}] Startposition für {ship.name} (Länge {ship.length}) eingeben: ").strip().upper()
                if not pos:
                    print("Leere Eingabe.")
                    continue

                row_char = pos[0]
                col_str = pos[1:]
                if not ('A' <= row_char <= chr(ord('A') + rows - 1)) or not col_str.isdigit():
                    print("Ungültiges Format. Verwende z.B. A1 bis J10.")
                    continue

                y = ord(row_char) - ord('A')
                x = int(col_str) - 1

                if not (0 <= y < rows and 0 <= x < cols):
                    print("Position außerhalb des Feldes. Bitte A-J und 1-10 verwenden.")
                    continue

                if x + ship.length > cols:
                    print(f"Schiff würde über das Feld hinausgehen. Wähle eine andere Startposition.")
                    continue

                # Überlappung prüfen
                overlap = False
                for i in range(ship.length):
                    if grid[y][x + i] != ".":
                        overlap = True
                        break
                if overlap:
                    print("Überlappung mit vorhandenen Schiffen. Wähle eine andere Position.")
                    continue

                # Platzieren: Markiere als 'X' und im Mapping die Ship-Instanz
                for i in range(ship.length):
                    grid[y][x + i] = "X"
                    pos_map[(y, x + i)] = ship
                print(f"{ship.name} (Spieler {player}) platziert bei {row_char}{x+1} bis {row_char}{x+ship.length}.")
                break  # nächstes Schiff

    def take_shot(self, player, pos):
        """
        player schießt auf den Gegner.
        player=1 schießt auf Spieler 2.
        Rückgabewerte:
          - "already" wenn Feld schon beschossen
          - "miss" wenn Wasser
          - "hit" wenn Treffer aber nicht versenkt
          - "sunk:<name>" wenn Schiff versenkt
          - "win" wenn letzter Treffer alle Schiffe des Gegners versenkt
          - "invalid" bei fehlerhafter Eingabe
        """
        # Ziel bestimmen
        target_grid = self.grid2 if player == 1 else self.grid1
        target_map = self.pos_to_ship_p2 if player == 1 else self.pos_to_ship_p1
        target_ships = self.ships_p2 if player == 1 else self.ships_p1

        pos = pos.strip().upper()
        if len(pos) < 2:
            return "invalid"
        row_char = pos[0]
        col_str = pos[1:]
        if not row_char.isalpha() or not col_str.isdigit():
            return "invalid"
        y = ord(row_char) - ord('A')
        x = int(col_str) - 1
        rows = len(target_grid)
        cols = len(target_grid[0])

        if not (0 <= y < rows and 0 <= x < cols):
            return "invalid"

        cell = target_grid[y][x]
        if cell == "H" or cell == "o":
            return "already"

        if (y, x) in target_map:
            # Treffer
            ship = target_map[(y, x)]
            ship.hit()
            target_grid[y][x] = "H"
            if ship.is_sunk():
                # Prüfen ob alle Schiffe versenkt
                if self.all_ships_sunk(2 if player == 1 else 1):
                    return f"win:{ship.name}"
                return f"sunk:{ship.name}"
            return "hit"
        else:
            target_grid[y][x] = "o"
            return "miss"

    def all_ships_sunk(self, player):
        ships = self.ships_p2 if player == 2 else self.ships_p1
        return all(s.is_sunk() for s in ships)
