from data_models.employee import Employee
from data_models.state import State
from apis.data_api import DataAPI

class EmployeeLogic:

    @staticmethod
    def __sort_list_by_name(a_list):
        '''Returns a new list sorted in alphabetical name order, returns [] if the list was empty'''
        return a_list if not a_list else sorted(a_list, key=lambda value: value.get_name())

    @staticmethod
    def get_all_employees():
        return EmployeeLogic.__sort_list_by_name(DataAPI.get_all_employees())

    @staticmethod
    def get_employee_by_ssn(ssn):
        all_employees = DataAPI.get_all_employees()

        for employee in all_employees:
            if employee.get_ssn() == ssn:
                return [employee]

        return []

    @staticmethod
    def get_employee_by_name(name):
        all_employees = DataAPI.get_all_employees()

        employees_with_name = []

        for employee in all_employees:
            if name in employee.get_name():
                employees_with_name.append(employee)

        return employees_with_name

    @staticmethod
    def get_employees_on_duty():
        all_employees = DataAPI.get_all_employees()
        not_scheduled_state = State.get_employee_states()[0]
        employees_on_duty = []
        for employee in all_employees:
            if employee.get_state() != not_scheduled_state:
                employees_on_duty.append(employee)

        return EmployeeLogic.__sort_list_by_name(employees_on_duty)

    @staticmethod
    def get_employees_off_duty():
        all_employees = DataAPI.get_all_employees()
        not_scheduled_state = State.get_employee_states()[0]
        employees_off_duty = []
        for employee in all_employees:
            if employee.get_state() == not_scheduled_state:
                employees_off_duty.append(employee)

        return EmployeeLogic.__sort_list_by_name(employees_off_duty)
