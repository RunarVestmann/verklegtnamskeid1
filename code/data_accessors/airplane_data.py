import csv
from data_models.airplane import Airplane


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

    @staticmethod
    def save_new_airplane(airplane):
        field_names = ["name", "aircraft_type", "manufacturer", "seat_count", "state"]
        with open(AirplaneData.__airplane_data_filename, 'a') as file_stream:
            writer = csv.DictWriter(file_stream, fieldnames=field_names)

            writer.writerow({
                 "name": airplane.get_name(),
                 "aircraft_type": airplane.get_type(),
                 "manufacturer": airplane.get_manufacturer(),
                 "seat_count": airplane.get_seat_count(),
                 "state": airplane.get_state()})

        if AirplaneData.__all_airplanes_list:
            AirplaneData.__all_airplanes_list.append(airplane)
