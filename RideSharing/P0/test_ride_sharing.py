import unittest
from ride_sharing import RideSharing


class MyTestCase(unittest.TestCase):

    ride_sharing = RideSharing()

    def test_1_add_driver(self):
        self.ride_sharing.add_driver("D1", 1, 1)
        self.ride_sharing.add_driver("D2", 4, 5)
        self.ride_sharing.add_driver("D3", 2, 2)

    def test_2_add_rider(self):
        self.ride_sharing.add_rider("R1", 0, 0)

    def test_3_match(self):
        # print(self.ride_sharing.match("R1"))
        self.assertEqual(self.ride_sharing.match("R1"), "DRIVERS_MATCHED D1 D3")

    def test_4_start_ride(self):
        self.assertEqual(self.ride_sharing.start_ride("RIDE-001", 2, "R1"), "RIDE_STARTED RIDE-001")

    def test_5_stop_ride(self):
        self.assertEqual(self.ride_sharing.stop_ride("RIDE-001", 4, 5, 32), "RIDE_STOPPED RIDE-001")

    def test_6_bill_generation(self):
        self.assertEqual(self.ride_sharing.bill("RIDE-001"), "BILL RIDE-001 D3 186.72")


class SecondTastCase(unittest.TestCase):

    ride_sharing = RideSharing()

    def test_1_add_driver(self):
        self.ride_sharing.add_driver("D1", 0, 1)
        self.ride_sharing.add_driver("D2", 2, 3)
        self.ride_sharing.add_driver("D3", 4, 2)

    def test_2_add_rider(self):
        self.ride_sharing.add_rider("R1", 3, 5)
        self.ride_sharing.add_rider("R2", 1, 1)

    def test_3_match(self):
        self.assertEqual(self.ride_sharing.match("R1"), "DRIVERS_MATCHED D2 D3 D1")
        self.assertEqual(self.ride_sharing.match("R2"), "DRIVERS_MATCHED D1 D2 D3")

    def test_4_start_ride(self):
        self.assertEqual(self.ride_sharing.start_ride("RIDE-101", 1, "R1"), "RIDE_STARTED RIDE-101")
        self.assertEqual(self.ride_sharing.start_ride("RIDE-102", 1, "R2"), "RIDE_STARTED RIDE-102")

    def test_5_stop_ride(self):
        self.assertEqual(self.ride_sharing.stop_ride("RIDE-101", 10, 2, 48), "RIDE_STOPPED RIDE-101")
        self.assertEqual(self.ride_sharing.stop_ride("RIDE-102", 7, 9, 50), "RIDE_STOPPED RIDE-102")

    def test_6_bill_generation(self):
        self.assertEqual(self.ride_sharing.bill("RIDE-101"), "BILL RIDE-101 D2 234.64")
        self.assertEqual(self.ride_sharing.bill("RIDE-102"), "BILL RIDE-102 D1 258.00")


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
        self.assertEqual(self.third_rider.start_ride("RIDE-101", 1, "R1"), "RIDE_STARTED RIDE-101")
        self.assertEqual(self.third_rider.start_ride("RIDE-102", 1, "R2"), "RIDE_STARTED RIDE-102")
        self.assertEqual(self.third_rider.stop_ride("RIDE-101", 10, 2, 48), "RIDE_STOPPED RIDE-101")
        self.assertEqual(self.third_rider.stop_ride("RIDE-102", 7, 9, 50), "RIDE_STOPPED RIDE-102")
        self.assertEqual(self.third_rider.bill("RIDE-101"), "BILL RIDE-101 D2 234.64")
        self.assertEqual(self.third_rider.bill("RIDE-102"), "BILL RIDE-102 D1 258.00")


class TestCaseSix(unittest.TestCase):

    ride_sharing_four = RideSharing()

    def test_scenario(self):
        self.assertEqual(self.ride_sharing_four.add_rider("R1", 0, 0), None)
        self.assertEqual(self.ride_sharing_four.match("R1"), "NO_DRIVERS_AVAILABLE")
        self.assertEqual(self.ride_sharing_four.start_ride("RIDE-001", 2, "R1"), "INVALID_RIDE")
        self.assertEqual(self.ride_sharing_four.stop_ride("RIDE-001", 4, 5, 32), "INVALID_RIDE")
        self.assertEqual(self.ride_sharing_four.bill("RIDE-001"), "INVALID_RIDE")


class TestCaseThree(unittest.TestCase):
    rs_three = RideSharing()

    def test_scenario(self):
        self.assertEqual(self.rs_three.add_rider("R1", 2, 7), None)
        self.assertEqual(self.rs_three.match("R1"), "NO_DRIVERS_AVAILABLE")
        self.assertEqual(self.rs_three.add_driver("D1", 3, 1), None)
        self.assertEqual(self.rs_three.add_driver("D2", 5, 6), None)
        self.assertEqual(self.rs_three.add_driver("D13", 1, 8), None)
        self.assertEqual(self.rs_three.add_driver("D4", 3, 6), None)
        self.assertEqual(self.rs_three.match("R1"), "DRIVERS_MATCHED D13 D4 D2")
        self.assertEqual(self.rs_three.start_ride("RIDE-001", 1, "R1"), "RIDE_STARTED RIDE-001")
        self.assertEqual(self.rs_three.stop_ride("RIDE-001", 4, 15, 60), "RIDE_STOPPED RIDE-001")
        self.assertEqual(self.rs_three.bill("RIDE-001"), "BILL RIDE-001 D13 268.36")


if __name__ == '__main__':
    unittest.main()
