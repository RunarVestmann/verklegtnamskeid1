from user_interface.component_ui import ComponentUI
from user_interface.window import Window


class QuitUI:

    @staticmethod
    def show():
        user_input = ""
        while not user_input.startswith('n'):

            ComponentUI.print_header(ComponentUI.get_main_options()[4])
            QuitUI.__print_quit_menu_body()

            user_input = ComponentUI.get_user_input()
            user_input = ComponentUI.remove_brackets(user_input)

            if user_input.startswith('y'):
                Window.clear()
                raise SystemExit

        return "Back to main menu"

    @staticmethod
    def __print_quit_menu_body():
        '''Prints the quit menu body that's below the header'''

        ComponentUI.centerd_text_message("Are you sure you want to quit?","(Y)es    (N)o")

        # window_width, window_height = Window.get_size()

        # #Calculate the how much space is left on the window
        # body_height = window_height - ComponentUI.get_header_height()

        # #Calculate how many new lines should be both above and below the quit text
        # offsetted_body_height_center = (body_height//2) - 2

        # #Print the empty space above the quit text
        # for _ in range(offsetted_body_height_center):
        #     print()

        # print("Are you sure you want to quit?".center(window_width))
        # print("(Y)es    (N)o".center(window_width))

        # #Print the empty space below the quit text
        # for _ in range(offsetted_body_height_center):
        #     print()

        # print("_" * window_width)
        