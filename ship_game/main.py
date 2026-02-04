from controller import Controller
from view import View
from model import Model

if __name__ == "__main__":
    model = Model()
    view = View()
    controller = Controller(model, view)

    # Schiffe anzeigen
    view.show_instruction_ships(model.ships)

    # Grid anzeigen und Schiff platzieren
    model.display_grid()
    model.place_ship()
    model.display_grid()
    model.place_ship()
    model.display_grid()