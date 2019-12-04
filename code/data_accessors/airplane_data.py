from data_models.airplane import Airplane
import csv

class AirplaneData:

    __airplane_data_filename = "../data_storage/airplanes.csv"
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
