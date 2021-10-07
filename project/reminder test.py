import unittest
from datetime import datetime
from reminder import Person
from reminder import BirthdayBook
class ReminderTest(unittest.TestCase):
    def setUp(self):
        person1 = Person("Саня", datetime(2001, 9, 9))
        person2 = Person("Леха", datetime(1999, 2, 6))
        person3 = Person("Серега", datetime(2001, 9, 10))
        person4 = Person("Вика", datetime(2001, 11, 28))
        person5 = Person("Еще один серега", datetime(2000, 9, 10))
        self.birthdayBook = BirthdayBook()
        self.birthdayBook.addPerson(person1)
        self.birthdayBook.addPerson(person2)
        self.birthdayBook.addPerson(person3)
        self.birthdayBook.addPerson(person4)
        self.birthdayBook.addPerson(person5)

    def testDay(self):
        self.assertEqual(self.birthdayBook.printBirthDateByName("Саня"), ['Саня', 9, 9, 2001])
    def testDay1(self):
        self.assertEqual(self.birthdayBook.printBirthDateByName("ААААА"), None)
    def testDay2(self):
        self.assertEqual(self.birthdayBook.printBirthDateByName("Саняяяя"), None)
    def testDay3(self):
        self.assertEqual(self.birthdayBook.printBirthdayByMonth(9), ['Саня', 'Серега', 'Еще один серега'])
    def testDay4(self):
        self.assertEqual(self.birthdayBook.printBirthdayByMonth(1), None)

if __name__ == '__main__':
    unittest.main()
