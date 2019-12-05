from user_interface.window import Window
from user_interface.component_ui import ComponentUI
from user_interface.text_editor import TextEditor


class EmployeeUI:
    #Generate a tuple that holds all the valid user inputs
    __option_tuple = ('New employees', 'Show all employees', 'Show all pilots', 'Show all flight attendants', 'Find employee by name',\
                       'Find pilots by license', 'Show employees on duty', 'Show employees off duty')
    

    @staticmethod
    def show_employee_menu():
        ComponentUI.print_header(ComponentUI.get_main_options()[1])
        option_tuple = EmployeeUI.__option_tuple
        print()
        for i, option in enumerate(option_tuple):
            print("({}) {}".format(i+1, option))
        ComponentUI.fill_window_and_print_action_line(len(option_tuple)+1)
    
     
    @staticmethod
    def action_employees_menu(user_input):
        option_tuple = EmployeeUI.__option_tuple  
        option_functions = (EmployeeUI.show_new_employee_constructor, EmployeeUI.show_all_employees, EmployeeUI.show_all_pilots, EmployeeUI.show_all_flight_attendants, EmployeeUI.show_employee_by_name_finder, EmployeeUI.show_pilot_by_license_finder, EmployeeUI.show_employees_on_duty, EmployeeUI.show_employees_off_duty)

       #####  Test input ####            
        selected_number = ComponentUI.test_user_input_chose_index(user_input, len(option_tuple)) #eather int>0 or False - may not be 0
        if selected_number:                                                                      #and is with in range of possible menu list
            selected_index = selected_number-1
            return option_functions[selected_index]
        else:
            return False
              



    DUMMYNMBR=1
    @staticmethod
    def show_new_employee_constructor():
        ComponentUI.print_header(ComponentUI.get_main_options()[1])
        print(TextEditor.format_text(EmployeeUI.__option_tuple[0], TextEditor.UNDERLINE_TEXT))
        ComponentUI.fill_window_and_print_action_line(EmployeeUI.DUMMYNMBR, False)
        pass

    @staticmethod
    def show_all_employees():
        ComponentUI.print_header(ComponentUI.get_main_options()[1])
        print(TextEditor.format_text(EmployeeUI.__option_tuple[1], TextEditor.UNDERLINE_TEXT))
        ComponentUI.fill_window_and_print_action_line(EmployeeUI.DUMMYNMBR, False)
        pass

    @staticmethod
    def show_all_pilots():
        ComponentUI.print_header(ComponentUI.get_main_options()[1])
        print(TextEditor.format_text(EmployeeUI.__option_tuple[2], TextEditor.UNDERLINE_TEXT))
        ComponentUI.fill_window_and_print_action_line(EmployeeUI.DUMMYNMBR, False)
        pass

    @staticmethod
    def show_all_flight_attendants():
        ComponentUI.print_header(ComponentUI.get_main_options()[1])
        print(TextEditor.format_text(EmployeeUI.__option_tuple[3], TextEditor.UNDERLINE_TEXT))
        ComponentUI.fill_window_and_print_action_line(EmployeeUI.DUMMYNMBR, False)
        pass

    @staticmethod
    def show_employee_by_name_finder():
        ComponentUI.print_header(ComponentUI.get_main_options()[1])
        print(TextEditor.format_text(EmployeeUI.__option_tuple[4], TextEditor.UNDERLINE_TEXT))
        ComponentUI.fill_window_and_print_action_line(EmployeeUI.DUMMYNMBR, False)
        pass

    @staticmethod
    def show_pilot_by_license_finder():
        ComponentUI.print_header(ComponentUI.get_main_options()[1])
        print(TextEditor.format_text(EmployeeUI.__option_tuple[5], TextEditor.UNDERLINE_TEXT))
        ComponentUI.fill_window_and_print_action_line(EmployeeUI.DUMMYNMBR, False)
        pass

    @staticmethod
    def show_employees_on_duty():
        ComponentUI.print_header(ComponentUI.get_main_options()[1])
        print(TextEditor.format_text(EmployeeUI.__option_tuple[6], TextEditor.UNDERLINE_TEXT))
        ComponentUI.fill_window_and_print_action_line(EmployeeUI.DUMMYNMBR, False)
        pass

    @staticmethod
    def show_employees_off_duty():
        ComponentUI.print_header(ComponentUI.get_main_options()[1])
        print(TextEditor.format_text(EmployeeUI.__option_tuple[7], TextEditor.UNDERLINE_TEXT))
        ComponentUI.fill_window_and_print_action_line(EmployeeUI.DUMMYNMBR, False)
        pass
