from user_interface.window import Window
from user_interface.component_ui import ComponentUI

class MainMenuUI:

    @staticmethod
    def __print_main_menu_body():
        ''' message on first screen '''
        ComponentUI.centered_text_message("Welcome to the NaN Air booking software",\
            "Press any of the keys in the brackets '()' to get started")
            

    @staticmethod
    def show():
        ''' Displaying message on the center of when program is opened '''
        ComponentUI.print_header()
        MainMenuUI.__print_main_menu_body()

        return ComponentUI.get_user_input()
