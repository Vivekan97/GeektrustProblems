from ride_sharing_model import RideSharingBase
from typing import Dict, Tuple
from location import Location
from driver import Driver, Rider
import helpers
from distance_calculator import DistanceCalculator


class RideSharing(RideSharingBase):

    def __init__(self):
        self.driver_and_location: Dict[int, Tuple[Driver, Location]] = {}
        self.rider_and_location: Dict[int, Tuple[Rider, Location]] = {}

    def add_driver(self, driver_id: str, x_coordinate: int, y_coordinate: int):
        new_location = Location(x_coordinate, y_coordinate)
        new_driver = Driver(driver_id)
        self.driver_and_location[new_driver.get_id()] = (new_driver, new_location)

    def add_rider(self, rider_id: str, x_coordinate: int, y_coordinate: int):
        new_rider = Rider(rider_id)
        new_location = Location(x_coordinate, y_coordinate)
        self.rider_and_location[new_rider.get_id()] = (new_rider, new_location)

    def match(self, rider_id: str):
        new_rider = Rider(rider_id)
        current_rider = self.rider_and_location.get(new_rider.get_id(), None)
        if not current_rider:
            return None
        rider_location = current_rider[1]
        if len(set(self.driver_and_location.keys())) == 0:
            return helpers.DRIVER_NOT_AVAILABLE

        available_drivers_and_location = []
        for count, driver, location in enumerate(self.driver_and_location.values()):
            # stop looping if number of drivers more than 5
            if count==5:
                break
            temp = DistanceCalculator(rider_location, location)
            if temp.euclidean_distance() <= 5:
                available_drivers_and_location.append((driver, temp.euclidean_distance()))
        # sort by lexicographical orders
        sorted_drivers_and_location = sorted(available_drivers_and_location, key=lambda a: (a[1], a[0]))
        only_drivers = [a[0].get_user_id() for a in sorted_drivers_and_location]
        return "DRIVERS_MATCHED "+" ".join(only_drivers)

    def start_ride(self, ride_id: str, nth_driver: int, rider_id: str):
        pass
