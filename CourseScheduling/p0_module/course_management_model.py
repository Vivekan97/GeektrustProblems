from abc import ABC, abstractmethod
from typing import List


class CourseManagementBase(ABC):

    @abstractmethod
    def course_management(self):
        pass

    @abstractmethod
    def course_offering(self, offering_inputs: List[str]):
        pass

    @abstractmethod
    def course_registering(self, registering_inputs: List[str]):
        pass

    @abstractmethod
    def course_allotting(self, allotting_inputs: List[str]):
        pass

    @abstractmethod
    def course_cancelling(self, cancelling_inputs: List[str]):
        pass
