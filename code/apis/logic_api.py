from flight_attendant_logic import FlightAttendantLogic
from pilot_logic import PilotLogic
from employee_logic import EmployeeLogic
from voyage_logic import VoyageLogic

from data_api import DataAPI



class LogicAPI:
    '''The logic layer API that enables the UI layer to save and
       get data from the data layer'''

    ####Employees####

    @staticmethod
    def get_all_employees():
        return []

    @staticmethod
    def get_employees_on_duty():
        return []

    @staticmethod
    def get_employees_off_duty():
        return []

    ####Pilots####

    @staticmethod
    def get_all_pilots():
        return []

    @staticmethod
    def get_licensed_pilots(pilot_license):
        return []

    @staticmethod
    def save_new_pilot(pilot):
        pass

    ####Flight attendants####

    @staticmethod
    def get_all_flight_attendants():
        return []

    @staticmethod
    def save_new_flight_attendat(flight_attendant):
        pass

    ####Voyages####

    @staticmethod
    def save_new_voyage(voyage):
        pass

    @staticmethod
    def get_ongoing_voyages():
        pass

    @staticmethod
    def get_voyages_by_date(date):
        return []

    @staticmethod
    def get_voyages_by_week(week):
        return []

    @staticmethod
    def get_voyages_by_destination(destination):
        return []

    ####Airplanes####

    @staticmethod
    def save_new_airplane(airplane):
        pass

    @staticmethod
    def get_all_airplanes():
        return []

    @staticmethod
    def get_all_airplanes_in_use():
        return []

    @staticmethod
    def get_all_airplane_types():
        return []

    @staticmethod
    def get_all_available_airplanes():
        return []

    ####Flight routes####

    @staticmethod
    def save_new_flight_route():
        pass

    @staticmethod
    def get_all_flight_routes():
        return []