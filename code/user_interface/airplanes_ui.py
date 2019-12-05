from user_interface.window import Window
from user_interface.text_editor import TextEditor
from user_interface.component_ui import ComponentUI

class AirplanesUI:
    __option_tuple = ('New airplane', 'Show all airplanes', 'Show airplanes in use', 'Show all airplane types')
   
 
    @staticmethod
    def show_airplanes_menu():
        ComponentUI.print_header(ComponentUI.get_main_options()[2])
        option_tuple = AirplanesUI.__option_tuple
        print()
        for i, option in enumerate(option_tuple):
            print("({}) {}".format(i+1,option))
        ComponentUI.fill_window_and_print_action_line(len(option_tuple)+1)
         
    
    @staticmethod
    def action_airplanes_menu(user_input):
        option_tuple = AirplanesUI.__option_tuple  
        option_functions = (AirplanesUI.show_new_airplane_constructor, AirplanesUI.show_all_airplanes, AirplanesUI.show_airplanes_in_use, AirplanesUI.show_all_airplane_types)

       #####  Test input ####            
        selected_number = ComponentUI.test_user_input_chose_index(user_input, len(option_tuple)) #eather int>0 or False - may not be 0
        if selected_number:                                                                      #and is with in range of possible menu list
            selected_index = selected_number-1
            return option_functions[selected_index]
        else:
            return False




      
    DUMMYNMBR=1
    @staticmethod
    def show_new_airplane_constructor():
        pass

    @staticmethod
    def show_all_airplanes():
        pass

    @staticmethod
    def show_airplanes_in_use():
        pass
    
    @staticmethod
    def show_all_airplane_types():
        ComponentUI.print_header(ComponentUI.get_main_options()[1])
        print(TextEditor.format_text(AirplanesUI.__option_tuple[3], TextEditor.UNDERLINE_TEXT))
        ComponentUI.fill_window_and_print_action_line(AirplanesUI.DUMMYNMBR, False)

        pass
