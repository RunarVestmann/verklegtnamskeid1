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
            if pilot.get_license() == pilot_license:
                licensed_pilots.append(pilot)
        return licensed_pilots

    @staticmethod
    def get_pilot(ssn):
        '''Returns a pilot with the given ssn,
           if no pilot has the given ssn None is returned'''

        all_pilots = DataAPI.get_all_pilots()

        for pilot in all_pilots:
            if pilot.get_ssn() == ssn:
                return pilot

        return None

    @staticmethod
    def save_new_pilot(pilot):
        DataAPI.save_new_pilot(pilot)
