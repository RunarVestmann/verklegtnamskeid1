from user_interface.menu_ui import MenuUI
from user_interface.window import Window
from user_interface.text_editor import TextEditor
from user_interface.component_ui import ComponentUI
from apis.logic_api import LogicAPI

class VoyageUI:

    @staticmethod
    def show_voyage_menu():
        MenuUI.print_header(MenuUI.get_main_options()[0])
        option_tuple = ('New voyage', 'Show ongoing voyages','Show completed voyages', 'Find voyages by date', 'Find voyages by week', 'Find voyages by destination')
        option_functions = (VoyageUI.show_new_voyage_constructor, VoyageUI.show_ongoing_voyages, VoyageUI.show_completed_voyages,\
            VoyageUI.show_find_voyages_by_date, VoyageUI.show_find_voyages_by_week, VoyageUI.show_find_voyages_by_destination)

        #Generate a tuple that holds all the valid user inputs
        valid_user_options_tuple = ComponentUI.make_valid_menu_options_tuple(len(option_tuple))

        user_input = ''

        #Keep displaying this menu as long as the user doesn't select anything
        while user_input not in valid_user_options_tuple:

            print()
            for i, option in enumerate(option_tuple):
                print("({}) {}".format(i+1,option))
            MenuUI.fill_window_and_print_action_line(len(option_tuple)+1)
            user_input = input("Your action: ").lower().strip()

            ####  Test input ####            
            selected_number = ComponentUI.test_user_input_chose_index(user_input, len(option_tuple)) #eather int>0 or False - may not be 0
            if selected_number:                                                                      #and is with in range of possible menu list
                selected_index = selected_number-1
                option_functions[selected_index](option_tuple[selected_index])
            else:
                VoyageUI.show_voyage_menu()


    @staticmethod
    def show_new_voyage_constructor(title):
        MenuUI.print_header(MenuUI.get_main_options()[0])
        title = TextEditor.format_text(title, TextEditor.UNDERLINE_TEXT)
        print(title)
        constructor_voyage_tuple = ('Flight route', 'Voyage schedule', 'Airplane', 'Pilots', 'Flight attendants')
        for i, option in enumerate(constructor_voyage_tuple):
            print("({}) {}: ".format(i+1,option))

        MenuUI.fill_window_and_print_action_line(len(constructor_voyage_tuple)+1, True)
        user_input = input("Your action: ").lower().strip()

    @staticmethod
    def show_ongoing_voyages(title):
        # MenuUI.print_header(MenuUI.get_main_options()[0])
        # title = TextEditor.format_text(title, TextEditor.UNDERLINE_TEXT)
        # print(title)
        pass

    
    
    @staticmethod
    def show_completed_voyages(title):
        # MenuUI.print_header(MenuUI.get_main_options()[0])
        # title = TextEditor.format_text(title, TextEditor.UNDERLINE_TEXT)
        # print(title)
        pass
    
    @staticmethod    
    def show_find_voyages_by_date(title):
        # MenuUI.print_header(MenuUI.get_main_options()[0])
        # title = TextEditor.format_text(title, TextEditor.UNDERLINE_TEXT)
        # print(title)
        pass
    
    @staticmethod
    def show_find_voyages_by_week(title):
        # MenuUI.print_header(MenuUI.get_main_options()[0])
        # title = TextEditor.format_text(title, TextEditor.UNDERLINE_TEXT)
        # print(title)
        pass
    
    @staticmethod
    def show_find_voyages_by_destination(title):
        # MenuUI.print_header(MenuUI.get_main_options()[0])
        # title = TextEditor.format_text(title, TextEditor.UNDERLINE_TEXT)
        # print(title)
        pass

 
        
        