from data_models.aircraft_type import AircraftType
from apis.data_api import DataAPI

class AircraftTypeLogic:

    @staticmethod
    def __sort_list_by_plane_type(a_list):
        '''Returns a new list sorted in alphabetical plane type order, returns [] if the list was empty'''
        return a_list if not a_list else sorted(a_list, key=lambda value: value.get_plane_type())

    @staticmethod
    def get_all_aircraft_types():
        return AircraftTypeLogic.__sort_list_by_plane_type(DataAPI.get_all_aircraft_types())

    @staticmethod
    def get_aircraft_type(plane_type):
        '''Returns an aircraft type with the given plane type,
           returns None if no such type is found'''
        return DataAPI.get_aircraft_type(plane_type)

    @staticmethod
    def save_new_aircraft_type(aircraft_type):
        DataAPI.save_new_aircraft_type(aircraft_type)
