from user_interface.menu_ui import MenuUI
from user_interface.window import Window
from user_interface.text_editor import TextEditor
from user_interface.component_ui import ComponentUI

class AirplanesUI:
 
    @staticmethod
    def show_airplanes_menu():
        MenuUI.print_header(MenuUI.get_main_options()[2])
        option_tuple = ('New airplane', 'Show all airplanes', 'Show airplanes in use', 'show all airplane types')
        option_functions = (AirplanesUI.show_new_airplane_constructor, AirplanesUI.show_all_airplanes, AirplanesUI.show_airplanes_in_use, AirplanesUI.show_all_airplane_types)

        #Generate a tuple that holds all the valid user inputs
        valid_user_options_tuple = ComponentUI.make_valid_menu_options_tuple(len(option_tuple))

        user_input = ''

        #Keep displaying this menu as long as the user doesn't select anything
        while user_input not in valid_user_options_tuple:
            print()
            for i, option in enumerate(option_tuple):
                print("({}) {}".format(i+1,option))
            MenuUI.fill_window_and_print_action_line(len(option_tuple)+1)
            user_input = input("Your action: ").lower().strip()

            ####  Test input ####            
            selected_number = ComponentUI.test_user_input_chose_index(user_input, len(option_tuple)) #eather int>0 or False - may not be 0
            if selected_number:                                                                      #and is with in range of possible menu list
                selected_index = selected_number-1
                option_functions[selected_index](option_tuple[selected_index])
            else:
                AirplanesUI.show_airplanes_menu()
    
      
    
    @staticmethod
    def show_new_airplane_constructor(title):
        pass

    @staticmethod
    def show_all_airplanes(title):
        pass

    @staticmethod
    def show_airplanes_in_use(title):
        pass
    
    @staticmethod
    def show_all_airplane_types(title):
        MenuUI.print_header(MenuUI.get_main_options()[1])
        print(TextEditor.format_text(title, TextEditor.UNDERLINE_TEXT))

        print("***** work in progess ****")
        pass
