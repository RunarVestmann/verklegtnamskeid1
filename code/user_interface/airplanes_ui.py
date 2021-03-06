from user_interface.window import Window
from user_interface.text_editor import TextEditor
from user_interface.component_ui import ComponentUI
from data_models.airplane import Airplane
from data_models.aircraft_type import AircraftType
from data_models.state import State
from apis.logic_api import LogicAPI

class AirplanesUI:
    __FRAME_IN_USE_STR = ComponentUI.get_main_options()[2]
    
    __NAVIGATION_BAR_OPTIONS = ComponentUI.get_navigation_options_tuple()
    #option_tuple = ('Name', 'Type', 'Manufacturer', "Seats", 'State') NOT CONSTANT because different in every function
    @staticmethod
    def show():

        #The options that show up at the start of this frame
        option_tuple = ('New airplane', 'Show all airplanes', 'Show airplanes in use', 'Show all airplane types')

        #The different inputs that allow the user to interact with this frame
        valid_user_inputs = ComponentUI.make_valid_menu_options_tuple(len(option_tuple))

        #The functions that this frame has stored in a tuple
        frame_functions = (AirplanesUI.__show_new_airplane_constructor, AirplanesUI.__show_all_airplanes,\
            AirplanesUI.__show_airplanes_in_use, AirplanesUI.__show_all_airplane_types)

        return ComponentUI.run_frame(option_tuple, AirplanesUI.__FRAME_IN_USE_STR, valid_user_inputs, frame_functions)


    
    @staticmethod
    def __show_new_airplane_constructor():
               
        option_tuple = ("Name", "Type", "Manufacturer", "Seating capacity")

        valid_user_inputs = ComponentUI.make_valid_menu_options_tuple(len(option_tuple))

        input_message_tuple = ("Insert Name: ", "Insert Type: ", "Insert Manufacturer: ", "Insert Seating capacity: ")

        user_input_list = [""] * len(option_tuple)
        user_input_list.append(State.get_airplane_states()[0]) #State default value
        valid_for_submit_list = [False, False] # only 2 chosse here * len(option_tuple) #list that contains bools if all true then ok to submit


        user_input = ""



        while user_input not in AirplanesUI.__NAVIGATION_BAR_OPTIONS:

            ComponentUI.print_frame_constructor_menu(option_tuple, ComponentUI.get_main_options()[2],\
                 "New airplane", user_input_list, True, 1000, [2,3], True)

            user_input = ComponentUI.get_user_input()

            if not user_input:
                continue

            user_input = ComponentUI.remove_brackets(user_input)

            if user_input in valid_user_inputs:
                index = int(user_input) - 1


                if index == 0:
                    ComponentUI.print_frame_constructor_menu(option_tuple, ComponentUI.get_main_options()[2],\
                     "New airplane", user_input_list, False, index)
                    user_input = input(input_message_tuple[index]).strip()
                elif index == 1:

                    #### PICK AIRPLANE TYPE BY TABLE LIST ###
                    table_header_tuple = ("Type", "Manufacturer", "Seats")
                 
                    airplane_type_list = LogicAPI.get_all_airplane_types()
                    airplanes_type_getfunctions_tuple = ([aircraft_type.get_plane_type() for aircraft_type in airplane_type_list],[aircraft_type.get_manufacturer() for aircraft_type in airplane_type_list],\
                        [aircraft_type.get_seat_count() for aircraft_type in airplane_type_list])
                    table_height = len(airplane_type_list)


                    ComponentUI.print_frame_table_menu(table_header_tuple, airplanes_type_getfunctions_tuple, table_height,\
                        ComponentUI.get_main_options()[2], "New airplane")

                    user_input = ComponentUI.get_user_input("Insert number of desired type: ")

                    user_input = ComponentUI.remove_brackets(user_input)
                    if not user_input.isdigit() or int(user_input) > table_height or not user_input:
                        continue

                    table_index = int(user_input) - 1
                    chosen_table_line = airplane_type_list[table_index]
                    ###                LINE PICKED           ##


                    user_input_list[1] = chosen_table_line.get_plane_type()
                    user_input_list[2] = chosen_table_line.get_manufacturer()
                    user_input_list[3] = chosen_table_line.get_seat_count()
                    valid_for_submit_list[1] = True

                #Check if airplane name already exists
                if index == 0: 
                    user_input = user_input.capitalize()
                    if not LogicAPI.is_airplane_name_available(user_input):
                        user_input = user_input + " " + TextEditor.color_text_background("Airplane name already exists, another input is required", TextEditor.RED_BACKGROUND)
                        valid_for_submit_list[0] = False
                    else:
                        valid_for_submit_list[0] = True

                if index == 0:
                    user_input_list[index] = user_input
                
                user_input = ""

            elif user_input.startswith('s'):
                if all(valid_for_submit_list):

                    new_airplane = Airplane(
                        user_input_list[0],
                        user_input_list[1],
                        user_input_list[2],
                        user_input_list[3],
                        user_input_list[4]
                    )
                    LogicAPI.save_new_airplane(new_airplane)
                    user_input = "A new airplane has been registered"

                    break

        return user_input

    @staticmethod
    def __show_all_airplanes():
        LogicAPI.update_states() #UPDATES ALL STATES BEFOR DISPLAYING


        ComponentUI.print_header(AirplanesUI.__FRAME_IN_USE_STR)
        print(TextEditor.format_text("All airplanes", TextEditor.UNDERLINE_TEXT))
    
        user_input = ""

        while user_input not in AirplanesUI.__NAVIGATION_BAR_OPTIONS:
            table_header_tuple = ("Name", "State", "Type", "Manufacturer", "Seats")
            airplanes_list = LogicAPI.get_all_airplanes()
            airplanes_getfunctions_tuple = ([airplane.get_name() for airplane in airplanes_list],[airplane.get_state() for airplane in airplanes_list],\
                [airplane.get_type() for airplane in airplanes_list], [airplane.get_manufacturer() for airplane in airplanes_list], [airplane.get_seat_count() for airplane in airplanes_list])

            table_height = len(airplanes_list)
            ComponentUI.print_frame_table_menu(table_header_tuple, airplanes_getfunctions_tuple, table_height, AirplanesUI.__FRAME_IN_USE_STR, "All airplanes")
            user_input = ComponentUI.get_user_input()
            user_input = ComponentUI.remove_brackets(user_input)
            if not user_input.isdigit() or int(user_input) > table_height:
                    continue
            table_index = int(user_input)-1
            airplane = airplanes_list[table_index]        

            user_input = AirplanesUI.__show_airplane(airplane)

        return user_input


    @staticmethod
    def __show_airplanes_in_use():
        LogicAPI.update_states() #UPDATES ALL STATES BEFOR DISPLAYING


        ComponentUI.print_header(AirplanesUI.__FRAME_IN_USE_STR)
        print(TextEditor.format_text("All airplanes in use", TextEditor.UNDERLINE_TEXT))
        user_input = ""
        while user_input not in AirplanesUI.__NAVIGATION_BAR_OPTIONS:
            table_header_tuple = ("Name", "State", "Type", "Manufacturer", "Seats")
            airplanes_list = LogicAPI.get_all_airplanes_in_use()
            if airplanes_list:
                airplanes_getfunctions_tuple = ([airplane.get_name() for airplane in airplanes_list],[airplane.get_state() for airplane in airplanes_list],\
                [airplane.get_type() for airplane in airplanes_list], [airplane.get_manufacturer() for airplane in airplanes_list], [airplane.get_seat_count() for airplane in airplanes_list])
                table_height = len(airplanes_list)
                ComponentUI.print_frame_table_menu(table_header_tuple,airplanes_getfunctions_tuple, table_height, AirplanesUI.__FRAME_IN_USE_STR, "All airplanes in use")
                user_input = ComponentUI.get_user_input()
                user_input = ComponentUI.remove_brackets(user_input)
                if not user_input.isdigit() or int(user_input) > table_height:
                    continue
                table_index = int(user_input)-1
                airplane = airplanes_list[table_index]        

                user_input = AirplanesUI.__show_airplane(airplane)
            else:
                ComponentUI.print_header(AirplanesUI.__FRAME_IN_USE_STR)
                print(TextEditor.format_text("All airplanes in use", TextEditor.UNDERLINE_TEXT))
                ComponentUI.centered_text_message("There are no airplanes in use at the moment !","",3)

           
            return user_input
  
    @staticmethod
    def __show_airplane(airplane):
        LogicAPI.update_states() #UPDATES ALL STATES BEFOR DISPLAYING

        user_input = ''
        user_input_list = [
            airplane.get_name(),
            airplane.get_type(),
            airplane.get_manufacturer(),
            airplane.get_seat_count(),
            airplane.get_state()
        ]
        valid_user_inputs = ["1"]
        option_tuple = ('Name', 'Type', 'Manufacturer', "Seats", 'State')          
        valid_for_submit_list = [False] #Can only change the name (one element) in this case (airplane)
        while user_input not in AirplanesUI.__NAVIGATION_BAR_OPTIONS:
            ComponentUI.print_frame_constructor_menu(option_tuple,\
            ComponentUI.get_main_options()[2], "Edit mode", user_input_list, True, 1000, [1,2,3,4])

            user_input = ComponentUI.get_user_input()
            user_input = ComponentUI.remove_brackets(user_input)
            if user_input in valid_user_inputs: 
                index = int(user_input) - 1
                ComponentUI.print_frame_constructor_menu(option_tuple,\
                    ComponentUI.get_main_options()[2], "Edit mode", user_input_list, False, 1000, [1,2,3,4])

                if(index == 0):
                    user_input = input("Insert name: ").strip()
                



                #Capitalize the first letters in the contacts name
                if index == 0:
                    if not user_input: #use existing name in case if user cancels or leaves it blank 
                        user_input = user_input_list[index]

                    airplane_name_list = []
                    for name in user_input.split():
                        airplane_name_list.append(name.capitalize())
                    user_input = " ".join(airplane_name_list)
                    valid_for_submit_list[0] = True

              
                
                user_input_list[index] = user_input
                user_input = ""
                   
            elif user_input.startswith('s'):
                if all(user_input_list):

                    edited_airplane = Airplane(
                        user_input_list[0],
                        user_input_list[1],
                        user_input_list[2],
                        user_input_list[3],
                        user_input_list[4]

                    )

                    LogicAPI.change_saved_airplane(airplane, edited_airplane)
                    
                    
                    user_input = "An airplane has been edited"
                    break
        return user_input



###########################  - AIRPLANE TYPES RELADED FUNCTIONS - #################
   #@staticmethod
    # def __get_airplane_types_data():
    #     airplane_type_list = LogicAPI.get_all_airplane_types()
    #     airplanes_type_getfunctions_tuple = ([aircraft_type.get_plane_type() for aircraft_type in airplane_type_list],[aircraft_type.get_manufacturer() for aircraft_type in airplane_type_list],\
    #         [aircraft_type.get_seat_count() for aircraft_type in airplane_type_list])
    #     line_count_int = len(airplane_type_list)
        
    #     return tuple(airplanes_type_getfunctions_tuple), int(line_count_int)






    @staticmethod
    def __show_all_airplane_types():
        ComponentUI.print_header(AirplanesUI.__FRAME_IN_USE_STR)
        print(TextEditor.format_text("All airplane types", TextEditor.UNDERLINE_TEXT))
        user_input = ""

        

        while user_input not in AirplanesUI.__NAVIGATION_BAR_OPTIONS:
            table_header_tuple = ("Type", "Manufacturer", "Seats")
                  
           
            airplane_type_list = LogicAPI.get_all_airplane_types()
            airplanes_type_getfunctions_tuple = ([aircraft_type.get_plane_type() for aircraft_type in airplane_type_list],[aircraft_type.get_manufacturer() for aircraft_type in airplane_type_list],\
                [aircraft_type.get_seat_count() for aircraft_type in airplane_type_list])
            table_height = len(airplane_type_list)

            ### - ONLY DISPLAY TABLE - ##

            ComponentUI.fill_in_table(table_header_tuple, airplanes_type_getfunctions_tuple, False)
            ComponentUI.fill_window_and_print_action_line(table_height+2) 


            #ComponentUI.print_frame_table_menu(table_header_tuple, airplanes_type_getfunctions_tuple, table_height, ComponentUI.print_header(AirplanesUI.__FRAME_IN_USE_STR),"All airplane types")
            user_input = ComponentUI.get_user_input()
            user_input = ComponentUI.remove_brackets(user_input)
            if not user_input.isdigit() or int(user_input) > table_height:
                    continue
            table_index = int(user_input)-1
            airplane = airplane_type_list[table_index]        

            user_input = AirplanesUI.__show_airplane(airplane)

        return user_input