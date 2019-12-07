from user_interface.window import Window
from user_interface.text_editor import TextEditor
from user_interface.component_ui import ComponentUI
from apis.logic_api import LogicAPI

class AirplanesUI:

    __option_tuple = ('New airplane', 'Show all airplanes', 'Show airplanes in use', 'Show all airplane types')

    @staticmethod
    def show():

        valid_user_inputs = ComponentUI.make_valid_menu_options_tuple(len(AirplanesUI.__option_tuple))

        navigation_bar_options = ComponentUI.get_navigation_options_tuple()

        frame_functions = (AirplanesUI.__show_new_airplane_constructor, AirplanesUI.__show_all_airplanes,\
            AirplanesUI.__show_airplanes_in_use, AirplanesUI.__show_all_airplane_types)

        user_input = ""

        while user_input not in navigation_bar_options:

            ComponentUI.print_frame_menu(AirplanesUI.__option_tuple, ComponentUI.get_main_options()[2])

            user_input = ComponentUI.get_user_input()

            if not user_input:
                continue

            user_input = ComponentUI.remove_brackets(user_input)

            if user_input in valid_user_inputs:

                index = int(user_input) - 1

                user_input = frame_functions[index]()

        return user_input

    #The functions below need to be implemented

    DUMMYNMBR=1
    @staticmethod
    def __show_new_airplane_constructor():
        ComponentUI.print_header(ComponentUI.get_main_options()[2])
        print(TextEditor.format_text(AirplanesUI.__option_tuple[0], TextEditor.UNDERLINE_TEXT))
        ComponentUI.fill_window_and_print_action_line(AirplanesUI.DUMMYNMBR, False)
        pass 

    @staticmethod
    def __show_all_airplanes():
            #þarf að setja inni loopu og vilid opions
        ComponentUI.print_header(ComponentUI.get_main_options()[2])
        print(TextEditor.format_text(AirplanesUI.__option_tuple[1], TextEditor.UNDERLINE_TEXT))

 
        table_header_tuple = ("Name", "State", "Type", "Manufacturer", "Seats")
        airplanes_list = LogicAPI.get_all_airplanes()
        airplanes_getfunctions_tuple = ([airplane.get_name for airplane in airplanes_list],[airplane.get_state for airplane in airplanes_list],\
           [airplane.get_type for airplane in airplanes_list], [airplane.get_manufacturer for airplane in airplanes_list], [airplane.get_seat_count for airplane in airplanes_list])

        ComponentUI.fill_in_table(table_header_tuple, airplanes_getfunctions_tuple, False)
                 
        ComponentUI.fill_window_and_print_action_line(len(airplanes_list)+2)


    @staticmethod
    def __show_airplanes_in_use():
        ComponentUI.print_header(ComponentUI.get_main_options()[2])
        print(TextEditor.format_text(AirplanesUI.__option_tuple[2], TextEditor.UNDERLINE_TEXT))
        ComponentUI.fill_window_and_print_action_line(AirplanesUI.DUMMYNMBR, False)
        pass
    
    @staticmethod
    def __show_all_airplane_types():
        ComponentUI.print_header(ComponentUI.get_main_options()[1])
        print(TextEditor.format_text(AirplanesUI.__option_tuple[3], TextEditor.UNDERLINE_TEXT))
        ComponentUI.fill_window_and_print_action_line(AirplanesUI.DUMMYNMBR, False)

        pass
