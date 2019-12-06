import csv
import os
import platform
import dateutil.parser as util
from data_models.voyage import Voyage
from data_models.flight import Flight
from data_accessors.airplane_data import AirplaneData
from data_accessors.flight_data import FlightData
from data_accessors.flight_attendant_data import FlightAttendantData
from data_accessors.pilot_data import PilotData

class VoyageData:

    #The paths we found worked for the different operating systems
    __mac_path = os.path.realpath("verklegtnamskeid1/data_storage/voyages.csv")
    __other_path = "../data_storage/voyages.csv"

    #Store the filename according to whether the user has a Mac or not
    __voyage_data_filename = __mac_path if platform.system() == "Darwin" else __other_path

    #A list to cache all the pilots once they've been fetched
    __all_voyages_list = []

    #Constants that have been predetermined
    __max_pilots_onboard = 10
    __max_flight_attendants_on_board = 10
    __flights_per_voyage = 2

    @staticmethod
    def __get_employees(head_employee_str, normal_employee_str, row):
        employees_list = []

        head_employee = row[head_employee_str]
            #populate the pilots_list if there is at least a captain registered
        if head_employee:
            employees_list.append(head_employee)
            for i in range(1, VoyageData.__max_pilots_onboard):
                employee = row[normal_employee_str + str(i)]

                #If there are more employees to add, we add them
                if employee:
                    employees_list.append(employee)

        return employees_list


    @staticmethod
    def get_all_voyages():
        '''Returns a list of voyages with some of the voyage data missing,
           VoyageLogic.get_all_voyages() is responsible for getting the missing data
           so don't call this function elsewhere'''

        #If we haven't cached all the voyages we grab them from the file
        if not VoyageData.__all_voyages_list:

            #A list to temporarily store all the voyages
            all_voyages_list = []

            with open(VoyageData.__voyage_data_filename, 'r') as file_stream:
                reader = csv.DictReader(file_stream)
                for row in reader:

                    flight1 = FlightData.get_flight(row["flight1_departure_location"], util.parse(row["flight1_departure_time"]))
                    flight2 = FlightData.get_flight(row["flight2_departure_location"], util.parse( row["flight2_departure_time"]))

                    pilots_ssn_list = VoyageData.__get_employees("captain", "copilot", row)

                    pilots_list = []

                    for pilot_ssn in pilots_ssn_list:
                        if pilot_ssn:
                            pilots_list.append(PilotData.get_pilot(pilot_ssn))

                    flight_attendants_ssn_list = VoyageData.__get_employees("cabin_manager", "flight_attendant", row)

                    flight_attendants_list = []

                    for flight_attendants_ssn in flight_attendants_ssn_list:
                        if flight_attendants_ssn:
                            flight_attendants_list.append(FlightAttendantData.get_flight_attendant(flight_attendants_ssn))

                    airplane = AirplaneData.get_airplane(row["airplane_name"])

                    schedule = row["schedule"].split("_")

                    #Change the data from being a string to a tuple of datetime objects
                    schedule = util.parse(schedule[0]), util.parse(schedule[1])

                    state = row["state"]

                    all_voyages_list.append(Voyage((flight1, flight2), pilots_list, flight_attendants_list, airplane, schedule, state))

                VoyageData.__all_voyages_list = all_voyages_list

            return VoyageData.__all_voyages_list

    @staticmethod
    def __fill_list_with_empty_strings(a_list, max_length):
        while len(a_list) < max_length:
            a_list.append("")

    @staticmethod
    def save_new_voyage(voyage):
        field_names = ["flight1_departure_location", "flight1_departure_time", "flight2_departure_location", "flight2_departure_time",\
             "captain", "copilot1", "copilot2", "copilot3", "copilot4", "copilot5", "copilot6", "copilot7", "copilot8", "copilot9",\
             "cabin_manager", "flight_attendant1", "flight_attendant2", "flight_attendant3", "flight_attendant4", "flight_attendant5",\
             "flight_attendant6", "flight_attendant7", "flight_attendant8", "flight_attendant9", "airplane_name", "schedule", "state"]

        with open(VoyageData.__voyage_data_filename, 'a') as file_stream:
            writer = csv.DictWriter(file_stream, fieldnames=field_names)

            flight1, flight2 = voyage.get_flights()
            pilots_ssn_list = []

            #Add all the pilots social security numbers to the list
            for pilot in voyage.get_pilots():
                pilots_ssn_list.append(pilot.get_ssn())

            #Fill the list with empty strings if the number of pilots registered < max
            VoyageData.__fill_list_with_empty_strings(pilots_ssn_list, VoyageData.__max_pilots_onboard)

            flight_attendants_ssn_list = []

            #Add all the flight attendants social security numbers to the list
            for flight_attendant in voyage.get_flight_attendants():
                flight_attendant.append(flight_attendant)

            #Fill the list with empty strings if the number of flight attendants registered < max
            VoyageData.__fill_list_with_empty_strings(flight_attendants_ssn_list, VoyageData.__max_flight_attendants_on_board)

            writer.writerow({
                 "flight1_departure_location": flight1.get_departure_location(),
                 "flight1_departure_time": flight1.get_departure_time(),
                 "flight2_departure_location": flight2.get_departure_location(),
                 "flight2_departure_time": flight2.get_departure_time(),
                 "captain": pilots_ssn_list[0],
                 "copilot1": pilots_ssn_list[1],
                 "copilot2": pilots_ssn_list[2],
                 "copilot3": pilots_ssn_list[3],
                 "copilot4": pilots_ssn_list[4],
                 "copilot5": pilots_ssn_list[5],
                 "copilot6": pilots_ssn_list[6],
                 "copilot7": pilots_ssn_list[7],
                 "copilot8": pilots_ssn_list[8],
                 "copilot9": pilots_ssn_list[9],
                 "cabin_manager": flight_attendants_ssn_list[0],
                 "flight_attendant1": flight_attendants_ssn_list[1],
                 "flight_attendant2": flight_attendants_ssn_list[2],
                 "flight_attendant3": flight_attendants_ssn_list[3],
                 "flight_attendant4": flight_attendants_ssn_list[4],
                 "flight_attendant5": flight_attendants_ssn_list[5],
                 "flight_attendant6": flight_attendants_ssn_list[6],
                 "flight_attendant7": flight_attendants_ssn_list[7],
                 "flight_attendant8": flight_attendants_ssn_list[8],
                 "flight_attendant9": flight_attendants_ssn_list[9],
                 "airplane_name": voyage.get_airplane().get_name(),
                 "schedule": voyage.get_schedule()[0].isoformat() + '_' + voyage.get_schedule()[1].isoformat(),
                 "state": voyage.get_state()
                 })

        #If we've have cached all the voyages, we add this new one to the cached list
        if VoyageData.__all_voyages_list:
            VoyageData.__all_voyages_list.append(voyage)
