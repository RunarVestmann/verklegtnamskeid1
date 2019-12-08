import csv
import os
import platform
from data_models.pilot import Pilot

class PilotData:

    #The paths we found worked for the different operating systems
    __mac_path = os.path.realpath("verklegtnamskeid1/data_storage/pilots.csv")
    __other_path = "../data_storage/pilots.csv"

    #Store the filename according to whether the user has a Mac or not
    __pilot_data_filename = __mac_path if platform.system() == "Darwin" else __other_path

    #A list to cache all the pilots once they've been fetched
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
    def get_pilot(ssn):
        for pilot in PilotData.get_all_pilots():
            if pilot.get_ssn() == ssn:
                return pilot
        return None

    @staticmethod
    def save_new_pilot(pilot):
        field_names = ["name", "ssn", "phonenumber", "home_address", "email", "state", "license"]
        with open(PilotData.__pilot_data_filename, 'a') as file_stream:
            writer = csv.DictWriter(file_stream, fieldnames=field_names, lineterminator='\n')

            writer.writerow({"name": pilot.get_name(),
                 "ssn": pilot.get_ssn(),
                 "phonenumber": pilot.get_phonenumber(),
                 "home_address": pilot.get_home_address(),
                 "email": pilot.get_email(),
                 "state": pilot.get_state(),
                 "license": pilot.get_license()
                 })

        if PilotData.__all_pilots_list:
            PilotData.__all_pilots_list.append(pilot)

    @staticmethod
    def change_saved_pilot(saved_pilot, changed_pilot):
        updated_list_of_pilots = []

        for pilot in PilotData.get_all_pilots():

            if pilot == saved_pilot:
                updated_list_of_pilots.append(changed_pilot)
            else:
                updated_list_of_pilots.append(pilot)

        PilotData.__overwrite_all_pilots(updated_list_of_pilots)

    @staticmethod
    def __overwrite_all_pilots(pilots):
        field_names = ["name", "ssn", "phonenumber", "home_address", "email", "state", "license"]
        with open(PilotData.__pilot_data_filename, 'w') as file_stream:
            writer = csv.DictWriter(file_stream, fieldnames=field_names, lineterminator='\n')

            writer.writeheader()

            PilotData.__all_pilots_list = []

            for pilot in pilots:
                PilotData.__all_pilots_list.append(pilot)
                writer.writerow({
                    "name": pilot.get_name(),
                    "ssn": pilot.get_ssn(),
                    "phonenumber": pilot.get_phonenumber(),
                    "home_address": pilot.get_home_address(),
                    "email": pilot.get_email(),
                    "state": pilot.get_state(),
                    "license": pilot.get_license()
                    })
