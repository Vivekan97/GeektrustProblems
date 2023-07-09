import unittest
from helpers import Helpers


class HelpersTestCase(unittest.TestCase):

    helper = Helpers()

    def test_course_id_generator(self):
        self.assertEqual(self.helper.course_offering_id_generator("JAVA", "JAMES"), "OFFERING-JAVA-JAMES")
        self.assertEqual(self.helper.course_offering_id_generator("KUBERNETES", "WOODY"), "OFFERING-KUBERNETES-WOODY")

    def test_register_message(self):
        self.assertEqual(self.helper.register_message("ANDY@GMAIL.COM", "JAVA"),
                         "REG-COURSE-ANDY-JAVA ACCEPTED")

    def test_course_registration_id_generator(self):
        self.assertEqual(self.helper.course_registration_id_generator("ANDY@GMAIL.COM", "JAVA"),
                         "REG-COURSE-ANDY-JAVA")
        self.assertEqual(self.helper.course_registration_id_generator("WOO@GMAIL.COM", "JAVA"),
                         "REG-COURSE-WOO-JAVA")


if __name__ == '__main__':
    unittest.main()
