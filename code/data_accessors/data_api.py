class DataAPI:

    __airplane_data = None
    __voyage_data = None
    __flight_route_data = None
    __pilot_data = None
    __flight_attendant = None

    @staticmethod
    def initialize():
        pass
        # __airplane_data = AirplaneData()
        # __voyage_data = VoyageData()
        # __flight_route_data = FlightRouteData()
        # __pilot_data = PilotData()
        # __flight_attendant = FlightAttendant()


    ####Employees####

    @staticmethod
    def get_all_employees():
        return []

    ####Pilots####

    @staticmethod
    def get_all_pilots():
        return []

    @staticmethod
    def save_new_pilot(pilot):
        pass

    ####Flight Atttendants####

    @staticmethod
    def get_all_flight_attendants():
        return []

    @ staticmethod
    def save_new_flight_attendant():
        pass

    ####Airplanes####

    @staticmethod
    def save_new_airplane():
        pass

    @staticmethod
    def get_all_airplanes():
        return []

    @staticmethod
    def save_new_voyage():
        pass

    @staticmethod
    def get_all_voyages():
        return []

    @staticmethod
    def save_new_flight_route():
        pass

    @staticmethod
    def get_all_flight_routes():
        return []
        