import unittest
from datetime import datetime
from reminder import Person
from reminder import BirthdayBook
class ReminderTest(unittest.TestCase):
    def setUp(self):
        person1 = Person("Саня", datetime(2001, 9, 9))
        self.birthdayBook = BirthdayBook()
        self.birthdayBook.addPerson(person1)

    def testDay(self):
        self.assertEqual(self.birthdayBook.printBirthDateByName("Саня"), ['Саня', 9, 9, 2001])
    def testDay1(self):
        self.assertEqual(self.birthdayBook.printBirthDateByName("ААААА"), None)
    def testDay2(self):
        self.assertEqual(self.birthdayBook.printBirthDateByName("Саняяяя"), None)


if __name__ == '__main__':
    unittest.main()
