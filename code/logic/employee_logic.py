from data_models.employee import Employee
from apis.data_api import DataAPI

class EmployeeLogic:

    def get_all_employees(self):
        return DataAPI.get_all_employees()

    def get_employees_on_duty(self):
        return []

    def get_employees_off_duty(self):
        return []
