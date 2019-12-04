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
        MenuUI.print_header(MenuUI.get_main_options()[3])
        title = TextEditor.format_text(title, TextEditor.UNDERLINE_TEXT)
        print(title)
        
        # print("{:<15s} {:<8s} {:<15s} {:<15s} {:<10s} {:<15s} {:<10s}".format(table_header[0], table_header[1],\
        #      table_header[2], table_header[3], table_header[4], table_header[5], table_header[6]))

        BETWEENCOLOMS = 4
        flrt = LogicAPI.get_all_flight_routes()
        table_header = ("Destination", "Airport", "Country", "Flight-time", "Distance", "Contact ", "Emergency phone")
        longest_dest = len(table_header[0])
        longest_airp = len(table_header[1])
        longest_coun = len(table_header[2])
        longest_time = len(table_header[3])
        longest_dist = len(table_header[4])
        longest_cont = len(table_header[5])
        longest_phon = len(table_header[6])
        
        for c_elem in flrt:
            compare = len (c_elem.get_destination())
            if compare > longest_dest:
                longest_dest = compare
            compare = len (c_elem.get_airport_id())
            if compare > longest_airp:
                longest_airp = compare
            compare = len (c_elem.get_country())
            if compare > longest_coun:
                longest_coun = compare    
            compare = len (c_elem.get_flight_time())
            if compare > longest_time:
                longest_time = compare 
            compare = len (c_elem.get_distance_from_iceland())
            if compare > longest_dist:
                longest_dist = compare
            compare = len (c_elem.get_contact_name())
            if compare > longest_cont:
                longest_cont = compare      
            compare = len (c_elem.get_emergency_phone())
            if compare > longest_phon:
                longest_phon = compare 

        BETWEENCOLOMS = 4
        colon_registration = "{:<"+str(longest_dest+BETWEENCOLOMS)+"s}{:<"\
            +str(longest_airp+BETWEENCOLOMS)+"s}{:<"\
            +str(longest_coun+BETWEENCOLOMS)+"s}{:<"\
            +str(longest_time+BETWEENCOLOMS)+"s}{:<"\
            +str(longest_dist+BETWEENCOLOMS)+"s}{:<"\
            +str(longest_cont+BETWEENCOLOMS)+"s}{:<"\
            +str(longest_phon+BETWEENCOLOMS)+"s}"
        
        print(colon_registration.format(table_header[0], table_header[1],\
            table_header[2], table_header[3], table_header[4], table_header[5], table_header[6]))
       
        for element in flrt:
            print(colon_registration.format(element.get_destination(), element.get_airport_id(), element.get_country(),\
                 element.get_flight_time(), element.get_distance_from_iceland(), element.get_contact_name(), element.get_emergency_phone()))
                 
        MenuUI.fill_window_and_print_action_line(len(flrt)+2)
        user_input = input("Your action: ").lower().strip()


