class Ride:

    def __init__(self, ride_id: str):
        self.__id: str = ride_id
        self._active: bool = False
        self.ride_x_location: int = 0
        self.ride_y_location: int = 0
        self.time_taken: int = 0

    def get_ride_status(self):
        return self._active

    def set_ride_status(self, ride_status: bool):
        self._active = ride_status

    def update_ride(self, x_position: int, y_position: int, time_taken: int):
        self.ride_x_location = x_position
        self.ride_y_location = y_position
        self.time_taken = time_taken

    def get_ride_current_position(self):
        return self.ride_x_location, self.ride_y_location

    def get_time_taken(self):
        return self.time_taken
