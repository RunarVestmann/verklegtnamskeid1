from data_models.employee import Employee
from apis.data_api import DataAPI

class EmployeeLogic:

    @staticmethod
    def get_all_employees():
        return DataAPI.get_all_employees()

    @staticmethod
    def get_employees_on_duty(Employee):
        all_employees = DataAPI.get_all_employees()
        employees_on_duty = []
        for employee in all_employees:
            if employee.get_state() != "Not scheduled for flight today":
                employees_on_duty.append(employee)                
            
        return employees_on_duty

    @staticmethod
    def get_employees_off_duty(Employee):
        all_employees = DataAPI.get_all_employees()
        employees_off_duty = []
        for employee in all_employees:
            if employee.get_state() == "Not scheduled for flight today":
                employees_off_duty.append(employee)                
            
        return employees_off_duty
