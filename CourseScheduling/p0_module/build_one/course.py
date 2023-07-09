from typing import Set, List, Tuple
# from models import Helpers, RegisteredUser, CourseBase
from helpers import Helpers
from course_models import CourseBase
from user import RegisteredUser


class Course(CourseBase):

    def __init__(self, name: str, instructor: str, date: str, minimum: int, maximum: int):
        self.course_name = name
        self.course_instructor = instructor
        self.course_date = date
        self.min_members = minimum
        self.max_members = maximum
        self.helper = Helpers()
        self.__course_offering_id = self.helper.course_offering_id_generator(name, instructor)
        self.current_members: Set[RegisteredUser] = set()
        self.allotted_members: Set[RegisteredUser] = set()

    def get_course_offering_id(self):
        return self.__course_offering_id

    def is_full(self):
        return self.max_members == len(self.current_members)

    def add_user(self, new_user: RegisteredUser):
        self.current_members.add(new_user)

    def get_course_name(self):
        return self.course_name

    def remove_user(self, user: RegisteredUser):
        if user in self.current_members:
            self.current_members.remove(user)
        if user in self.allotted_members:
            self.allotted_members.remove(user)

    def remove_user_by_registration_id(self, course_registration_id: str):
        for member in self.current_members:
            if member.get_course_registration_id() == course_registration_id:
                self.remove_user(member)
                return f"{course_registration_id} {self.helper.cancel_accepted}"

    def cancellation_available(self):
        return len(self.allotted_members) > 0

    def allot_members(self):
        allotted_result: List[Tuple[str, str]] = []
        for member in self.current_members:
            member.is_allotted = True
            self.allotted_members.add(member)
            message = self.helper.allotment_confirmed
            if len(self.current_members) < self.min_members:
                message = self.helper.course_cancelled
            temp = (member.get_course_registration_id(),
                    f" {member.get_user_email()} {self.get_course_offering_id()} {self.course_name} "
                    f"{self.course_instructor} {self.course_date} {message}")
            allotted_result.append(temp)
        return [res[0]+res[1] for res in sorted(allotted_result, key=lambda a: a[0])]
