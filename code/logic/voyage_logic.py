from datetime import datetime
from data_models.voyage import Voyage
from data_models.state import State
from apis.data_api import DataAPI
from logic.flight_logic import FlightLogic
from logic.pilot_logic import PilotLogic
from logic.flight_attendant_logic import FlightAttendantLogic
from logic.airplane_logic import AirplaneLogic

class VoyageLogic:

    @staticmethod
    def save_new_voyage(voyage):
        DataAPI.save_new_voyage(voyage)

    @staticmethod
    def get_all_voyages():

        #Get all the voyages but some data isn't stored in the csv
        all_voyages_with_limited_data = DataAPI.get_all_voyages()
        all_voyages = []

        #Fetch all the missing data and append to a new list of voyages
        for voyage in all_voyages_with_limited_data:
            airplane = AirplaneLogic.get_airplane(voyage.get_airplane())

            flight1_departure_location, flight1_departue_time, \
            flight2_departure_location, flight2_departure_time = voyage.get_flights()

            flight1 = FlightLogic.get_flight(flight1_departure_location, flight1_departue_time)
            flight2 = FlightLogic.get_flight(flight2_departure_location, flight2_departure_time)

            pilots_list = []
            if voyage.get_pilots():
                pilots_list = [PilotLogic.get_pilot(pilot) for pilot in voyage.get_pilots()]

            flight_attendants_list = []
            if voyage.get_flight_attendants():
                flight_attendants_list = [FlightAttendantLogic.get_flight_attendant(flight_attendant)\
                     for flight_attendant in voyage.get_flight_attendants()]

            voyage_with_all_data = Voyage((flight1, flight2), pilots_list, flight_attendants_list,\
                 airplane, voyage.get_schedule(), voyage.get_state())

            all_voyages.append(voyage_with_all_data)

        return all_voyages


    @staticmethod
    def get_ongoing_voyages():#needs testing
        all_voyages = VoyageLogic.get_all_voyages()
        ongoing_voyages = []
        completed_state = State.get_voyage_states()[4]

        for voyage in all_voyages:
            if voyage.get_state() != completed_state:
                ongoing_voyages.append(voyage)

        return ongoing_voyages

    @staticmethod
    def get_completed_voyages():#needs testing
        all_voyages = VoyageLogic.get_all_voyages()
        completed_voyages = []
        completed_state = State.get_voyage_states()[4]

        for voyage in all_voyages:
            if voyage.get_state() == completed_state:
                completed_voyages.append(voyage)

        return completed_voyages

    @staticmethod
    def get_voyages_by_date(date):#needs testing
        all_voyages = VoyageLogic.get_all_voyages()
        desired_voyages = []

        for voyage in all_voyages:
            if voyage.get_schedule[0] == date:
                desired_voyages.append(voyage)

        return desired_voyages

    @staticmethod
    def get_voyages_by_week(week): #needs testing
        all_voyages = VoyageLogic.get_all_voyages()
        desired_voyages = []

        for voyage in all_voyages:

            #Store what date the voyage departs
            year, month, date = voyage.get_schedule().split("-")

            #Get which week in the year each voyage is scheduled
            voyage_week_in_year_int = datetime.date(year, month, date).isocalendar()[1]
            if voyage_week_in_year_int == week:
                desired_voyages.append(voyage)

        return desired_voyages

    @staticmethod
    def get_voyages_by_destination(destination):#needs testing
        all_voyages = VoyageLogic.get_all_voyages()
        desired_voyages = []

        for voyage in all_voyages:
            if voyage.get_flights[0].get_departure_location() == destination:
                desired_voyages.append(voyage)

        return desired_voyages

    @staticmethod
    def get_airplane_voyages(airplane):#needs testing
        all_voyages = VoyageLogic.get_all_voyages()
        airplane_voyages = []

        for voyage in all_voyages:
            if voyage.get_airplane() == airplane:
                airplane_voyages.append(voyage)

        return airplane_voyages
