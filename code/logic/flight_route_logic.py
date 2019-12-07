from data_models.flight_route import FlightRoute
from apis.data_api import DataAPI

class FlightRouteLogic:

    @staticmethod
    def save_new_flight_route():
        DataAPI.save_new_flight_route()

    @staticmethod
    def get_all_flight_routes():
        return DataAPI.get_all_flight_routes()

    @staticmethod
    def is_airport_id_available(airport_id):
        all_flight_routes = DataAPI.get_all_flight_routes()
        for flight_route in all_flight_routes:
            if flight_route.get_airport_id() == airport_id:
                return False
        return True
        