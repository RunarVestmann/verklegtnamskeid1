from data_models.flight_attendant import FlightAttendant
from apis.data_api import DataAPI

class FlightAttendantLogic:

    @staticmethod
    def get_all_flight_attendants():
        return DataAPI.get_all_flight_attendants()

    @staticmethod
    def save_new_flight_attendant(flight_attendant):
        DataAPI.save_new_flight_attendant(flight_attendant)
