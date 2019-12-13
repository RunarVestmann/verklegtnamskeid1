from user_interface.window import Window
from user_interface.component_ui import ComponentUI
from user_interface.text_editor import TextEditor
from data_models.flight_attendant import FlightAttendant
from apis.logic_api import LogicAPI
from data_models.pilot import Pilot
from data_models.employee import Employee
from data_models.state import State
from user_interface.voyage_ui import VoyageUI

class EmployeeUI:
    #Generate a tuple that holds all the valid user inputs
    __option_tuple = ('New employees', 'Show all employees', 'Show all pilots', 'Show all flight attendants', 'Find employee by name or ssn',\
                       'Find pilots by license', 'Show employees on duty', 'Show employees off duty')
  
    __FRAME_IN_USE_STR = ComponentUI.get_main_options()[1]
           
    __NAVIGATION_BAR_OPTIONS = ComponentUI.get_navigation_options_tuple()

   
    @staticmethod
    def show():
        
        valid_user_inputs = ComponentUI.make_valid_menu_options_tuple(len(EmployeeUI.__option_tuple))

        frame_functions = (EmployeeUI.__show_new_employee_constructor, EmployeeUI.__show_all_employees, EmployeeUI.__show_all_pilots,\
            EmployeeUI.__show_all_flight_attendants, EmployeeUI.__show_employee_by_name_finder, EmployeeUI.__show_pilot_by_license_finder,\
                EmployeeUI.__show_employees_on_duty, EmployeeUI.__show_employees_off_duty)

        return ComponentUI.run_frame(EmployeeUI.__option_tuple, EmployeeUI.__FRAME_IN_USE_STR, valid_user_inputs, frame_functions)
    
    @staticmethod
    def __constructor_error_check(user_input, valid_user_inputs_bool_list, index, user_input_list):
        #Only accept something that starts with f or p in the input for the job title
        if index == 0:

            if user_input.lower().startswith('f'):
                user_input = "Flight attendant"
                user_input_list[6] = ""
            elif user_input.lower().startswith('p'):
                user_input = "Pilot"

            if not user_input.lower().startswith("f") and not user_input.lower().startswith("p"):
                valid_user_inputs_bool_list[index] = False
                user_input = user_input + " " + TextEditor.color_text_background("Please insert 'f' or 'p', another input is required", TextEditor.RED_BACKGROUND)
            else:
                valid_user_inputs_bool_list[index] = True

        #Capitalize the first letters of the name the user inputs
        elif index == 1:
            name_list = []
            for name in user_input.split():
                name_list.append(name.capitalize())
            user_input = " ".join(name_list)

        #Remove any '-' and whitespace from the ssn and tell the user if the input is invalid
        elif index == 2 or index == 3:

            if '-' in user_input:
                user_input = user_input.replace('-', '')
            if '' in user_input:
                user_input = user_input.replace(' ', '')
            
            if not user_input.isdigit():
                user_input = user_input + " " + TextEditor.color_text_background("Can not contain letters, another input is required", TextEditor.RED_BACKGROUND)
                valid_user_inputs_bool_list[index] = False
            elif len(user_input) < 7 and index == 3:
                user_input = user_input + " " + TextEditor.color_text_background("Must be of length 7, another input is required", TextEditor.RED_BACKGROUND)
                valid_user_inputs_bool_list[index] = False
            elif len(user_input) < 10 and index == 2:
                user_input = user_input + " " + TextEditor.color_text_background("Must be of length 10, another input is required", TextEditor.RED_BACKGROUND)
                valid_user_inputs_bool_list[index] = False
            else:
                valid_user_inputs_bool_list[index] = True

        #Check if email is at least of length 5 and contains @ and .
        elif index == 5:
            if "@" not in user_input and "." not in user_input or len(user_input) < 5:
                valid_user_inputs_bool_list[index] = False
                user_input = user_input + " " + TextEditor.color_text_background("Invalid e-mail, another input is required", TextEditor.RED_BACKGROUND)
            else:
                valid_user_inputs_bool_list[index] = True

        user_input_list[index] = user_input
        user_input = ""

        return user_input

    @staticmethod
    def __airplane_type_picker(header="License"):
    
            #### PICK AIRPLANE TYPE BY TABLE LIST ###
        table_header_tuple = ("Type", "Manufacturer", "Seats")
        
        airplane_type_list = LogicAPI.get_all_airplane_types()
        airplanes_type_getfunctions_tuple = ([aircraft_type.get_plane_type() for aircraft_type in airplane_type_list],[aircraft_type.get_manufacturer() for aircraft_type in airplane_type_list],\
            [aircraft_type.get_seat_count() for aircraft_type in airplane_type_list])
        table_height = len(airplane_type_list)


        ComponentUI.print_frame_table_menu(table_header_tuple, airplanes_type_getfunctions_tuple, table_height,\
            ComponentUI.get_main_options()[2], header)

        user_input = ComponentUI.get_user_input("Insert number of desired type: ")

        user_input = ComponentUI.remove_brackets(user_input)
        if not user_input.isdigit() or int(user_input) > table_height or not user_input:
            return None

        table_index = int(user_input) - 1
        chosen_table_line = airplane_type_list[table_index]
        ###                LINE PICKED           ##
        return chosen_table_line.get_plane_type()
    
    
    @staticmethod
    def __show_new_employee_constructor():
        input_message_tuple = ("Insert job title(" + TextEditor.format_text('f', TextEditor.BOLD_TEXT) + " for flight attendant, "\
            + TextEditor.format_text('p', TextEditor.BOLD_TEXT)+ " for pilot): ", "Insert Name: ", "Insert Social security number: ",\
            "Insert Phone number: ", "Insert Home address: ", "Insert E-mail: ", "Insert License: ")
        user_input = ""
        option_tuple = ("Job title", "Name", "Social security number", "Phone number", "Home address", "E-mail", "License")
        user_input_list = [""] * len(option_tuple)
        valid_user_inputs = ComponentUI.make_valid_menu_options_tuple(len(option_tuple))
        valid_user_inputs_bool_list = [True] * len(option_tuple)
        while user_input not in EmployeeUI.__NAVIGATION_BAR_OPTIONS:

            greyed_out_option_index_list = [6] if not user_input_list[0].lower().startswith('p') else []

            ComponentUI.print_frame_constructor_menu(option_tuple, EmployeeUI.__FRAME_IN_USE_STR, "New employeee",\
            user_input_list, True, greyed_out_option_index_list=greyed_out_option_index_list)
            user_input = ComponentUI.get_user_input()
            
            
            if not user_input:
                continue

            user_input = ComponentUI.remove_brackets(user_input)
            
            if user_input in valid_user_inputs:

                index = int(user_input) - 1

                #Don't allow the user to enter a license if the employee ain't a pilot
                if index == 6:
                    if not user_input_list[0].lower().startswith('p'):
                        continue


                ComponentUI.print_frame_constructor_menu(option_tuple, EmployeeUI.__FRAME_IN_USE_STR, "New employeee",\
                user_input_list, False, index)
                
                
                if index == 6:
                    #display table of airplane types and return the type-name the of chosen one , head above the the table
                    user_input = EmployeeUI.__airplane_type_picker("New employeee")
                else:
                    user_input = input(input_message_tuple[index]).strip()

               
                if not user_input:
                    continue

                user_input = EmployeeUI.__constructor_error_check(user_input,\
                     valid_user_inputs_bool_list, index, user_input_list)

            elif user_input.startswith('s'):
                job_title_str = user_input_list[0].lower()

                if all(user_input_list) and job_title_str.startswith('p') and all(valid_user_inputs_bool_list):
                    
                    pilot = Pilot(
                        user_input_list[1],
                        user_input_list[2],
                        user_input_list[3],
                        user_input_list[4],
                        user_input_list[5],
                        State.get_employee_states()[0],
                        user_input_list[6]
                    )
                    LogicAPI.save_new_pilot(pilot)

                    user_input = "A new pilot has been registered"

                    break
                
                elif all(user_input_list[:-1]) and job_title_str.startswith('f') and all(valid_user_inputs_bool_list[:-1]):

                    flight_attendant = FlightAttendant(
                        user_input_list[1],
                        user_input_list[2],
                        user_input_list[3],
                        user_input_list[4],
                        user_input_list[5],
                        "Not scheduled for flight to day"
                    )
                    LogicAPI.save_new_flight_attendant(flight_attendant)

                    user_input = "A new flight attendant has been registered"

                    break


        return user_input


    @staticmethod
    def __show_all_employees():
        LogicAPI.update_states() #UPDATES ALL STATES BEFOR DISPLAYING


        user_input = ""
        while user_input not in EmployeeUI.__NAVIGATION_BAR_OPTIONS:
            table_header_tuple = ("Job title", "Name", "SSN", "Phone number", "Home address", "E-mail", "State")
            all_employees_list = LogicAPI.get_all_employees()
            employees_getfunctions_tuple = (["Pilot" if isinstance(employee, Pilot) else "Flight attendant" for employee in all_employees_list], [employee.get_name() for employee in all_employees_list],[employee.get_ssn() for employee in all_employees_list],\
            [employee.get_phonenumber() for employee in all_employees_list],[employee.get_home_address() for employee in all_employees_list],[employee.get_email() for employee in all_employees_list],\
            [employee.get_state() for employee in all_employees_list])
            table_height = len(all_employees_list)
            ComponentUI.print_frame_table_menu(table_header_tuple, employees_getfunctions_tuple, table_height, EmployeeUI.__FRAME_IN_USE_STR, "All employees")
            user_input = ComponentUI.get_user_input()
            user_input = ComponentUI.remove_brackets(user_input)
            if not user_input.isdigit() or int(user_input) > table_height:
                    continue
            table_index = int(user_input)-1
            employee = all_employees_list[table_index]        

            user_input = EmployeeUI.__show_employee(employee)

        return user_input


    @staticmethod
    def __show_all_pilots():
        LogicAPI.update_states() #UPDATES ALL STATES BEFOR DISPLAYING


        user_input = ""
        while user_input not in EmployeeUI.__NAVIGATION_BAR_OPTIONS:
            table_header_tuple = ("Name", "SSN", "Phone number", "Home address", "E-mail", "State", "License")
            pilots_list = LogicAPI.get_all_pilots()
            pilots_value_tuple = ([pilot.get_name() for pilot in pilots_list],[pilot.get_ssn() for pilot in pilots_list],\
            [pilot.get_phonenumber() for pilot in pilots_list], [pilot.get_home_address() for pilot in pilots_list],\
            [pilot.get_email() for pilot in pilots_list], [pilot.get_state() for pilot in pilots_list], [pilot.get_license() for pilot in pilots_list])
            table_height = len(pilots_list)

            ComponentUI.print_frame_table_menu(table_header_tuple, pilots_value_tuple, table_height, EmployeeUI.__FRAME_IN_USE_STR, "All pilots")
            user_input = ComponentUI.get_user_input()
            user_input = ComponentUI.remove_brackets(user_input)
            if not user_input.isdigit() or int(user_input) > table_height:
                    continue
            table_index = int(user_input)-1
            pilot = pilots_list[table_index]        

            user_input = EmployeeUI.__show_employee(pilot)

        return user_input

    @staticmethod
    def __show_all_flight_attendants():
        LogicAPI.update_states() #UPDATES ALL STATES BEFOR DISPLAYING


        user_input = ""
        while user_input not in EmployeeUI.__NAVIGATION_BAR_OPTIONS:
            table_header_tuple = ("Name", "SSN", "Phone number", "Home address", "E-mail", "State")
            flight_attendants_list = LogicAPI.get_all_flight_attendants()
            flight_attendants_value_tuple = ([flight_attendant.get_name() for flight_attendant in flight_attendants_list],[flight_attendant.get_ssn() for flight_attendant in flight_attendants_list],\
            [flight_attendant.get_phonenumber() for flight_attendant in flight_attendants_list], [flight_attendant.get_home_address() for flight_attendant in flight_attendants_list],\
            [flight_attendant.get_email() for flight_attendant in flight_attendants_list], [flight_attendant.get_state() for flight_attendant in flight_attendants_list])
            table_height = len(flight_attendants_list)

            ComponentUI.print_frame_table_menu(table_header_tuple, flight_attendants_value_tuple, table_height, EmployeeUI.__FRAME_IN_USE_STR,"All flight attendants")
            user_input = ComponentUI.get_user_input()
            user_input = ComponentUI.remove_brackets(user_input)
            if not user_input.isdigit() or int(user_input) > table_height:
                    continue
            table_index = int(user_input)-1
            flight_attendant = flight_attendants_list[table_index]        

            user_input = EmployeeUI.__show_employee(flight_attendant)

        return user_input


    @staticmethod
    def __show_employee_by_name_finder():
        LogicAPI.update_states() #UPDATES ALL STATES BEFOR DISPLAYING



        user_input = ""

        info_header_tuple = ("Job title", "Name", "SSN", "Phone number", "Home address", "E-mail", "State")

        while user_input not in EmployeeUI.__NAVIGATION_BAR_OPTIONS:
            ComponentUI.print_header(EmployeeUI. __FRAME_IN_USE_STR)
            print(TextEditor.format_text("Find employee by name or ssn", TextEditor.UNDERLINE_TEXT))

            ComponentUI.fill_window_and_print_action_line(1)

            user_input = input("Insert name or ssn: ").strip()

            employees = []

            if not user_input:
                continue

            #If he enters  a digit
            if user_input.isdigit():
                if '-' in user_input:
                    user_input = user_input.replace('-', '')
                if ' ' in user_input:
                    user_input = user_input.replace(' ', '')

                employees = LogicAPI.get_employee_by_ssn(user_input)

                ComponentUI.print_header(EmployeeUI.__FRAME_IN_USE_STR)
                print(TextEditor.format_text("Find employee by name or ssn", TextEditor.UNDERLINE_TEXT))

                if not employees:
                    ComponentUI.centered_text_message("No employee found with the ssn: {}".format(user_input),"", 3)

                    return ComponentUI.get_user_input()

                else: 
                    employee_info_tuple =  (["Pilot" if isinstance(employee, Pilot) else "Flight attendant" for employee in employees], [employee.get_name() for employee in employees],[employee.get_ssn() for employee in employees],\
                    [employee.get_phonenumber() for employee in employees],[employee.get_home_address() for employee in employees],[employee.get_email() for employee in employees],\
                    [employee.get_state() for employee in employees])
                    
                    table_height = len(employees)
                    ComponentUI.print_frame_table_menu(info_header_tuple, employee_info_tuple, table_height, EmployeeUI.__FRAME_IN_USE_STR, "Employee")
                    user_input = ComponentUI.get_user_input()
                    user_input = ComponentUI.remove_brackets(user_input)
                    if not user_input.isdigit() or int(user_input) > table_height:
                        continue
                    table_index = int(user_input)-1
                    employee = employees[table_index]        

                    user_input = EmployeeUI.__show_employee(employee)

                return user_input
            else:
                name_list = []
                for name in user_input.split():
                    name_list.append(name.capitalize())

                user_input = " ".join(name_list)


                employees = LogicAPI.get_employee_by_name(user_input)

                ComponentUI.print_header(EmployeeUI. __FRAME_IN_USE_STR)
                print(TextEditor.format_text("Find employee by name or ssn", TextEditor.UNDERLINE_TEXT))

                if not employees:
                    
                    ComponentUI.centered_text_message("Could not find an employee named {}".format(user_input),"",3)
                
                    return ComponentUI.get_user_input()

                else: 
                    employee_info_tuple =  (["Pilot" if isinstance(employee, Pilot) else "Flight attendant" for employee in employees], [employee.get_name() for employee in employees],[employee.get_ssn() for employee in employees],\
                    [employee.get_phonenumber() for employee in employees],[employee.get_home_address() for employee in employees],[employee.get_email() for employee in employees],\
                    [employee.get_state() for employee in employees])
                    table_height = len(employees)
                    ComponentUI.print_frame_table_menu(info_header_tuple, employee_info_tuple, table_height, EmployeeUI.__FRAME_IN_USE_STR, "Employee")
                    user_input = ComponentUI.get_user_input()
                    user_input = ComponentUI.remove_brackets(user_input)
                    if not user_input.isdigit() or int(user_input) > table_height:
                        continue
                    table_index = int(user_input)-1
                    employee = employees[table_index]        

                    user_input = EmployeeUI.__show_employee(employee)

                return user_input


    @staticmethod
    def __show_pilot_by_license_finder():
        LogicAPI.update_states() #UPDATES ALL STATES BEFOR DISPLAYING


        user_input = ""

        info_header_tuple = ("Name", "SSN", "Phone number", "Home address", "E-mail", "State")

        while user_input not in EmployeeUI.__NAVIGATION_BAR_OPTIONS:
            ComponentUI.print_header(EmployeeUI.__FRAME_IN_USE_STR)
            #display table of airplane types and return the type-name the of chosen one , head above the the table
            user_input = EmployeeUI.__airplane_type_picker("Find pilots by license")


            if not user_input:
                continue

            user_input = user_input
            
            pilots_list = []

            pilots_list = LogicAPI.get_licensed_pilots(user_input)

            ComponentUI.print_header(EmployeeUI.__FRAME_IN_USE_STR)
            

            if not pilots_list:
                print(TextEditor.format_text("Find pilots by license", TextEditor.UNDERLINE_TEXT))
                ComponentUI.centered_text_message("Could not find a pilot with a license for {}".format(user_input),"",3)
                user_input = ComponentUI.get_user_input()
                if not user_input:
                    return EmployeeUI.__show_pilot_by_license_finder()
                
                return user_input

            else:
                #print(TextEditor.format_text("Pilots with license for " + user_input, TextEditor.UNDERLINE_TEXT)) 
                pilot_info_tuple = ([pilot.get_name() for pilot in pilots_list],[pilot.get_ssn() for pilot in pilots_list],\
                [pilot.get_phonenumber() for pilot in pilots_list],[pilot.get_home_address() for pilot in pilots_list],[pilot.get_email() for pilot in pilots_list],\
                [pilot.get_state() for pilot in pilots_list])
                table_height = len(pilots_list)
                ComponentUI.print_frame_table_menu(info_header_tuple, pilot_info_tuple, table_height, EmployeeUI.__FRAME_IN_USE_STR, "Pilots with license for " + user_input)
                user_input = ComponentUI.get_user_input()
                user_input = ComponentUI.remove_brackets(user_input)
                if not user_input.isdigit() or int(user_input) > table_height:
                    continue
                table_index = int(user_input)-1
                employee = pilots_list[table_index]        

                user_input = EmployeeUI.__show_employee(employee)


            return user_input


    @staticmethod
    def __show_employees_on_duty():
        LogicAPI.update_states() #UPDATES ALL STATES BEFOR DISPLAYING

        
        ComponentUI.print_header(EmployeeUI.__FRAME_IN_USE_STR)
        print(TextEditor.format_text("All employees on duty", TextEditor.UNDERLINE_TEXT))
        user_input = ""
        while user_input not in EmployeeUI.__NAVIGATION_BAR_OPTIONS:
            table_header_tuple = ("Name", "SSN", "Phone number", "Home address", "E-mail", "State")
            employees_on_duty_list = LogicAPI.get_employees_on_duty()
            if employees_on_duty_list:
                employees_on_duty_value_tuple = ([employees_on_duty.get_name() for employees_on_duty in employees_on_duty_list],[employees_on_duty.get_ssn() for employees_on_duty in employees_on_duty_list],\
                [employees_on_duty.get_phonenumber() for employees_on_duty in employees_on_duty_list], [employees_on_duty.get_home_address() for employees_on_duty in employees_on_duty_list],\
                [employees_on_duty.get_email() for employees_on_duty in employees_on_duty_list], [employees_on_duty.get_state() for employees_on_duty in employees_on_duty_list])
                table_height = len(employees_on_duty_list)
                ComponentUI.print_frame_table_menu(table_header_tuple, employees_on_duty_value_tuple, table_height, EmployeeUI.__FRAME_IN_USE_STR, "All employees on duty")
                user_input = ComponentUI.get_user_input()
                user_input = ComponentUI.remove_brackets(user_input)
                if not user_input.isdigit() or int(user_input) > table_height:
                        continue
                table_index = int(user_input)-1
                employee_on_duty = employees_on_duty_list[table_index]        

                user_input = EmployeeUI.__show_employee(employee_on_duty)
            else:
                ComponentUI.print_header(EmployeeUI.__FRAME_IN_USE_STR)
                print(TextEditor.format_text("Employees off duty", TextEditor.UNDERLINE_TEXT))
                ComponentUI.centered_text_message("No employee is on duty at the moment","",3)
                user_input = ComponentUI.get_user_input()
            return user_input

    @staticmethod
    def __show_employees_off_duty(): 
        LogicAPI.update_states() #UPDATES ALL STATES BEFOR DISPLAYING

        
        ComponentUI.print_header(EmployeeUI.__FRAME_IN_USE_STR)
        print(TextEditor.format_text("All employees off duty", TextEditor.UNDERLINE_TEXT))
        user_input = ""
        while user_input not in EmployeeUI.__NAVIGATION_BAR_OPTIONS:
            table_header_tuple = ("Name", "SSN", "Phone number", "Home address", "E-mail", "State")
            employees_off_duty_list = LogicAPI.get_employees_off_duty()
            if employees_off_duty_list:
                employees_off_duty_value_tuple = ([employees_off_duty.get_name() for employees_off_duty in employees_off_duty_list],[employees_off_duty.get_ssn() for employees_off_duty in employees_off_duty_list],\
                [employees_off_duty.get_phonenumber() for employees_off_duty in employees_off_duty_list], [employees_off_duty.get_home_address() for employees_off_duty in employees_off_duty_list],\
                [employees_off_duty.get_email() for employees_off_duty in employees_off_duty_list], [employees_off_duty.get_state() for employees_off_duty in employees_off_duty_list])
                table_height = len(employees_off_duty_list)
                ComponentUI.print_frame_table_menu(table_header_tuple, employees_off_duty_value_tuple, table_height, EmployeeUI.__FRAME_IN_USE_STR, "All employees off duty")
                user_input = ComponentUI.get_user_input()
                user_input = ComponentUI.remove_brackets(user_input)
                if not user_input.isdigit() or int(user_input) > table_height:
                        continue
                table_index = int(user_input)-1
                employee_off_duty = employees_off_duty_list[table_index]        

                user_input = EmployeeUI.__show_employee(employee_off_duty)

            else:
                ComponentUI.print_header(EmployeeUI.__FRAME_IN_USE_STR)
                print(TextEditor.format_text("Employees off duty", TextEditor.UNDERLINE_TEXT))

                ComponentUI.centered_text_message("No employee is off duty at the moment","",3)
                user_input = ComponentUI.get_user_input()

            return user_input

    @staticmethod
    def __show_employee(employee):
        LogicAPI.update_states() #UPDATES ALL STATES BEFOR DISPLAYING

        
        user_input = ''
        user_input_list = []
        valid_user_inputs_bool_list = [True] * 7

        is_pilot = isinstance(employee, Pilot)

        user_input_list.append(employee.get_name())
        user_input_list.append(employee.get_ssn())
        user_input_list.append(employee.get_phonenumber())
        user_input_list.append(employee.get_home_address())
        user_input_list.append(employee.get_email())
        user_input_list.append(employee.get_state())

        valid_user_inputs = ["4","5","6"]
        invalid_user_input_index_list = [0,1,2,6]

        if is_pilot:
            user_input_list.append(employee.get_license())
            valid_user_inputs_bool_list.append(True)
            valid_user_inputs.append("8")
            user_input_list.insert(0, "Pilot")
            option_tuple = ("Job title", "Name","SSN","Phonenumber","Home address","Email","State","License")  
        else:
            user_input_list.insert(0, "Flight Attendant")
            invalid_user_input_index_list.append(7)
            option_tuple = ("Job title", "Name","SSN","Phonenumber","Home address","Email","State")  

                  
       
        # employee_info_already_exists = False
        while user_input not in EmployeeUI.__NAVIGATION_BAR_OPTIONS:
            ComponentUI.print_frame_constructor_menu(option_tuple,\
            ComponentUI.get_main_options()[1], "Edit mode", user_input_list, True, 1000, invalid_user_input_index_list, print_check_voyages=True)
            
           
            user_input = ComponentUI.get_user_input()
            user_input = ComponentUI.remove_brackets(user_input)
            if user_input in valid_user_inputs: 
                index = int(user_input) - 1
                ComponentUI.print_frame_constructor_menu(option_tuple,\
            ComponentUI.get_main_options()[1], "Edit mode", user_input_list, False, index, invalid_user_input_index_list)

                if index == 3:
                    user_input = input("Insert new phone number: ").strip()
                elif index == 4:
                    user_input = input("Insert new home address: ").strip()
                elif index == 5:
                    user_input = input("Insert new e-mail: ").strip()
                elif index == 7 and is_pilot:
                    user_input = EmployeeUI.__airplane_type_picker("Edit mode - choose license")      # input("Insert new license: ").strip() #Vantar sub menu



                if not user_input and (index == 2 or index == 3 or index == 4):
                    user_input = user_input_list[index]
                else:

                    user_input = EmployeeUI.__constructor_error_check(user_input, valid_user_inputs_bool_list,\
                            index, user_input_list)

                    
            

            elif user_input.startswith('s'):
                if all(user_input_list) and all(valid_user_inputs_bool_list):
                    
                    edited_employee = None

                    if is_pilot:
                        edited_employee = Pilot(
                            user_input_list[1], #Name
                            user_input_list[2], #SSN
                            user_input_list[3], #Phonenumber
                            user_input_list[4], #Home address
                            user_input_list[5], #Email
                            user_input_list[6], #State
                            user_input_list[7]  #License
                        )
                        LogicAPI.change_saved_pilot(employee, edited_employee)
                    else:
                        edited_employee = FlightAttendant(
                            user_input_list[1], #Name
                            user_input_list[2], #SSN
                            user_input_list[3], #Phonenumber
                            user_input_list[4], #Home address
                            user_input_list[5], #Email
                            user_input_list[6]  #State
                        )
                        LogicAPI.change_saved_flight_attendant(employee, edited_employee)

                    #þarfnast skoðunnar(Kannski er þetta ok þar sem breytingar sjást, næ ekki að láta þetta virka heldur)
                    user_input = "An employee has been edited"
                    break

            elif user_input.startswith('c'):
                user_input = EmployeeUI.__show_employee_voyages(employee)

        return user_input


    @staticmethod
    def __show_employee_voyages(employee):
        is_pilot = isinstance(employee, Pilot)

        user_input = ""

        info_header_tuple = ("Destination", "Airplane name", "Start time", "End time", "State")

        while user_input not in EmployeeUI.__NAVIGATION_BAR_OPTIONS:
            ComponentUI.print_header(EmployeeUI. __FRAME_IN_USE_STR)
            print(TextEditor.format_text("Voyages for {}".format(employee.get_name()), TextEditor.UNDERLINE_TEXT))

            ComponentUI.fill_window_and_print_action_line(1)

            user_input = input("Insert a week number: ").strip()

            if not user_input:
                continue

            voyages_list = []

            if user_input.isdigit():
                voyages_list = LogicAPI.get_all_pilot_voyages_in_a_week(employee, int(user_input)) if is_pilot\
                    else LogicAPI.get_all_flight_attendant_voyages_in_a_week(employee ,int(user_input))

            if not voyages_list:
                ComponentUI.print_header(EmployeeUI.__FRAME_IN_USE_STR)
                print(TextEditor.format_text("Find employees voyages", TextEditor.UNDERLINE_TEXT))
                ComponentUI.centered_text_message("Could not find a voyage going for {} in week {}".format(employee.get_name(), user_input),"",3)
            
                return ComponentUI.get_user_input()

            else:
                voyage_info_tuple = ([voyage.get_flights()[0].get_arrival_location() for voyage in voyages_list],\
                [voyage.get_airplane().get_name() for voyage in voyages_list],\
                [voyage.get_schedule()[0] for voyage in voyages_list],\
                [voyage.get_schedule()[1] for voyage in voyages_list],\
                [voyage.get_state() for voyage in voyages_list])

                table_height = len(voyages_list)
                ComponentUI.print_frame_table_menu(info_header_tuple, voyage_info_tuple, \
                    table_height, ComponentUI.print_header(EmployeeUI.__FRAME_IN_USE_STR),"Voyages for {}".format(employee.get_name()))
                user_input = ComponentUI.get_user_input()
                user_input = ComponentUI.remove_brackets(user_input)
                if not user_input.isdigit() or int(user_input) > table_height:
                        continue
                table_index = int(user_input)-1
                voyage = voyages_list[table_index]        
                user_input = VoyageUI.show_voyage(voyage)

            return user_input
