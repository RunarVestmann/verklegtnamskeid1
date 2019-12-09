from user_interface.window import Window
from user_interface.component_ui import ComponentUI
from user_interface.text_editor import TextEditor
from data_models.flight_attendant import FlightAttendant
from apis.logic_api import LogicAPI
from data_models.pilot import Pilot

class EmployeeUI:
    #Generate a tuple that holds all the valid user inputs
    __option_tuple = ('New employees', 'Show all employees', 'Show all pilots', 'Show all flight attendants', 'Find employee by name or ssn',\
                       'Find pilots by license', 'Show employees on duty', 'Show employees off duty')
    
    __FRAME_IN_USE_STR = ComponentUI.get_main_options()[1]
    @staticmethod
    def show():
        
        valid_user_inputs = ComponentUI.make_valid_menu_options_tuple(len(EmployeeUI.__option_tuple))

        frame_functions = (EmployeeUI.__show_new_employee_constructor, EmployeeUI.__show_all_employees, EmployeeUI.__show_all_pilots,\
            EmployeeUI.__show_all_flight_attendants, EmployeeUI.__show_employee_by_name_finder, EmployeeUI.__show_pilot_by_license_finder,\
                EmployeeUI.__show_employees_on_duty, EmployeeUI.__show_employees_off_duty)

        return ComponentUI.run_frame(EmployeeUI.__option_tuple, EmployeeUI.__FRAME_IN_USE_STR, valid_user_inputs, frame_functions)
    
    @staticmethod
    def __show_new_employee_constructor():
        input_message_tuple = ("Insert job title('f' for flight attendant, 'p' for pilot): ", "Insert Name: ", "Insert Social security number: ",\
            "Insert Phone number: ", "Insert Home address: ", "Insert E-mail: ", "Insert License: ")
        user_input = ""
        navigation_bar_options = ComponentUI.get_navigation_options_tuple()
        option_tuple = ("Job title", "Name", "Social security number", "Phone number", "Home address", "E-mail", "License")
        user_input_list = [""] * len(option_tuple)
        valid_user_inputs = ComponentUI.make_valid_menu_options_tuple(len(option_tuple))
        employee_info_already_exists = False
        while user_input not in navigation_bar_options:

            greyed_out_option_index = [6] if not user_input_list[0].lower().startswith('p') else [1000]

            ComponentUI.print_frame_constructor_menu(option_tuple, EmployeeUI.__FRAME_IN_USE_STR, "New employeee",\
            user_input_list, True, greyed_out_option_index_list=greyed_out_option_index)
            user_input = ComponentUI.get_user_input()
            
            
            if not user_input:
                continue
            user_input = ComponentUI.remove_brackets(user_input)
            
            
            if user_input in valid_user_inputs:

                index = int(user_input) - 1

                if index == 6:
                    if not user_input_list[0].lower().startswith('p'):
                        continue


                ComponentUI.print_frame_constructor_menu(option_tuple, EmployeeUI.__FRAME_IN_USE_STR, "New employeee",\
                user_input_list, False, index)

                user_input = input(input_message_tuple[index]).strip()
                if not user_input:
                    continue

                if index == 0:

                    if user_input.lower().startswith('f'):
                        user_input = "Flight attendant"
                        user_input_list[6] = ""
                    elif user_input.lower().startswith('p'):
                        user_input = "Pilot"

                    if not user_input.lower().startswith("f") and not user_input.lower().startswith("p"):
                        employee_info_already_exists = True
                        user_input = user_input + " " + TextEditor.color_text_background("Please insert 'f' or 'p', another input is required", TextEditor.RED_BACKGROUND)
                    else:
                        employee_info_already_exists = False

                elif index == 1:
                    contact_name_list = []
                    for name in user_input.split():
                        contact_name_list.append(name.capitalize())
                    user_input = " ".join(contact_name_list)

                elif index == 2 or index == 3:

                    if '-' in user_input:
                        user_input = user_input.replace('-', '')
                    if '' in user_input:
                        user_input = user_input.replace(' ', '')
                    
                    if not user_input.isdigit():
                        user_input = user_input + " " + TextEditor.color_text_background("Can not contain letters, another input is required", TextEditor.RED_BACKGROUND)
                        employee_info_already_exists = True
                    else:
                        employee_info_already_exists = False

                #Email error check
                elif index == 5:
                    if "@" not in user_input and "." not in user_input and len(user_input) < 5:
                        employee_info_already_exists = True
                        user_input = user_input + " " + TextEditor.color_text_background("Invalid e-mail, another input is required", TextEditor.RED_BACKGROUND)

                user_input_list[index] = user_input
                user_input = ""

            elif user_input.startswith('s'):
                job_title_str = user_input_list[0].lower()

                if all(user_input_list) and job_title_str.startswith('p') and not employee_info_already_exists:
                    
                    pilot = Pilot(
                        user_input_list[1],
                        user_input_list[2],
                        user_input_list[3],
                        user_input_list[4],
                        user_input_list[5],
                        "Not scheduled for flight",
                        user_input_list[6]
                    )
                    LogicAPI.save_new_pilot(pilot)

                    user_input = "A new pilot has been registered"

                    break
                
                elif all(user_input_list[:-1]) and job_title_str.startswith('f') and not employee_info_already_exists:

                    flight_attendant = FlightAttendant(
                        user_input_list[1],
                        user_input_list[2],
                        user_input_list[3],
                        user_input_list[4],
                        user_input_list[5],
                        "Not scheduled for flight"
                    )
                    LogicAPI.save_new_flight_attendant(flight_attendant)

                    user_input = "A new flight attendant has been registered"

                    break


        return user_input


    @staticmethod
    def __show_all_employees():
        ComponentUI.print_header(EmployeeUI.__FRAME_IN_USE_STR)
        print(TextEditor.format_text("Show all employees", TextEditor.UNDERLINE_TEXT))
        
        table_header = ("Job title", "Name", "SSN", "Phone number", "Home address", "E-mail", "State")
        all_employees = LogicAPI.get_all_employees()
        employees_getfunctions_tuple = (["Pilot" if isinstance(employee, Pilot) else "Flight attendant" for employee in all_employees], [employee.get_name() for employee in all_employees],[employee.get_ssn() for employee in all_employees],\
            [employee.get_phonenumber() for employee in all_employees],[employee.get_home_address() for employee in all_employees],[employee.get_email() for employee in all_employees],\
                [employee.get_state() for employee in all_employees])

        ComponentUI.fill_in_table(table_header,employees_getfunctions_tuple, False)
                 
        ComponentUI.fill_window_and_print_action_line(len(all_employees)+2)

        return ComponentUI.get_user_input()

    @staticmethod
    def __show_all_pilots():
        ComponentUI.print_header(EmployeeUI. __FRAME_IN_USE_STR)
        print(TextEditor.format_text("All pilots", TextEditor.UNDERLINE_TEXT))
 
        table_header_tuple = ("Name", "SSN", "Phone number", "Home address", "E-mail", "State", "License")
        pilots_list = LogicAPI.get_all_pilots()
        pilots_value_list = ([pilot.get_name() for pilot in pilots_list],[pilot.get_ssn() for pilot in pilots_list],\
           [pilot.get_phonenumber() for pilot in pilots_list], [pilot.get_home_address() for pilot in pilots_list],\
           [pilot.get_email() for pilot in pilots_list], [pilot.get_state() for pilot in pilots_list], [pilot.get_license() for pilot in pilots_list])

        ComponentUI.print_table(table_header_tuple,pilots_value_list)

        return ComponentUI.get_user_input()

    @staticmethod
    def __show_all_flight_attendants():
        ComponentUI.print_header(EmployeeUI. __FRAME_IN_USE_STR)
        print(TextEditor.format_text("All flight attendants", TextEditor.UNDERLINE_TEXT))
 
        table_header_tuple = ("Name", "SSN", "Phone number", "Home address", "E-mail", "State")
        flight_attendants_list = LogicAPI.get_all_flight_attendants()
        flight_attendants_value_tuple = ([flight_attendant.get_name() for flight_attendant in flight_attendants_list],[flight_attendant.get_ssn() for flight_attendant in flight_attendants_list],\
           [flight_attendant.get_phonenumber() for flight_attendant in flight_attendants_list], [flight_attendant.get_home_address() for flight_attendant in flight_attendants_list],\
           [flight_attendant.get_email() for flight_attendant in flight_attendants_list], [flight_attendant.get_state() for flight_attendant in flight_attendants_list])

        ComponentUI.print_table(table_header_tuple,flight_attendants_value_tuple)

        return ComponentUI.get_user_input()


    @staticmethod
    def __show_employee_by_name_finder():

        navigation_bar_options = ComponentUI.get_navigation_options_tuple()

        user_input = ""

        info_header_tuple = ("Job title", "Name", "SSN", "Phone number", "Home address", "E-mail", "State")

        input_message = "Invalid input"

        invalid_input = False

        while user_input not in navigation_bar_options:
            ComponentUI.print_header(EmployeeUI. __FRAME_IN_USE_STR)
            print(TextEditor.format_text("Find employee by name or ssn", TextEditor.UNDERLINE_TEXT))

            ComponentUI.fill_window_and_print_action_line(1)

            user_input = input(TextEditor.color_text_background("Insert name or ssn: ") if invalid_input else "Insert name or ssn: ").strip()

            employees = []

            if not user_input:
                continue

            #If he enters  a digit
            if user_input.isdigit():
                if '-' in user_input:
                    user_input = user_input.replace('-', '')
                if '' in user_input:
                    user_input = user_input.replace(' ', '')

                employees = LogicAPI.get_employee_by_ssn(user_input)

                ComponentUI.print_header(EmployeeUI.__FRAME_IN_USE_STR)
                print(TextEditor.format_text("Find employee by name or ssn", TextEditor.UNDERLINE_TEXT))

                if not employees:
                    ComponentUI.centered_text_message("No employee found with the ssn: {}".format(user_input))

                    return ComponentUI.get_user_input()

                else:
                    
                    employee_info_tuple =  (["Pilot" if isinstance(employee, Pilot) else "Flight attendant" for employee in employees], [employee.get_name() for employee in employees],[employee.get_ssn() for employee in employees],\
                        [employee.get_phonenumber() for employee in employees],[employee.get_home_address() for employee in employees],[employee.get_email() for employee in employees],\
                        [employee.get_state() for employee in employees])                    

                    ComponentUI.print_frame_table_menu(info_header_tuple,employee_info_tuple, len(employee_info_tuple[0]),  EmployeeUI.__FRAME_IN_USE_STR, "Find employee by name or ssn")
                    break
            else:
                name_list = []
                for name in user_input.split():
                    name_list.append(name.capitalize())

                user_input = " ".join(name_list)


                employees = LogicAPI.get_employee_by_name(user_input)

                ComponentUI.print_header(EmployeeUI. __FRAME_IN_USE_STR)
                print(TextEditor.format_text("Find employee by name or ssn", TextEditor.UNDERLINE_TEXT))

                if not employees:
                    
                    ComponentUI.centered_text_message("Could not find an employee named {}".format(user_input))
                
                    return ComponentUI.get_user_input()

                else: 
                    employee_info_tuple = (["Pilot" if isinstance(employee, Pilot) else "Flight attendant" for employee in employees], [employee.get_name() for employee in employees],[employee.get_ssn() for employee in employees],\
                    [employee.get_phonenumber() for employee in employees],[employee.get_home_address() for employee in employees],[employee.get_email() for employee in employees],\
                    [employee.get_state() for employee in employees])

                ComponentUI.print_frame_table_menu(info_header_tuple,employee_info_tuple, len(employee_info_tuple[0]),  EmployeeUI.__FRAME_IN_USE_STR, "Find employee by name or ssn")
                
                break #Needs more 


        return ComponentUI.get_user_input()

    @staticmethod
    def __show_pilot_by_license_finder():
        pass
        

    @staticmethod
    def __show_employees_on_duty():
        # ComponentUI.print_header(EmployeeUI. __FRAME_IN_USE_STR)
        # print(TextEditor.format_text("All employees on duty", TextEditor.UNDERLINE_TEXT))
 
        table_header_tuple = ("Name", "SSN", "Phone number", "Home address", "E-mail", "State")
        employees_on_duty_list = LogicAPI.get_employees_on_duty()
        employees_on_duty_value_tuple = ([employees_on_duty.get_name() for employees_on_duty in employees_on_duty_list],[employees_on_duty.get_ssn() for employees_on_duty in employees_on_duty_list],\
           [employees_on_duty.get_phonenumber() for employees_on_duty in employees_on_duty_list], [employees_on_duty.get_home_address() for employees_on_duty in employees_on_duty_list],\
           [employees_on_duty.get_email() for employees_on_duty in employees_on_duty_list], [employees_on_duty.get_state() for employees_on_duty in employees_on_duty_list])

        if not employees_on_duty_list:
            ComponentUI.centered_text_message("No employee is on duty at the moment")
        else:
            ComponentUI.print_frame_table_menu(table_header_tuple, employees_on_duty_value_tuple, len(employees_on_duty_value_tuple[0]),\
                EmployeeUI. __FRAME_IN_USE_STR, "All employees on duty")
        return ComponentUI.get_user_input()

    @staticmethod
    def __show_employees_off_duty():
        ComponentUI.print_header(ComponentUI.get_main_options()[1])
        ComponentUI.print_header(EmployeeUI. __FRAME_IN_USE_STR)
        print(TextEditor.format_text("All employees off duty", TextEditor.UNDERLINE_TEXT))
 
        table_header_tuple = ("Name", "SSN", "Phone number", "Home address", "E-mail", "State")
        employees_off_duty_list = LogicAPI.get_employees_off_duty()
        

        employees_off_duty_value_tuple = ([employees_off_duty.get_name() for employees_off_duty in employees_off_duty_list],[employees_off_duty.get_ssn() for employees_off_duty in employees_off_duty_list],\
           [employees_off_duty.get_phonenumber() for employees_off_duty in employees_off_duty_list], [employees_off_duty.get_home_address() for employees_off_duty in employees_off_duty_list],\
           [employees_off_duty.get_email() for employees_off_duty in employees_off_duty_list], [employees_off_duty.get_state() for employees_off_duty in employees_off_duty_list])
        if not employees_off_duty_list:
            ComponentUI.centered_text_message("No employee is off duty at the moment")
        else:
            ComponentUI.print_table(table_header_tuple,employees_off_duty_value_tuple)

        return ComponentUI.get_user_input()
