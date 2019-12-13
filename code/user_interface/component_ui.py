from user_interface.text_editor import TextEditor
from user_interface.window import Window

class ComponentUI:

    @staticmethod
    def fill_window_and_print_action_line(menu_line_count, is_submit_available=False, submit_message="", is_check_voyages_available=False):
        bottom_space_for_user_input = 2
        if is_submit_available or submit_message:
            bottom_space_for_user_input += 1
        window_width, window_height = Window.get_size()
        body_height = window_height - ComponentUI.get_header_height()
        offset_bottom_window = body_height - menu_line_count - bottom_space_for_user_input
        for _ in range(offset_bottom_window):
            print()
        if is_submit_available and is_check_voyages_available:
            print('(S)ubmit    (C)heck voyages')
        elif is_submit_available:
            print('(S)ubmit')
        elif submit_message:
            print(TextEditor.edit_text(submit_message, TextEditor.GREEN_TEXT, text_format=TextEditor.BOLD_TEXT))

        print('_' * window_width)

    @staticmethod
    def print_frame_menu(option_tuple, underlined_main_option, underlined_sub_option="", save_message=""):
        ComponentUI.print_header(underlined_main_option)
        print(TextEditor.format_text(underlined_sub_option, TextEditor.UNDERLINE_TEXT))

        for i, option in enumerate(option_tuple):
            print("({}) {}".format(i+1, option))

        ComponentUI.fill_window_and_print_action_line(len(option_tuple)+1, False, save_message)

    @staticmethod
    def print_frame_constructor_menu(option_tuple, underlined_main_option, underlined_sub_option,\
         user_input_list, print_submit=False, selected_option_index=1000, greyed_out_option_index_list=[], greyed_with_out_number=False, print_check_voyages=False):

        ComponentUI.print_header(underlined_main_option)
        print(TextEditor.format_text(underlined_sub_option, TextEditor.UNDERLINE_TEXT))

        for i, option in enumerate(option_tuple):
            if i in greyed_out_option_index_list and greyed_with_out_number:
                prefix_str = " - "
            else:
                prefix_str = "(" + str(i+1) +")"


            if print_submit:
                print("{} {}: {}".format(prefix_str, TextEditor.color_text(option, TextEditor.DARKGRAY_TEXT)\
                     if i in greyed_out_option_index_list else option, "" if not user_input_list else user_input_list[i]))
            else:
                print("- {}: {}".format(option if selected_option_index != i else TextEditor.edit_text(option, TextEditor.BLUE_TEXT, text_format=TextEditor.BOLD_TEXT),\
                     "" if not user_input_list else user_input_list[i]))

        ComponentUI.fill_window_and_print_action_line(len(option_tuple)+1, print_submit, is_check_voyages_available=print_check_voyages)

    @staticmethod
    def print_frame_table_menu(heads, value_tuple, table_height, underlined_main_option, underlined_sub_option, print_submit=False, greyout_line_list=[]):

        ComponentUI.print_header(underlined_main_option)
        print(TextEditor.format_text(underlined_sub_option, TextEditor.UNDERLINE_TEXT))

        ComponentUI.fill_in_table(heads, value_tuple, True, greyout_line_list)

        ComponentUI.fill_window_and_print_action_line(table_height+2, print_submit) 

    # @staticmethod
    # def run_constructor(option_tuple, underlined_main_option_str, underlined_sub_option_str,\
    #     input_message_list_str, value_getter_function, user_input_list=None, greyed_out_option_index_list=None):

    #     #Fill the input list with all the string values the user has inputted
    #     #and whether or not that input value was valid
    #     if not user_input_list:
    #         user_input_list = [["", False]] * len(option_tuple)

    #     valid_input_list = []

    #     #Get all the valid inputs(1,2,3,...)
    #     for i in range(len(option_tuple)):
    #         if greyed_out_option_index_list:
    #             if i not in greyed_out_option_index_list:
    #                 valid_input_list.append(i)
    #         else:
    #             valid_input_list.append(i)

    #     user_input = ""

    #     while user_input not in ComponentUI.get_navigation_options_tuple():

    #         ComponentUI.print_frame_constructor_menu(option_tuple, underlined_main_option_str,\
    #                 underlined_sub_option_str,  user_input_list, True, )

    #         user_input = ComponentUI.get_user_input()

    #         if not user_input:
    #             continue

    #         user_input = ComponentUI.remove_brackets(user_input)

    #         if user_input in valid_input_list:

    #             selected_index = int(user_input) - 1

    #             ComponentUI.print_frame_constructor_menu(option_tuple, underlined_main_option_str,\
    #                     underlined_sub_option_str, user_input_list, False, selected_index, greyed_out_option_index_list, True)
            


            


    
    # # @staticmethod
    # # def run_option_select(option_tuple)




    @staticmethod
    def run_frame(option_tuple, underlined_main_option, valid_user_inputs, frame_functions):
        user_input = ""

        while user_input not in ComponentUI.get_navigation_options_tuple():

            if user_input:
                if "has been" in user_input:
                    ComponentUI.print_frame_menu(option_tuple, underlined_main_option, save_message=user_input)
                else:
                    ComponentUI.print_frame_menu(option_tuple, underlined_main_option)
            else:
                ComponentUI.print_frame_menu(option_tuple, underlined_main_option)

            user_input = ComponentUI.get_user_input()

            if not user_input:
                continue

            user_input = ComponentUI.remove_brackets(user_input)

            if user_input in valid_user_inputs:

                selected_index = int(user_input) - 1

                user_input = frame_functions[selected_index]()

        return user_input

    ############# HEADER RELATED FUNCTIONS AND VARIABLES #################

    __MAIN_OPTIONS = ("(V)oyages", "(E)mployees", "(A)irplanes", "(F)light routes", "(Q)uit")
    __MENU_VALID_OPTIONS_TUPLE = ('v', 'e', 'a', 'f', 'q')
    __MAIN_OPTIONS_CHAR_COUNT = sum([len(i) for i in __MAIN_OPTIONS])
    __HEADER_HEIGHT = 7

    @staticmethod # NOT IN USE CHECK - IF POSSIBLE TO TAKE OUT
    def print_table(table_header_tuple, value_list):
        ComponentUI.fill_in_table(table_header_tuple, value_list, False)
        ComponentUI.fill_window_and_print_action_line(len(value_list)+2)

    @staticmethod
    def get_navigation_options_tuple():
        return ComponentUI.__MENU_VALID_OPTIONS_TUPLE

    @staticmethod
    def get_header_height():
        '''Returns the height of the header in characters'''
        return ComponentUI.__HEADER_HEIGHT

    @staticmethod
    def get_main_options():
        return ComponentUI.__MAIN_OPTIONS

    @staticmethod
    def __print_banner():
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
                    option = TextEditor.format_text(option, TextEditor.UNDERLINE_TEXT + TextEditor.BOLD_TEXT)
                main_options.append(option)

            print(spaces_between.join(main_options))

    @staticmethod
    def print_header(selected_option=""):
        '''Prints the NaN Air banner and the main options below the banner'''
        Window.clear()
        ComponentUI.__print_banner()
        ComponentUI.__print_main_options(selected_option)

    


    @staticmethod
    def centered_text_message(message_str, second_line_str='', offset=2):
        '''Prints a centered feedback message'''

        window_width, window_height = Window.get_size()

        #Calculate the how much space is left on the window
        body_height = window_height - ComponentUI.get_header_height()

        #Calculate how many new lines should be both above and below the quit text
        offsetted_body_height_center = (body_height//2) - offset
        for _ in range(offsetted_body_height_center):
            print()
        print(message_str.center(window_width))
        print(second_line_str.center(window_width))
        for _ in range(offsetted_body_height_center+1):
            print()

        print("_" * window_width)

  ############# TABLE RELATED FUNCTIONS #################
    __DEFAULT_SPACE_BETWEEN_COLUMNS = 2

    @staticmethod
    def generate_columns_registration_list(heads, values, between=__DEFAULT_SPACE_BETWEEN_COLUMNS):
        '''generate list of number that is used for align space in tables'''
        longest_values = []
        for head in heads:
            longest_values.append(len(head))

        for i, column in enumerate(values):
            for row in column:
                row_value = row
                testlength = len(str(row_value))
                
                if testlength > longest_values[i]:
                    longest_values[i] = testlength

        return longest_values

    @staticmethod
    def generate_columns_registration_string(heads, getfunctions, between=__DEFAULT_SPACE_BETWEEN_COLUMNS):
        ''' generate string that can be used as format info in table row '''
        ''' to use in table that not will use fill in table function '''
        
        registration_list = ComponentUI.generate_columns_registration_list(heads, getfunctions, between)

        columns_registration = ""
        for reg in registration_list:
            columns_registration = columns_registration + "{:<"+str(reg+between)+"s}"

        return columns_registration

    @staticmethod
    def fill_in_table(heads, getfunctions, has_numbers=True, greyout_line_list=[], between=__DEFAULT_SPACE_BETWEEN_COLUMNS):
        ''' Fill in and print out table'''

        registration_list = ComponentUI.generate_columns_registration_list(heads, getfunctions, between)

        

        if has_numbers:
            print("{:<5s}".format(""),end="")
        for i in range(len(heads)):
            reg = "{:<"+str(registration_list[i]+between)+"s}"
            print(reg.format(heads[i]),end="")
        print()

        for row in range(len(getfunctions[0])):
            if has_numbers:
                brc= " (" if row < 9 else "("  #ajust alignment in case of more then 9 lines 
                print(brc+str(row+1)+")",end=" ")

            for i in range(len(heads)):
                reg = "{:<"+str(registration_list[i]+between)+"s}"
                if row in greyout_line_list:
                    option = reg.format(str(getfunctions[i][row]))
                    print(TextEditor.edit_text(option, TextEditor.DARKGRAY_TEXT), end="")
                    
                else:    
                    print(reg.format(str(getfunctions[i][row])),end="")
            print()



    ############# USER CHOSE ACTION RELATED FUNCTIONS #################

    @staticmethod
    def get_user_input(message="Your action: "):
        return input(message).lower().strip()

    @staticmethod
    def remove_brackets(user_input):
        if user_input.startswith("(") and user_input.endswith(")") and len(user_input)>2:
            user_input = user_input[1:-1] #in case if user inputs "()" around the number

        return user_input

    @staticmethod
    def test_user_input_chose_index(user_input, menu_list):
        '''Test if input from user can be handle as int and used as index  - return int or False'''
        
        user_input = ComponentUI.remove_brackets(user_input)

        try:
            # test if user inputs is valid number
            user_input_chose_index = abs(int(user_input)) #"abs" in case if user inputs "-" in front of number
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
        