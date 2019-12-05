from data_models.aircraft_type import AircraftType
from apis.data_api import DataAPI

class AircraftTypeLogic:

    @staticmethod
    def get_all_aircraft_types():
        return DataAPI.get_all_aircraft_types()
    
    @staticmethod
    def save_new_aircraft_type(aircraft_type):
        DataAPI.save_new_aircraft_type(aircraft_type)

