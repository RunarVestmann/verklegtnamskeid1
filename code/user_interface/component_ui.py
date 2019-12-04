from user_interface.text_editor import TextEditor
from user_interface.window import Window



class ComponentUI:

############# TABLE REALADED FUNCTIONs #################
    __DEFAULT_SPACE_BETWEEN_COLOMNS = 2


  #workinprogress - Gummi
    @staticmethod
    def generate_colomns_registration_list(heads, getfunctions, between=__DEFAULT_SPACE_BETWEEN_COLOMNS):
        '''generate list of number that is used for align space in tables'''
        longest_values = []
        for head in heads:
            longest_values.append(len(head))

        for i, colomn in enumerate(getfunctions):
            for row in colomn:
                if len(row()) > longest_values[i]:
                    longest_values[i] = len(row())

        return longest_values

    @staticmethod
    def generate_colomns_registration_string(heads, getfunctions, between=__DEFAULT_SPACE_BETWEEN_COLOMNS):
        ''' generate string that can be used as format info in table row '''
        ''' to use in table that not will use fill in table function '''
        
        registration_list = ComponentUI.generate_colomns_registration_list(heads, getfunctions, between)

        colomns_registration = ""
        for reg in registration_list:
            colomns_registration = colomns_registration + "{:<"+str(reg+between)+"s}"

        return colomns_registration

    @staticmethod
    def fill_in_table(heads, getfunctions, has_numbers=True, between=__DEFAULT_SPACE_BETWEEN_COLOMNS):
        ''' Fill in and print out table'''

        registration_list = ComponentUI.generate_colomns_registration_list(heads, getfunctions, between)

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


    ############# USER CHOSE ACTION REALADED FUNCTIONS #################

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

        