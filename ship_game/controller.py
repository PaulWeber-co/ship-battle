from model import Model
class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
        self.view.show_menu_single()
        n = self.view.get_input()
        print(n)

    def test(self):
        self.view.show_instruction()