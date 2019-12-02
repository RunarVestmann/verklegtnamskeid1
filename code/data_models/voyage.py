class Voyage:

    def __init__(self, flights, pilots, flight_attendants, airplane, voyage_schedule, fully_manned, state):
        self.__flights = flights
        self.__pilots = pilots
        self.__flight_attendants = flight_attendants
        self.__airplane = airplane
        self.__voyage_schedule = voyage_schedule
        self.__fully_manned = fully_manned
        self.__state = state

    def get_airplane(self):
        return self.__airplane

    def is_fully_manned(self): # work on later
        return False

    def get_voyage_schedule(self):
        return self.__voyage_schedule

    def get_state(self):
        return self.__state

    def set_state(self, state):
        self.__state = state
