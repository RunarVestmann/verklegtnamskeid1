from data_models.flight import Flight
import csv

class FlightData:

    __flight_data_filename = "../data_storage/flights.csv"
    __all_flights_list = []

    @staticmethod
    def get_all_flights():
        if not FlightData.__all_flights_list:
            all_flights_list = []
            with open(FlightData.__flight_data_filename, 'r') as file_stream:
                reader = csv.DictReader(file_stream)
                for row in reader:
                    all_flights_list.append(Flight(row["departure_location"], row["departure_time"],\
                        row["arrival_location"], row["arrival_time"], row["number"]))

            FlightData.__all_flights_list = all_flights_list

        return FlightData.__all_flights_list

    @staticmethod
    def save_new_flight(flight):
        field_names = ["departure_location", "departure_time", "arrival_location", "arrival_time", "number"]
        with open(FlightData.__flight_data_filename, 'a') as file_stream:
            writer = csv.DictWriter(file_stream, fieldnames=field_names)

            writer.writerow({"departure_location": flight.get_departure_location(),\
                 "departure_time": flight.get_departure_time(),\
                 "arrival_location": flight.get_arrival_location(),\
                 "number": flight.get_numger()})

        if FlightData.__all_flights_list:
            FlightData.__all_flights_list.append(flight)

