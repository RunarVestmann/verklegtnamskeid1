from data_models.airplanes import Airplane
from apis.data_api import DataAPI


class AirplaneLogic:

    def save_new_airplane(self, airplane):
        DataAPI.save_new_airplane(airplane)

    def get_all_airplanes(self):
        return DataAPI.get_all_airplanes()
        