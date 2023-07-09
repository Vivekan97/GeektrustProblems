from typing import List
# from models import Course, helpers, CourseScheduler
from course import Course
import helpers
from scheduler import CourseScheduler


def course_management(user_inputs: List[List[str]]):
    scheduler = CourseScheduler()

    for user_input in user_inputs:
        if user_input[0] == helpers.COURSE_OFFERING_MODE:
            if len(user_input) != helpers.OFFERING_INPUT_COUNT:
                print(helpers.INPUT_ERROR_MESSAGE)
            else:
                course = Course(user_input[1], user_input[2], user_input[3], int(user_input[4]), int(user_input[5]))
                print(scheduler.add_course(course))
        if user_input[0] == helpers.COURSE_REGISTERING_MODE:
            if len(user_input) != helpers.REGISTERING_INPUT_COUNT:
                print(helpers.INPUT_ERROR_MESSAGE)
            else:
                print(scheduler.register_course(user_input[1], user_input[2]))

        if user_input[0] == helpers.COURSE_ALLOTTING_MODE:
            if len(user_input) != helpers.ALLOTTING_INPUT_COUNT:
                print(helpers.INPUT_ERROR_MESSAGE)
            else:
                for message in scheduler.course_allotment(user_input[1]):
                    print(message)

        if user_input[0] == helpers.COURSE_CANCELLING_MODE:
            if len(user_input) != helpers.CANCELLING_INPUT_COUNT:
                print(helpers.INPUT_ERROR_MESSAGE)
            else:
                print(scheduler.cancel_registration(user_input[1]))
