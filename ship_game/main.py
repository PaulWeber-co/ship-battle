from controller import Controller
from model import GameModel
from view import View

if __name__ == "__main__":
    model = GameModel()
    view = View()
    controller = Controller(model, view)
    controller.run()
