from data_models.voyage import Voyage
from data_models.state import State
from apis.data_api import DataAPI
from datetime import datetime

class VoyageLogic:

    @staticmethod
    def save_new_voyage(voyage):
        DataAPI.save_new_voyage(voyage)

    @staticmethod
    def get_ongoing_voyages():#needs testing
        all_voyages = DataAPI.get_all_voyages()
        ongoing_voyages = []
        completed_state = State.get_voyage_state()[4]

        for voyage in all_voyages:
            if voyage.get_state() != completed_state:
                ongoing_voyages.append(voyage)

        return ongoing_voyages


    @staticmethod
    def get_completed_voyages():#needs testing
        all_voyages = DataAPI.get_all_voyages()
        completed_voyages = []
        completed_state = State.get_voyage_state()[4]

        for voyage in all_voyages:
            if voyage.get_state() == completed_state:
                completed_voyages.append(voyage)

        return completed_voyages

    @staticmethod
    def get_voyages_by_date(date):#needs testing
        all_voyages = DataAPI.get_all_voyages()
        desired_voyages = []

        for voyage in all_voyages:
            if voyage.get_voyage_schedule[0] == date:
                desired_voyages.append(voyage)

        return desired_voyages

    @staticmethod
    def get_voyages_by_week(week): #needs testing
        all_voyages = DataAPI.get_all_voyages()
        desired_voyages = []

        for voyage in all_voyages:

            #Store what date the voyage departs
            year, month, date = voyage.get_voyage_schedule().split("-")

            #Get which week in the year each voyage is scheduled
            voyage_week_in_year_int = datetime.date(year, month, date).isocalendar()[1]
            if voyage_week_in_year_int == week:
                desired_voyages.append(voyage)

        return desired_voyages

    @staticmethod
    def get_voyages_by_destination(destination):#needs testing
        all_voyages = DataAPI.get_all_voyages()
        desired_voyages = []

        for voyage in all_voyages:
            if voyage.get_flights[0].get_departure_location() == destination:
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