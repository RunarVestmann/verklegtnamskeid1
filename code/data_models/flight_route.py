class FlightRoute: 

    def __init__(self, country, destination, airport_id, flight_time,\
                 distance_from_iceland, contact_name, emergency_phone):
        self.__country = country
        self.__destination = destination
        self.__airport_id = airport_id
        self.__flight_time = flight_time
        self.__distance_from_iceland = distance_from_iceland
        self.__contact_name = contact_name
        self.__emergency_phone = emergency_phone

    def get_country(self):
        return self.__country

    def get_destination(self):
        return self.__destination

    def get_airport_id(self):
        return self.__airport_id

    def get_flight_time(self):
        return self.__flight_time

    def get_distance_from_iceland(self):
        return self.__distance_from_iceland

    def get_contact_name(self):
        return self.__contact_name

    def set_contact_name(self, contact_name):
        self.__contact_name = contact_name

    def get_emergency_phone(self):
        return self.__emergency_phone

    def set_emergency_phone(self, emergency_phone):
        self.__emergency_phone = emergency_phone
