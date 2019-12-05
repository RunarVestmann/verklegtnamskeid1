from data_accessors.aircraft_type_data import AircraftTypeData
from data_accessors.airplane_data import AirplaneData
from data_accessors.flight_attendant_data import FlightAttendantData
from data_accessors.flight_route_data import FlightRouteData
from data_accessors.pilot_data import PilotData
from data_accessors.voyage_data import VoyageData
from data_accessors.flight_data import FlightData

class DataAPI:
    '''The DataAPI that enables saving and getting data from the csv files'''

    ####  Employees  ####

    @staticmethod
    def get_all_employees():
        return PilotData.get_all_pilots() + FlightAttendantData.get_all_flight_attendants()

    ####  Pilots  ####

    @staticmethod
    def get_all_pilots():
        return PilotData.get_all_pilots()

    @staticmethod
    def save_new_pilot(pilot):
        PilotData.save_new_pilot(pilot)

    ####  Flight Atttendants  ####

    @staticmethod
    def get_all_flight_attendants():
        return FlightAttendantData.get_all_flight_attendants()

    @ staticmethod
    def save_new_flight_attendant(flight_attendant):
        FlightAttendantData.save_new_flight_attendant(flight_attendant)

    ####  Airplanes  ####

    @staticmethod
    def save_new_airplane(airplane):
        AirplaneData.save_new_airplane(airplane)

    @staticmethod
    def get_all_airplanes():
        return AirplaneData.get_all_airplanes()

    ####  Voyages ####

    @staticmethod
    def save_new_voyage(voyage):
        VoyageData.save_new_voyage(voyage)

    @staticmethod
    def get_all_voyages():
        return VoyageData.get_all_voyages()

    @staticmethod
    def save_new_flight_route(flight_route):
        FlightRouteData.save_new_flight_route(flight_route)

    @staticmethod
    def get_all_flight_routes():
        return FlightRouteData.get_all_flight_routes()

    #### Aircraft types  ####

    @staticmethod
    def get_all_aircraft_types():
        return AircraftTypeData.get_all_aircraft_types()
    @staticmethod
    def save_new_aircraft_type(aircraft_type):
        AircraftTypeData.save_new_aircraft_type(aircraft_type)

    ####  Flights  ####

    @staticmethod
    def get_all_flights():
        return FlightData.get_all_flights()

    @staticmethod
    def save_new_flight(flight):
        FlightData.save_new_flight(flight)
        