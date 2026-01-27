from controller import RPSController
from view import RPSView
from modelrps import RPSModel

if __name__ == "__main__":
    model = RPSModel()
    view = RPSView()
    controller = RPSController(model, view)
    controller.run()
