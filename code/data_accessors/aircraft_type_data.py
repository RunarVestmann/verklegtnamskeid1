import csv
from data_models.aircraft_type import AircraftType


class AircraftTypeData:

    __aircraft_data_filename = "../data_storage/aircraft_types.csv"
    __all_aircrafts_list = []

    @staticmethod
    def get_all_aircraft_types():
        all_aircrafts_list = []

        if not AircraftTypeData.__all_aircrafts_list:
            with open(AircraftTypeData.__aircraft_data_filename, 'r') as file_stream:
                reader = csv.DictReader(file_stream)
                for row in reader:
                    all_aircrafts_list.append(AircraftType(row["plane_type"], row["model"],\
                        row["capacity"], row["empty_weight"], row["max_takeoff_weight"],\
                        row["unit_thrust"], row["service_ceiling"], row["length"], row["height"],\
                        row["wingspan"]))
            AircraftTypeData.__all_aircrafts_list = all_aircrafts_list

        return AircraftTypeData.__all_aircrafts_list

    @staticmethod
    def save_new_aircraft(aircraft):
        field_names = ["plane_type", "model", "capacity", "empty_weight", "max_takeoff_weight",\
            "unit_thrust","service_ceiling","length","height","wingspan"]
        with open(AircraftTypeData.__aircraft_data_filename, 'a') as file_stream:
            writer = csv.DictWriter(file_stream, fieldnames=field_names)

            writer.writerow({
                "plane_type": aircraft.get_plane_type(),
                "model": aircraft.get_model(),
                "capacity": aircraft.get_capacity(),
                "empty_weight": aircraft.get_empty_weight(),
                "max_takeoff_weight": aircraft.get_max_takeoff_weight(),
                "unit_thrust": aircraft.get_unit_thrust(),
                "service_ceiling": aircraft.get_service_ceiling(),
                "length": aircraft.get_length(),
                "height": aircraft.get_height(),
                "wingspan": aircraft.get_wingspan()})

        if AircraftTypeData.__all_aircrafts_list:
            AircraftTypeData.__all_aircrafts_list.append(aircraft)
        