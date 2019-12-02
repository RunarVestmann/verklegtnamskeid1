from data_models.flight_route import FlightRoute
from apis.data_api import DataAPI

class FlightRouteLogic:

    @staticmethod
    def save_new_flight_route():
        DataAPI.save_new_flight_route()

    @staticmethod
    def get_all_flight_routes():
        return DataAPI.get_all_flight_routes()
        