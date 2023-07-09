from abc import ABC, abstractmethod
from typing import Union
from course import Course


class Scheduler(ABC):

    @abstractmethod
    def add_course(self, course: Union[Course, None]):
        pass

    @abstractmethod
    def register_course(self, user_email: Union[str, None] = None, course_name: Union[str, None] = None):
        pass

    @abstractmethod
    def cancel_registration(self, course_registration_id: Union[str, None]):
        pass

    @abstractmethod
    def course_allotment(self, course_unique_id: Union[str, None]):
        pass
