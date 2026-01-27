
from datetime import date

class Person:
    def __init__(self, name, bd):
        self.name = name
        self.bd = bd


class BirthdayModel:
    def __init__(self):
        self.personen = [
            Person("paul", "13.01"),
            Person("lukas", "23.05"),
            Person("markus", "13.09"),
            Person("robert", "28.04")
        ]

    def add_person(self, name, bd):
        self.personen.append(Person(name, bd))

    def find_person(self, name):
        name = name.lower()
        return [p for p in self.personen if p.name.lower() == name]

    def todays_birthdays(self):
        today = date.today().strftime("%d.%m")
        return [p for p in self.personen if p.bd == today]
