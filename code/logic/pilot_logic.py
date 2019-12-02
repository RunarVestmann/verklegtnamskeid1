from data_models.pilot import Pilot
from apis.data_api import DataAPI

class PilotLogic:

    @staticmethod
    def get_all_pilots():
        return DataAPI.get_all_pilots()

    @staticmethod
    def get_licensed_pilots():
        return []

    @staticmethod
    def save_new_pilot(pilot):
        DataAPI.save_new_pilot(pilot)
