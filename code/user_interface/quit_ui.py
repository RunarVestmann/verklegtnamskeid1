from user_interface.component_ui import ComponentUI
from user_interface.window import Window

class QuitUI:

    @staticmethod
    def show():
        ''' Displaying the Quit confirmation message '''
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

        ComponentUI.centered_text_message("Are you sure you want to quit?","(Y)es    (N)o")

        