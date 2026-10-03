import random

SIZE = 10
FLEET = [5, 4, 3, 3, 2, 2, 1]
SHIP_NAMES = ["Carrier", "Battleship", "Cruiser", "Submarine",
              "Destroyer 1", "Destroyer 2", "Patrol Boat"]


class Ship:
    def __init__(self, name, length, row, col, horizontal):
        self.name = name
        self.length = length
        self.horizontal = horizontal
        self.hits = 0
        self.cells = [
            (row + (0 if horizontal else i), col + (1 if horizontal else 0))
            for i in range(length)
        ]

    @property
    def sunk(self):
        return self.hits >= self.length


class Board:
    def __init__(self, player_name):
        self.player_name = player_name
        self.ships = []
        self.grid = [[None] * SIZE for _ in range(SIZE)]
        self.shots = set()  # cells already fired at this board

    def place_randomly(self):
        for name, length in zip(SHIP_NAMES, FLEET):
            while True:
                horizontal = random.random() < 0.5
                row = random.randrange(SIZE)
                col = random.randrange(SIZE)
                if (horizontal and col + length > SIZE) or \
                   (not horizontal and row + length > SIZE):
                    continue
                cells = [(row + (0 if horizontal else i),
                          col + (1 if horizontal else 0))
                         for i in range(length)]
                if any(self.grid[r][c] for r, c in cells):
                    continue
                ship = Ship(name, length, row, col, horizontal)
                for r, c in cells:
                    self.grid[r][c] = ship
                self.ships.append(ship)

    def all_sunk(self):
        return all(ship.sunk for ship in self.ships)


class GameModel:
    def __init__(self):
        self.boards = [Board("Player 1"), Board("Player 2")]
        for board in self.boards:
            board.place_randomly()
        self.current = 0

    @property
    def shooter(self):
        return self.boards[self.current]

    @property
    def target(self):
        return self.boards[1 - self.current]

    def fire(self, row, col):
        """Fire at (row, col) of the target board. Returns a result string."""
        if not 0 <= row < SIZE or not 0 <= col < SIZE:
            return "invalid"
        if (row, col) in self.target.shots:
            return "already"
        self.target.shots.add((row, col))
        ship = self.target.grid[row][col]
        if ship is None:
            result = "miss"
        else:
            ship.hits += 1
            result = f"sunk {ship.name}!" if ship.sunk else "hit"
        if not self.target.all_sunk():
            self.current = 1 - self.current
        return result

    @property
    def game_over(self):
        return any(board.all_sunk() for board in self.boards)

    @property
    def winner(self):
        return self.boards[self.current].player_name