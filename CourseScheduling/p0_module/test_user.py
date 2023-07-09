import unittest
from user import RegisteredUser


class UserTestCase(unittest.TestCase):

    email = "WOO@GMAIL.COM"
    course_name = "OFFERING-PYTHON-JOHN"
    user = RegisteredUser(email, course_name)

    def test_a_user_instance(self):
        self.assertIsInstance(self.user, RegisteredUser)

    def test_b_user_email(self):
        self.assertEqual(self.user.get_user_email(),self.email)

    def test_c_user_allotted_status(self):
        self.assertEqual(self.user.is_user_allotted(), False)

    def test_d_registration_id(self):
        self.assertIsInstance(self.user.get_course_registration_id(), str)


if __name__ == '__main__':
    unittest.main()
