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

    def _getPersonsBirthdayWithinTheWeek(self, month, day):
        marches = [];
        currentDatetime = datetime.now()
        userDateWeekday = datetime(currentDatetime.year, month, day).weekday()
        firstWeekdayTimestamp = datetime(currentDatetime.year, month, day).timestamp()
        lastWeekdayTimestamp = (datetime(currentDatetime.year, month, day) + timedelta(6 - userDateWeekday)).timestamp()
        for p in self.personList.values():
            pBirthDate = p.getBirthDate()
            if pBirthDate.month == month:
                pBirthDate = datetime(currentDatetime.year, pBirthDate.month, pBirthDate.day)
                ptimestamp = pBirthDate.timestamp()
                if ptimestamp >= firstWeekdayTimestamp and ptimestamp <= lastWeekdayTimestamp:
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

    def printBirthdayWithinTheWeek(self, month, day):
        marches = self._getPersonsBirthdayWithinTheWeek(month, day)
        if marches != []:
            print("В течении недели родились: ", month, day)
            for p in marches:
                print(p.getName())
            return [p.getName() for p in marches]
        else:
            print("Никто не родился в течении недели")
            return None


if __name__ == '__main__':
    person1 = Person("Саня", datetime(2001,9,9))
    birthdayBook=BirthdayBook()
    birthdayBook.addPerson(person1)
    birthdayBook.printBirthdayByMonth(9)
    print(birthdayBook.printBirthDateByName("Саня"))
    birthdayBook.printBirthdayWithinTheWeek(9, 8)
