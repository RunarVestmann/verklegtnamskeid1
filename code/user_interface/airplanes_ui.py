from user_interface.window import Window
from user_interface.text_editor import TextEditor
from user_interface.component_ui import ComponentUI
from data_models.airplane import Airplane
from data_models.aircraft_type import AircraftType
from apis.logic_api import LogicAPI

class AirplanesUI:
    __FRAME_IN_USE_STR = ComponentUI.get_main_options()[2]
    

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
               
        navigation_bar_options = ComponentUI.get_navigation_options_tuple()

        option_tuple = ("Name", "Type", "Manufacturer", "Seating capacity")

        valid_user_inputs = ComponentUI.make_valid_menu_options_tuple(len(option_tuple))

        input_message_tuple = ("Insert Name: ", "Insert Type: ", "Insert Manufacturer: ", "Insert Seating capacity: ")

        user_input_list = [""] * len(option_tuple)
        user_input_list.append("Not scheduled") #State default value

        user_input = ""

        airplane_info_already_exists = False

        while user_input not in navigation_bar_options:

            ComponentUI.print_frame_constructor_menu(option_tuple, ComponentUI.get_main_options()[2],\
                 "New airplane", user_input_list, True, 1000, [2,3], True)

            user_input = ComponentUI.get_user_input()

            if not user_input:
                continue

            user_input = ComponentUI.remove_brackets(user_input)

            if user_input in valid_user_inputs:
                index = int(user_input) - 1
                # ComponentUI.print_frame_constructor_menu(option_tuple, ComponentUI.get_main_options()[2],\
                #      "New airplane", user_input_list, False, index)


                if index == 0: # ath með aðra hér
                    ComponentUI.print_frame_constructor_menu(option_tuple, ComponentUI.get_main_options()[2],\
                     "New airplane", user_input_list, False, index)
                    user_input = input(input_message_tuple[index]).strip()
                elif index == 1:
                    table_header_tuple = ("Type", "Manufacturer", "Seats")
                    aircrafttype_list = LogicAPI.get_all_airplane_types()
                    airplanes_getfunctions_tuple = ([aircraft_type.get_plane_type() for aircraft_type in aircrafttype_list],[aircraft_type.get_model() for aircraft_type in aircrafttype_list],\
                        [aircraft_type.get_capacity() for aircraft_type in aircrafttype_list])
                    
                    table_height = len(aircrafttype_list)
                    ComponentUI.print_frame_table_menu(table_header_tuple, airplanes_getfunctions_tuple, table_height,\
                        ComponentUI.get_main_options()[2], "New airplane")

                    user_input = ComponentUI.get_user_input("Insert number of desired type: ")

                    user_input = ComponentUI.remove_brackets(user_input)
                    if not user_input.isdigit() or int(user_input) > table_height or not user_input:
                        continue

                    table_index = int(user_input) - 1
                    chosen_table_line = aircrafttype_list[table_index]
                    user_input_list[1] = chosen_table_line.get_plane_type()
                    user_input_list[2] = chosen_table_line.get_model()
                    user_input_list[3] = chosen_table_line.get_capacity()
                

                #Capitalize the first letter of the Name , Type and Manufacturer 
                if index == 0:       # or index == 1 or index == 2:
                    user_input = user_input.capitalize()

                #Check if airplane name already exists
                if index == 0: 
                    if not LogicAPI.is_airplane_name_available(user_input):
                        user_input = user_input + " " + TextEditor.color_text_background("Airplane name already exists, another input is required", TextEditor.RED_BACKGROUND)
                        airplane_info_already_exists = True
                    else:
                        airplane_info_already_exists = False

            

               
                if index == 0:
                    user_input_list[index] = user_input
                
                user_input = ""

            elif user_input.startswith('s'):
                if all(user_input_list) and not airplane_info_already_exists:

                    new_airplane = Airplane(
                        user_input_list[0],
                        user_input_list[1],
                        user_input_list[2],
                        user_input_list[3],
                        user_input_list[4]
                    )
                    LogicAPI.save_new_airplane(new_airplane)

                    break

        return user_input 

    @staticmethod
    def __show_all_airplanes():
        ComponentUI.print_header(AirplanesUI.__FRAME_IN_USE_STR)
        print(TextEditor.format_text("All airplanes", TextEditor.UNDERLINE_TEXT))
 
        table_header_tuple = ("Name", "State", "Type", "Manufacturer", "Seats")
        airplanes_list = LogicAPI.get_all_airplanes()
        airplanes_getfunctions_tuple = ([airplane.get_name() for airplane in airplanes_list],[airplane.get_state() for airplane in airplanes_list],\
           [airplane.get_type() for airplane in airplanes_list], [airplane.get_manufacturer() for airplane in airplanes_list], [airplane.get_seat_count() for airplane in airplanes_list])

        ComponentUI.fill_in_table(table_header_tuple, airplanes_getfunctions_tuple, False)
                 
        ComponentUI.fill_window_and_print_action_line(len(airplanes_list)+2)

        return ComponentUI.get_user_input()


    @staticmethod
    def __show_airplanes_in_use():
        ComponentUI.print_header(AirplanesUI.__FRAME_IN_USE_STR)
        print(TextEditor.format_text("All airplanes in use", TextEditor.UNDERLINE_TEXT))
 
        table_header_tuple = ("Name", "State", "Type", "Manufacturer", "Seats")
        airplanes_list = LogicAPI.get_all_airplanes_in_use()
        if airplanes_list:
            airplanes_getfunctions_tuple = ([airplane.get_name() for airplane in airplanes_list],[airplane.get_state() for airplane in airplanes_list],\
            [airplane.get_type() for airplane in airplanes_list], [airplane.get_manufacturer() for airplane in airplanes_list], [airplane.get_seat_count() for airplane in airplanes_list])

            ComponentUI.fill_in_table(table_header_tuple, airplanes_getfunctions_tuple, False)
            ComponentUI.fill_window_and_print_action_line(len(airplanes_list)+2)
        
        else:
            ComponentUI.centered_text_message("There are no airpanes in use at the moment !","",3)

           
        return ComponentUI.get_user_input()
    


    @staticmethod
    def __show_all_airplane_types():
        ComponentUI.print_header(AirplanesUI.__FRAME_IN_USE_STR)
        print(TextEditor.format_text("All airplanes types", TextEditor.UNDERLINE_TEXT))
 
        table_header_tuple = ("Type", "Manufacturer", "Seats")
        aircrafttype_list = LogicAPI.get_all_airplane_types()
        airplanes_getfunctions_tuple = ([aircraft_type.get_plane_type() for aircraft_type in aircrafttype_list],[aircraft_type.get_model() for aircraft_type in aircrafttype_list],\
           [aircraft_type.get_capacity() for aircraft_type in aircrafttype_list])

        ComponentUI.fill_in_table(table_header_tuple, airplanes_getfunctions_tuple, False)
                 
        ComponentUI.fill_window_and_print_action_line(len(aircrafttype_list)+2)

        return ComponentUI.get_user_input()
