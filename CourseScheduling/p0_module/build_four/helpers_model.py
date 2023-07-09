from abc import ABC, abstractmethod


class HelpersBase(ABC):

    @abstractmethod
    def course_offering_id_generator(self, course_title: str, course_instructor: str):
        pass

    @abstractmethod
    def register_message(self, user_email: str, course_name: str):
        pass

    @abstractmethod
    def course_registration_id_generator(self, user_email: str, course_name: str):
        pass
