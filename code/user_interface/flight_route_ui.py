from user_interface.menu_ui import MenuUI
from user_interface.window import Window
from user_interface.text_editor import TextEditor
from user_interface.component_ui import ComponentUI
from apis.logic_api import LogicAPI

class FlightRouteUI:

    @staticmethod
    def show_flight_route_menu():
        MenuUI.print_header(MenuUI.get_main_options()[3])
        option_tuple = ('New flightroute', 'Show all flight routes')
        option_functions = (FlightRouteUI.show_new_flight_route_constructor, FlightRouteUI.show_all_flight_routes)

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
                FlightRouteUI.show_flight_route_menu()


    @staticmethod
    def show_new_flight_route_constructor(title):
        MenuUI.print_header(MenuUI.get_main_options()[3])
        title = TextEditor.format_text(title, TextEditor.UNDERLINE_TEXT)
        print(title)
        constructor_flrt_tuple = ('Country', 'Destination', 'Airport id', 'Flight time', 'Distance from Iceland', 'Contact name', 'Emergency phonenumber')
        for i, option in enumerate(constructor_flrt_tuple):
            print("({}) {}: ".format(i+1,option))

        MenuUI.fill_window_and_print_action_line(len(constructor_flrt_tuple)+1, True)
        user_input = input("Your action: ").lower().strip()

    @staticmethod
    def show_all_flight_routes(title):
        MenuUI.print_header(MenuUI.get_main_options()[3])
        title = TextEditor.format_text(title, TextEditor.UNDERLINE_TEXT)
        print(title)
        
        table_header = ("Destination", "Airport", "Country", "Flight-time", "Distance", "Contact ", "Emergency phone")
        flrt_list = LogicAPI.get_all_flight_routes()
        flight_routes_getfunctions_tuple = ([flightr.get_destination for flightr in flrt_list],[flightr.get_airport_id for flightr in flrt_list],\
            [flightr.get_country for flightr in flrt_list],[flightr.get_flight_time for flightr in flrt_list],[flightr.get_distance_from_iceland for flightr in flrt_list],\
                [flightr.get_contact_name for flightr in flrt_list],[flightr.get_emergency_phone for flightr in flrt_list])

        ComponentUI.fill_in_table(table_header,flight_routes_getfunctions_tuple, False)
                 
        MenuUI.fill_window_and_print_action_line(len(flrt_list)+2)
        user_input = input("Your action: ").lower().strip()


