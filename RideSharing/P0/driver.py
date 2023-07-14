class User:

    def __init__(self, user_id: str):
        self.__id = user_id
        self.type = ''

    def get_id(self):
        return hash(self.__id)

    def __repr__(self):
        return f"{self.type} and {self.__id}"

    def get_user_id(self):
        return self.__id


class Driver(User):

    def __init__(self, driver_id: str):
        super().__init__(driver_id)
        self.type = "DRIVER"


class Rider(User):

    def __init__(self, rider_id: str):
        super().__init__(rider_id)
        self.type = "RIDER"
