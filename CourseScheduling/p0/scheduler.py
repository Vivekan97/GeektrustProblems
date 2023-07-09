
#  course scheduling geektrust problem

from abc import ABC, abstractmethod
from typing import Union, Dict, Set, List, Tuple
from helpers import Helpers
# from models import RegisteredUser, Course


class User:

    def __init__(self, email: str):
        self.user_email = email


class RegisteredUser(User):

    def __init__(self, email: str, course_name: str):
        super().__init__(email)
        self.course_registration_id = Helpers.course_registration_id_generator(self.user_email, course_name)
        self.is_alloted = False


class Course:

    def __init__(self, name: str, instructor: str, date: str, minimum: int, maximum: int):
        self.course_name = name
        self.course_instructor = instructor
        self.course_date = date
        self.min_members = minimum
        self.max_members = maximum
        self.course_offering_id = Helpers.course_offering_id_generator(name, instructor)
        self.current_members: Set[RegisteredUser] = set()
        self.alloted_members: Set[RegisteredUser] = set()

    def is_full(self):
        return self.max_members == len(self.current_members)

    def add_user(self, new_user: RegisteredUser):
        self.current_members.add(new_user)

    def get_course_name(self):
        return self.course_name

    def remove_user(self, user: RegisteredUser):
        if user in self.current_members:
            self.current_members.remove(user)
        if user in self.alloted_members:
            self.alloted_members.remove(user)

    def remove_user_by_registration_id(self, course_registration_id: str):
        for member in self.current_members:
            if member.course_registration_id == course_registration_id:
                self.remove_user(member)
                return f"{course_registration_id} {Helpers.cancel_accepted}"

    def cancellation_available(self):
        return len(self.alloted_members) > 0

    def allot_members(self):
        alloted_result: List[Tuple[str, str]] = []
        for member in self.current_members:
            member.is_alloted = True
            self.alloted_members.add(member)
            message = Helpers.allotment_confirmed
            if len(self.current_members) < self.min_members:
                message = Helpers.course_cancelled
            temp = (member.course_registration_id,
                    f" {member.user_email} {self.course_offering_id} {self.course_name} "
                    f"{self.course_instructor} {self.course_date} {message}")
            alloted_result.append(temp)
            # result = f"{member.course_registration_id} {member.user_email} {self.course_offering_id}" \
            #          f" {self.course_name} {self.course_instructor} {self.course_date} {Helpers.allotment_confirmed}"


            # print(result)
        temp = [res[0]+res[1] for res in sorted(alloted_result, key=lambda a: a[0])]
        return temp


class Scheduler(ABC):

    @abstractmethod
    def add_course(self, course_title: Union[str, None] = None, course_instructor: Union[str, None] = None,
                   course_date: Union[str, None] = None,
                   min_emp: Union[int, None] = None, max_emp: Union[int, None] = None):
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


class CourseScheduler(Scheduler):

    def __init__(self):
        self.available_courses: Dict[str, Course] = {}

    def add_course(self, course_title: Union[str, None] = None, course_instructor: Union[str, None] = None,
                   course_date: Union[str, None] = None,
                   min_emp: Union[int, None] = None, max_emp: Union[int, None] = None):

        if not all([course_title, course_instructor, course_date, min_emp, max_emp]):
            return Helpers.input_error
        course_unique_id = Helpers.course_offering_id_generator(course_title, course_instructor)
        self.available_courses[course_unique_id] = Course(course_title, course_instructor, course_date,
                                                          min_emp, max_emp)
        return course_unique_id

    def register_course(self, user_email: Union[str, None] = None, course_name: Union[str, None] = None):

        if not all([user_email, course_name]):
            return Helpers.input_error
        course = self.available_courses.get(course_name, None)
        if course is None:
            return None
        if course.is_full():
            return Helpers.full_error
        new_user = RegisteredUser(user_email, course.get_course_name())
        course.add_user(new_user)
        return Helpers.register_message(user_email, course.get_course_name())

    def course_allotment(self, course_unique_id: Union[str, None]):
        if not course_unique_id:
            return Helpers.input_error
        course = self.available_courses.get(course_unique_id, None)
        if course is None:
            return None
        return course.allot_members()

    def cancel_registration(self, course_registration_id: Union[str, None]):
        if not course_registration_id:
            return None
        for course in self.available_courses.values():
            for alloted_member in course.alloted_members:
                if course_registration_id == alloted_member.course_registration_id:
                    return f"{course_registration_id} {Helpers.cancel_rejected}"
            for current_member in course.current_members:
                if course_registration_id == current_member.course_registration_id:
                    return course.remove_user_by_registration_id(course_registration_id)


if __name__ == "__main__":
    s = CourseScheduler()
    print(s.add_course("JAVA", "JAMES", "15062022", 1, 2))
