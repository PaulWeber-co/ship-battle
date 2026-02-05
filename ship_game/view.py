from model import Model

class View:


    #def show_menu_single(self):
       # print("1 Player Mode (1) or 2 Player Mode (2)")

    def get_input(self):
        try:
            return int(input())
        except:
            return None

    def show_instruction_ships(self, ships):
        text = ", ".join(f"{s.name} (Länge {s.length})" for s in ships)
        print(
            "Du kannst folgende Schiffe: "
            f"{text} "
            "in einem 10x10 Grid horizontal platzieren."
        )

    def get_coord(self, prompt="Koordinate: "):
        return input(prompt).strip()
