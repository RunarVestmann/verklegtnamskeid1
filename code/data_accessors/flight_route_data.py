import csv
import os
import platform
from data_models.flight_route import FlightRoute

class FlightRouteData:

    #Store the filename path
    __flight_route_data_filename = os.path.realpath("../data_storage/flight_routes.csv")

    #A list to cache all the flight routes once they've been fetched
    __all_flight_routes_list = []

    @staticmethod
    def get_all_flight_routes():
        if not FlightRouteData.__all_flight_routes_list:
            all_flight_routes_list = []
            with open(FlightRouteData.__flight_route_data_filename, 'r', encoding="utf8") as file_stream:
                reader = csv.DictReader(file_stream)
                for row in reader:
                    all_flight_routes_list.append(FlightRoute(row["country"], row["destination"],\
                        row["airport_id"], row["flight_time"], row["distance_from_iceland"], row["contact_name"], row["emergency_phone"]))
            FlightRouteData.__all_flight_routes_list = all_flight_routes_list

        return FlightRouteData.__all_flight_routes_list

    @staticmethod
    def change_saved_flight_route(saved_flight_route, changed_flight_route):
        updated_list_of_flight_routes = []

        for flight_route in FlightRouteData.get_all_flight_routes():

            if flight_route == saved_flight_route:
                updated_list_of_flight_routes.append(changed_flight_route)
            else:
                updated_list_of_flight_routes.append(flight_route)

        FlightRouteData.__overwrite_all_flight_routes(updated_list_of_flight_routes)
        
        
    @staticmethod
    def __overwrite_all_flight_routes(flight_routes):
        field_names = ["country", "destination", "airport_id", "flight_time", "distance_from_iceland", "contact_name", "emergency_phone"]
        FlightRouteData.__all_flight_routes_list = []
        with open(FlightRouteData.__flight_route_data_filename, 'w', encoding="utf8") as file_stream:
            writer = csv.DictWriter(file_stream, fieldnames=field_names, lineterminator='\n')
            writer.writeheader()
            for flight_route in flight_routes:
                FlightRouteData.__all_flight_routes_list.append(flight_route)
                writer.writerow({"country": flight_route.get_country(),
                "destination": flight_route.get_destination(),
                "airport_id": flight_route.get_airport_id(),
                "flight_time": flight_route.get_flight_time(),
                "distance_from_iceland": flight_route.get_distance_from_iceland(),
                "contact_name": flight_route.get_contact_name(),
                "emergency_phone": flight_route.get_emergency_phone()
                })

    @staticmethod
    def save_new_flight_route(flight_route):
        field_names = ["country", "destination", "airport_id", "flight_time", "distance_from_iceland", "contact_name", "emergency_phone"]
        with open(FlightRouteData.__flight_route_data_filename, 'a', encoding="utf8") as file_stream:
            writer = csv.DictWriter(file_stream, fieldnames=field_names, lineterminator='\n')

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
