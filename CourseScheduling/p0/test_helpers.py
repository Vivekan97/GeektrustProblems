import unittest
from helpers import Helpers


class HelpersTestCase(unittest.TestCase):

    def test_course_id_generator(self):
        self.assertEqual(Helpers.course_offering_id_generator("JAVA", "JAMES"), "OFFERING-JAVA-JAMES")
        self.assertEqual(Helpers.course_offering_id_generator("KUBERNETES", "WOODY"), "OFFERING-KUBERNETES-WOODY")

    def test_register_message(self):
        self.assertEqual(Helpers.register_message("ANDY@GMAIL.COM", "JAVA"),
                         "REG-COURSE-ANDY-JAVA ACCEPTED")

    def test_course_registration_id_generator(self):
        self.assertEqual(Helpers.course_registration_id_generator("ANDY@GMAIL.COM", "JAVA"),
                         "REG-COURSE-ANDY-JAVA")
        self.assertEqual(Helpers.course_registration_id_generator("WOO@GMAIL.COM", "JAVA"),
                         "REG-COURSE-WOO-JAVA")


if __name__ == '__main__':
    unittest.main()
