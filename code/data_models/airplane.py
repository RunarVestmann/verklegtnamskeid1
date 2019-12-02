class Airplane:

    def __init__(self, name, airplane_type, manufacturer, seat_count, state):
        self.__name = name
        self.__airplane_type = airplane_type
        self.__manufacturer = manufacturer
        self.__seat_count = seat_count
        self.__state = state
    
    def get_name(self):
        return self.__name

    def get_type(self):
        return self.__airplane_type

    def get_manufacturer(self):
        return self.__manufacturer
    
    def get_seat_count(self):
        return self.__seat_count
    
    def get_state(self):
        return self.__state
    
    def set_state(self, state):
        self.__state = state