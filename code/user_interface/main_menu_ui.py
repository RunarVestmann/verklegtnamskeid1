from user_interface.text_editor import TextEditor
from user_interface.window import Window
from user_interface.component_ui import ComponentUI
from user_interface.voyage_ui import VoyageUI
from user_interface.employees_ui import EmployeeUI
from user_interface.airplanes_ui import AirplanesUI
from user_interface.flight_route_ui import FlightRouteUI
from user_interface.quit_ui import QuitUI


class MainMenuUI:

    __MAIN_MENU_VALID_OPTIONS_TUPLE = ('v', 'e', 'a', 'f', 'q')

    @staticmethod
    def __print_main_menu_body():
        window_width, window_height = Window.get_size()

        #Calculate the how much space is left on the window
        body_height = window_height - ComponentUI.get_header_height()

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
    def show_frame(show_function, extra_menu_function=False, input_message="Your action: "):
        ''' common element around every display window '''
        user_input = ''
        valid_options_tuple = list(MainMenuUI.__MAIN_MENU_VALID_OPTIONS_TUPLE)
        
    

        while user_input not in valid_options_tuple:
            show_function() #function that needs to be handled
            user_input = input(input_message).lower().strip()
            MainMenuUI.main_menu_action(user_input, valid_options_tuple) #handle main menu options
            if extra_menu_function and user_input != '':
                new_menu = extra_menu_function(user_input) #handle sub-menu and other option than main menu
                if new_menu:
                    MainMenuUI.show_frame(new_menu)


    
    
    @staticmethod
    def show_main_menu():
        ComponentUI.print_header()
        MainMenuUI.__print_main_menu_body()

    @staticmethod
    def main_menu_action(user_input, valid_options_tuple):
        main_menu_option_functions = (MainMenuUI.show_voyage,MainMenuUI.show_employee,AirplanesUI.show_airplanes_menu, FlightRouteUI.show_flight_route_menu, MainMenuUI.show_quit)

        #If the user inputs nothing, we do nothing
        if not user_input:
            return

        #Remove brackets from each side of the user input string
        if user_input.startswith("(") and user_input.endswith(")") and len(user_input) > 2:
            user_input = user_input[1:-1] #in case if user inputs "()" around the number

        if user_input[0] in valid_options_tuple:
            main_menu_option_functions[valid_options_tuple.index(user_input[0])]()

    @staticmethod
    def confirm_quit(user_input):
        #Clear the window and exit the program if the user wants to exit
        if user_input.startswith('y'):
            QuitUI.terminate_program()
        elif user_input.startswith('n'):
            MainMenuUI.show_frame(MainMenuUI.show_main_menu)

    @staticmethod
    def show_voyage():
        MainMenuUI.show_frame(VoyageUI.show_voyage_menu,VoyageUI.action_voyage_menu)

    @staticmethod
    def show_employee():
        MainMenuUI.show_frame(EmployeeUI.show_employee_menu,EmployeeUI.action_employees_menu)
    
    
    @staticmethod
    def show_quit():
        MainMenuUI.show_frame(QuitUI.show_quit_menu2, MainMenuUI.confirm_quit)

    #það þarf að setja inn show fyrir alla flokkana og aðlaga Klasana að því!






             



    