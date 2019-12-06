from data_models.flight import Flight
from apis.data_api import DataAPI

class FlightLogic:

    @staticmethod
    def get_all_flights():
        return DataAPI.get_all_flights()

    @staticmethod
    def get_flight(departure_location, departure_time):
        '''Returns a flight at the given departure time, if no flight was found,
           None is returned'''
        return DataAPI.get_flight(departure_location, departure_time)

    @staticmethod
    def save_new_flight(flight):
        DataAPI.save_new_flight(flight)
