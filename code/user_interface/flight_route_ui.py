from user_interface.window import Window
from user_interface.text_editor import TextEditor
from user_interface.component_ui import ComponentUI
from apis.logic_api import LogicAPI

class FlightRouteUI:
    __option_tuple = ('New flight route', 'Show all flight routes')
     

    @staticmethod
    def show_flight_route_menu():
        ComponentUI.print_header(ComponentUI.get_main_options()[3])
        option_tuple = FlightRouteUI.__option_tuple
        print()
        for i, option in enumerate(option_tuple):
            print("({}) {}".format(i+1,option))
        ComponentUI.fill_window_and_print_action_line(len(option_tuple)+1)
        
    @staticmethod
    def action_flight_route_menu(user_input):
        option_tuple = FlightRouteUI.__option_tuple  #ath 
        option_functions = (FlightRouteUI.show_new_flight_route_constructor, FlightRouteUI.show_all_flight_routes)


        ####  Test input ####            
        selected_number = ComponentUI.test_user_input_chose_index(user_input, len(option_tuple)) #eather int>0 or False - may not be 0
        if selected_number:                                                                  #and is with in range of possible menu list
            selected_index = selected_number-1
            new_display = [option_functions[selected_index], FlightRouteUI.action_new_flight_route]
            return new_display
        else:
            return False


    @staticmethod
    def show_new_flight_route_constructor():
        ComponentUI.print_header(ComponentUI.get_main_options()[3])
        print(TextEditor.format_text(FlightRouteUI.__option_tuple[0], TextEditor.UNDERLINE_TEXT))
        constructor_flrt_tuple = ('Country', 'Destination', 'Airport id', 'Flight time', 'Distance from Iceland', 'Contact name', 'Emergency phonenumber')
        for i, option in enumerate(constructor_flrt_tuple):
            print("({}) {}: ".format(i+1,option))

        ComponentUI.fill_window_and_print_action_line(len(constructor_flrt_tuple)+1, True)
    
    @staticmethod
    def action_new_flight_route(user_input):
        #option_functions = (FlightRouteUI.field_new_input)

        ####  Test input ####            
        selected_number = user_input # ComponentUI.test_user_input_chose_index(user_input, 7) #ath           #eather int>0 or False - may not be 0
        if selected_number == '1':                                                                  #and is with in range of possible menu list
            #selected_index = selected_number-1
            new_display = [FlightRouteUI.field_new_input, FlightRouteUI.action_field_new_input,"Insert country name: "]
            return new_display
        else:
            return False

    
    
    @staticmethod
    def field_new_input():
        ComponentUI.print_header(ComponentUI.get_main_options()[3])
        print(TextEditor.format_text(FlightRouteUI.__option_tuple[0], TextEditor.UNDERLINE_TEXT))
        ComponentUI.fill_window_and_print_action_line(2)

    @staticmethod
    def action_field_new_input(user_input):
        pass





    @staticmethod
    def show_all_flight_routes():
        ComponentUI.print_header(ComponentUI.get_main_options()[3])
        print(TextEditor.format_text(FlightRouteUI.__option_tuple[1], TextEditor.UNDERLINE_TEXT))
        
        table_header = ("Destination", "Airport", "Country", "Flight-time", "Distance", "Contact", "Emergency phone")
        flrt_list = LogicAPI.get_all_flight_routes()
        flight_routes_getfunctions_tuple = ([flightr.get_destination for flightr in flrt_list],[flightr.get_airport_id for flightr in flrt_list],\
            [flightr.get_country for flightr in flrt_list],[flightr.get_flight_time for flightr in flrt_list],[flightr.get_distance_from_iceland for flightr in flrt_list],\
                [flightr.get_contact_name for flightr in flrt_list],[flightr.get_emergency_phone for flightr in flrt_list])

        ComponentUI.fill_in_table(table_header,flight_routes_getfunctions_tuple, False)
                 
        ComponentUI.fill_window_and_print_action_line(len(flrt_list)+2)
        



