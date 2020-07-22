import os
import platform
import csv
import dateutil.parser as util
from data_models.flight import Flight

class FlightData:

    #Store the filename path
    __flight_data_filename = os.path.realpath("../data_storage/flights.csv")

    #A list to cache all the flights once they've been fetched
    __all_flights_list = []

    @staticmethod
    def get_all_flights():
        if not FlightData.__all_flights_list:
            all_flights_list = []
            with open(FlightData.__flight_data_filename, 'r', encoding="utf8") as file_stream:
                reader = csv.DictReader(file_stream)
                for row in reader:
                    #Append to the list and change the times to be of type datetime with util.parse()
                    all_flights_list.append(Flight(row["departure_location"], util.parse(row["departure_time"]),\
                        row["arrival_location"], util.parse(row["arrival_time"]), row["number"]))

            FlightData.__all_flights_list = all_flights_list

        return FlightData.__all_flights_list

    @staticmethod
    def get_flight(departure_location, departure_time):
        all_flights_list = FlightData.get_all_flights()

        for flight in all_flights_list:
            if flight.get_departure_location() == departure_location and\
                flight.get_departure_time() == departure_time:
                return flight

        return None

    @staticmethod
    def change_saved_flight(saved_flight, changed_flight):
        updated_list_of_flights = []

        for flight in FlightData.get_all_flights():

            if flight == saved_flight:
                updated_list_of_flights.append(changed_flight)
            else:
                updated_list_of_flights.append(flight)

        FlightData.__overwrite_all_flights(updated_list_of_flights)

    @staticmethod
    def __overwrite_all_flights(flights):
        field_names = ["departure_location", "departure_time", "arrival_location", "arrival_time", "number"]
        FlightData.__all_flights_list = []
        with open(FlightData.__flight_data_filename, 'w', encoding="utf8") as file_stream:
            writer = csv.DictWriter(file_stream, fieldnames=field_names, lineterminator='\n')
            writer.writeheader()
            for flight in flights:
                FlightData.__all_flights_list.append(flight)
                writer.writerow({
                    "departure_location": flight.get_departure_location(),
                    "departure_time": flight.get_departure_time().isoformat(),
                    "arrival_location": flight.get_arrival_location(),
                    "arrival_time": flight.get_arrival_time().isoformat(),
                    "number": flight.get_number()
                    })


    @staticmethod
    def save_new_flight(flight):
        field_names = ["departure_location", "departure_time", "arrival_location", "arrival_time", "number"]
        with open(FlightData.__flight_data_filename, 'a', encoding="utf8") as file_stream:
            writer = csv.DictWriter(file_stream, fieldnames=field_names, lineterminator='\n')

            writer.writerow({"departure_location": flight.get_departure_location(),
                 "departure_time": flight.get_departure_time().isoformat(),
                 "arrival_location": flight.get_arrival_location(),
                 "arrival_time": flight.get_arrival_time().isoformat(),
                 "number": flight.get_number()})

        if FlightData.__all_flights_list:
            FlightData.__all_flights_list.append(flight)
