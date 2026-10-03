from model import SIZE


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
        self.view.update(self.model)
        while not self.model.game_over:
            name = self.model.shooter.player_name
            raw = input(f"{name} to fire (A1-J10, 'q' to quit): ").strip()
            if not raw or raw.lower() == "q":
                break
            pos = self._parse(raw)
            if pos is None:
                print("Invalid coordinate. Use e.g. A5 (A-J, 1-10).")
                continue
            result = self.model.fire(*pos)
            if result == "already":
                print(f"{raw.upper()} has already been fired at.")
                continue
            print(f"{name} fires {raw.upper()} -> {result}")
            self.view.update(self.model)
        if self.model.game_over:
            print(f"{self.model.winner()} wins the battle!")
        else:
            print("Game quit, no winner.")

    @staticmethod
    def _parse(raw):
        raw = raw.upper()
        if len(raw) != 2 or not "A" <= raw[0] <= "J" or not raw[1].isdigit():
            return None
        row_label = int(raw[1])
        if not 1 <= row_label <= SIZE:
            return None
        return SIZE - row_label, "ABCDEFGHIJ".index(raw[0])