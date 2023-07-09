INPUT_FILE_MODE = "r"
COURSE_OFFERING_MODE = "ADD-COURSE-OFFERING"
COURSE_REGISTERING_MODE = "REGISTER"
COURSE_ALLOTING_MODE = "ALLOT"
COURSE_CANCELLING_MODE = "CANCEL"
INPUT_ERROR_MESSAGE = "INPUT_DATA_ERROR"
CANCELLING_INPUT_COUNT = 2
ALLOTING_INPUT_COUNT = 2
OFFERING_INPUT_COUNT = 6
REGISTERING_INPUT_COUNT = 3


class Helpers:

    input_error: str = "INPUT_DATA_ERROR"
    full_error: str = "COURSE_FULL_ERROR"
    cancel_accepted: str = "CANCEL_ACCEPTED"
    cancel_rejected: str = "CANCEL_REJECTED"
    course_cancelled: str = "COURSE_CANCELED"
    course_accepted: str = "ACCEPTED"
    offering: str = "OFFERING-"
    register_course: str = "REG-COURSE-"
    allotment_confirmed: str = "CONFIRMED"

    @classmethod
    def course_offering_id_generator(cls, course_title: str, course_instructor: str):
        return f"{cls.offering}{course_title}-{course_instructor}"

    @classmethod
    def register_message(cls, user_email: str, course_name: str):
        user_name = user_email.split("@")[0]
        # print(f"Inputs are -> {user_email} {course_name} Register Message -> {cls.register_course}{user_name}-{course_name} {cls.course_accepted}")
        return f"{cls.register_course}{user_name}-{course_name} {cls.course_accepted}"

    @classmethod
    def course_registration_id_generator(cls, user_email: str, course_name: str):
        user_name = user_email.split("@")[0]
        # print(f"Inputs are -> {user_email} {course_name} Course Registn ID Gen -> {cls.register_course}{user_name}-{course_name}")
        return f"{cls.register_course}{user_name}-{course_name}"
