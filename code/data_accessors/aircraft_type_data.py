import csv
import os
import platform
from data_models.aircraft_type import AircraftType


class AircraftTypeData:

    #Store the filename according to whether the user has a Mac or not
    __aircraft_data_filename = os.path.realpath("../data_storage/aircraft_types.csv")

    #A list to cache all the aircraft types once they've been fetched
    __all_aircrafts_list = []

    @staticmethod
    def get_all_aircraft_types():
        all_aircrafts_list = []

        if not AircraftTypeData.__all_aircrafts_list:
            with open(AircraftTypeData.__aircraft_data_filename, 'r', encoding="utf8") as file_stream:
                reader = csv.DictReader(file_stream)
                for row in reader:
                    all_aircrafts_list.append(AircraftType(row["plane_type"], row["manufacturer"],\
                        row["seat_count"]))
            AircraftTypeData.__all_aircrafts_list = all_aircrafts_list

        return AircraftTypeData.__all_aircrafts_list

    # @staticmethod
    # def get_aircraft_type(plane_type):
    #     for aircraft_type in AircraftTypeData.get_all_aircraft_types():
    #         if aircraft_type.get_plane_type() == plane_type:
    #             return aircraft_type

    #     return None

    # @staticmethod
    # def save_new_aircraft_type(aircraft):
    #     field_names = ["plane_type", "model", "capacity", "empty_weight", "max_takeoff_weight",\
    #         "unit_thrust", "service_ceiling", "length", "height", "wingspan"]
    #     with open(AircraftTypeData.__aircraft_data_filename, 'a') as file_stream:
    #         writer = csv.DictWriter(file_stream, fieldnames=field_names, lineterminator='\n')

    #         writer.writerow({
    #             "plane_type": aircraft.get_plane_type(),
    #             "model": aircraft.get_model(),
    #             "capacity": aircraft.get_capacity(),
    #             "empty_weight": aircraft.get_empty_weight(),
    #             "max_takeoff_weight": aircraft.get_max_takeoff_weight(),
    #             "unit_thrust": aircraft.get_unit_thrust(),
    #             "service_ceiling": aircraft.get_service_ceiling(),
    #             "length": aircraft.get_length(),
    #             "height": aircraft.get_height(),
    #             "wingspan": aircraft.get_wingspan()})

    #     if AircraftTypeData.__all_aircrafts_list:
    #         AircraftTypeData.__all_aircrafts_list.append(aircraft)
        