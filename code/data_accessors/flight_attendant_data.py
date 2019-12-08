import csv
import os
import platform
from data_models.flight_attendant import FlightAttendant

class FlightAttendantData:

    #The paths we found worked for the different operating systems
    __mac_path = os.path.realpath("verklegtnamskeid1/data_storage/flight_attendants.csv")
    __other_path = "../data_storage/flight_attendants.csv"

    #Store the filename according to whether the user has a Mac or not
    __flight_attendant_data_filename = __mac_path if platform.system() == "Darwin" else __other_path

    #A list to cache all the flight attendants once they've been fetched
    __all_flight_attendants_list = []

    @staticmethod
    def get_all_flight_attendants():
        if not FlightAttendantData.__all_flight_attendants_list:
            all_flight_attendants_list = []
            with open(FlightAttendantData.__flight_attendant_data_filename, 'r') as file_stream:
                reader = csv.DictReader(file_stream)
                for row in reader:
                    all_flight_attendants_list.append(FlightAttendant(row["name"], row["ssn"],\
                         row["phonenumber"], row["home_address"], row["email"], row["state"]))
            FlightAttendantData.__all_flight_attendants_list = all_flight_attendants_list

        return FlightAttendantData.__all_flight_attendants_list

    @staticmethod
    def get_flight_attendant(ssn):
        for flight_attendant in FlightAttendantData.get_all_flight_attendants():
            if flight_attendant.get_ssn() == ssn:
                return flight_attendant

        return None

    @staticmethod
    def save_new_flight_attendant(flight_attendant):
        field_names = ["name", "ssn", "phonenumber", "home_address", "email", "state"]
        with open(FlightAttendantData.__flight_attendant_data_filename, 'a') as file_stream:
            writer = csv.DictWriter(file_stream, fieldnames=field_names, lineterminator='\n')

            writer.writerow({
                "name": flight_attendant.get_name(),
                "ssn": flight_attendant.get_ssn(),
                "phonenumber": flight_attendant.get_phonenumber(),
                "home_address": flight_attendant.get_home_address(),
                "email": flight_attendant.get_email(),
                "state": flight_attendant.get_state()
            })

        if FlightAttendantData.__all_flight_attendants_list:
            FlightAttendantData.__all_flight_attendants_list.append(flight_attendant)

    @staticmethod
    def change_saved_flight_attendant(saved_flight_attendant, changed_flight_attendant):
        updated_list_of_flight_attendants = []

        for flight_attendant in FlightAttendantData.get_all_flight_attendants():

            if flight_attendant == saved_flight_attendant:
                updated_list_of_flight_attendants.append(changed_flight_attendant)
            else:
                updated_list_of_flight_attendants.append(flight_attendant)

        FlightAttendantData.__overwrite_all_flight_attendants(updated_list_of_flight_attendants)

    @staticmethod
    def __overwrite_all_flight_attendants(flight_attendants):
        field_names = ["name", "ssn", "phonenumber", "home_address", "email", "state"]
        FlightAttendantData.__all_flight_attendants_list = []
        with open(FlightAttendantData.__flight_attendant_data_filename, 'w') as file_stream:
            writer = csv.DictWriter(file_stream, fieldnames=field_names, lineterminator='\n')
            writer.writeheader()
            for flight_attendant in flight_attendants:
                FlightAttendantData.__all_flight_attendants_list.append(flight_attendant)
                writer.writerow({
                    "name": flight_attendant.get_name(),
                    "ssn": flight_attendant.get_ssn(),
                    "phonenumber": flight_attendant.get_phonenumber(),
                    "home_address": flight_attendant.get_home_address(),
                    "email": flight_attendant.get_email(),
                    "state": flight_attendant.get_state()
                })
