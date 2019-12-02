from user_interface.text_editor import TextEditor
from user_interface.window import Window

class MenuUI:

    __MAIN_OPTIONS = ("(V)oyages", "(E)mployees", "(A)irplanes", "(F)light routes", "(Q)uit")
    __MAIN_OPTIONS_CHAR_COUNT = sum([len(i) for i in __MAIN_OPTIONS])
    __HEADER_HEIGHT = 7

    @staticmethod
    def __print_banner():
        Window.clear()
        window_width = Window.get_size()[0]

        print("‾" * window_width)
        print("--x-O-x--".center(window_width))
        print()
        print("NaN Air".center(window_width))
        print()
        print("_" * window_width)

    @staticmethod
    def __print_main_options(selected_option=""):
        window_width = Window.get_size()[0]

        #Calculate how much space should be between each main option
        spaces_between = " " * ((window_width - MenuUI.__MAIN_OPTIONS_CHAR_COUNT) // (len(MenuUI.__MAIN_OPTIONS) - 1))

        #Print the options normally if no option is selected
        if not selected_option:
            print(spaces_between.join(MenuUI.__MAIN_OPTIONS))

        #Underline the selected option
        else:
            main_options = []
            for option in MenuUI.__MAIN_OPTIONS:
                if selected_option == option:
                    option = TextEditor.format_text(option, TextEditor.UNDERLINE_TEXT)
                main_options.append(option)

            print(spaces_between.join(main_options))

    @staticmethod
    def __print_main_menu_body():
        pass

    @staticmethod
    def get_header_height():
        '''Returns the height of the header in characters'''
        return MenuUI.__HEADER_HEIGHT

    @staticmethod
    def get_main_options():
        return MenuUI.__MAIN_OPTIONS

    @staticmethod
    def print_header(selected_option=""):
        '''Prints the NaN Air banner and the main options below the banner'''
        MenuUI.__print_banner()
        MenuUI.__print_main_options(selected_option)

    @staticmethod
    def show_main_menu():
        MenuUI.print_header()
        MenuUI.__print_main_menu_body() #needs to be implemented

        user_input = input("Your action: ").lower().strip()
        #if checks...
    