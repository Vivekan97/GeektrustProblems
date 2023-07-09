from typing import Union, Dict
# from models import RegisteredUser, Scheduler, Course, Helpers
from user import RegisteredUser
from scheduler_models import Scheduler
from course import Course
from helpers import Helpers


class CourseScheduler(Scheduler):

    def __init__(self):
        self.available_courses: Dict[str, Course] = {}
        self.helper = Helpers()

    def add_course(self, course: Union[Course, None] = None):

        if not course:
            return self.helper.input_error
        course_unique_id = self.helper.course_offering_id_generator(course.course_name, course.course_instructor)
        self.available_courses[course_unique_id] = course
        return course_unique_id

    def register_course(self, user_email: Union[str, None] = None, course_name: Union[str, None] = None):

        if not all([user_email, course_name]):
            return self.helper.input_error
        course = self.available_courses.get(course_name, None)
        # if course is None:
        #     return None
        if course.is_full():
            return self.helper.full_error
        new_user = RegisteredUser(user_email, course.get_course_name())
        course.add_user(new_user)
        return self.helper.register_message(user_email, course.get_course_name())

    def course_allotment(self, course_unique_id: Union[str, None]):
        if not course_unique_id:
            return self.helper.input_error
        course = self.available_courses.get(course_unique_id, None)
        # if course is None:
        #     return None
        return course.allot_members()

    def cancel_registration(self, course_registration_id: Union[str, None]):
        # if not course_registration_id:
        #     return None
        for course in self.available_courses.values():
            for allotted_member in course.allotted_members:
                if course_registration_id == allotted_member.get_course_registration_id():
                    return f"{course_registration_id} {self.helper.cancel_rejected}"
            for current_member in course.current_members:
                if course_registration_id == current_member.get_course_registration_id():
                    return course.remove_user_by_registration_id(course_registration_id)
