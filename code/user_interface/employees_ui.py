from user_interface.menu_ui import MenuUI
from user_interface.window import Window

class EmployeeUI:

    @staticmethod
    def __make_valid_employee_menu_options_tuple(option_count):
        '''Returns a tuple containing valid user inputs in the employee menu screen'''
        valid_user_options_list = []
        for i in range(option_count):
            valid_user_options_list.append(str(i+1))
            valid_user_options_list.append("({})".format(i+1))

        return tuple(valid_user_options_list)

    @staticmethod
    def show_employee_menu():
        option_tuple = ('New employees', 'Show all employees', 'Show all pilots', 'Show all flight attendants', 'Find employee by name',\
                       'Find pilots by license', 'Show employees on duty', 'Show employees off duty')

        #Generate a tuple that holds all the valid user inputs
        valid_user_options_tuple = EmployeeUI.__make_valid_employee_menu_options_tuple(len(option_tuple))

        user_input = ''

        #Keep displaying this menu as long as the user doesn't select anything
        while user_input not in valid_user_options_tuple:

            MenuUI.print_header(MenuUI.get_main_options()[1])

            print()
            for i, option in enumerate(option_tuple):
                print("({}) {}".format(i+1, option))
            MenuUI.fill_window_and_print_action_line(len(option_tuple)+1)

            if user_input == '1' or user_input == '(1)':
                EmployeeUI.show_new_employee_constructor(option_tuple[0])

            elif user_input == '2' or user_input == '(2)':
                EmployeeUI.show_all_employees(option_tuple[1])

            elif user_input == '3' or user_input == '(3)':
                EmployeeUI.show_all_pilots(option_tuple[2])

            elif user_input == '4' or user_input == '(4)':
                EmployeeUI.show_all_flight_attendants(option_tuple[3])

            elif user_input == '5' or user_input == '(5)':
                EmployeeUI.show_employee_by_name_finder(option_tuple[4])

            elif user_input == '6' or user_input == '(6)':
                EmployeeUI.show_pilot_by_license_finder(option_tuple[5])

            elif user_input == '7' or user_input == '(7)':
                EmployeeUI.show_employees_on_duty(option_tuple[6])

            elif user_input == '8' or user_input == '(8)':
                EmployeeUI.show_employees_off_duty(option_tuple[7])

            user_input = input("Your action: ").lower().strip()


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
