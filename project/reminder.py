from datetime import datetime, timedelta
import time
from calendar import calendar

class Person:
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name
    def setBirthDate(self, birthdate):
        self.birthdate = birthdate

    def getBirthDate(self):
        return self.birthdate


class BirthdayBook:
    def __init__(self, personList = {}):
        self.personList = personList
    def addPerson(self, person):
        self.personList[person.getName()] = person
    def _getBirthdayByName(self, name):
        if self.personList.get(name):
            return self.personList.get(name).getBirthDate()
        return None
    def _getPersonByBirthDateMonth(self, month):
        marches = [];
        for p in self.personList.values():
            if p.getBirthDate().month == month:
                marches.append(p)
        return marches
    def printBirthDateByName(self, name):
        d = self._getBirthdayByName(name)
        if d!= None:
            print("Имя: ", name, " День рождения: ", d.day, "/", d.month, "/", d.year)
            return [name, d.day, d.month, d.year]

    def printBirthdayByMonth(self, month):
        marches = self._getPersonByBirthDateMonth(month)
        if marches != []:
            print("Родились в месяца: ", month)
            for p in marches:
                print(p.getName())
            return [p.getName() for p in marches]
        else:
            return None


if __name__ == '__main__':
    person1 = Person("Саня", datetime(2001,9,9))
    birthdayBook=BirthdayBook()
    birthdayBook.addPerson(person1)
    birthdayBook.printBirthdayByMonth(9)
    print(birthdayBook.printBirthDateByName("Саня"))

