from modelrps import RPSModel

class RPSView:

    def show_menu(self):
        print("Wähle Stein (1), Schere (2) oder Papier (3)")

    def get_input(self):
        try:
            return int(input())
        except:
            return None

    def show_output(self, text):
        print(text)

    def invalid_input(self):
        print("Wrong input")

    def statistics(self, text):
        print(text)
        print(text)