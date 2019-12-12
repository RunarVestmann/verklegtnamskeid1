from datetime import datetime
from data_models.voyage import Voyage
from data_models.state import State
from apis.data_api import DataAPI

class VoyageLogic:

    @staticmethod
    def save_new_voyage(voyage):
        DataAPI.save_new_voyage(voyage)

    @staticmethod
    def get_all_voyages():
        return DataAPI.get_all_voyages()

    @staticmethod
    def change_saved_voyage(saved_voyage, changed_voyage):
        DataAPI.change_saved_voyage(saved_voyage, changed_voyage)

    @staticmethod
    def get_ongoing_voyages():#needs testing
        all_voyages = DataAPI.get_all_voyages()
        ongoing_voyages = []
        completed_state = State.get_voyage_states()[4]

        for voyage in all_voyages:
            if voyage.get_state() != completed_state:
                ongoing_voyages.append(voyage)

        return ongoing_voyages

    @staticmethod
    def get_completed_voyages():#needs testing
        all_voyages = DataAPI.get_all_voyages()
        completed_voyages = []
        completed_state = State.get_voyage_states()[4]

        for voyage in all_voyages:
            if voyage.get_state() == completed_state:
                completed_voyages.append(voyage)

        return completed_voyages

    @staticmethod
    def get_voyages_by_date(date):#needs testing
        all_voyages = DataAPI.get_all_voyages()
        desired_voyages = []

        for voyage in all_voyages:
            if voyage.get_schedule()[0].date() == date:
                desired_voyages.append(voyage)

        return desired_voyages

    @staticmethod
    def get_voyages_by_week(week): #needs testing
        all_voyages = DataAPI.get_all_voyages()
        desired_voyages = []

        for voyage in all_voyages:

            #Get which week in the year each voyage is scheduled
            voyage_week_in_year_int = voyage.get_schedule()[0].date().isocalendar()[1]
            if voyage_week_in_year_int == week:
                desired_voyages.append(voyage)

        return desired_voyages

    @staticmethod
    def get_voyages_by_destination(destination):#needs testing
        all_voyages = DataAPI.get_all_voyages()
        desired_voyages = []

        for voyage in all_voyages:
            if destination in voyage.get_flights()[0].get_arrival_location():
                desired_voyages.append(voyage)

        return desired_voyages

    @staticmethod
    def get_airplane_voyages(airplane):#needs testing
        all_voyages = DataAPI.get_all_voyages()
        airplane_voyages = []

        for voyage in all_voyages:
            if voyage.get_airplane() == airplane:
                airplane_voyages.append(voyage)

        return airplane_voyages

    @staticmethod
    def is_voyage_schedule_start_day_and_time_available(voyage_day_and_time):
        all_voyages = DataAPI.get_all_voyages()
        for voyage in all_voyages:
            if voyage.get_schedule()[0] == voyage_day_and_time:
                return False
        return True
