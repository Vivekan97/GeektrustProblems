from typing import List
import helpers
from ride_sharing import RideSharing


class RideManagement:

    def __init__(self, user_inputs: List[List[str]]):
        self.user_inputs = user_inputs
        self.ride_sharing = RideSharing()

    def ride_management(self):
        for user_input in self.user_inputs:
            if user_input[0] == helpers.ADD_DRIVER:
                self.ride_sharing.add_driver(user_input[1], int(user_input[2]), int(user_input[3]))
            if user_input[0] == helpers.ADD_RIDER:
                self.ride_sharing.add_rider(user_input[1], int(user_input[2]), int(user_input[3]))
            if user_input[0] == helpers.START_MATCHING:
                print(self.ride_sharing.match(user_input[1]))
            if user_input[0] == helpers.START_RIDE:
                print(self.ride_sharing.start_ride(user_input[1], int(user_input[2]), user_input[3]))
            if user_input[0] == helpers.STOP_RIDE:
                print(self.ride_sharing.stop_ride(user_input[1], int(user_input[2]),
                                                  int(user_input[3]), int(user_input[4])))
            if user_input[0] == helpers.START_BILLING:
                print(self.ride_sharing.bill(user_input[1]))
