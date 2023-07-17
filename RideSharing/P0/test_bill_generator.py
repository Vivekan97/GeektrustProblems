import unittest
from driver import Driver, Rider
from ride import Ride
from bill_generator import BillGenerator


class BillGeneratorCaseOne(unittest.TestCase):

    rider = Rider("R1", 3, 5)
    ride = Ride("RIDE-101", rider, False, 10, 2, 48)
    driver = Driver("D2", 2, 3)
    bill = BillGenerator(ride, driver)

    def test_1_ride_generation(self):
        self.assertIsInstance(self.ride, Ride)

    def test_2_driver_generation(self):
        self.assertIsInstance(self.driver, Driver)

    def test_3_generate_bill(self):
        self.assertEqual(self.bill.generate_bill(), '234.64')


class BillGeneratorCaseTwo(unittest.TestCase):

    rider = Rider("R2", 1, 1)
    ride = Ride("RIDE-102", rider, False, 7, 9, 50)
    driver = Driver("D1", 0, 1)
    bill = BillGenerator(ride, driver)

    def test_1_ride_generation(self):
        self.assertIsInstance(self.ride, Ride)

    def test_2_driver_generation(self):
        self.assertIsInstance(self.driver, Driver)

    def test_3_generate_bill(self):
        self.assertEqual(self.bill.generate_bill(), '258.00')


if __name__ == '__main__':
    unittest.main()
