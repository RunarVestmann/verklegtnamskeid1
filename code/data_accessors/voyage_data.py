from data_models.voyage import Voyage
from data_models.flight import Flight
from apis.logic_api import LogicAPI
import csv

class VoyageData:

    __voyage_data_filename = "../data_storage/pilots.csv"
    __all_voyages_list = []

    @staticmethod
    def get_all_voyages():

        #If we haven't cached all the voyages we grab them from the file
        if not VoyageData.__all_voyages_list:
            all_voyages_list = []
            with open(VoyageData.__voyage_data_filename, 'r') as file_stream:
                reader = csv.DictReader(file_stream)
                for row in reader:
                    flights_tuple = (LogicAPI.get_flight(row["flight1"]), LogicAPI.get_flight(row["flight2"]))
                    pilots_list = []
                    flight_attendants_list = []

                    #populate pilots_list if there is at least a captain registered
                    if row["captain"]:
                        pass

                    #populate flight_attendants_list if there is at least a cabin manager registered
                    if row["cabin_manager"]:
                        pass

                    airplane = LogicAPI.get_airplane(row["airplane"])#Needs implementation

                    state = row["state"]

                    #fullymanned (False) need implementation

                    all_voyages_list.append(Voyage(flights_tuple, pilots_list, flight_attendants_list, airplane,\
                         (flights_tuple[0].get_departure_time(), flights_tuple[1].get_departure_time()), False, state))

                VoyageData.__all_voyages_list = all_voyages_list

            return VoyageData.__all_voyages_list

    @staticmethod
    def save_new_voyage(voyage):
        pass
