import datetime
from user_interface.window import Window
from user_interface.text_editor import TextEditor
from user_interface.component_ui import ComponentUI
from apis.logic_api import LogicAPI
from data_models.voyage import Voyage

class VoyageUI:


    __FRAME_IN_USE_STR = ComponentUI.get_main_options()[0]

    __option_tuple = ('New voyage', 'Show ongoing voyages','Show completed voyages', 'Find voyages by date',\
         'Find voyages by week', 'Find voyages by destination')

    __INFO_TUPLE = ("Destination", "Airplane name", "Start time", "End time", "State")

    __NAVIGATION_BAR_OPTIONS = ComponentUI.get_navigation_options_tuple()

    @staticmethod
    def show():
        valid_user_inputs = ComponentUI.make_valid_menu_options_tuple(len(VoyageUI.__option_tuple))

        frame_functions = (VoyageUI.__show_new_voyage_constructor, VoyageUI.__show_ongoing_voyages, VoyageUI.__show_completed_voyages,\
            VoyageUI.__show_find_voyages_by_date, VoyageUI.__show_find_voyages_by_week, VoyageUI.__show_find_voyages_by_destination)

        return ComponentUI.run_frame(VoyageUI.__option_tuple, ComponentUI.get_main_options()[0], valid_user_inputs, frame_functions) 

    @staticmethod
    def __show_new_voyage_constructor():
        
        option_tuple = ('Flight route', 'Voyage schedule', 'Airplane', 'Pilots', 'Flight attendants')
        user_input_list = [""] * len(option_tuple)

        valid_user_inputs = ComponentUI.make_valid_menu_options_tuple(len(option_tuple))

        navigation_bar_options = ComponentUI.get_navigation_options_tuple()

        user_input = ""
        voyage_info_already_exists = False

        input_message_tuple = ("Insert Flight route: ", "Insert Voyage schedule: ", "Insert Airplane: ", "Insert Pilots: ",\
            "Insert Flight attendants: ")

        while user_input not in navigation_bar_options:

            greyed_out_option_index_list = [] if not user_input_list[2] else [3,4]

            ComponentUI.print_frame_constructor_menu(option_tuple, VoyageUI.__FRAME_IN_USE_STR,\
                 "New voyage", user_input_list, True, greyed_out_option_index_list=greyed_out_option_index_list)
            
            user_input = ComponentUI.get_user_input()

            if not user_input:
                continue

            user_input = ComponentUI.remove_brackets(user_input)

            if user_input in valid_user_inputs:
                index = int(user_input) - 1
                all_flight_routes = LogicAPI.get_all_flight_routes()
                flight_route_info_tuple = ([flight_route.get_destination() for flight_route in all_flight_routes],\
                [flight_route.get_airport_id() for flight_route in all_flight_routes])
                ComponentUI.print_frame_table_menu(("Destination","Airport id"),\
                    flight_route_info_tuple, [[]]*len(flight_route_info_tuple) if not flight_route_info_tuple else len(flight_route_info_tuple[0]),ComponentUI.get_main_options()[0],"Flight route")
                

                user_input = input(input_message_tuple[index]).strip()

                #Error checks and selection screens need to be added

                user_input_list[index] = user_input
                user_input = ""

            elif user_input.startswith("s"):
                if all(user_input_list) and not voyage_info_already_exists:

                    new_voyage = Voyage(
                        user_input_list[0],
                        user_input_list[1],
                        user_input_list[2],
                        user_input_list[3],
                        user_input_list[4],
                        user_input_list[5]
                    )
                    LogicAPI.save_new_voyage(new_voyage)
                    user_input = "A new voyage has been registered"
                    break

        return user_input

    @staticmethod
    def __show_ongoing_voyages():

        table_header_tuple = ("Destination", "Airplane name", "Start time", "End time", "State")

        ongoing_voyages_list = LogicAPI.get_ongoing_voyages()

        voyage_value_tuple = ([voyage.get_flights()[0].get_arrival_location() for voyage in ongoing_voyages_list],
                              [voyage.get_airplane().get_name() for voyage in ongoing_voyages_list],
                              [voyage.get_schedule()[0] for voyage in ongoing_voyages_list],
                              [voyage.get_schedule()[1] for voyage in ongoing_voyages_list],
                              [voyage.get_state() for voyage in ongoing_voyages_list])

        ComponentUI.print_frame_table_menu(table_header_tuple, voyage_value_tuple,\
             len(voyage_value_tuple) if not voyage_value_tuple\
             else len(voyage_value_tuple[0]),\
            VoyageUI.__FRAME_IN_USE_STR, "Ongoing voyages")



        return ComponentUI.get_user_input()

    @staticmethod
    def __show_completed_voyages():
        table_header_tuple = ("Destination", "Airplane name", "Start time", "End time")

        completed_voyages_list = LogicAPI.get_completed_voyages()

        voyage_value_tuple = ([voyage.get_flights()[0].get_arrival_location() for voyage in completed_voyages_list],
                              [voyage.get_airplane().get_name() for voyage in completed_voyages_list],
                              [voyage.get_schedule()[0] for voyage in completed_voyages_list],
                              [voyage.get_schedule()[1] for voyage in completed_voyages_list],
                              [voyage.get_state() for voyage in completed_voyages_list])

        ComponentUI.print_frame_table_menu(table_header_tuple, voyage_value_tuple,len(voyage_value_tuple) if not voyage_value_tuple\
             else len(voyage_value_tuple[0]),\
            VoyageUI.__FRAME_IN_USE_STR, "Completed voyages")



        return ComponentUI.get_user_input()

    @staticmethod    
    def __show_find_voyages_by_date():
        user_input = ""

        info_header_tuple = ("Destination", "Airplane name", "Start time", "End time", "State")

        navigation_bar_options = ComponentUI.get_navigation_options_tuple()

        while not user_input.startswith(navigation_bar_options):
            ComponentUI.print_header(VoyageUI. __FRAME_IN_USE_STR)
            print(TextEditor.format_text("Find voyages by date", TextEditor.UNDERLINE_TEXT))

            ComponentUI.fill_window_and_print_action_line(1)

            user_input = input("Insert date(dd-mm-yyyy): ").strip()

            if not user_input:
                continue

            #Error checks needed (perhaps let the user input the day, month and year seperately?)

            day, month, year = user_input.split("-")

            user_input = datetime.date(int(year), int(month), int(day))
            voyages_list = []

            voyages_list = LogicAPI.get_voyages_by_date(user_input)

            ComponentUI.print_header(VoyageUI.__FRAME_IN_USE_STR)
            print(TextEditor.format_text("Find voyages by date", TextEditor.UNDERLINE_TEXT))

            if not voyages_list:
                
                ComponentUI.centered_text_message("Could not find a voyage on the date: {}-{}-{}".format(user_input.day, user_input.month, user_input.year))
            
                return ComponentUI.get_user_input()

            else: 
                voyage_info_tuple = ([voyage.get_flights()[0].get_arrival_location() for voyage in voyages_list],
                              [voyage.get_airplane().get_name() for voyage in voyages_list],
                              [voyage.get_schedule()[0] for voyage in voyages_list],
                              [voyage.get_schedule()[1] for voyage in voyages_list],
                              [voyage.get_state() for voyage in voyages_list])

            ComponentUI.print_frame_table_menu(info_header_tuple, voyage_info_tuple, len(voyage_info_tuple[0]), VoyageUI.__FRAME_IN_USE_STR, "Find voyages by date")
            
            break #Needs profile functionality

        return ComponentUI.get_user_input()
    
    @staticmethod
    def __show_find_voyages_by_week():
        user_input = ""

        info_header_tuple = ("Destination", "Airplane name", "Start time", "End time", "State")

        navigation_bar_options = ComponentUI.get_navigation_options_tuple()

        while not user_input.startswith(navigation_bar_options):
            ComponentUI.print_header(VoyageUI. __FRAME_IN_USE_STR)
            print(TextEditor.format_text("Find voyages by week", TextEditor.UNDERLINE_TEXT))

            ComponentUI.fill_window_and_print_action_line(1)

            user_input = input("Insert week number: ").strip()

            if not user_input:
                continue

            #Error checks needed

            voyages_list = []

            voyages_list = LogicAPI.get_voyages_by_week(int(user_input))

            ComponentUI.print_header(VoyageUI.__FRAME_IN_USE_STR)
            print(TextEditor.format_text("Find voyages by week", TextEditor.UNDERLINE_TEXT))

            if not voyages_list:
                
                ComponentUI.centered_text_message("Could not find a voyage on week: {}".format(user_input))
            
                return ComponentUI.get_user_input()

            else:
                voyage_info_tuple = ([voyage.get_flights()[0].get_arrival_location() for voyage in voyages_list],
                              [voyage.get_airplane().get_name() for voyage in voyages_list],
                              [voyage.get_schedule()[0] for voyage in voyages_list],
                              [voyage.get_schedule()[1] for voyage in voyages_list],
                              [voyage.get_state() for voyage in voyages_list])

            ComponentUI.print_frame_table_menu(info_header_tuple, voyage_info_tuple, len(voyage_info_tuple[0]),\
                 VoyageUI.__FRAME_IN_USE_STR, "Find voyages by week")
            
            break #Needs profile functionality

        return ComponentUI.get_user_input()
    
    @staticmethod
    def __show_find_voyages_by_destination():
        user_input = ""

        info_header_tuple = ("Destination", "Airplane name", "Start time", "End time", "State")

        navigation_bar_options = ComponentUI.get_navigation_options_tuple()

        while not user_input.startswith(navigation_bar_options):
            ComponentUI.print_header(VoyageUI. __FRAME_IN_USE_STR)
            print(TextEditor.format_text("Find voyages by destination", TextEditor.UNDERLINE_TEXT))

            ComponentUI.fill_window_and_print_action_line(1)

            user_input = input("Insert destination: ").strip()

            if not user_input:
                continue

            #Error checks needed

            user_input = user_input.capitalize()

            voyages_list = []

            voyages_list = LogicAPI.get_voyages_by_destination(user_input)

            ComponentUI.print_header(VoyageUI.__FRAME_IN_USE_STR)
            print(TextEditor.format_text("Find voyages by destination", TextEditor.UNDERLINE_TEXT))

            if not voyages_list:
                
                ComponentUI.centered_text_message("Could not find a voyage going to destination: {}".format(user_input))
            
                return ComponentUI.get_user_input()

            else:
                voyage_info_tuple = ([voyage.get_flights()[0].get_arrival_location() for voyage in voyages_list],
                              [voyage.get_airplane().get_name() for voyage in voyages_list],
                              [voyage.get_schedule()[0] for voyage in voyages_list],
                              [voyage.get_schedule()[1] for voyage in voyages_list],
                              [voyage.get_state() for voyage in voyages_list])

            ComponentUI.print_frame_table_menu(info_header_tuple, voyage_info_tuple, len(voyage_info_tuple[0]),\
                 VoyageUI.__FRAME_IN_USE_STR, "Find voyages by destination")
            
            break #Needs profile functionality

        return ComponentUI.get_user_input()

    @staticmethod
    def __show_voyage(voyage): #Needs work!!
        user_input = ''
        user_input_list = [
            voyage.get_country(),
            voyage.get_destination(),
            voyage.get_airport_id(),
            voyage.get_flight_time(),
            voyage.get_distance_from_iceland(),
            voyage.get_contact_name(),
            voyage.get_emergency_phone()
        ]

        valid_user_inputs = ["6","7","(6)","(7)"]
        #ComponentUI.make_valid_menu_options_tuple(len(FlightRouteUI.FLIGHT_ROUTE_OPTION_TUBLE))            
       
        voyage_info_already_exists = False
        while user_input not in VoyageUI.__NAVIGATION_BAR_OPTIONS:
            ComponentUI.print_frame_constructor_menu(VoyageUI.__INFO_TUPLE,\
            ComponentUI.get_main_options()[3], "Flight route to " + user_input_list[1], user_input_list, True, 1000, [0,1,2,3,4])
            
           
            user_input = ComponentUI.get_user_input()
            user_input = ComponentUI.remove_brackets(user_input)
            if user_input in valid_user_inputs: 
                index = int(user_input) - 1
                ComponentUI.print_frame_constructor_menu(VoyageUI.__INFO_TUPLE,\
            ComponentUI.get_main_options()[3], "Flight route to " + user_input_list[1], user_input_list, True, 1000, [0,1,2,3,4])

                if(index == 5):
                    user_input = input("Insert new contact name: ").strip()
                elif(index == 6):
                    user_input = input("Insert new Emergency phonenumber: ").strip()



                #Capitalize the first letters in the contacts name
                if index == 5:
                    if not user_input: #use existing name in case if user cancels or leaves it blank 
                        user_input = user_input_list[index]

                    contact_name_list = []
                    for name in user_input.split():
                        contact_name_list.append(name.capitalize())
                    user_input = " ".join(contact_name_list)

                #Remove any spaces or dashes from the phonenumber
                elif index == 6:
                    if not user_input: #use existing phonenumber in case if user cancels or leaves it blank
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

                    LogicAPI.change_saved_flight_route(voyage, edited_flight_route)
                    #þarfnast skoðunnar(Kannski er þetta ok þar sem breytingar sjást, næ ekki að láta þetta virka heldur)
                    user_input = "A voyage has been edited"
                    break

        return user_input
