from controller import RPSController
from view import RPSView
from model import RPSModel

if __name__ == "__main__":
    model = Model()
    view = View()
    controller = Controller(model, view)
    controller.run()
