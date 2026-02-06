from model import Model

class View:
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
