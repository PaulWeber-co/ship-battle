import tkinter as tk
import string
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

    def print_grid(self):

        cols = list(range(0, 10))                  # 1–10
        rows = list(range(0, 10))   # A–J

        print("   ", end="")
        for c in cols:
            print(f"{c:>3}", end="")
        print()
        for r in rows:
            print(f"{r} |", end="")
            for _ in cols:
                print(" . ", end="")
            print()



