import unittest
# from models import Course, CourseScheduler, Helpers
from helpers import Helpers
from course import Course
from scheduler import CourseScheduler


class SchedulerTestCase(unittest.TestCase):

    scheduler = CourseScheduler()
    helper = Helpers()
    java_course = Course("JAVA", "JAMES", "15062022", 1, 2)
    kubernetes_course = Course("KUBERNETES", "WOODY", "16062022", 2, 5)

    def test_a_add_course(self):
        self.assertEqual(self.scheduler.add_course(), self.helper.input_error)
        self.assertEqual(self.scheduler.add_course(self.java_course), "OFFERING-JAVA-JAMES")
        self.assertEqual(self.scheduler.add_course(self.kubernetes_course),
                         "OFFERING-KUBERNETES-WOODY")

    def test_b_register(self):
        self.assertEqual(self.scheduler.register_course("ANDY@GMAIL.COM", "OFFERING-JAVA-JAMES"),
                         "REG-COURSE-ANDY-JAVA ACCEPTED")
        self.assertEqual(self.scheduler.register_course("WOO@GMAIL.COM", "OFFERING-JAVA-JAMES"),
                         "REG-COURSE-WOO-JAVA ACCEPTED")
        self.assertEqual(self.scheduler.register_course("ALICE@GMAIL.COM", "OFFERING-JAVA-JAMES"),
                         "COURSE_FULL_ERROR")
        self.assertEqual(self.scheduler.register_course("JON"), "INPUT_DATA_ERROR")

    def test_c_allot(self):

        self.assertEqual(True, True)
        self.assertEqual(self.scheduler.course_allotment("OFFERING-JAVA-JAMES"),
                         [
              "REG-COURSE-ANDY-JAVA ANDY@GMAIL.COM OFFERING-JAVA-JAMES JAVA JAMES 15062022 CONFIRMED",
              "REG-COURSE-WOO-JAVA WOO@GMAIL.COM OFFERING-JAVA-JAMES JAVA JAMES 15062022 CONFIRMED"
                         ])

    def test_d_cancel(self):
        self.assertEqual(self.scheduler.cancel_registration("REG-COURSE-ANDY-JAVA"),
                         "REG-COURSE-ANDY-JAVA CANCEL_REJECTED")


class TestScenarioOne(unittest.TestCase):

    scheduler_one = CourseScheduler()

    def test_scenario_one(self):
        course = Course("DATASCIENCE", "BOB", "05062022", 1, 3)
        self.assertEqual(self.scheduler_one.add_course(course),
                         "OFFERING-DATASCIENCE-BOB")
        self.assertEqual(self.scheduler_one.register_course("WOO@GMAIL.COM", "OFFERING-DATASCIENCE-BOB"),
                         "REG-COURSE-WOO-DATASCIENCE ACCEPTED")
        self.assertEqual(self.scheduler_one.register_course("ANDY@GMAIL.COM", "OFFERING-DATASCIENCE-BOB"),
                         "REG-COURSE-ANDY-DATASCIENCE ACCEPTED")
        self.assertEqual(self.scheduler_one.course_allotment("OFFERING-DATASCIENCE-BOB"),
                         [
             "REG-COURSE-ANDY-DATASCIENCE ANDY@GMAIL.COM OFFERING-DATASCIENCE-BOB DATASCIENCE BOB 05062022 CONFIRMED",
             "REG-COURSE-WOO-DATASCIENCE WOO@GMAIL.COM OFFERING-DATASCIENCE-BOB DATASCIENCE BOB 05062022 CONFIRMED"
                         ])


class TestScenarioTwo(unittest.TestCase):

    scheduler_two = CourseScheduler()

    def test_scenario_two(self):
        course = Course("PYTHON", "JOHN", "05062022", 1, 3)
        self.assertEqual(self.scheduler_two.add_course(course), "OFFERING-PYTHON-JOHN")
        self.assertEqual(self.scheduler_two.register_course("WOO@GMAIL.COM", "OFFERING-PYTHON-JOHN"),
                         "REG-COURSE-WOO-PYTHON ACCEPTED")
        self.assertEqual(self.scheduler_two.register_course("ANDY@GMAIL.COM", "OFFERING-PYTHON-JOHN"),
                         "REG-COURSE-ANDY-PYTHON ACCEPTED")
        self.assertEqual(self.scheduler_two.register_course("BOBY@GMAIL.COM", "OFFERING-PYTHON-JOHN"),
                         "REG-COURSE-BOBY-PYTHON ACCEPTED")
        self.assertEqual(self.scheduler_two.cancel_registration("REG-COURSE-BOBY-PYTHON"),
                         "REG-COURSE-BOBY-PYTHON CANCEL_ACCEPTED")
        self.assertEqual(self.scheduler_two.course_allotment("OFFERING-PYTHON-JOHN"),
                         [
            "REG-COURSE-ANDY-PYTHON ANDY@GMAIL.COM OFFERING-PYTHON-JOHN PYTHON JOHN 05062022 CONFIRMED",
            "REG-COURSE-WOO-PYTHON WOO@GMAIL.COM OFFERING-PYTHON-JOHN PYTHON JOHN 05062022 CONFIRMED"
                         ])


if __name__ == '__main__':
    unittest.main()
