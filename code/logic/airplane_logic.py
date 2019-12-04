from data_models.airplanes import Airplane
from apis.data_api import DataAPI

class AirplaneLogic:

    @staticmethod
    def save_new_airplane(airplane):
        DataAPI.save_new_airplane(airplane)

    @staticmethod
    def get_all_airplanes():
        return DataAPI.get_all_airplanes()

    @staticmethod
    def get_all_available_airplanes(schedule):
        
        all_airplanes = DataAPI.get_all_airplanes()
        return [schedule("")]
        