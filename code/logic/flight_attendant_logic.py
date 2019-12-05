from data_models.flight_attendant import FlightAttendant
from apis.data_api import DataAPI

class FlightAttendantLogic:

    @staticmethod
    def get_all_flight_attendants():
        return DataAPI.get_all_flight_attendants()

    @staticmethod
    def get_flight_attendant(ssn):
        '''Returns a flight_attendant with the given ssn,
           if no flight_attendant has the given ssn None is returned'''

        all_flight_attendants = DataAPI.get_all_flight_attendants()

        for flight_attendant in all_flight_attendants:
            if flight_attendant.get_ssn() == ssn:
                return flight_attendant

        return None

    @staticmethod
    def save_new_flight_attendant(flight_attendant):
        DataAPI.save_new_flight_attendant(flight_attendant)
