from user_interface.window import Window
from user_interface.text_editor import TextEditor
from user_interface.component_ui import ComponentUI
from data_models.airplane import Airplane
from apis.logic_api import LogicAPI

class AirplanesUI:
    __FRAME_IN_USE_STR = ComponentUI.get_main_options()[2]
    __option_tuple = ('New airplane', 'Show all airplanes', 'Show airplanes in use', 'Show all airplane types')

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

    DUMMYNMBR=1
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
                 "New airplane", user_input_list, True)

            user_input = ComponentUI.get_user_input()

            if not user_input:
                continue

            user_input = ComponentUI.remove_brackets(user_input)

            if user_input in valid_user_inputs:
                index = int(user_input) - 1
                ComponentUI.print_frame_constructor_menu(option_tuple, ComponentUI.get_main_options()[2],\
                     "New airplane", user_input_list, False, index)

                user_input = input(input_message_tuple[index]).strip()

                if not user_input:
                    continue

                #Capitalize the first letter of the Name , Type and Manufacturer 
                if index == 0 or index == 1 or index == 2:
                    user_input = user_input.capitalize()

                #Check if airplane name already exists
                if index == 0: 
                    if not LogicAPI.is_airplane_name_available(user_input):
                        user_input = user_input + " " + TextEditor.color_text_background("Airplane name already exists, another input is required", TextEditor.RED_BACKGROUND)
                        airplane_info_already_exists = True
                    else:
                        airplane_info_already_exists = False

                #Seat capacity cannot contain letters except "seats"
                elif index == 3:
                    if 'seats' in user_input.lower():
                        user_input = user_input.lower().replace('seats', '')
                    user_input = user_input.strip()
                    if not user_input.isdigit():
                        user_input = user_input + " " + TextEditor.color_text_background("Can not contain letters, another input is required", TextEditor.RED_BACKGROUND)
                        airplane_info_already_exists = True
                    else:
                        airplane_info_already_exists = False


               

                
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
        airplanes_getfunctions_tuple = ([airplane.get_name for airplane in airplanes_list],[airplane.get_state for airplane in airplanes_list],\
           [airplane.get_type for airplane in airplanes_list], [airplane.get_manufacturer for airplane in airplanes_list], [airplane.get_seat_count for airplane in airplanes_list])

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
            airplanes_getfunctions_tuple = ([airplane.get_name for airplane in airplanes_list],[airplane.get_state for airplane in airplanes_list],\
            [airplane.get_type for airplane in airplanes_list], [airplane.get_manufacturer for airplane in airplanes_list], [airplane.get_seat_count for airplane in airplanes_list])

            ComponentUI.fill_in_table(table_header_tuple, airplanes_getfunctions_tuple, False)
            ComponentUI.fill_window_and_print_action_line(len(airplanes_list)+2)
        
        else:
            ComponentUI.centered_text_message("There are no airplanes in use at the moment !")

           
        return ComponentUI.get_user_input()
    


    @staticmethod
    def __show_all_airplane_types():
        ComponentUI.print_header(AirplanesUI.__FRAME_IN_USE_STR)
        print(TextEditor.format_text("All airplanes types", TextEditor.UNDERLINE_TEXT))
 
        table_header_tuple = ("Type", "Manufacturer", "Seats")
        airplanes_list = LogicAPI.get_all_airplane_types()
        airplanes_getfunctions_tuple = ([airplane.get_type for airplane in airplanes_list],[airplane.get_manufacturer for airplane in airplanes_list],\
           [airplane.get_seat_count for airplane in airplanes_list])

        ComponentUI.fill_in_table(table_header_tuple, airplanes_getfunctions_tuple, False)
                 
        ComponentUI.fill_window_and_print_action_line(len(airplanes_list)+2)

        return ComponentUI.get_user_input()
