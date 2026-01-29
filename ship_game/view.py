
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
        for row in board.grid:
            print(" ".join(row))



