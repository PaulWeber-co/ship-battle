
class BirthdayView:
    def show_menu(self):
        print("Wähle:")
        print("1 → Neuen Geburtstag hinzufügen")
        print("2 → Alle Geburtstage anzeigen")
        print("3 → Nach Namen suchen")
        return input()

    def show_all(self, personen):
        print("\nGeburtstagsliste:")
        for p in personen:
            print(p.name, "->", p.bd)

    def ask_for_name(self):
        return input("Name eingeben: ")

    def ask_for_birthday(self):
        return input("Geburtstag eingeben (z.B. 13.01): ")

    def show_search_result(self, results):
        if not results:
            print("Name nicht gefunden")
        else:
            for p in results:
                print("Gefunden:", p.name, "hat am", p.bd, "Geburtstag")

    def show_today(self, personen):
        if not personen:
            print("Heute hat keiner Geburtstag")
        else:
            print("Heute hat jemand Geburtstag!")
            for p in personen:
                print("🎉", p.name, "hat heute Geburtstag!")
