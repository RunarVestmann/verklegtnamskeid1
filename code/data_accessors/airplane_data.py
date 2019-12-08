import csv
import os
import platform
from data_models.airplane import Airplane
from data_models.aircraft_type import AircraftType
from data_accessors.aircraft_type_data import AircraftTypeData


class AirplaneData:

    #The paths we found worked for the different operating systems
    __mac_path = os.path.realpath("verklegtnamskeid1/data_storage/airplanes.csv")
    __other_path = "../data_storage/airplanes.csv"

    #Store the filename according to whether the user has a Mac or not
    __airplane_data_filename = __mac_path if platform.system() == "Darwin" else __other_path

    __NOT_IN_USE_STATES_TUPLE = ("Not scheduled","Not in use")      #for testing emty,"Waiting for flight from Iceland")

    #A list to cache all the airplanes once they've been fetched
    __all_airplanes_list = []

    @staticmethod
    def get_all_airplanes():
        all_airplanes_list = []

        if not AirplaneData.__all_airplanes_list:
            with open(AirplaneData.__airplane_data_filename, 'r') as file_stream:
                reader = csv.DictReader(file_stream)
                for row in reader:
                    all_airplanes_list.append(Airplane(row["name"], row["aircraft_type"],\
                        row["manufacturer"], row["seat_count"], row["state"]))  #AircraftTypeData.get_aircraft_type(row["aircraft_type"])
                        
            AirplaneData.__all_airplanes_list = all_airplanes_list

        return AirplaneData.__all_airplanes_list

    @staticmethod
    def get_airplane(airplane_name):
        '''Returns an airplane that has the given name,
           returns None if no such airplane is found'''

        for airplane in AirplaneData.get_all_airplanes():
            if airplane.get_name() == airplane_name:
                return airplane

        return None


    @staticmethod
    def get_all_airplanes_in_use():
        '''Returns airplanes in use by exluding airplanes that have-not-in-us-state form all airplane list'''
        airplane_in_use = []

        for airplane in AirplaneData.get_all_airplanes():
            if airplane.get_state() not in AirplaneData.__NOT_IN_USE_STATES_TUPLE:
                airplane_in_use.append(airplane)
        
        return airplane_in_use

            

    @staticmethod
    def save_new_airplane(airplane):
        field_names = ["name", "aircraft_type", "manufacturer", "seat_count", "state"]
        with open(AirplaneData.__airplane_data_filename, 'a') as file_stream:
            writer = csv.DictWriter(file_stream, fieldnames=field_names, lineterminator='\n')

            writer.writerow({
                 "name": airplane.get_name(),
                 "aircraft_type": airplane.get_type(), #.get_plane_type(),
                 "manufacturer": airplane.get_manufacturer(),
                 "seat_count": airplane.get_seat_count(),
                 "state": airplane.get_state()})

        if AirplaneData.__all_airplanes_list:
            AirplaneData.__all_airplanes_list.append(airplane)
