from data_models.employee import Employee
from data_models.state import State
from apis.data_api import DataAPI

class EmployeeLogic:

    @staticmethod
    def get_all_employees():
        return DataAPI.get_all_employees()

    @staticmethod
    def get_employees_on_duty():
        all_employees = DataAPI.get_all_employees()
        not_scheduled_state = State.get_employee_states()[0]
        employees_on_duty = []
        for employee in all_employees:
            if employee.get_state() != not_scheduled_state:
                employees_on_duty.append(employee)

        return employees_on_duty

    @staticmethod
    def get_employees_off_duty():
        all_employees = DataAPI.get_all_employees()
        not_scheduled_state = State.get_employee_states()[0]
        employees_off_duty = []
        for employee in all_employees:
            if employee.get_state() == not_scheduled_state:
                employees_off_duty.append(employee)

        return employees_off_duty
