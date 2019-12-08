from user_interface.window import Window
from user_interface.text_editor import TextEditor
from user_interface.component_ui import ComponentUI
from data_models.airplane import Airplane
from apis.logic_api import LogicAPI

class AirplanesUI:
    __FRAME_IN_USE_STRING = ComponentUI.get_main_options()[2]
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

        return ComponentUI.run_frame(option_tuple, AirplanesUI.__FRAME_IN_USE_STRING, valid_user_inputs, frame_functions)

    DUMMYNMBR=1
    @staticmethod
    def __show_new_airplane_constructor():
               
        print(TextEditor.format_text(AirplanesUI.__FRAME_IN_USE_STRING, TextEditor.UNDERLINE_TEXT))
        ComponentUI.fill_window_and_print_action_line(AirplanesUI.DUMMYNMBR, False)
        pass 

    @staticmethod
    def __show_all_airplanes():
            #þarf að setja inni loopu og vilid opions
        print(TextEditor.format_text(AirplanesUI.__FRAME_IN_USE_STRING, TextEditor.UNDERLINE_TEXT))
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
        print(TextEditor.format_text(AirplanesUI.__FRAME_IN_USE_STRING, TextEditor.UNDERLINE_TEXT))
        print(TextEditor.format_text(AirplanesUI.__option_tuple[2], TextEditor.UNDERLINE_TEXT))
        ComponentUI.fill_window_and_print_action_line(AirplanesUI.DUMMYNMBR, False)
        pass
    
    @staticmethod
    def __show_all_airplane_types():
        print(TextEditor.format_text(AirplanesUI.__FRAME_IN_USE_STRING, TextEditor.UNDERLINE_TEXT))
        print(TextEditor.format_text(AirplanesUI.__option_tuple[3], TextEditor.UNDERLINE_TEXT))
        ComponentUI.fill_window_and_print_action_line(AirplanesUI.DUMMYNMBR, False)

        pass
