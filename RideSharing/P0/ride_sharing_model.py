from abc import ABC, abstractmethod


class RideSharingBase(ABC):

    @abstractmethod
    def add_driver(self, driver_id: str, x_coordinate: int, y_coordinate: int):
        pass

    @abstractmethod
    def add_rider(self, rider_id: str, x_coordinate: int, y_coordinate: int):
        pass

    @abstractmethod
    def match(self, rider_id: str):
        pass

    @abstractmethod
    def start_ride(self, ride_id: str, nth_driver: int, rider_id: str):
        pass

    @abstractmethod
    def stop_ride(self, ride_id: str, destination_x: int, destination_y: int, time_taken_in_min: int):
        pass

    @abstractmethod
    def bill(self, ride_id: str):
        pass
