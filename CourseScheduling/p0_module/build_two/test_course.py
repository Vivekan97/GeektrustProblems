import unittest
from course import Course


class CourseTestCase(unittest.TestCase):
    course_name = "PYTHON"
    instructor_name = "JOHN"
    course_date = "05062022"
    minimum_members = 1
    maximum_members = 3
    course = Course(course_name, instructor_name, course_date, minimum_members, maximum_members)

    def test_a_course_creation(self):
        self.assertIsInstance(self.course, Course)

    def test_b_course_name(self):
        self.assertEqual(self.course.get_course_name(), self.course_name)

    def test_c_course_status(self):
        self.assertFalse(self.course.is_full())

    def test_d_cancellation(self):
        self.assertFalse(self.course.cancellation_available())

    def test_e_allott(self):
        self.assertListEqual(self.course.allot_members(), [])


if __name__ == '__main__':
    unittest.main()
