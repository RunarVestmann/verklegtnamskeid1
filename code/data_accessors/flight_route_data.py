import csv
import os
import platform
from data_models.flight_route import FlightRoute


class FlightRouteData:

    #The paths we found worked for the different operating systems
    __mac_path = os.path.realpath("verklegtnamskeid1/data_storage/flight_routes.csv")
    __other_path = "../data_storage/flight_routes.csv"

    #Store the filename according to whether the user has a Mac or not
    __flight_route_data_filename = __mac_path if platform.system() == "Darwin" else __other_path

    #A list to cache all the flight routes once they've been fetched
    __all_flight_routes_list = []

    @staticmethod
    def get_all_flight_routes():
        if not FlightRouteData.__all_flight_routes_list:
            all_flight_routes_list = []
            with open(FlightRouteData.__flight_route_data_filename, 'r') as file_stream:
                reader = csv.DictReader(file_stream)
                for row in reader:
                    all_flight_routes_list.append(FlightRoute(row["country"], row["destination"],\
                        row["airport_id"], row["flight_time"], row["distance_from_iceland"], row["contact_name"], row["emergency_phone"]))
            FlightRouteData.__all_flight_routes_list = all_flight_routes_list

        return FlightRouteData.__all_flight_routes_list

    @staticmethod
    def save_new_flight_route(flight_route):
        field_names = ["country", "destination", "airport_id", "flight_time", "distance_from_iceland", "contact_name", "emergency_phone"]
        with open(FlightRouteData.__flight_route_data_filename, 'a') as file_stream:
            writer = csv.DictWriter(file_stream, fieldnames=field_names)

            writer.writerow({"country": flight_route.get_country(),
                 "destination": flight_route.get_destination(),
                 "airport_id": flight_route.get_airport_id(),
                 "flight_time": flight_route.get_flight_time(),
                 "distance_from_iceland": flight_route.get_distance_from_iceland(),
                 "contact_name": flight_route.get_contact_name(),
                 "emergency_phone": flight_route.get_emergency_phone()
                 })

        if FlightRouteData.__all_flight_routes_list:
            FlightRouteData.__all_flight_routes_list.append(flight_route)
