from data_models.aircraft_type import AircraftType

class AircraftTypeData:

    __aircraft_data_filename = "../data_storage/aircraft_types.csv"
    __all_aircrafts_list = []

    @staticmethod
    def get_all_aircraft_types():
        all_aircrafts_list = []

        if not AircraftData.__all_aircrafts_list:
            with open(AircraftsData.__aircrafts_data_filename, 'r') as file_stream:
                reader = csv.DictReader(file_stream)
                for row in reader:
                    all_aircrafts_list.append(AircraftType(row["plane_type"], row["model"],\
                        row["capacity"], row["empty_weight"], row["max_takeoff_weight"],\
                        row["unit_thrust"], row["service_ceiling"], row["length"], row["height"],\
                        row["wingspan"]))
            AircraftTypeData.__all_aircrafts_list = all_aircrafts_list

        return AircraftTypeData.__all_aircrafts_list
        
        