from user_interface.window import Window
from user_interface.text_editor import TextEditor
from user_interface.component_ui import ComponentUI
from apis.logic_api import LogicAPI

class FlightRouteUI:
    __option_tuple = ('New flight route', 'Show all flight routes')
    __constructor_flrt_tuple = ('Country', 'Destination', 'Airport id', 'Flight time', 'Distance from Iceland', 'Contact name', 'Emergency phonenumber')
    __input_field_tuple = tuple(["Insert" + option + ": " for option in __constructor_flrt_tuple])
    
    # __show_functions = (show_new_country_input_field)

    @staticmethod
    def __print_flight_route_menu():
        ComponentUI.print_header(ComponentUI.get_main_options()[3])
        print()
        for i, option in enumerate(FlightRouteUI.__option_tuple):
            print("({}) {}".format(i+1,option))
        ComponentUI.fill_window_and_print_action_line(len(FlightRouteUI.__option_tuple)+1)

    @staticmethod
    def show_flight_route_menu():

        menu_option_functions = (FlightRouteUI.__show_new_flight_route_constructor,\
             FlightRouteUI.__show_all_flight_routes)

        valid_input = False

        while not valid_input:

            FlightRouteUI.__print_flight_route_menu()

            user_input = input("Your action: ").lower().strip()

            user_input = ComponentUI.remove_brackets(user_input)

            if user_input[0].isdigit():
                valid_input = ComponentUI.test_user_input_chose_index(user_input, len(menu_option_functions))
                if valid_input:
                    index = valid_input - 1
                    menu_option_functions[index]()
            
            return user_input

    @staticmethod
    def action_flight_route_menu(user_input):
        option_tuple = FlightRouteUI.__option_tuple
        option_functions = (FlightRouteUI.__show_new_flight_route_constructor, FlightRouteUI.__show_all_flight_routes)
        action_functions = (FlightRouteUI.action_new_flight_route, False)

        ####  Test input ####            
        selected_number = ComponentUI.test_user_input_chose_index(user_input, len(option_tuple)) #eather int>0 or False - may not be 0
        if selected_number:                                                                  #and is with in range of possible menu list
            selected_index = selected_number-1
            new_display = [option_functions[selected_index], action_functions[selected_index] if action_functions[selected_index] else False ]
            return new_display
        else:
            return False


    @staticmethod
    def __show_input_field_options(user_input_list, in_field = False):
        ComponentUI.print_header(ComponentUI.get_main_options()[3])
        print(TextEditor.format_text(FlightRouteUI.__option_tuple[0], TextEditor.UNDERLINE_TEXT))

        if not in_field:
            for i, option in enumerate(FlightRouteUI.__constructor_flrt_tuple):
                print("({}) {}: {}".format(i+1,option, "" if not user_input_list else user_input_list[i]))
        else: 
            for i, option in enumerate(FlightRouteUI.__constructor_flrt_tuple):
                print("- {}: {}".format(option, "" if not user_input_list else user_input_list[i]))

        ComponentUI.fill_window_and_print_action_line(len(FlightRouteUI.__constructor_flrt_tuple)+1, not in_field)

    @staticmethod
    def __show_new_flight_route_constructor():

        user_input = ""

        valid_options = list(ComponentUI.make_valid_menu_options_tuple(\
            len(FlightRouteUI.__constructor_flrt_tuple))) + \
                list(ComponentUI.get_menu_valid_options_tuple())

        user_input_list = []

        while user_input not in valid_options:

            FlightRouteUI.__show_input_field_options(user_input_list)

            user_input = input("Your action: ").lower().split()

            valid_input = ComponentUI.test_user_input_chose_index(user_input, len(FlightRouteUI.__constructor_flrt_tuple))

            if valid_input:
                index = valid_input - 1
                
                FlightRouteUI.__show_input_field_options(user_input_list, True)
                user_input = input(FlightRouteUI.__input_field_tuple[index]).lower().strip()

                #error check

                user_input_list.append(user_input)
                
                
    # @staticmethod
    # def show_new_country_input_field(user_input_list):
    #     FlightRouteUI.__show_input_field_options(user_input_list, )





        
    
    @staticmethod
    def action_new_flight_route(user_input):
        #option_functions = (FlightRouteUI.field_new_input)

        ####  Test input ####            
        selected_number = ComponentUI.test_user_input_chose_index(user_input, 7) #ath           #eather int>0 or False - may not be 0
        if selected_number:                                                                  #and is with in range of possible menu list
            #selected_index = selected_number-1
            new_display = [FlightRouteUI.__show_new_flight_route_constructor, FlightRouteUI.action_field_new_input,"Insert country name: "]
            return new_display
        else:
            return False

    
    
    @staticmethod
    def field_new_input():
        ComponentUI.print_header(ComponentUI.get_main_options()[3])
        print(TextEditor.format_text(FlightRouteUI.__option_tuple[0], TextEditor.UNDERLINE_TEXT))
        print("eitthvað sniðugt")
        ComponentUI.fill_window_and_print_action_line(2)

    @staticmethod
    def action_field_new_input(user_input):
        FlightRouteUI.field_new_input()
        
    @staticmethod
    def __show_all_flight_routes():
        ComponentUI.print_header(ComponentUI.get_main_options()[3])
        print(TextEditor.format_text(FlightRouteUI.__option_tuple[1], TextEditor.UNDERLINE_TEXT))
        
        table_header = ("Destination", "Airport", "Country", "Flight-time", "Distance", "Contact", "Emergency phone")
        flrt_list = LogicAPI.get_all_flight_routes()
        flight_routes_getfunctions_tuple = ([flightr.get_destination for flightr in flrt_list],[flightr.get_airport_id for flightr in flrt_list],\
            [flightr.get_country for flightr in flrt_list],[flightr.get_flight_time for flightr in flrt_list],[flightr.get_distance_from_iceland for flightr in flrt_list],\
                [flightr.get_contact_name for flightr in flrt_list],[flightr.get_emergency_phone for flightr in flrt_list])

        ComponentUI.fill_in_table(table_header,flight_routes_getfunctions_tuple, False)
                 
        ComponentUI.fill_window_and_print_action_line(len(flrt_list)+2)
        

