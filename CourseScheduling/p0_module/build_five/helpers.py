from helpers_model import HelpersBase

INPUT_FILE_MODE = "r"
COURSE_OFFERING_MODE = "ADD-COURSE-OFFERING"
COURSE_REGISTERING_MODE = "REGISTER"
COURSE_ALLOTTING_MODE = "ALLOT"
COURSE_CANCELLING_MODE = "CANCEL"
INPUT_ERROR_MESSAGE = "INPUT_DATA_ERROR"
CANCELLING_INPUT_COUNT = 2
ALLOTTING_INPUT_COUNT = 2
OFFERING_INPUT_COUNT = 6
REGISTERING_INPUT_COUNT = 3


class Helpers(HelpersBase):

    def __init__(self):
        self.input_error: str = "INPUT_DATA_ERROR"
        self.full_error: str = "COURSE_FULL_ERROR"
        self.cancel_accepted: str = "CANCEL_ACCEPTED"
        self.cancel_rejected: str = "CANCEL_REJECTED"
        self.course_cancelled: str = "COURSE_CANCELED"
        self.course_accepted: str = "ACCEPTED"
        self.offering: str = "OFFERING-"
        self.register_course: str = "REG-COURSE-"
        self.allotment_confirmed: str = "CONFIRMED"

    def course_offering_id_generator(self, course_title: str, course_instructor: str):
        return f"{self.offering}{course_title}-{course_instructor}"

    def register_message(self, user_email: str, course_name: str):
        user_name = user_email.split("@")[0]
        return f"{self.register_course}{user_name}-{course_name} {self.course_accepted}"

    def course_registration_id_generator(self, user_email: str, course_name: str):
        user_name = user_email.split("@")[0]
        return f"{self.register_course}{user_name}-{course_name}"
