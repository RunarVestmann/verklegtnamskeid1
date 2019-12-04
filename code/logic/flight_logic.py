from data_models.flight import Flight
from apis.data_api import DataAPI

class FlightLogic:

    @staticmethod
    def get_all_flights():
        return DataAPI.get_all_flights()

    @staticmethod
    def get_flight(departure_time):
        '''Returns a flight at the given departure time, if no flight was found,
           None is returned'''
        all_flights_list = DataAPI.get_all_flights()

        for flight in all_flights_list:
            if flight.departure_time == departure_time:
                return flight

        return None

    @staticmethod
    def save_new_flight(flight):
        DataAPI.save_new_flight(flight)
