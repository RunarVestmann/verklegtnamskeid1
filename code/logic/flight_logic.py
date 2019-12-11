from data_models.flight import Flight
from apis.data_api import DataAPI

class FlightLogic:

    @staticmethod
    def get_all_flights():
        return DataAPI.get_all_flights()

    @staticmethod
    def get_available_flight_number(airport_id, departure_date_and_time, offset=0):
        all_flights = DataAPI.get_all_flights()

        highest_flight_number = 0

        for flight in all_flights:
            f_dep_time = flight.get_departure_time()
            if f_dep_time.date == departure_date_and_time.date:
                f_num = flight.get_number()
                if f_num > highest_flight_number:
                    highest_flight_number = f_num
                if f_dep_time > departure_date_and_time:
                    DataAPI.change_saved_flight(flight, Flight(flight.get_departure_location, f_dep_time,\
                         flight.get_arrival_location(), flight.get_arrival_time(), f_num[:-1] + str(int(f_num[-1]) + 2)))

        return "NA" + str(airport_id) + str(highest_flight_number+1+offset)


    @staticmethod
    def get_flight(departure_location, departure_time):
        '''Returns a flight at the given departure time, if no flight was found,
           None is returned'''
        return DataAPI.get_flight(departure_location, departure_time)

    @staticmethod
    def change_saved_flight(saved_flight, changed_flight):
        DataAPI.change_saved_flight(saved_flight, changed_flight)

    @staticmethod
    def save_new_flight(flight):
        DataAPI.save_new_flight(flight)
