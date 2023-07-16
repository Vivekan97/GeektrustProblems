from ride import Ride
from driver import Driver
from distance_calculator import DistanceCalculator


class BillGenerator:

    base_fare: float = 50.0
    charge_per_kilometer: float = 6.5
    charge_per_minute: float = 2.0
    service_tax: float = 1.2

    def __init__(self, ride: Ride, driver: Driver):
        self.ride_for_billing: Ride = ride
        self.assigned_driver: Driver = driver

    def generate_bill(self):
        # starting_point = self.assigned_driver.
        pass
