from abc import ABC, abstractmethod


class RideSharingBase(ABC):

    @abstractmethod
    def add_driver(self):
        pass

    @abstractmethod
    def add_rider(self):
        pass

    @abstractmethod
    def match(self):
        pass

    @abstractmethod
    def start_ride(self):
        pass

    @abstractmethod
    def stop_ride(self):
        pass

    @abstractmethod
    def bill(self):
        pass
