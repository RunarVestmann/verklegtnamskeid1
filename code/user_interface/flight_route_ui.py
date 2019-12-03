from user_interface.menu_ui import MenuUI
from user_interface.window import Window
from user_interface.text_editor import TextEditor
from apis.logic_api import LogicAPI

class FlightRouteUI:

    @staticmethod
    def show_flight_route_menu():
        MenuUI.print_header(MenuUI.get_main_options()[3])
        option_list = ('New flightroute', 'Show all flight routes')
        option_functions = (FlightRouteUI.show_new_flight_route_constructor, FlightRouteUI.show_all_flight_routes)
        print()
        for i, option in enumerate(option_list):
            print("({}) {}".format(i+1,option))
        MenuUI.fill_window_and_print_action_line(len(option_list)+1)
        user_input = input("Your action: ").lower().strip()

        ####  Test input ####            
        selected_number = MenuUI.test_user_input_chose_index(user_input, len(option_list)) #eather int>0 or False - may not be 0
        if selected_number:                                                                #and is with in range of possible menu list
            selected_index = selected_number-1
            option_functions[selected_index](option_list[selected_index])
        else:
            FlightRouteUI.show_flight_route_menu()


    @staticmethod
    def show_new_flight_route_constructor(title):
        MenuUI.print_header(MenuUI.get_main_options()[3])
        title = TextEditor.format_text(title, TextEditor.UNDERLINE_TEXT)
        print(title)
        constructor_option_list = ('Country', 'Destination', 'Airport id', 'Flight time', 'Distance from Iceland', 'Contact name', 'Emergency phonenumber')
        for i, option in enumerate(constructor_option_list):
            print("({}) {}: ".format(i+1,option))

        MenuUI.fill_window_and_print_action_line(len(constructor_option_list)+1, True)
        user_input = input("Your action: ").lower().strip()

    @staticmethod
    def show_all_flight_routes(title):
        table_header = ("Destination", "Airport", "Country", "Flight-time", "Distance", "Contact ", "Emergency phone")
        MenuUI.print_header(MenuUI.get_main_options()[3])
        title = TextEditor.format_text(title, TextEditor.UNDERLINE_TEXT)
        print(title)
        print("{:<15s} {:<8s} {:<15s} {:<15s} {:<10s} {:<15s} {:<10s}".format(table_header[0], table_header[1],\
             table_header[2], table_header[3], table_header[4], table_header[5], table_header[6]))

        flrt = LogicAPI.get_all_flight_routes()
        for element in flrt:
            print("{:<15s} {:<8s} {:<15s} {:<15s} {:<10s} {:<15s} {:<10s}".format(element.get_destination(), element.get_airport_id(), element.get_country(),\
                 element.get_flight_time(), element.get_distance_from_iceland(), element.get_contact_name(), element.get_emergency_phone()))
                 
        MenuUI.fill_window_and_print_action_line(len(flrt)+2)
        user_input = input("Your action: ").lower().strip()


