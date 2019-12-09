from user_interface.window import Window
from user_interface.text_editor import TextEditor
from user_interface.component_ui import ComponentUI
from data_models.flight_route import FlightRoute
from apis.logic_api import LogicAPI

class FlightRouteUI:
    __FRAME_IN_USE_STR = ComponentUI.get_main_options()[3]
    NAVIGATION_BAR_OPTIONS = ComponentUI.get_navigation_options_tuple()
    FLIGHT_ROUTE_OPTION_TUBLE = ("Country", "Destination", "Airport id", "Flight time", "Distance from Iceland",\
             "Contact name", "Emergency phonenumber") # to use when displaying flight route profile and new flight route

    @staticmethod
    def show():
        option_tuple = ('New flight route', 'Show all flight routes')

        valid_user_inputs = ComponentUI.make_valid_menu_options_tuple(len(option_tuple))

        frame_functions = (FlightRouteUI.__show_new_flight_route_constructor, FlightRouteUI.__show_all_flight_routes)

        return ComponentUI.run_frame(option_tuple, FlightRouteUI.__FRAME_IN_USE_STR, valid_user_inputs, frame_functions)

    @staticmethod
    def __show_new_flight_route_constructor():

        #navigation_bar_options = ComponentUI.get_navigation_options_tuple()

        #option_tuple = ("Country", "Destination", "Airport id", "Flight time", "Distance from Iceland",\
        #     "Contact name", "Emergency phonenumber")

        valid_user_inputs = ComponentUI.make_valid_menu_options_tuple(len(FlightRouteUI.FLIGHT_ROUTE_OPTION_TUBLE))

        input_message_tuple = ("Insert Country: ", "Insert Destination: ", "Insert Airport id: ", "Insert Flight time(hours:minutes): ",\
             "Insert Distance from Iceland in km: ", "Insert Contact name: ", "Insert Emergency phonenumber: ")

        user_input_list = [""] * len(FlightRouteUI.FLIGHT_ROUTE_OPTION_TUBLE)

        user_input = ""

        flight_route_info_already_exists = False

        while user_input not in FlightRouteUI.NAVIGATION_BAR_OPTIONS:

            ComponentUI.print_frame_constructor_menu(FlightRouteUI.FLIGHT_ROUTE_OPTION_TUBLE, \
                ComponentUI.get_main_options()[3], "New flight route", user_input_list, True)

            user_input = ComponentUI.get_user_input()

            if not user_input:
                continue

            user_input = ComponentUI.remove_brackets(user_input)

            if user_input in valid_user_inputs:
                index = int(user_input) - 1
                ComponentUI.print_frame_constructor_menu(FlightRouteUI.FLIGHT_ROUTE_OPTION_TUBLE,\
                     ComponentUI.get_main_options()[3], "New flight route", user_input_list, False, index)

                user_input = input(input_message_tuple[index]).strip()

                if not user_input:
                    continue

                #Capitalize the first letter of the Country and Destination
                if index == 0 or index == 1:
                    user_input = user_input.capitalize()

                #Check if the airport id already exists
                elif index == 3:
                    if not LogicAPI.is_airport_id_available(user_input):
                        user_input = user_input + " " + TextEditor.color_text_background("Airport id already exists", TextEditor.RED_BACKGROUND)
                        flight_route_info_already_exists = True
                    else:
                        flight_route_info_already_exists = False

                #Distance from Iceland can not contain letters excluding 'km'
                elif index == 4:
                    if 'km' in user_input:
                        user_input = user_input.replace('km', '')
                    if not user_input.isdigit():
                        user_input = user_input + " " + TextEditor.color_text_background("Can not contain letters", TextEditor.RED_BACKGROUND)
                        flight_route_info_already_exists = True
                    else:
                        flight_route_info_already_exists = False


                #Capitalize the first letters in the contacts name
                elif index == 5:
                    contact_name_list = []
                    for name in user_input.split():
                        contact_name_list.append(name.capitalize())
                    user_input = " ".join(contact_name_list)

                #Remove any spaces or dashes from the phonenumber
                elif index == 6:
                    if '-' in user_input:
                        user_input = user_input.replace('-', '')
                    if '' in user_input:
                        user_input = user_input.replace(' ', '')

                    #Put a message on the screen indicating the phonenumber is invalid
                    if not user_input.isdigit():
                        user_input = user_input + " " + TextEditor.color_text_background("Can not contain letters", TextEditor.RED_BACKGROUND)
                        flight_route_info_already_exists = True
                    else:
                        flight_route_info_already_exists = False
                
                user_input_list[index] = user_input
                user_input = ""

            elif user_input.startswith('s'):
                if all(user_input_list) and not flight_route_info_already_exists:

                    new_flight_route = FlightRoute(
                        user_input_list[0],
                        user_input_list[1],
                        user_input_list[2],
                        user_input_list[3],
                        user_input_list[4],
                        user_input_list[5],
                        user_input_list[6]
                    )
                    LogicAPI.save_new_flight_route(new_flight_route)
                    user_input = "A new flight route has been registered"
                    break

        return user_input

    @staticmethod
    def __show_all_flight_routes():

        user_input = ''

        #ComponentUI.print_header(FlightRouteUI.__FRAME_IN_USE_STR)
        #print(TextEditor.format_text("Show all flight routes", TextEditor.UNDERLINE_TEXT))
        
        while user_input not in FlightRouteUI.NAVIGATION_BAR_OPTIONS:

            table_header = ("Destination", "Airport", "Country", "Flight-time", "Distance", "Contact", "Emergency phone")
            flrt_list = LogicAPI.get_all_flight_routes()
            flight_routes_value_tuple = ([flightr.get_destination() for flightr in flrt_list],[flightr.get_airport_id() for flightr in flrt_list],\
                [flightr.get_country() for flightr in flrt_list],[flightr.get_flight_time() for flightr in flrt_list],[flightr.get_distance_from_iceland() for flightr in flrt_list],\
                    [flightr.get_contact_name() for flightr in flrt_list],[flightr.get_emergency_phone() for flightr in flrt_list])


            table_height = len(flrt_list)
            ComponentUI.print_frame_table_menu(table_header, flight_routes_value_tuple, table_height, ComponentUI.print_header(FlightRouteUI.__FRAME_IN_USE_STR),"All flight routes")

            user_input = ComponentUI.get_user_input()

            user_input = ComponentUI.remove_brackets(user_input)
            if not user_input.isdigit() or int(user_input) > table_height:
                continue

            
            table_index = int(user_input)-1

            selected_flrt = flrt_list[table_index]
            # senda inn í nýtt fall

            user_input = FlightRouteUI.__show_flight_route(selected_flrt)


        return user_input


    @staticmethod
    def __show_flight_route(flrt):
        
        user_input = ''
        user_input_list = []
        user_input_list.append(flrt.get_country())
        user_input_list.append(flrt.get_destination())
        user_input_list.append(flrt.get_airport_id())
        user_input_list.append(flrt.get_flight_time())
        user_input_list.append(flrt.get_distance_from_iceland())
        user_input_list.append(flrt.get_contact_name())
        user_input_list.append(flrt.get_emergency_phone())

        valid_user_inputs = ["6","7","(6)","(7)"]
        #ComponentUI.make_valid_menu_options_tuple(len(FlightRouteUI.FLIGHT_ROUTE_OPTION_TUBLE))            
       
        flight_route_info_already_exists = False
        while user_input not in FlightRouteUI.NAVIGATION_BAR_OPTIONS:
            ComponentUI.print_frame_constructor_menu(FlightRouteUI.FLIGHT_ROUTE_OPTION_TUBLE,\
            ComponentUI.get_main_options()[3], "Flight route to " + user_input_list[1], user_input_list, True, 1000, [0,1,2,3,4])
            
           
            user_input = ComponentUI.get_user_input()
            user_input = ComponentUI.remove_brackets(user_input)
            if user_input in valid_user_inputs: 
                index = int(user_input) - 1
                ComponentUI.print_frame_constructor_menu(FlightRouteUI.FLIGHT_ROUTE_OPTION_TUBLE,\
                    ComponentUI.get_main_options()[3], "Flight route to " + user_input_list[1], user_input_list, False, index, [0,1,2,3,4])

                if(index == 5):
                    user_input = input("Insert new contact name: ").strip()
                elif(index == 6):
                    user_input = input("Insert new Emergency phonenumber: ").strip()



                #Capitalize the first letters in the contacts name
                if index == 5:
                    if not user_input: #use existing name in case if user cancel or leve blanc 
                        user_input = user_input_list[index]

                    contact_name_list = []
                    for name in user_input.split():
                        contact_name_list.append(name.capitalize())
                    user_input = " ".join(contact_name_list)

                #Remove any spaces or dashes from the phonenumber
                elif index == 6:
                    if not user_input: #use existing phonenumber in case if user cancel or leve blanc 
                        user_input = user_input_list[index]

                    if '-' in user_input:
                        user_input = user_input.replace('-', '')
                    if '' in user_input:
                        user_input = user_input.replace(' ', '')

                    #Put a message on the screen indicating the phonenumber is invalid
                    if not user_input.isdigit():
                        user_input = user_input + " " + TextEditor.color_text_background("Can not contain letters", TextEditor.RED_BACKGROUND)
                        flight_route_info_already_exists = True
                    else:
                        flight_route_info_already_exists = False
                
                user_input_list[index] = user_input
                user_input = ""

            elif user_input.startswith('s'):
                if all(user_input_list) and not flight_route_info_already_exists:

                    edited_flight_route = FlightRoute(
                        user_input_list[0],
                        user_input_list[1],
                        user_input_list[2],
                        user_input_list[3],
                        user_input_list[4],
                        user_input_list[5],
                        user_input_list[6]
                    )

                    LogicAPI.change_saved_flight_route(flrt, edited_flight_route)
                    #þarfnast skoðunnar
                    user_input = "A new flight route contact information has been edited"
                    break

        return user_input
