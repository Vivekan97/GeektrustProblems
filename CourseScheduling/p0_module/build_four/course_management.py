from typing import List
from course import Course
import helpers
from scheduler import CourseScheduler
from course_management_model import CourseManagementBase


class CourseManagement(CourseManagementBase):

    def __init__(self, user_inputs: List[List[str]]):
        self.scheduler = CourseScheduler()
        self.user_inputs = user_inputs

    def course_management(self):

        for user_input in self.user_inputs:
            print(self.function_decider(user_input[0])(user_input))
            # if user_input[0] == helpers.COURSE_OFFERING_MODE:
            #     print(self.course_offering(user_input))
            # if user_input[0] == helpers.COURSE_REGISTERING_MODE:
            #     print(self.course_registering(user_input))
            # if user_input[0] == helpers.COURSE_ALLOTTING_MODE:
            #     self.course_allotting(user_input)
            # if user_input[0] == helpers.COURSE_CANCELLING_MODE:
            #     print(self.course_cancelling(user_input))

    def function_decider(self, input_value: str):
        input_actions = {
            helpers.COURSE_OFFERING_MODE: getattr(self, "course_offering"),
            helpers.COURSE_REGISTERING_MODE: getattr(self, "course_registering"),
            helpers.COURSE_ALLOTTING_MODE: getattr(self, "course_allotting"),
            helpers.COURSE_CANCELLING_MODE: getattr(self, "course_cancelling")
        }
        return input_actions.get(input_value, None)

    def course_offering(self, offering_inputs: List[str]):
        if len(offering_inputs) != helpers.OFFERING_INPUT_COUNT:
            return helpers.INPUT_ERROR_MESSAGE
        if len(offering_inputs) == helpers.OFFERING_INPUT_COUNT:
            course = Course(offering_inputs[1], offering_inputs[2], offering_inputs[3],
                            int(offering_inputs[4]), int(offering_inputs[5]))
            return self.scheduler.add_course(course)

    def course_registering(self, registering_inputs: List[str]):
        if len(registering_inputs) != helpers.REGISTERING_INPUT_COUNT:
            return helpers.INPUT_ERROR_MESSAGE
        if len(registering_inputs) == helpers.REGISTERING_INPUT_COUNT:
            return self.scheduler.register_course(registering_inputs[1], registering_inputs[2])

    def course_allotting(self, allotting_inputs: List[str]):
        # added new result variable
        result = ""
        if len(allotting_inputs) != helpers.ALLOTTING_INPUT_COUNT:
            print(helpers.INPUT_ERROR_MESSAGE)
        if len(allotting_inputs) == helpers.ALLOTTING_INPUT_COUNT:
            for message in self.scheduler.course_allotment(allotting_inputs[1]):
                result += message + "\n"
                # print(message)
        return result.rstrip()

    def course_cancelling(self, cancelling_inputs: List[str]):
        if len(cancelling_inputs) != helpers.CANCELLING_INPUT_COUNT:
            return helpers.INPUT_ERROR_MESSAGE
        if len(cancelling_inputs) == helpers.CANCELLING_INPUT_COUNT:
            return self.scheduler.cancel_registration(cancelling_inputs[1])
