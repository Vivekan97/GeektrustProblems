from abc import ABC


class HelpersBase(ABC):

    @classmethod
    def course_offering_id_generator(cls, course_title: str, course_instructor: str):
        pass

    @classmethod
    def register_message(cls, user_email: str, course_name: str):
        pass

    @classmethod
    def course_registration_id_generator(cls, user_email: str, course_name: str):
        pass
