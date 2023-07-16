class IdGenerator:

    def __init__(self, value: str):
        self.__value = value

    def get_secret_id(self):
        return hash(self.__value)


class User(IdGenerator):

    def __init__(self, user_id: str, x_position: int, y_position: int):
        self.__id = user_id
        self.type = ''
        super().__init__(user_id)
        self.x_position = x_position
        self.y_position = y_position

    def get_id(self):
        return self.get_secret_id()

    def __repr__(self):
        return f"{self.type} and {self.__id}"

    def get_user_id(self):
        return self.__id


class Driver(User):

    def __init__(self, driver_id: str, x_position: int, y_position: int):
        super().__init__(driver_id, x_position, y_position)
        self.type = "DRIVER"
        self.is_busy: bool = False

    def change_driver_status(self, status: bool):
        self.is_busy = status


class Rider(User):

    def __init__(self, rider_id: str, x_position: int, y_position: int):
        super().__init__(rider_id, x_position, y_position)
        self.type = "RIDER"
