
from model import BirthdayModel
from view import BirthdayView

class BirthdayController:
    def __init__(self):
        self.model = BirthdayModel()
        self.view = BirthdayView()

    def run(self):
        # Zeige Geburtstage von heute
        todays = self.model.todays_birthdays()
        self.view.show_today(todays)

        # Menü
        choice = self.view.show_menu()

        if choice == "1":
            name = self.view.ask_for_name()
            bd = self.view.ask_for_birthday()
            self.model.add_person(name, bd)
            self.view.show_all(self.model.personen)

        elif choice == "2":
            self.view.show_all(self.model.personen)

        elif choice == "3":
            name = self.view.ask_for_name()
            results = self.model.find_person(name)
            self.view.show_search_result(results)

        else:
            print("Ungültige Eingabe: Bitte nur 1, 2 oder 3")
