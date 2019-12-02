from data_accessors.aircraft_type_data import AircraftTypeData
from data_accessors.airplane_data import AirplaneData
from data_accessors.flight_attendant_data import FlightAttendantData

class DataAPI:
    '''The DataAPI that enables saving and getting data from the csv files'''

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
