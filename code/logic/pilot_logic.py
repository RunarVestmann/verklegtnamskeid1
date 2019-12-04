from data_models.pilot import Pilot
from apis.data_api import DataAPI

class PilotLogic:

    @staticmethod
    def get_all_pilots():
        return DataAPI.get_all_pilots()


    @staticmethod
    def get_licensed_pilots(pilot_license):
        all_pilots = DataAPI.get_all_pilots()
        licensed_pilots = []
        for pilot in all_pilots:
            if pilot_license in pilot.get_license():
                licensed_pilots.append(pilot)
        return licensed_pilots

    @staticmethod
    def save_new_pilot(pilot):
        DataAPI.save_new_pilot(pilot)
