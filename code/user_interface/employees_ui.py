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
        option_functions = (EmployeeUI.show_new_employee_constructor, EmployeeUI.show_all_employees, EmployeeUI.show_all_pilots, EmployeeUI.show_all_flight_attendants, EmployeeUI.show_employee_by_name_finder, EmployeeUI.show_pilot_by_license_finder, EmployeeUI.show_employees_on_duty, EmployeeUI.show_employees_off_duty)

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
            user_input = input("Your action: ").lower().strip()

            ####  Test input ####            
            selected_number = MenuUI.test_user_input_chose_index(user_input, len(option_tuple)) #eather int>0 or False - may not be 0
            if selected_number:                                                                #and is with in range of possible menu list
                selected_index = selected_number-1
                option_functions[selected_index](option_tuple[selected_index])
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
