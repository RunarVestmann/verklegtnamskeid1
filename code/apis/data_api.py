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
    def get_pilot(ssn):
        return PilotData.get_pilot(ssn)

    @staticmethod
    def save_new_pilot(pilot):
        PilotData.save_new_pilot(pilot)

    @staticmethod
    def change_saved_pilot(saved_pilot, changed_pilot):
        PilotData.change_saved_pilot(saved_pilot, changed_pilot)

    ####  Flight Atttendants  ####

    @staticmethod
    def get_all_flight_attendants():
        return FlightAttendantData.get_all_flight_attendants()

    @staticmethod
    def get_flight_attendant(ssn):
        return FlightAttendantData.get_flight_attendant(ssn)

    @ staticmethod
    def save_new_flight_attendant(flight_attendant):
        FlightAttendantData.save_new_flight_attendant(flight_attendant)

    @staticmethod
    def change_saved_flight_attendant(saved_flight_attendant, changed_flight_attendant):
        FlightAttendantData.change_saved_flight_attendant(saved_flight_attendant, changed_flight_attendant)

    ####  Airplanes  ####

    @staticmethod
    def save_new_airplane(airplane):
        AirplaneData.save_new_airplane(airplane)

    @staticmethod
    def change_saved_airplane(saved_airplane, changed_airplane):
        AirplaneData.change_saved_airplane(saved_airplane, changed_airplane)

    @staticmethod
    def get_airplane(name):
        return AirplaneData.get_airplane(name)

    @staticmethod
    def get_all_airplanes():
        return AirplaneData.get_all_airplanes()

    @staticmethod
    def get_all_airplanes_in_use():
        return AirplaneData.get_all_airplanes_in_use()

    ####  Voyages ####

    @staticmethod
    def save_new_voyage(voyage):
        VoyageData.save_new_voyage(voyage)

    @staticmethod
    def change_saved_voyage(saved_voyage, changed_voyage):
        VoyageData.change_saved_voyage(saved_voyage, changed_voyage)

    @staticmethod
    def get_all_voyages():
        return VoyageData.get_all_voyages()

    @staticmethod
    def get_airplane_voyages(airplane):
        return VoyageData.get_airplane_voyages(airplane)

    ####  Flight routes  ####

    @staticmethod
    def save_new_flight_route(flight_route):
        FlightRouteData.save_new_flight_route(flight_route)

    @staticmethod
    def change_saved_flight_route(saved_flight_route, changed_flight_route):
        FlightRouteData.change_saved_flight_route(saved_flight_route, changed_flight_route)

    @staticmethod
    def get_all_flight_routes():
        return FlightRouteData.get_all_flight_routes()

    #### Aircraft types  ####

    @staticmethod
    def get_all_aircraft_types():
        return AircraftTypeData.get_all_aircraft_types()

    @staticmethod
    def get_aircraft_type(plane_type):
        return AircraftTypeData.get_aircraft_type(plane_type)

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

    @staticmethod
    def get_flight(departure_location, departure_time):
        return FlightData.get_flight(departure_location, departure_time)

    @staticmethod
    def change_saved_flight(saved_flight, changed_flight):
        FlightData.change_saved_flight(saved_flight, changed_flight)
        