from data_models.pilot import Pilot
from apis.data_api import DataAPI

class PilotLogic:

    @staticmethod
    def __sort_list_by_name(a_list):
        '''Returns a new list sorted in alphabetical name order, returns [] if the list was empty'''
        return a_list if not a_list else sorted(a_list, key=lambda value: value.get_name())

    @staticmethod
    def get_all_pilots():
        return PilotLogic.__sort_list_by_name(DataAPI.get_all_pilots())

    @staticmethod
    def get_licensed_pilots(pilot_license):
        all_pilots = DataAPI.get_all_pilots()
        licensed_pilots = []
        for pilot in all_pilots:
            if pilot.get_license() == pilot_license:
                licensed_pilots.append(pilot)
        return PilotLogic.__sort_list_by_name(licensed_pilots)

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

    @staticmethod
    def change_saved_pilot(saved_pilot, changed_pilot):
        DataAPI.change_saved_pilot(saved_pilot, changed_pilot)

    @staticmethod
    def is_pilot_ssn_available(pilot_ssn):
        all_pilots = DataAPI.get_all_pilots()
        for pilot in all_pilots:
            if pilot.get_ssn() == pilot_ssn:
                return False
        return True
