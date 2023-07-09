from user import RegisteredUser
from abc import ABC, abstractmethod


class CourseBase(ABC):

    @abstractmethod
    def is_full(self):
        pass

    @abstractmethod
    def add_user(self, new_user: RegisteredUser):
        pass

    @abstractmethod
    def get_course_name(self):
        pass

    @abstractmethod
    def remove_user(self, user: RegisteredUser):
        pass

    @abstractmethod
    def remove_user_by_registration_id(self, course_registration_id: str):
        pass

    @abstractmethod
    def cancellation_available(self):
        pass

    @abstractmethod
    def allot_members(self):
        pass
