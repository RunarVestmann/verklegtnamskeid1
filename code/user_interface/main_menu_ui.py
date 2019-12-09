from user_interface.window import Window
from user_interface.component_ui import ComponentUI

class MainMenuUI:

    @staticmethod
    def __print_main_menu_body():
        ComponentUI.centered_text_message("Welcome to the NaN Air booking software",\
            "Press any of the keys in the brackets '()' to get started")
            
        # window_width, window_height = Window.get_size()

        # #Calculate the how much space is left on the window
        # body_height = window_height - ComponentUI.get_header_height()

        # #Calculate how many new lines should be both above and below the quit text
        # offsetted_body_height_center = (body_height//2) - 2

        # #Print the empty space above the welcome text
        # for _ in range(offsetted_body_height_center):
        #     print()

        # print("Welcome to the NaN Air booking software".center(window_width))
        # print("Press any of the keys in the brackets '()' to get started".center(window_width))

        # #Print the empty space below the welcome text
        # for _ in range(offsetted_body_height_center):
        #     print()

        # print("_" * window_width)

    @staticmethod
    def show():
        ComponentUI.print_header()
        MainMenuUI.__print_main_menu_body()

        return ComponentUI.get_user_input()
