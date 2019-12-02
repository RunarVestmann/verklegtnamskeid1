from logic.airplane_logic import AirplaneLogic
from logic.aircraft_type_logic import AircraftTypeLogic
from logic.flight_attendant_logic import FlightAttendantLogic
from logic.flight_route_logic import FlightRouteLogic
from logic.pilot_logic import PilotLogic
from logic.employee_logic import EmployeeLogic
from logic.voyage_logic import VoyageLogic

from data_api import DataAPI

class LogicAPI:
    '''The logic layer API that enables the UI layer to save and
       get data from the data layer'''

    ####Employees####

    @staticmethod
    def get_all_employees():
        return EmployeeLogic.get_all_employees()

    @staticmethod
    def get_employees_on_duty():
        return EmployeeLogic.get_employees_on_duty()

    @staticmethod
    def get_employees_off_duty():
        return EmployeeLogic.get_employees_off_duty()

    ####Pilots####

    @staticmethod
    def get_all_pilots():
        return PilotLogic.get_all_pilots()

    @staticmethod
    def get_licensed_pilots(pilot_license):
        return PilotLogic.get_licensed_pilots(pilot_license)

    @staticmethod
    def save_new_pilot(pilot):
        PilotLogic.save_new_pilot(pilot)

    ####Flight attendants####

    @staticmethod
    def get_all_flight_attendants():
        return FlightAttendantLogic.get_all_flight_attendants()

    @staticmethod
    def save_new_flight_attendant(flight_attendant):
        FlightAttendantLogic.save_new_flight_attendant(flight_attendant)

    ####Voyages####

    @staticmethod
    def save_new_voyage(voyage):
        VoyageLogic.save_new_voyage(voyage)

    @staticmethod
    def get_ongoing_voyages():
        return VoyageLogic.get_ongoing_voyages()

    @staticmethod
    def get_voyages_by_date(date):
        return VoyageLogic.get_voyages_by_date(date)

    @staticmethod
    def get_voyages_by_week(week):
        return VoyageLogic.get_voyages_by_week(week)

    @staticmethod
    def get_voyages_by_destination(destination):
        return VoyageLogic.get_voyages_by_destination(destination)

    ####Airplanes####

    @staticmethod
    def save_new_airplane(airplane):
        AirplaneLogic.save_new_airplane(airplane)

    @staticmethod
    def get_all_airplanes():
        return AirplaneLogic.get_all_airplanes()

    @staticmethod
    def get_all_airplanes_in_use():
        return AirplaneLogic.get_all_airplanes_in_use()

    @staticmethod
    def get_all_airplane_types():
        return AircraftTypeLogic.get_all_aircraft_types()

    @staticmethod
    def get_all_available_airplanes():
        return AirplaneLogic.get_all_available_airplanes()

    ####Flight routes####

    @staticmethod
    def save_new_flight_route(flight_route):
        FlightRouteLogic.save_new_flight_route(flight_route)

    @staticmethod
    def get_all_flight_routes():
        return DataAPI.get_all_flight_routes()
