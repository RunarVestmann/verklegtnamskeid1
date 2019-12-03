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
        window_width, window_height = Window.get_size()

        #Calculate the how much space is left on the window
        body_height = window_height - MenuUI.get_header_height()

        #Calculate how many new lines should be both above and below the quit text
        offsetted_body_height_center = (body_height//2) - 2

        #Print the empty space above the welcome text
        for _ in range(offsetted_body_height_center):
            print()

        print("Welcome to the NaN Air booking software".center(window_width))
        print("Press any of the keys in the brackets '()' to get started".center(window_width))

        #Print the empty space below the welcome text
        for _ in range(offsetted_body_height_center):
            print()

        print("_" * window_width)

    @staticmethod
    def initialize():
        #Call the timer and check if any flight,
        #voyage or employee state needs to be updated according to the current time
        #also check all of them and start an async/await for when the states will get updated
        pass

    @staticmethod
    def get_header_height():
        '''Returns the height of the header in characters'''
        return MenuUI.__HEADER_HEIGHT

    @staticmethod
    def get_main_options():
        return MenuUI.__MAIN_OPTIONS

    @staticmethod
    def fill_window_and_print_action_line(menu_line_count, is_submit_available=False):
        bottom_space_for_user_input = 2
        if is_submit_available:
            bottom_space_for_user_input += 1
        window_width, window_height = Window.get_size()
        body_height = window_height - MenuUI.get_header_height()
        offset_bottom_window = body_height - menu_line_count - bottom_space_for_user_input
        for _ in range(offset_bottom_window):
            print()
        if is_submit_available:
            print('(S)ubmit')
        print('_' * window_width)

    @staticmethod
    def print_header(selected_option=""):
        '''Prints the NaN Air banner and the main options below the banner'''
        MenuUI.__print_banner()
        MenuUI.__print_main_options(selected_option)

    @staticmethod
    def test_user_input_chose_index(input_form_user, menu_list):
        '''Test if input from user can be handle as int and used as index  - return int or False'''
        if input_form_user.startswith("(") and input_form_user.endswith(")") and len(input_form_user)>2:
            input_form_user = input_form_user[1:-1] #in case if user inputs "()" around the number

        try:
            # test if user inputs is valid number
            user_input_chose_index = abs(int(input_form_user)) #"abs" in case if user inputs "-" in front of number
            if user_input_chose_index > menu_list:
                user_input_chose_index = False #not valid if out range of menu list
        except: 
            user_input_chose_index = False #not valid if string can not handle as int

        return user_input_chose_index    

    @staticmethod
    def show_main_menu():

        MenuUI.print_header()
        MenuUI.__print_main_menu_body()

        user_input = input("Your action: ").lower().strip()
        #if checks...
    