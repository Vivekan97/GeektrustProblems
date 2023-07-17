from ride import Ride
from driver import Driver
from distance_calculator import DistanceCalculator
from location import Location


class BillGenerator:

    base_fare: float = 50.0
    charge_per_kilometer: float = 6.5
    charge_per_minute: float = 2.0
    service_tax: float = 1.2

    def __init__(self, ride: Ride, driver: Driver):
        self.ride_for_billing: Ride = ride
        self.assigned_driver: Driver = driver

    def generate_bill(self):
        driver_x, driver_y = self.ride_for_billing.rider.get_current_position()
        ride_x, ride_y = self.ride_for_billing.get_ride_current_position()
        driver_location = Location(driver_x, driver_y)
        ride_location = Location(ride_x, ride_y)
        rode_distance = DistanceCalculator(driver_location, ride_location).euclidean_distance()
        kilometer_charge = round(rode_distance, 2) * self.charge_per_kilometer
        # kilometer_charge = rode_distance * self.charge_per_kilometer
        time_charge = self.ride_for_billing.get_time_taken() * self.charge_per_minute
        raw_amount = self.base_fare + kilometer_charge + time_charge
        value = raw_amount * self.service_tax
        # if value ends with single digit adding a zero at the end
        decimal_value: str = str(value).split(".")[-1]
        if len(decimal_value) < 2:
            return str(round(value, 2))+'0'
        return str(round(value, 2))
