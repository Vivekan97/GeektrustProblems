from user_models import RegisteredUserBase
from helpers import Helpers


# class User(UserBase):
#
#     def __init__(self, email: str):
#         self.__user_email = email
#
#     def get_user_email(self):
#         return self.__user_email


class RegisteredUser(RegisteredUserBase):

    def __init__(self, email: str, course_name: str):
        self.__email = email
        self.helper = Helpers()
        self.__course_registration_id = self.helper.course_registration_id_generator(self.get_user_email(), course_name)
        self.is_allotted = False

    def is_user_allotted(self):
        return self.is_allotted

    def get_course_registration_id(self):
        return self.__course_registration_id

    def get_user_email(self):
        return self.__email
