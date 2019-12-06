from data_models.airplane import Airplane
from data_models.voyage import Voyage
from logic.aircraft_type_logic import AircraftTypeLogic
from apis.data_api import DataAPI

class AirplaneLogic:

    @staticmethod
    def save_new_airplane(airplane):
        DataAPI.save_new_airplane(airplane)

    @staticmethod
    def get_all_airplanes(): #needs testing
        all_airplanes_with_limited_data = DataAPI.get_all_airplanes()

        all_airplanes = []

        for airplane in all_airplanes_with_limited_data:
            aircraft_type = AircraftTypeLogic.get_aircraft_type(airplane.get_type())

            all_airplanes.append(Airplane(airplane.get_name(), aircraft_type, airplane.get_manufacturer,\
                airplane.get_seat_count(), airplane.get_state()))

        return all_airplanes

    @staticmethod
    def get_airplane(name):
        all_airplanes = DataAPI.get_all_airplanes()
        for airplane in all_airplanes:
            if airplane.get_name() == name:
                return airplane

        return None

    @staticmethod
    def get_all_available_airplanes(schedule_tuple): # needs testing
        all_airplanes = DataAPI.get_all_airplanes()
        available_airplanes = []
        for airplane in all_airplanes:
            voyages = DataAPI.get_airplane_voyages(airplane)

            # if there are no voyages for a specific airplane then it is available
            if not voyages:
                available_airplanes.append(airplane)
            
            else:
                for voyage in voyages:
                    voyage_schedule = voyage.get_schedule()
                    if schedule_tuple[0] > voyage_schedule[1] or schedule_tuple[1] < voyage_schedule[0]:
                        available_airplanes.append(airplane)
                        
        return available_airplanes