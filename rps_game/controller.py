
from rps_game.modelrps import Result  # wichtig: gleiches Enum wie im Model!

class RPSController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
        self.view.show_menu()
        n = self.view.get_input()

        if n not in [1, 2, 3]:
            self.view.invalid_input()
            return

        x = self.model.computer_choice()
        value = self.model.evaluate(n, x)

        try:
            result = Result(value)
        except ValueError:
            self.view.invalid_input()
            return

        self.view.show_output(result.name)
        print("Wins:", self.model.wcount)
        print("Looses:", self.model.lcount)