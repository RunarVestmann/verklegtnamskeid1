from data_models.flight_attendant import FlightAttendant
from apis.data_api import DataAPI

class FlightAttendantLogic:

    @staticmethod
    def __sort_list_by_name(a_list):
        '''Returns a new list sorted in alphabetical name order, returns [] if the list was empty'''
        return a_list if not a_list else sorted(a_list, key=lambda value: value.get_name())

    @staticmethod
    def get_available_flight_attendants(schedule_tuple):
        all_flight_attendants = DataAPI.get_all_flight_attendants()

        available_flight_attendants = []

        for flight_attendant in all_flight_attendants:
            voyages = FlightAttendantLogic.get_all_flight_attendant_voyages(flight_attendant)

            if not voyages:
                available_flight_attendants.append(flight_attendant)
            else:

                for voyage in voyages:
                    voyage_schedule = voyage.get_schedule()
                    if schedule_tuple[0] > voyage_schedule[1] or schedule_tuple[1] < voyage_schedule[0]:
                        available_flight_attendants.append(flight_attendant)

        return FlightAttendantLogic.__sort_list_by_name(available_flight_attendants)


    @staticmethod
    def get_all_flight_attendant_voyages(flight_attendant):
        all_voyages = DataAPI.get_all_voyages()

        flight_attendant_voyages_list = []

        for voyage in all_voyages:
            if flight_attendant in voyage.get_flight_attendants():
                flight_attendant_voyages_list.append(voyage)

        return FlightAttendantLogic.__sort_list_by_name(flight_attendant_voyages_list)

    @staticmethod
    def get_all_flight_attendant_voyages_in_a_week(flight_attendant, week_number):
        flight_attendant_voyages = FlightAttendantLogic.get_all_flight_attendant_voyages(flight_attendant)

        flight_attendant_voyages_in_week = []

        for voyage in flight_attendant_voyages:
            if week_number == voyage.get_schedule()[0].date().isocalendar()[1]:
                flight_attendant_voyages_in_week.append(voyage)

        return FlightAttendantLogic.__sort_list_by_name(flight_attendant_voyages_in_week)

    @staticmethod
    def get_all_flight_attendants():
        return FlightAttendantLogic.__sort_list_by_name(DataAPI.get_all_flight_attendants())

    @staticmethod
    def get_flight_attendant(ssn):
        '''Returns a flight_attendant with the given ssn,
           if no flight_attendant has the given ssn None is returned'''

        all_flight_attendants = DataAPI.get_all_flight_attendants()

        for flight_attendant in all_flight_attendants:
            if flight_attendant.get_ssn() == ssn:
                return flight_attendant

        return None

    @staticmethod
    def save_new_flight_attendant(flight_attendant):
        DataAPI.save_new_flight_attendant(flight_attendant)

    @staticmethod
    def change_saved_flight_attendant(saved_flight_attendant, changed_flight_attendant):
        DataAPI.change_saved_flight_attendant(saved_flight_attendant, changed_flight_attendant)

    @staticmethod
    def is_flight_attendant_ssn_avaliable(flight_attendant_ssn):
        all_flight_attendants = DataAPI.get_all_flight_attendants()
        for flight_attendant in all_flight_attendants:
            if flight_attendant.get_ssn() == flight_attendant_ssn:
                return 

        return True