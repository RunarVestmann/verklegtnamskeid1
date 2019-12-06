import csv
import os
import platform
from data_models.airplane import Airplane
from data_models.aircraft_type import AircraftType


class AirplaneData:

    #The paths we found worked for the different operating systems
    __mac_path = os.path.realpath("verklegtnamskeid1/data_storage/airplanes.csv")
    __other_path = "../data_storage/airplanes.csv"

    #Store the filename according to whether the user has a Mac or not
    __airplane_data_filename = __mac_path if platform.system() == "Darwin" else __other_path

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
                        row["manufacturer"], row["seat_count"], row["state"]))
            AirplaneData.__all_airplanes_list = all_airplanes_list

        return AirplaneData.__all_airplanes_list

    @staticmethod
    def save_new_airplane(airplane):
        field_names = ["name", "aircraft_type", "manufacturer", "seat_count", "state"]
        with open(AirplaneData.__airplane_data_filename, 'a') as file_stream:
            writer = csv.DictWriter(file_stream, fieldnames=field_names)

            writer.writerow({
                 "name": airplane.get_name(),
                 "aircraft_type": airplane.get_type().get_plane_type(),
                 "manufacturer": airplane.get_manufacturer(),
                 "seat_count": airplane.get_seat_count(),
                 "state": airplane.get_state()})

        if AirplaneData.__all_airplanes_list:
            AirplaneData.__all_airplanes_list.append(airplane)
