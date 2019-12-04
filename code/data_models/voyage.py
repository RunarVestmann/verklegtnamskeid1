class Voyage:

    def __init__(self, flights, pilots, flight_attendants, airplane, schedule, state):
        self.__flights = flights
        self.__pilots = pilots
        self.__flight_attendants = flight_attendants
        self.__airplane = airplane
        self.__schedule = schedule
        self.__state = state

    def get_airplane(self):
        return self.__airplane

    def get_pilots(self):
        return self.__pilots

    def get_flight_attendants(self):
        return self.__flight_attendants

    def get_flights(self):
        return self.__flights

    def get_schedule(self):
        return self.__schedule

    def get_state(self):
        return self.__state

    def set_state(self, state):
        self.__state = state
