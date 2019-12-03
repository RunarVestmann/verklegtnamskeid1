from user_interface.menu_ui import MenuUI
from user_interface.window import Window

class EmployeeUI:
 
    @staticmethod
    def show_employee_menu():
        MenuUI.print_header(MenuUI.get_main_options()[1])
        option_list = ('New employees', 'Show all employees', 'Show all pilots', 'Show all flight attendants', 'Find employee by name', 'Find pilots by license', 'Show employees on duty', 'Show employees off duty')
        print()
        for i, option in enumerate(option_list):
            print("({}) {}".format(i+1,option))
        MenuUI.fill_window_and_print_action_line(len(option_list)+1)
        user_input = input("Your action: ").lower().strip()

        if user_input == '1' or user_input == '(1)':
            EmployeeUI.show_new_employee_constructor(option_list[0])

        elif user_input == '2' or user_input == '(2)':
            EmployeeUI.show_all_employees(option_list[1])

        elif user_input == '3' or user_input == '(3)':
            EmployeeUI.show_all_pilots(option_list[2])

        elif user_input == '4' or user_input == '(4)':
            EmployeeUI.show_all_flight_attendants(option_list[3])
        
        if user_input == '5' or user_input == '(5)':
            EmployeeUI.show_employee_by_name_finder(option_list[4])

        elif user_input == '6' or user_input == '(6)':
            EmployeeUI.show_pilot_by_license_finder(option_list[5])

        elif user_input == '7' or user_input == '(7)':
            EmployeeUI.show_employees_on_duty(option_list[6])

        elif user_input == '8' or user_input == '(8)':
            EmployeeUI.show_employees_off_duty(option_list[7])

        else:
            EmployeeUI.show_employee_menu()
              
    @staticmethod
    def show_new_employee_constructor(title):
        pass

    @staticmethod
    def show_all_employees(title):
        pass

    @staticmethod
    def show_all_pilots(title):
        pass

    @staticmethod
    def show_all_flight_attendants(title):
        pass

    @staticmethod
    def show_employee_by_name_finder(title):
        pass

    @staticmethod
    def show_pilot_by_license_finder(title):
        pass

    @staticmethod
    def show_employees_on_duty(title):
        pass

    @staticmethod
    def show_employees_off_duty(title):
        pass
    
