import csv
from data_models.voyage import Voyage
from data_models.flight import Flight

class VoyageData:

    __voyage_data_filename = "../data_storage/voyages.csv"
    __all_voyages_list = []

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

        #If we haven't cached all the voyages we grab them from the file
        if not VoyageData.__all_voyages_list:
            all_voyages_list = []
            with open(VoyageData.__voyage_data_filename, 'r') as file_stream:
                reader = csv.DictReader(file_stream)
                for row in reader:

                    flight1_departure_location = row["flight1_departure_location"]
                    flight1_departure_time = row["flight1_departure_time"]
                    flight2_departure_location = row["flight2_departure_location"]
                    flight2_departure_time = row["flight2_departure_time"]


                    pilots_list = VoyageData.__get_employees("captain", "copilot", row)

                    flight_attendants_list = VoyageData.__get_employees("cabin_manager", "flight_attendant", row)

                    airplane_name = row["airplane_name"]

                    schedule = row["schedule"].split("_")

                    state = row["state"]

                    all_voyages_list.append(Voyage((flight1_departure_location, flight1_departure_time,\
                         flight2_departure_location, flight2_departure_time),\
                         pilots_list, flight_attendants_list, airplane_name, (schedule[0], schedule[1]), state))

                VoyageData.__all_voyages_list = all_voyages_list

            return VoyageData.__all_voyages_list

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

            for pilot in voyage.get_pilots():
                pilots_ssn_list.append(pilot.get_ssn())

            while len(pilots_ssn_list < VoyageData.__max_pilots_onboard):
                pilots_ssn_list.append("")

            flight_attendants_ssn_list = []

            for flight_attendant in voyage.get_flight_attendants():
                flight_attendant.append(flight_attendant)

            while len(flight_attendants_ssn_list < VoyageData.__max_flight_attendants_on_board):
                flight_attendants_ssn_list.append("")

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
                 "schedule": voyage.get_schedule(),
                 "state": voyage.get_state()
                 })

        if VoyageData.__all_voyages_list:
            VoyageData.__all_voyages_list.append(voyage)
