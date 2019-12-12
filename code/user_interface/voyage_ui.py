import datetime
import calendar
from user_interface.window import Window
from user_interface.text_editor import TextEditor
from user_interface.component_ui import ComponentUI
from apis.logic_api import LogicAPI
from data_models.voyage import Voyage
from data_models.flight import Flight
from data_models.state import State

class VoyageUI:

    __FRAME_IN_USE_STR = ComponentUI.get_main_options()[0]

    __option_tuple = ('New voyage', 'Show ongoing voyages', 'Show completed voyages', 'Find voyages by date',\
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

        flight1 = None
        flight2 = None
        voyage_schedule = None
        airplane = None
        pilot_list = []
        flight_attendant_list = []

        navigation_bar_options = ComponentUI.get_navigation_options_tuple()

        user_input = ""
        selected_flight_route = None

        # greyed_out_option_index_list = []

        input_message_tuple = ("Insert number of desired flight route: ", "Insert Voyage schedule: ",\
             "Insert number of desired Airplane ", "Insert Pilots: ", "Insert Flight attendants: ")

        while user_input not in navigation_bar_options:

            greyed_out_option_index_list = [1, 2, 3, 4]

            if user_input_list[2]:
                greyed_out_option_index_list = []

            elif user_input_list[1]:
                greyed_out_option_index_list = [3, 4]

            elif user_input_list[0]:
                greyed_out_option_index_list = [2, 3, 4]

            ComponentUI.print_frame_constructor_menu(option_tuple, VoyageUI.__FRAME_IN_USE_STR,\
                 "New voyage", user_input_list, True, greyed_out_option_index_list=greyed_out_option_index_list)
            
            user_input = ComponentUI.get_user_input()

            if not user_input or user_input in greyed_out_option_index_list:
                continue

            user_input = ComponentUI.remove_brackets(user_input)


            if user_input.startswith("s"):
                if all(user_input_list[:-2]):

                    new_voyage = Voyage(
                        (flight1, flight2),          #Flights
                        pilot_list,                  #Pilots
                        flight_attendant_list,       #Flight Attendants
                        airplane,                    #Airplane
                        voyage_schedule,             #Schedule
                        State.get_voyage_states()[0] #State
                    )
                    LogicAPI.save_new_voyage(new_voyage)

                    LogicAPI.save_new_flight(flight1)
                    LogicAPI.save_new_flight(flight2)

                    user_input = "A new voyage has been registered"
                    break

            if not user_input.isdigit() or int(user_input) > len(option_tuple):
                continue


            index = int(user_input) - 1

            if index in greyed_out_option_index_list:
                continue

            if index == 0:
                all_flight_routes = LogicAPI.get_all_flight_routes()
                flight_route_info_tuple = ([flight_route.get_country() for flight_route in all_flight_routes],\
                [flight_route.get_destination() for flight_route in all_flight_routes],\
                [flight_route.get_airport_id() for flight_route in all_flight_routes])
                ComponentUI.print_frame_table_menu(("Country", "Destination", "Airport id"),\
                    flight_route_info_tuple, [[]]*len(flight_route_info_tuple) if not flight_route_info_tuple else len(flight_route_info_tuple[0]),ComponentUI.get_main_options()[0],"Flight route")
            
                user_input = input(input_message_tuple[index]).strip()

                #Error checks need to be added for the date inputs...

                if not user_input or not user_input.isdigit() or int(user_input) > len(all_flight_routes):
                    continue

                selected_flight_route = all_flight_routes[int(user_input)-1]
                user_input = selected_flight_route.get_country() + ", " + selected_flight_route.get_destination()

            elif index == 1 and selected_flight_route:
                user_input, flight1, flight2, voyage_schedule = VoyageUI.__schedule_select(selected_flight_route)
                if not voyage_schedule:
                    continue

            elif index == 2:
                user_input, airplane = VoyageUI.__airplane_select(voyage_schedule)

            elif index == 3:
                user_input, pilot_list = VoyageUI.__pilot_select(voyage_schedule, airplane.get_type())#.get_plane_type())

            elif index == 4:
                user_input, flight_attendant_list = VoyageUI.__flight_attendant_select(voyage_schedule)

            user_input_list[index] = user_input
            user_input = ""

            

        return user_input


    @staticmethod
    def __pilot_select(voyage_schedule, pilot_license, pilot_list_start_val=[]):
        pilot_info_tuple = ("Name", "State", "Type", "Manufacturer", "Seats")
        available_pilots = LogicAPI.get_available_licensed_pilots(voyage_schedule, pilot_license)
        pilot_list = pilot_list_start_val
        user_input = ""

        greyed_out_option_index_list = []

        while user_input not in VoyageUI.__NAVIGATION_BAR_OPTIONS:

            if available_pilots:
                pilot_value_tuple = ([pilot.get_name() for pilot in pilots_list],[pilot.get_ssn() for pilot in pilots_list],\
                [pilot.get_phonenumber() for pilot in pilots_list], [pilot.get_home_address() for pilot in pilots_list],\
                [pilot.get_email() for pilot in pilots_list], [pilot.get_state() for pilot in pilots_list])

                ComponentUI.print_frame_table_menu(pilot_info_tuple, pilot_value_tuple, len(available_pilots),
                    VoyageUI.__FRAME_IN_USE_STR, "All available pilots", True)

                user_input = ComponentUI.get_user_input("Insert number of desired captain: ")
                user_input = ComponentUI.remove_brackets(user_input)

                if not user_input.isdigit() or len(available_pilots) < int(user_input):
                    continue

                index = int(user_input) - 1

                if index in greyed_out_option_index_list:
                    continue

                if not pilot_list:
                    pilot_list.append(available_pilots[index])
                    greyed_out_option_index_list.append(index) #use this list to see which pilot should be greyed out

                while user_input not in VoyageUI.__NAVIGATION_BAR_OPTIONS or user_input.startswith("s"):

                    user_input = ComponentUI.get_user_input()
                    user_input = ComponentUI.remove_brackets(user_input)

                    if not user_input.isdigit() or len(available_pilots) < int(user_input):
                        continue

                    index = int(user_input) - 1

                    if index in greyed_out_option_index_list:
                        continue

                    pilot_list.append(available_pilots[index])

                if user_input.startswith("s"):
                    user_input = "{} pilots".format(len(pilot_list))
                    break

            else:
                ComponentUI.print_header(VoyageUI.__FRAME_IN_USE_STR)
                ComponentUI.centered_text_message("There are no available pilots".format(voyage_schedule))
                user_input = ComponentUI.get_user_input()
                break

        return user_input, pilot_list

    @staticmethod
    def __flight_attendant_select(voyage_schedule):
        flight_attendant_info_tuple = ("Name", "State", "Type", "Manufacturer", "Seats")
        available_flight_attendants = LogicAPI.get_available_flight_attendants(voyage_schedule)
        flight_attendant_list = []
        user_input = ""

        greyed_out_option_index_list = []

        while user_input not in VoyageUI.__NAVIGATION_BAR_OPTIONS:

            if available_flight_attendants:
                flight_attendant_value_tuple = ([flight_attendant.get_name() for flight_attendant in  flight_attendant_list],[flight_attendant.get_ssn() for flight_attendant in  flight_attendant_list],\
                [flight_attendant.get_phonenumber() for flight_attendant in  flight_attendant_list], [flight_attendant.get_home_address() for flight_attendant in  flight_attendant_list],\
                [flight_attendant.get_email() for flight_attendant in  flight_attendant_list], [flight_attendant.get_state() for flight_attendant in  flight_attendant_list])

                ComponentUI.print_frame_table_menu(flight_attendant_info_tuple, flight_attendant_value_tuple, len(available_flight_attendants),
                    VoyageUI.__FRAME_IN_USE_STR, "All available flight attendants", True)

                user_input = ComponentUI.get_user_input("Insert number of desired cabin manager: ")
                user_input = ComponentUI.remove_brackets(user_input)

                if not user_input.isdigit() or len(available_flight_attendants) < int(user_input):
                    continue

                index = int(user_input) - 1

                if index in greyed_out_option_index_list:
                    continue

                flight_attendant_list.append(available_flight_attendants[index])
                greyed_out_option_index_list.append(index) #use this list to see which flight_ attendant should be greyed out

                while user_input not in VoyageUI.__NAVIGATION_BAR_OPTIONS or user_input.startswith("s"):

                    user_input = ComponentUI.get_user_input()
                    user_input = ComponentUI.remove_brackets(user_input)

                    if not user_input.isdigit() or len(available_flight_attendants) < int(user_input):
                        continue

                    index = int(user_input) - 1

                    if index in greyed_out_option_index_list:
                        continue

                    flight_attendant_list.append(available_flight_attendants[index])

                if user_input.startswith("s"):
                    user_input = "{} flight_attendants".format(len(flight_attendant_list))
                    break

            else:
                ComponentUI.print_header(VoyageUI.__FRAME_IN_USE_STR)
                ComponentUI.centered_text_message("There are no available flight_attendants".format(voyage_schedule))
                user_input = ComponentUI.get_user_input()
                break

        return user_input, flight_attendant_list



    @staticmethod
    def __airplane_select(voyage_schedule):

        airplane_info_tuple = ("Name", "State", "Type", "Manufacturer", "Seats")
        available_airplanes = LogicAPI.get_all_available_airplanes(voyage_schedule)
        airplane = None
        user_input = ""

        while user_input not in VoyageUI.__NAVIGATION_BAR_OPTIONS:

            if available_airplanes:
                airplane_value_tuple = ([airplane.get_name() for airplane in available_airplanes],[airplane.get_state() for airplane in available_airplanes],\
                    [airplane.get_type() for airplane in available_airplanes], [airplane.get_manufacturer() for airplane in available_airplanes],\
                    [airplane.get_seat_count() for airplane in available_airplanes])

                ComponentUI.print_frame_table_menu(airplane_info_tuple, airplane_value_tuple, len(available_airplanes),
                    VoyageUI.__FRAME_IN_USE_STR, "All available airplanes", False)

                user_input = ComponentUI.get_user_input()
                user_input = ComponentUI.remove_brackets(user_input)

                if not user_input.isdigit() or len(available_airplanes) < int(user_input):
                    continue

                index = int(user_input) - 1

                airplane = available_airplanes[index]

                user_input = airplane.get_name()

                break

            else:
                ComponentUI.print_header(VoyageUI.__FRAME_IN_USE_STR)
                ComponentUI.centered_text_message("There are no available airplanes between: {}".format(voyage_schedule))
                user_input = ComponentUI.get_user_input()
                break

        return user_input, airplane


    @staticmethod
    def __schedule_select(selected_flight_route):
        schedule_option_tuple = ("First flight date", "Time of first flight", "Second flight date", "Time of second flight")
        
        user_input_list = [""] * len(schedule_option_tuple)
        valid_user_input_bool_list = [True] * len(schedule_option_tuple)

        flight1 = None
        flight2 = None
        voyage_schedule = None

        flight1_start_date = None
        flight1_start_time = None

        flight2_start_date = None
        flight2_start_time = None


        user_input = ""

        while user_input not in VoyageUI.__NAVIGATION_BAR_OPTIONS:

            ComponentUI.print_frame_constructor_menu(schedule_option_tuple,\
            VoyageUI.__FRAME_IN_USE_STR, "Voyage schedule", user_input_list, True)

            user_input = ComponentUI.get_user_input()

            user_input = ComponentUI.remove_brackets(user_input)

            if not user_input.startswith('s'):

                if not user_input or not user_input.isdigit() or int(user_input) > len(schedule_option_tuple):
                    continue

                user_input = ComponentUI.remove_brackets(user_input)

                index = int(user_input) - 1

                ComponentUI.print_frame_constructor_menu(schedule_option_tuple,\
                VoyageUI.__FRAME_IN_USE_STR, "Voyage schedule", user_input_list, False, index)

                if index == 0:
                    user_input, flight1_start_date, valid_user_input_bool_list[index] = VoyageUI.__date_select()

                elif index == 1:
                    user_input, flight1_start_time, valid_user_input_bool_list[index] = VoyageUI.__time_select()

                elif index == 2:
                    user_input, flight2_start_date, valid_user_input_bool_list[index] = VoyageUI.__date_select()
                    
                elif index == 3:
                    user_input, flight2_start_time, valid_user_input_bool_list[index] = VoyageUI.__time_select()
                else:
                    continue

                user_input_list[index] = user_input
                user_input = ""

            else:
                if all(user_input_list) and all(valid_user_input_bool_list):

                    flight1_arrival_time_hour = (flight1_start_time.hour + int(selected_flight_route.get_flight_time().split(":")[0])) % 24
                    flight1_arrival_time_minute = (flight1_start_time.minute + int(selected_flight_route.get_flight_time().split(":")[1]))
                    flight1_arrival_time_hour += flight1_arrival_time_minute // 60
                    flight1_arrival_time_minute %= 60

                    flight1_arrival_date = flight1_start_date
                    
                    #If the date is the same as the last date of the month and the time is smaller than the start time, we add +1 to the date
                    if flight1_start_time > datetime.time(flight1_arrival_time_hour, flight1_arrival_time_minute):
                        if calendar.monthrange(flight1_start_date.year, flight1_start_date.month)[1] == flight1_start_date.day:
                            if month < 12:
                                flight1_arrival_date = datetime.date(flight1_arrival_date.year, flight1_arrival_date.month+1, 1)
                            else:
                                flight1_arrival_date = datetime.date(flight1_arrival_date.year, 1, flight1_arrival_date.day)

                        else:
                            flight1_arrival_date = datetime.date(flight1_arrival_date.year, flight1_arrival_date.month, flight1_arrival_date.day+1)


                    flight2_arrival_time_hour = (flight2_start_time.hour + int(selected_flight_route.get_flight_time().split(":")[0])) % 24
                    flight2_arrival_time_minute = (flight2_start_time.minute + int(selected_flight_route.get_flight_time().split(":")[1]))
                    flight2_arrival_time_hour += flight2_arrival_time_minute // 60
                    flight2_arrival_time_minute %= 60

                    flight2_arrival_date = flight2_start_date
                    
                    #If the date is the same as the last date of the month and the time is smaller than the start time, we add +1 to the date
                    if flight2_start_time > datetime.time(flight2_arrival_time_hour, flight2_arrival_time_minute):
                        if calendar.monthrange(flight2_start_date.year, flight2_start_date.month)[1] == flight2_start_date.day:
                            if month < 12:
                                flight2_arrival_date = datetime.date(flight2_arrival_date.year, flight2_arrival_date.month+1, 1)
                            else:
                                flight2_arrival_date = datetime.date(flight2_arrival_date.year, 1, flight2_arrival_date.day)

                        else:
                            flight2_arrival_date = datetime.date(flight2_arrival_date.year, flight2_arrival_date.month, flight2_arrival_date.day+1)

                    flight1_departure_date_and_time = datetime.datetime(flight1_start_date.year, flight1_start_date.month,\
                         flight1_start_date.day, flight1_start_time.hour, flight1_start_time.minute) 

                    flight1 = Flight(
                        "Iceland",
                        flight1_departure_date_and_time,
                        selected_flight_route.get_country(),
                        datetime.datetime(flight1_arrival_date.year, flight1_arrival_date.month, flight1_arrival_date.day, flight1_arrival_time_hour, flight1_arrival_time_minute),
                        LogicAPI.get_available_flight_number(selected_flight_route.get_airport_id(), flight1_departure_date_and_time)
                        )

                    flight2_departure_date_and_time = datetime.datetime(flight2_start_date.year, flight2_start_date.month,\
                         flight2_start_date.day, flight2_start_time.hour, flight2_start_time.minute) 

                    flight2 = Flight(
                        selected_flight_route.get_country(),
                        flight2_departure_date_and_time,
                        "Iceland",
                        datetime.datetime(flight2_start_date.year, flight2_start_date.month, flight2_start_date.day, flight2_arrival_time_hour, flight2_arrival_time_minute),
                        LogicAPI.get_available_flight_number(selected_flight_route.get_airport_id(), flight2_departure_date_and_time, 1)
                        )

                    voyage_schedule = (flight1.get_departure_time(), flight2.get_arrival_time())

                    user_input = "Start:{}    End:{}".format(flight1_arrival_date, flight2_arrival_date)

                    break
            

        return user_input, flight1, flight2, voyage_schedule

    @staticmethod
    def __time_select(previous_time=None, latter_time=None):

        user_input = input("Insert time(hh:mm):").strip()

        time = None

        valid_input_bool = True

        user_input = user_input.replace("/", ":").replace("-", ":").replace(" ", ":")

        if not user_input:
            return user_input, time, valid_input_bool

        user_input = ComponentUI.remove_brackets(user_input)

        split_list = user_input.split(":")

        if not user_input.replace(":", "").isdigit() or len(split_list) != 2:
            user_input = user_input + " " + TextEditor.color_text_background("Invalid input, another input is required", TextEditor.RED_BACKGROUND)
            valid_input_bool = False
        else:

            hour, minute = [int(number) for number in split_list]

            hour = hour % 24
            hour += minute // 60
            minute = minute % 60

            time = datetime.time(hour, minute)

        return user_input, time, valid_input_bool

    @staticmethod
    def __date_select():
        user_input = input("Insert date(dd-mm-yyyy):").strip()
        date = None
        valid_input_bool = True

        user_input = user_input.replace("/", "-").replace(":", "-").replace(" ", "-")

        if not user_input:
            return user_input, date, valid_input_bool

        user_input = ComponentUI.remove_brackets(user_input)

        split_list = user_input.split("-")

        if not user_input.replace("-", "").isdigit() or len(split_list) != 3 or not (0 < len(split_list[0]) < 3) or not (0 < len(split_list[1]) < 3) or not (0 < len(split_list[2]) < 5):
            user_input = user_input + " " + TextEditor.color_text_background("Invalid input, another input is required", TextEditor.RED_BACKGROUND)
            valid_input_bool = False
        else:

            day, month, year = [int(number) for number in split_list]

            if month > 12 or month < 1:
                user_input = user_input + " " + TextEditor.color_text_background("Month needs to be in range from 1-12, another input is required", TextEditor.RED_BACKGROUND)
                valid_input_bool = False
                return user_input, date, valid_input_bool

            elif calendar.monthrange(year, month)[1] < day:
                day = datetime._days_in_month(year, month)


            date = datetime.date(year, month, day)

            # if previous_date:
            #     if previous_date > date:
            #         user_input = user_input + " " + TextEditor.color_text_background("Invalid input, another input is required", TextEditor.RED_BACKGROUND)
            #         valid_input_bool = False
            # else:


            if datetime.date.today() > date:
                user_input = user_input + " " + TextEditor.color_text_background("Date has passed, another input is required", TextEditor.RED_BACKGROUND)
                valid_input_bool = False

        return user_input, date, valid_input_bool

    @staticmethod
    def __show_ongoing_voyages():

        user_input = ""
        while user_input not in VoyageUI.__NAVIGATION_BAR_OPTIONS:
            table_header_tuple = ("Destination", "Airplane name", "Start time", "End time", "State")

            ongoing_voyages_list = LogicAPI.get_ongoing_voyages()

            voyage_value_tuple = ([voyage.get_flights()[0].get_arrival_location() for voyage in ongoing_voyages_list],
                                [voyage.get_airplane().get_name() for voyage in ongoing_voyages_list],
                                [voyage.get_schedule()[0] for voyage in ongoing_voyages_list],
                                [voyage.get_schedule()[1] for voyage in ongoing_voyages_list],
                                [voyage.get_state() for voyage in ongoing_voyages_list])
            table_height = len(ongoing_voyages_list)
            ComponentUI.print_frame_table_menu(table_header_tuple, voyage_value_tuple, table_height, ComponentUI.print_header(VoyageUI.__FRAME_IN_USE_STR),"Ongoing voyages")
            user_input = ComponentUI.get_user_input()
            user_input = ComponentUI.remove_brackets(user_input)
            if not user_input.isdigit() or int(user_input) > table_height:
                    continue
            table_index = int(user_input)-1
            ongoing_voyage = ongoing_voyages_list[table_index]        

            user_input = VoyageUI.__show_voyage(ongoing_voyage)

        return user_input

    @staticmethod
    def __show_completed_voyages():
        ComponentUI.print_header(VoyageUI.__FRAME_IN_USE_STR)
        print(TextEditor.format_text("Completed voyages", TextEditor.UNDERLINE_TEXT))
    
        user_input = ""
        while user_input not in VoyageUI.__NAVIGATION_BAR_OPTIONS:
            table_header_tuple = ("Destination", "Airplane name", "Start time", "End time", "State")
            completed_voyages_list = LogicAPI.get_completed_voyages()
            voyage_value_tuple = ([voyage.get_flights()[0].get_arrival_location() for voyage in completed_voyages_list],
                                [voyage.get_airplane().get_name() for voyage in completed_voyages_list],
                                [voyage.get_schedule()[0] for voyage in completed_voyages_list],
                                [voyage.get_schedule()[1] for voyage in completed_voyages_list],
                                [voyage.get_state() for voyage in completed_voyages_list])
            table_height = len(completed_voyages_list)
            ComponentUI.print_frame_table_menu(table_header_tuple, voyage_value_tuple, table_height, ComponentUI.print_header(VoyageUI.__FRAME_IN_USE_STR),"Completed voyages")
            user_input = ComponentUI.get_user_input()
            user_input = ComponentUI.remove_brackets(user_input)
            if not user_input.isdigit() or int(user_input) > table_height:
                continue
            if completed_voyages_list: 
                table_index = int(user_input)-1
                voyage = completed_voyages_list[table_index]        

                user_input = VoyageUI.__show_voyage(voyage)
            else:
                ComponentUI.centered_text_message("There are no completed voyages at the moment !","",3)

        return user_input

    @staticmethod    
    def __show_find_voyages_by_date():
        navigation_bar_options = ComponentUI.get_navigation_options_tuple()

        user_input = ""

        info_header_tuple = ("Destination", "Airplane name", "Start time", "End time", "State")

        while user_input not in navigation_bar_options:
            ComponentUI.print_header(VoyageUI. __FRAME_IN_USE_STR)
            print(TextEditor.format_text("Find voyages by date", TextEditor.UNDERLINE_TEXT))

            ComponentUI.fill_window_and_print_action_line(1)


            

            #Error checks needed

            user_input, date, valid_input_bool = VoyageUI.__date_select()

            voyages_list = []
            voyages_list = LogicAPI.get_voyages_by_date(date)

            ComponentUI.print_header(VoyageUI.__FRAME_IN_USE_STR)
            print(TextEditor.format_text("Find voyages by date", TextEditor.UNDERLINE_TEXT))

            if not voyages_list or not valid_input_bool:
                
                ComponentUI.centered_text_message("Could not find a voyage on date: {}".format(user_input))
            
                return ComponentUI.get_user_input()

            else:
                
                voyage_info_tuple = ([voyage.get_flights()[0].get_arrival_location() for voyage in voyages_list],\
                [voyage.get_airplane().get_name() for voyage in voyages_list],\
                [voyage.get_schedule()[0] for voyage in voyages_list],\
                [voyage.get_schedule()[1] for voyage in voyages_list],\
                [voyage.get_state() for voyage in voyages_list])

                table_height = len(voyages_list)
                ComponentUI.print_frame_table_menu(info_header_tuple, voyage_info_tuple, table_height, ComponentUI.print_header(VoyageUI.__FRAME_IN_USE_STR),"Voyages by date")
                user_input = ComponentUI.get_user_input()
                user_input = ComponentUI.remove_brackets(user_input)
                if not user_input.isdigit() or int(user_input) > table_height:
                        continue
                table_index = int(user_input)-1
                voyage = voyages_list[table_index]        
                user_input = VoyageUI.__show_voyage(voyage)


            return user_input
    
    @staticmethod
    def __show_find_voyages_by_week():
        navigation_bar_options = ComponentUI.get_navigation_options_tuple()

        user_input = ""

        info_header_tuple = ("Destination", "Airplane name", "Start time", "End time", "State")

        while user_input not in navigation_bar_options:
            ComponentUI.print_header(VoyageUI. __FRAME_IN_USE_STR)
            print(TextEditor.format_text("Find voyages by week", TextEditor.UNDERLINE_TEXT))

            ComponentUI.fill_window_and_print_action_line(1)

            user_input = input("Insert week: ").strip()

            if not user_input:
                continue

            #Error checks needed

            voyages_list = []
            voyages_list = LogicAPI.get_voyages_by_week(user_input)

            
            ComponentUI.print_header(VoyageUI.__FRAME_IN_USE_STR)
            print(TextEditor.format_text("Find voyages by week", TextEditor.UNDERLINE_TEXT))

            if not voyages_list or user_input.isdigit():
                
                ComponentUI.centered_text_message("Could not find a voyage on week: {}".format(user_input))
            
                return ComponentUI.get_user_input()

            else:
                voyage_info_tuple = ([voyage.get_flights()[0].get_arrival_location() for voyage in voyages_list],\
                [voyage.get_airplane().get_name() for voyage in voyages_list],\
                [voyage.get_schedule()[0] for voyage in voyages_list],\
                [voyage.get_schedule()[1] for voyage in voyages_list],\
                [voyage.get_state() for voyage in voyages_list])

                table_height = len(voyages_list)
                ComponentUI.print_frame_table_menu(info_header_tuple, voyage_info_tuple, table_height, ComponentUI.print_header(VoyageUI.__FRAME_IN_USE_STR),"Voyages by week")
                user_input = ComponentUI.get_user_input()
                user_input = ComponentUI.remove_brackets(user_input)
                if not user_input.isdigit() or int(user_input) > table_height:
                        continue
                table_index = int(user_input)-1
                voyage = voyages_list[table_index]        
                user_input = VoyageUI.__show_voyage(voyage)


            return user_input
    
    @staticmethod
    def __show_find_voyages_by_destination():

        navigation_bar_options = ComponentUI.get_navigation_options_tuple()

        user_input = ""

        info_header_tuple = ("Destination", "Airplane name", "Start time", "End time", "State")

        while user_input not in navigation_bar_options:
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

            

            if not voyages_list:
                ComponentUI.print_header(VoyageUI.__FRAME_IN_USE_STR)
                # print(TextEditor.format_text("Find voyages by destination", TextEditor.UNDERLINE_TEXT))
                ComponentUI.centered_text_message("Could not find a voyage going to destination: {}".format(user_input))
            
                return ComponentUI.get_user_input()

            else:
                voyage_info_tuple = ([voyage.get_flights()[0].get_arrival_location() for voyage in voyages_list],\
                [voyage.get_airplane().get_name() for voyage in voyages_list],\
                [voyage.get_schedule()[0] for voyage in voyages_list],\
                [voyage.get_schedule()[1] for voyage in voyages_list],\
                [voyage.get_state() for voyage in voyages_list])

                table_height = len(voyages_list)
                ComponentUI.print_frame_table_menu(info_header_tuple, voyage_info_tuple, table_height, ComponentUI.print_header(VoyageUI.__FRAME_IN_USE_STR),"Voyages by destination")
                user_input = ComponentUI.get_user_input()
                user_input = ComponentUI.remove_brackets(user_input)
                if not user_input.isdigit() or int(user_input) > table_height:
                        continue
                table_index = int(user_input)-1
                voyage = voyages_list[table_index]        
                user_input = VoyageUI.__show_voyage(voyage)


            return user_input

    @staticmethod
    def __show_voyage(voyage): #Needs work!!

        info_tuple = ("Destination", "Pilots", "Flight attendants", "Airplane name", "Schedule", "State")

        pilot_list = voyage.get_pilots()
        flight_attendant_list = voyage.get_flight_attendants()

        airplane = voyage.get_airplane()
        schedule = voyage.get_schedule()
        state = voyage.get_state()


        user_input = ''
        user_input_list = [
            voyage.get_flights()[0].get_arrival_location(),
            str(len(voyage.get_pilots())) + " pilots",
            str(len(voyage.get_flight_attendants())) + " flight attendants",
            airplane.get_name(),
            "{}-{}-{} - {}-{}-{}".format(schedule[0].day,schedule[0].month, schedule[0].year,schedule[1].day,schedule[1].month, schedule[1].year),
            state
        ]

        valid_user_inputs = ["2","3"]
        greyed_out_option_index_list = [0,3,4,5]

        if state == State.get_voyage_states()[4]:
            greyed_out_option_index_list = [0,1,2,3,4,5]
            valid_user_inputs = []
        
        while user_input not in VoyageUI.__NAVIGATION_BAR_OPTIONS:
            ComponentUI.print_frame_constructor_menu(info_tuple,\
            ComponentUI.get_main_options()[0], "Edit mode", user_input_list, True, 1000, greyed_out_option_index_list)
            
           
            user_input = ComponentUI.get_user_input()
            user_input = ComponentUI.remove_brackets(user_input)
            if user_input in valid_user_inputs: 
                index = int(user_input) - 1
                ComponentUI.print_frame_constructor_menu(VoyageUI.__INFO_TUPLE,\
            ComponentUI.get_main_options()[0], "Edit mode", user_input_list, False, index, greyed_out_option_index_list)

                if(index == 1):
                    user_input, pilot_list = VoyageUI.__pilot_select(schedule, airplane.get_type())
                elif(index == 2):
                    user_input, flight_attendant_list = VoyageUI.__flight_attendant_select(schedule)


                user_input_list[index] = user_input
                user_input = ""

            elif user_input.startswith('s'):
                if all(user_input_list):

                    if pilot_list == voyage.get_pilots() and flight_attendant_list == voyage.get_flight_attendants():
                        break

                    edited_voyage = Voyage(
                        voyage.get_flights(),
                        pilot_list,
                        flight_attendant_list,
                        airplane,
                        voyage.get_schedule(),
                        state,
                    )

                    LogicAPI.change_saved_voyage(voyage, edited_voyage)
                    #þarfnast skoðunnar(Kannski er þetta ok þar sem breytingar sjást, næ ekki að láta þetta virka heldur)
                    user_input = "A voyage has been edited"
                    break

        return user_input
