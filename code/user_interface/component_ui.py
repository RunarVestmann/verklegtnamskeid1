from user_interface.text_editor import TextEditor
from user_interface.window import Window

class ComponentUI:

    @staticmethod
    def fill_window_and_print_action_line(menu_line_count, is_submit_available=False):
        bottom_space_for_user_input = 2
        if is_submit_available:
            bottom_space_for_user_input += 1
        window_width, window_height = Window.get_size()
        body_height = window_height - ComponentUI.get_header_height()
        offset_bottom_window = body_height - menu_line_count - bottom_space_for_user_input
        for _ in range(offset_bottom_window):
            print()
        if is_submit_available:
            print('(S)ubmit')
        print('_' * window_width)

    ############# HEADER RELATED FUNCTIONS AND VARIABLES #################

    __MAIN_OPTIONS = ("(V)oyages", "(E)mployees", "(A)irplanes", "(F)light routes", "(Q)uit")
    __MAIN_OPTIONS_CHAR_COUNT = sum([len(i) for i in __MAIN_OPTIONS])
    __HEADER_HEIGHT = 7

    @staticmethod
    def get_header_height():
        '''Returns the height of the header in characters'''
        return ComponentUI.__HEADER_HEIGHT

    @staticmethod
    def get_main_options():
        return ComponentUI.__MAIN_OPTIONS

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
        spaces_between = " " * ((window_width - ComponentUI.__MAIN_OPTIONS_CHAR_COUNT) // (len(ComponentUI.__MAIN_OPTIONS) - 1))

        #Print the options normally if no option is selected
        if not selected_option:
            print(spaces_between.join(ComponentUI.__MAIN_OPTIONS))

        #Underline the selected option
        else:
            main_options = []
            for option in ComponentUI.__MAIN_OPTIONS:
                if selected_option == option:
                    option = TextEditor.format_text(option, TextEditor.UNDERLINE_TEXT)
                main_options.append(option)

            print(spaces_between.join(main_options))

    @staticmethod
    def print_header(selected_option=""):
        '''Prints the NaN Air banner and the main options below the banner'''
        ComponentUI.__print_banner()
        ComponentUI.__print_main_options(selected_option)


    ############# TABLE RELATED FUNCTIONS #################
    __DEFAULT_SPACE_BETWEEN_columnS = 2

    @staticmethod
    def generate_columns_registration_list(heads, getfunctions, between=__DEFAULT_SPACE_BETWEEN_columnS):
        '''generate list of number that is used for align space in tables'''
        longest_values = []
        for head in heads:
            longest_values.append(len(head))

        for i, column in enumerate(getfunctions):
            for row in column:
                if len(row()) > longest_values[i]:
                    longest_values[i] = len(row())

        return longest_values

    @staticmethod
    def generate_columns_registration_string(heads, getfunctions, between=__DEFAULT_SPACE_BETWEEN_columnS):
        ''' generate string that can be used as format info in table row '''
        ''' to use in table that not will use fill in table function '''
        
        registration_list = ComponentUI.generate_columns_registration_list(heads, getfunctions, between)

        columns_registration = ""
        for reg in registration_list:
            columns_registration = columns_registration + "{:<"+str(reg+between)+"s}"

        return columns_registration

    @staticmethod
    def fill_in_table(heads, getfunctions, has_numbers=True, between=__DEFAULT_SPACE_BETWEEN_columnS):
        ''' Fill in and print out table'''

        registration_list = ComponentUI.generate_columns_registration_list(heads, getfunctions, between)

        for i in range(len(heads)):
            if has_numbers:
                print("{:<4s}".format(""),end="")
            reg =  "{:<"+str(registration_list[i]+between)+"s}"
            print(reg.format(heads[i]),end="")
        print()

        for row in range(len(getfunctions[0])):
            if has_numbers:
                print("("+str(row+1)+")",end=" ")

            for i in range(len(heads)):
                reg = "{:<"+str(registration_list[i]+between)+"s}"
                print(reg.format(getfunctions[i][row]()),end="")
            print()


    ############# USER CHOSE ACTION RELATED FUNCTIONS #################

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
    def make_valid_menu_options_tuple(option_count):
        '''Returns a tuple containing valid user inputs in menu screens'''
        valid_user_options_list = []
        for i in range(option_count):
            valid_user_options_list.append(str(i+1))
            valid_user_options_list.append("({})".format(i+1))

        return tuple(valid_user_options_list)

        