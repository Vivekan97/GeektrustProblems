from abc import ABC, abstractmethod


# class UserBase(ABC):
#
#     @abstractmethod
#     def get_user_email(self):
#         pass


class RegisteredUserBase(ABC):

    @abstractmethod
    def is_user_allotted(self):
        pass

    @abstractmethod
    def get_course_registration_id(self):
        pass
