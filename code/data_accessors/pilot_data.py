import csv
from data_models.pilot import Pilot


class PilotData:

    __pilot_data_filename = "../data_storage/pilots.csv"
    __all_pilots_list = []

    @staticmethod
    def get_all_pilots():
        if not PilotData.__all_pilots_list:
            all_pilots_list = []
            with open(PilotData.__pilot_data_filename, 'r') as file_stream:
                reader = csv.DictReader(file_stream)
                for row in reader:
                    all_pilots_list.append(Pilot(row["name"], row["ssn"], row["phonenumber"],\
                                                row["home_address"], row["email"], row["state"], row["license"]))
            PilotData.__all_pilots_list = all_pilots_list

        return PilotData.__all_pilots_list

    @staticmethod
    def save_new_pilot(pilot):
        pass
    