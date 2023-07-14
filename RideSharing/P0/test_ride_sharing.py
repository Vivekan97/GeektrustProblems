import unittest
from ride_sharing import RideSharing


class MyTestCase(unittest.TestCase):

    ride_sharing = RideSharing()

    def test_add_driver(self):
        self.ride_sharing.add_driver("D1", 1, 1)
        self.ride_sharing.add_driver("D2", 4, 5)
        self.ride_sharing.add_driver("D3", 2, 2)

    def test_add_rider(self):
        self.ride_sharing.add_rider("R1", 0, 0)

    def test_match(self):
        # print(self.ride_sharing.match("R1"))
        self.assertEqual(self.ride_sharing.match("R1"), "DRIVERS_MATCHED D1 D3")


class SecondTastCase(unittest.TestCase):

    ride_sharing = RideSharing()

    def test_add_driver(self):
        self.ride_sharing.add_driver("D1", 0, 1)
        self.ride_sharing.add_driver("D2", 2, 3)
        self.ride_sharing.add_driver("D3", 4, 2)

    def test_add_rider(self):
        self.ride_sharing.add_rider("R1", 3, 5)
        self.ride_sharing.add_rider("R2", 1, 1)

    def test_match(self):
        self.assertEqual(self.ride_sharing.match("R1"), "DRIVERS_MATCHED D2 D3 D1")
        self.assertEqual(self.ride_sharing.match("R2"), "DRIVERS_MATCHED D1 D2 D3")


class ThirdTestCase(unittest.TestCase):

    third_rider = RideSharing()

    def test_entirely(self):
        self.third_rider.add_driver("D1", 0, 1)
        self.third_rider.add_driver("D2", 2, 3)
        self.third_rider.add_rider("R1", 3, 5)
        self.third_rider.add_driver("D3", 4, 2)
        self.third_rider.add_rider("R2", 1, 1)
        self.assertEqual(self.third_rider.match("R1"), "DRIVERS_MATCHED D2 D3 D1")
        self.assertEqual(self.third_rider.match("R2"), "DRIVERS_MATCHED D1 D2 D3")


if __name__ == '__main__':
    unittest.main()
