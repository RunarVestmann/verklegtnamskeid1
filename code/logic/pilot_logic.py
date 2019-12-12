from data_models.pilot import Pilot
from apis.data_api import DataAPI
import datetime

class PilotLogic:

    @staticmethod
    def __sort_list_by_name(a_list):
        '''Returns a new list sorted in alphabetical name order, returns [] if the list was empty'''
        return a_list if not a_list else sorted(a_list, key=lambda value: value.get_name())

    @staticmethod
    def get_all_pilots():
        return PilotLogic.__sort_list_by_name(DataAPI.get_all_pilots())

    @staticmethod
    def get_all_pilot_voyages(pilot):
        all_voyages = DataAPI.get_all_voyages()

        pilot_voyages_list = []

        for voyage in all_voyages:
            if pilot in voyage.get_pilots():
                pilot_voyages_list.append(voyage)

        return pilot_voyages_list

    @staticmethod
    def get_all_pilot_voyages_in_a_week(pilot, week_number):
        pilot_voyages = PilotLogic.get_all_pilot_voyages(pilot)

        pilot_voyages_in_week = []

        for voyage in pilot_voyages:
            if week_number == voyage.get_schedule()[0].date().isocalendar()[1]:
                pilot_voyages_in_week.append(voyage)

        return pilot_voyages_in_week

    @staticmethod
    def get_available_pilots(schedule_tuple):
        all_pilots = DataAPI.get_all_pilots()

        available_pilots = []

        for pilot in all_pilots:
            voyages = PilotLogic.get_all_pilot_voyages(pilot)

            if not voyages:
                available_pilots.append(pilot)
            else:

                for voyage in voyages:
                    voyage_schedule = voyage.get_schedule()
                    if schedule_tuple[0] > voyage_schedule[1] or schedule_tuple[1] < voyage_schedule[0]:
                        available_pilots.append(pilot)

        return PilotLogic.__sort_list_by_name(available_pilots)

    @staticmethod
    def get_available_licensed_pilots(schedule_tuple, pilot_license):
        
        available_licensed_pilots = []

        for pilot in PilotLogic.get_available_pilots(schedule_tuple):
            if pilot.get_license == pilot_license:
                available_licensed_pilots.append(pilot)

        return available_licensed_pilots
           
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
