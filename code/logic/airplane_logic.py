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
        return DataAPI.get_all_airplanes()

    @staticmethod
    def get_airplane(name):
        return DataAPI.get_airplane(name)

    @staticmethod
    def is_airplane_name_available(plane_name):
        all_airplanes = DataAPI.get_all_airplanes()
        for airplane in all_airplanes:
            if airplane.get_name() == plane_name:
                return False

        return True

    @staticmethod
    def get_all_available_airplanes(schedule_tuple): # needs testing
        available_airplanes = []
        for airplane in DataAPI.get_all_airplanes():
            airplanes_voyages = DataAPI.get_airplane_voyages(airplane)

            # if there are no voyages for a specific airplane then it is available
            if not airplanes_voyages:
                available_airplanes.append(airplane)

            else:
                for voyage in airplanes_voyages:
                    voyage_schedule = voyage.get_schedule()
                    if schedule_tuple[0] > voyage_schedule[1] or schedule_tuple[1] < voyage_schedule[0]:
                        available_airplanes.append(airplane)

        return available_airplanes
