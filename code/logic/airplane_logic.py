from data_models.airplanes import Airplane
from data_models.voyage import Voyage
from apis.data_api import DataAPI

class AirplaneLogic:

    @staticmethod
    def save_new_airplane(airplane):
        DataAPI.save_new_airplane(airplane)

    @staticmethod
    def get_all_airplanes():
        return DataAPI.get_all_airplanes()

    @staticmethod
    def get_all_available_airplanes(schedule_tuple): # needs testing
        all_airplanes = DataAPI.get_all_airplanes()
        available_airplanes = []
        for airplane in all_airplanes:
            voyages = DataAPI.get_airplanes_voyages(airplane)

            # if there are no voyages for specific airplane then it is available
            if not voyages:
                available_airplanes.append(airplane)

            else:
                for voyage in voyages:
                    voyage_schedule = voyage.get_voyage_schedule()
                    if schedule_tuple [0] > voyage_schedule [1] or schedule_tuple [1] < voyage_schedule [0]:
                        available_airplanes.append(airplane)
        return available_airplanes