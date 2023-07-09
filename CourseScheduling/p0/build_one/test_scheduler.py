import unittest
from scheduler import CourseScheduler
from helpers import Helpers


class SchedulerTestCase(unittest.TestCase):

    scheduler = CourseScheduler()

    def test_a_add_course(self):
        self.assertEqual(self.scheduler.add_course(), Helpers.input_error)
        self.assertEqual(self.scheduler.add_course("JAVA", "JAMES", "15062022", 1, 2), "OFFERING-JAVA-JAMES")
        self.assertEqual(self.scheduler.add_course("KUBERNETES", "WOODY", "16062022", 2, 5), "OFFERING-KUBERNETES-WOODY")

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
             ["REG-COURSE-ANDY-JAVA ANDY@GMAIL.COM OFFERING-JAVA-JAMES JAVA JAMES 15062022 CONFIRMED",
              "REG-COURSE-WOO-JAVA WOO@GMAIL.COM OFFERING-JAVA-JAMES JAVA JAMES 15062022 CONFIRMED"])

    def test_d_cancel(self):
        self.assertEqual(self.scheduler.cancel_registration("REG-COURSE-ANDY-JAVA"),
                         "REG-COURSE-ANDY-JAVA CANCEL_REJECTED")


class TestScenarioOne(unittest.TestCase):

    scheduler_one = CourseScheduler()

    def test_scenario_one(self):
        self.assertEqual(self.scheduler_one.add_course("DATASCIENCE", "BOB", "05062022", 1, 3),
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
        self.assertEqual(self.scheduler_two.add_course("PYTHON", "JOHN", "05062022", 1, 3), "OFFERING-PYTHON-JOHN")
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
