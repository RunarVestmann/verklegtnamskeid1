from text_editor import TextEditor
from window import Window

class MenuUI:

    MAIN_OPTIONS = ("(V)oyages", "(E)mployees", "(A)irplanes", "(F)light routes", "(Q)uit")
    MAIN_OPTIONS_CHAR_COUNT = sum([len(i) for i in MAIN_OPTIONS])

    @staticmethod
    def __print_banner():
        Window.clear()
        window_width = Window.get_size()[0]

        print("*" * window_width)
        print("--x-O-x--".center(window_width))
        print()
        print("NaN Air".center(window_width))
        print()
        print("*" * window_width)

    @staticmethod
    def __print_main_options(selected_option=""):
        window_width = Window.get_size()[0]

        #Calculate how much space should be between each main option
        spaces_between = " " * ((window_width - MenuUI.MAIN_OPTIONS_CHAR_COUNT) // (len(MenuUI.MAIN_OPTIONS) - 1))

        #Print the options normally if no option is selected
        if not selected_option:
            print(spaces_between.join(MenuUI.MAIN_OPTIONS))

        #Underline the selected option
        else:
            main_options = []
            for option in MenuUI.MAIN_OPTIONS:
                if selected_option == option:
                    option = TextEditor.format_text(option, TextEditor.UNDERLINE_TEXT)
                main_options.append(option)

            print(spaces_between.join(main_options))

    @staticmethod
    def print_header(selected_option=""):
        '''Prints the NaN Air banner and the main options below the banner'''
        MenuUI.__print_banner()
        MenuUI.__print_main_options(selected_option)
