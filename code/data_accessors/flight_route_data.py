import csv
from data_models.flight_route import FlightRoute


class FlightRouteData:

    __flight_route_data_filename = "../data_storage/flight_routes.csv"
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
    def save_new_flight_attendant(flight_attendant):
        pass
