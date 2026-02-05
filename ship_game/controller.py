from model import Model
class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
        #Schiffstypen
        self.view.show_instruction_ships(self.model.ship_list)

        # Spieler 1
        print("\nSpieler 1 platziert")
        self.model.display_grid(player=1, show_ships=True)
        self.model.place_ship(player=1)
        print("\nFertig Spieler 1:")
        self.model.display_grid(player=1, show_ships=True)

        input("\nWeitergeben an Spieler 2 und Enter drücken...")

        # Spieler 2
        print("\nSpieler 2 platziert")
        self.model.display_grid(player=2, show_ships=True)
        self.model.place_ship(player=2)
        print("\nFertig Spieler 2:")
        self.model.display_grid(player=2, show_ships=True)

        input("\nSpiel starten. Enter drücken")


        current = 1
        while True:
            opponent = 2 if current == 1 else 1
            print(f"\nSpieler {current} ist am Zug")
            # Zeige das gegnerische Feld ohne Schiffe
            print("Gegnerisches Feld:")
            self.model.display_grid(player=opponent, show_ships=False)

            coord = self.view.get_coord(f"[Spieler {current}] Ziel eingeben ")
            result = self.model.take_shot(current, coord)

            if result == "invalid":
                print("Ungültige Eingabe. Versuch es nochmal.")
                continue
            if result == "already":
                print("Dieses Feld wurde bereits beschossen. Versuch ein anderes.")
                continue
            if result == "miss":
                print("Wasser. Kein Treffer.")
            elif result == "hit":
                print("Treffer!")
            elif result.startswith("sunk:"):
                name = result.split(":",1)[1]
                print(f"Treffer! Du hast das Schiff {name} versenkt.")
            elif result.startswith("win:"):
                name = result.split(":",1)[1]
                print(f"Treffer! Du hast das letzte Schiff ({name}) versenkt.")
                print(f"Spieler {current} gewinnt! Herzlichen Glückwunsch.")
                # Zeige Endstände
                print("\nEndstände:")
                print("Spieler 1 Board:")
                self.model.display_grid(player=1, show_ships=True)
                print()
                print("Spieler 2 Board:")
                self.model.display_grid(player=2, show_ships=True)
                break
            if result == "miss":
                current = opponent

