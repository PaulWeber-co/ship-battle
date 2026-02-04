from controller import Controller
from view import View
from model import Model

if __name__ == "__main__":
    model = Model()
    view = View()
    controller = Controller(model, view)
    controller.test()
    board = model.Board()
    ship = model.ships[0]
    positions = [(0, i) for i in range(ship.length)]
    board.place_ship(ship, positions)
    console_view = View.ConsoleView()
    console_view.show_board(board)

