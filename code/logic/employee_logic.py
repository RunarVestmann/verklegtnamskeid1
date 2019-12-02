from data_models.employee import Employee
from apis.data_api import DataAPI

class EmployeeLogic:

    @staticmethod
    def get_all_employees():
        return DataAPI.get_all_employees()

    @staticmethod
    def get_employees_on_duty():
        return []

    @staticmethod
    def get_employees_off_duty():
        return []
