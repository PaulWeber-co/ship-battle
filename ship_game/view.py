from model import Model

class View:


    def show_menu_single(self):
        print("1 Player Mode (1) or 2 Player Mode (2)")

    def get_input(self):
        try:
            return int(input())
        except:
            return None
    def show_instruction(self):
        text = ", ".join(f"{s.name} (Länge {s.length})" for s in Model.ships)
        print(
        "Du kannst folgende Schiffe: "
        f"{text} "
        "in einem 10x10 Grid von oben nach unten platzieren.\nWo soll das Schiff hin?"
        )


    class ConsoleView:
        def show_board(self, board):
            size = board.size
            # Kopfzeile: Platz für Zeilenlabel + Spaltennummern (ausgerichtet für bis zu 2 Stellen)
            header = " " + " ".join(f"{i+1:2}" for i in range(size))
            print(header)
            # Jede Zeile mit Buchstabenlabel (A, B, C, ...)
            for r, row in enumerate(board.grid):
                label = chr(ord('A') + r) if r < 26 else str(r)
                # Zellen ebenfalls etwas gepolstert, damit die Spalten ausgerichtet bleiben
                print(f"{label} " + " ".join(f"{cell:2}" for cell in row))
