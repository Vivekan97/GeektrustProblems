from ride_sharing_model import RideSharingBase
from typing import Dict, Tuple, Set
from location import Location
from driver import Driver, Rider, IdGenerator
import helpers
from distance_calculator import DistanceCalculator
from ride import Ride
from bill_generator import BillGenerator


class RideSharing(RideSharingBase):

    def __init__(self):
        self.driver_and_location: Dict[int, Tuple[Driver, Location]] = {}
        self.rider_and_location: Dict[int, Tuple[Rider, Location]] = {}
        self.rides: Dict[str, Tuple[Ride, Driver]] = {}
        self.started_rides: Set[str] = set()

    def add_driver(self, driver_id: str, x_coordinate: int, y_coordinate: int):
        new_location = Location(x_coordinate, y_coordinate)
        new_driver = Driver(driver_id, x_coordinate, y_coordinate)
        self.driver_and_location[new_driver.get_id()] = (new_driver, new_location)

    def add_rider(self, rider_id: str, x_coordinate: int, y_coordinate: int):
        new_rider = Rider(rider_id, x_coordinate, y_coordinate)
        new_location = Location(x_coordinate, y_coordinate)
        self.rider_and_location[new_rider.get_id()] = (new_rider, new_location)

    def get_matching_drivers(self, rider_location: Location):
        available_drivers_and_location = []
        for count, driver_with_location in enumerate(self.driver_and_location.values(), start=1):
            # stop looping if number of drivers more than 5
            if count == 5:
                break
            driver_location = driver_with_location[1]
            driver = driver_with_location[0]
            temp = DistanceCalculator(rider_location, driver_location)
            if temp.euclidean_distance() <= 5:
                available_drivers_and_location.append((driver, temp.euclidean_distance()))
        # sort by lexicographical orders
        sorted_drivers_and_location = sorted(available_drivers_and_location,
                                             key=lambda driver_and_location: (driver_and_location[1],
                                                                              driver_and_location[0].get_user_id()))
        return [a[0].get_user_id() for a in sorted_drivers_and_location]

    def match(self, rider_id: str):
        new_rider = IdGenerator(rider_id)
        # print(self.rider_and_location.items())
        current_rider = self.rider_and_location.get(new_rider.get_secret_id(), None)
        if not current_rider:
            return None
        rider_location = current_rider[1]
        if len(set(self.driver_and_location.keys())) == 0:
            return helpers.DRIVER_NOT_AVAILABLE
        return "DRIVERS_MATCHED "+" ".join(self.get_matching_drivers(rider_location))

    def get_a_rider_location(self, rider_id: str):
        rider_id = IdGenerator(rider_id).get_secret_id()
        current_driver_and_location = self.rider_and_location.get(rider_id, None)
        if not current_driver_and_location:
            return None
        return current_driver_and_location[1]

    def assign_ride(self, ride_id: str, driver_id: str, rider_id: str):
        rider_key = IdGenerator(rider_id).get_secret_id()
        rider_and_location = self.rider_and_location.get(rider_key)
        rider = rider_and_location[0]
        new_ride = Ride(ride_id, rider)
        self.started_rides.add(ride_id)
        new_ride.set_ride_status(True)
        driver_id = IdGenerator(driver_id).get_secret_id()
        assigned_driver = self.driver_and_location.pop(driver_id)[0]
        self.rides[ride_id] = new_ride, assigned_driver
        return ride_id

    def cleanup_ride(self, ride_id: str, ride: Ride, driver: Driver, destination_x: int,
                     destination_y: int, time_taken_in_min: int):
        self.started_rides.remove(ride_id)
        ride.set_ride_status(False)
        ride.update_ride(destination_x, destination_y, time_taken_in_min)
        driver.change_driver_status(False)
        self.rides[ride_id] = ride, driver
        return ride_id

    def start_ride(self, ride_id: str, nth_driver: int, rider_id: str):
        rider_location = self.get_a_rider_location(rider_id)
        available_drivers = self.get_matching_drivers(rider_location)
        # fewer than n no of drivers
        if len(available_drivers) < nth_driver-1:
            return helpers.INVALID_RIDE
        # ride id already exists
        if ride_id in self.started_rides:
            return helpers.INVALID_RIDE
        # self.assign_ride(ride_id, available_drivers[nth_driver-1])
        # new_ride = Ride(ride_id)
        # self.started_rides.add(ride_id)
        # new_ride.set_ride_status(True)
        # driver_id = IdGenerator(available_drivers[nth_driver-1]).get_secret_id()
        # assigned_driver = self.driver_and_location.pop(driver_id)[0]
        # self.rides[ride_id] = new_ride, assigned_driver
        # return helpers.RIDE_STARTED + f" {ride_id}"
        return helpers.RIDE_STARTED + f" {self.assign_ride(ride_id, available_drivers[nth_driver-1], rider_id)}"

    def stop_ride(self, ride_id: str, destination_x: int, destination_y: int, time_taken_in_min: int):
        if time_taken_in_min < 0:
            return helpers.INVALID_RIDE
        if ride_id in self.started_rides:
            # fetching current ride
            current_ride_and_driver = self.rides.get(ride_id, None)
            # if ride not exist
            if not current_ride_and_driver:
                return helpers.INVALID_RIDE
            # checking if ride is already stopped
            current_ride = current_ride_and_driver[0]
            current_driver = current_ride_and_driver[1]
            if not current_ride.get_ride_status():
                return helpers.INVALID_RIDE
            # self.started_rides.remove(ride_id)
            # current_ride.set_ride_status(False)
            # current_ride.update_ride(destination_x, destination_y, time_taken_in_min)
            # current_driver.change_driver_status(False)
            # self.rides[ride_id] = current_ride, current_driver
            # return helpers.RIDE_STOPPED + f" {ride_id}"
            return helpers.RIDE_STOPPED + f" {self.cleanup_ride(ride_id, current_ride, current_driver, destination_x, destination_y, time_taken_in_min)}"
        return helpers.INVALID_RIDE

    def bill(self, ride_id: str):
        if ride_id not in self.started_rides:
            if ride_id not in self.rides:
                return helpers.INVALID_RIDE
            current_ride_and_driver = self.rides.pop(ride_id)
            current_ride = current_ride_and_driver[0]
            current_driver = current_ride_and_driver[1]
            # current_rider =
            # if ride is active then bill should not be generated
            if current_ride.get_ride_status():
                return helpers.RIDE_NOT_COMPLETED
            new_bill = BillGenerator(current_ride, current_driver)
            return f"BILL {ride_id} {current_driver.get_user_id()} {new_bill.generate_bill()}"
        return helpers.INVALID_RIDE
