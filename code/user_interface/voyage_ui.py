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
         'Find voyages by week', 'Find voyages by destination') #the menu to display - 1.level for voyage

    __INFO_TUPLE = ("Destination", "Airplane name", "Start time", "End time", "State")

    __NAVIGATION_BAR_OPTIONS = ComponentUI.get_navigation_options_tuple()

    @staticmethod
    def show():
        ''' Displaying the voyage 1.level menu '''
        valid_user_inputs = ComponentUI.make_valid_menu_options_tuple(len(VoyageUI.__option_tuple))

        frame_functions = (VoyageUI.__show_new_voyage_constructor, VoyageUI.__show_ongoing_voyages, VoyageUI.__show_completed_voyages,\
            VoyageUI.__show_find_voyages_by_date, VoyageUI.__show_find_voyages_by_week, VoyageUI.__show_find_voyages_by_destination)

        return ComponentUI.run_frame(VoyageUI.__option_tuple, ComponentUI.get_main_options()[0], valid_user_inputs, frame_functions) 

    @staticmethod
    def __show_new_voyage_constructor():
        ''' Displaying the new voyage menu and gather together values to save  '''
        
        option_tuple = ('Flight route', 'Voyage schedule', 'Airplane', 'Pilots', 'Flight attendants') #the menu to display
        user_input_list = [""] * len(option_tuple) # the values to save

        flight1 = None
        flight2 = None
        voyage_schedule = None
        airplane = None
        pilot_list = []
        flight_attendant_list = []


        user_input = ""
        selected_flight_route = None

        
        #the message the are in front of the input from the user
        input_message_tuple = ("Insert number of desired flight route: ", "Insert Voyage schedule: ",\
             "Insert number of desired Airplane ", "Insert Pilots: ", "Insert Flight attendants: ")

        while user_input not in VoyageUI.__NAVIGATION_BAR_OPTIONS:

            #wizard control options that are not valable are grayed out
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


            if user_input.startswith("s"): #save new voyage / send values to API
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

            if index == 0: # flight-rout menu
                all_flight_routes = LogicAPI.get_all_flight_routes()
                flight_route_info_tuple = ([flight_route.get_country() for flight_route in all_flight_routes],\
                [flight_route.get_destination() for flight_route in all_flight_routes],\
                [flight_route.get_airport_id() for flight_route in all_flight_routes])
                ComponentUI.print_frame_table_menu(("Country", "Destination", "Airport id"),\
                    flight_route_info_tuple, [[]]*len(flight_route_info_tuple) if not flight_route_info_tuple else len(flight_route_info_tuple[0]),ComponentUI.get_main_options()[0],"Flight route")
            
                user_input = input(input_message_tuple[index]).strip()

                if not user_input or not user_input.isdigit() or int(user_input) > len(all_flight_routes):
                    continue

                selected_flight_route = all_flight_routes[int(user_input)-1]
                user_input = selected_flight_route.get_country() + ", " + selected_flight_route.get_destination()

            elif index == 1 and selected_flight_route: # schedule menu - open new selecetion process
                user_input, flight1, flight2, voyage_schedule = VoyageUI.__schedule_select(selected_flight_route)
                if not voyage_schedule:
                    continue

            elif index == 2: # airplane menu
                user_input, airplane = VoyageUI.__airplane_select(voyage_schedule)

            elif index == 3: # avalable pilot menu - multible chose 
                user_input, pilot_list = VoyageUI.__pilot_select(voyage_schedule, airplane.get_type())

            elif index == 4: # flight attendant menu -  multible chose
                user_input, flight_attendant_list = VoyageUI.__flight_attendant_select(voyage_schedule)

            if user_input in VoyageUI.__NAVIGATION_BAR_OPTIONS:
                continue

            user_input_list[index] = user_input
            user_input = ""

        return user_input


    @staticmethod
    def __pilot_select(voyage_schedule, pilot_license, pilot_list_start_val=[]):
        ''' process to select a pilot captain and other pilots '''

        pilot_info_tuple = ("Name", "SSN", "Phone number", "Home address", "Email", "State")
        available_pilots = LogicAPI.get_available_licensed_pilots(voyage_schedule, pilot_license)
        pilot_list = pilot_list_start_val
        user_input = ""

        greyed_out_option_index_list = []

        for pilot in pilot_list:
            available_pilots.append(pilot)

        while user_input not in VoyageUI.__NAVIGATION_BAR_OPTIONS:

            if available_pilots:
                pilot_value_tuple = ([pilot.get_name() for pilot in available_pilots],[pilot.get_ssn() for pilot in available_pilots],\
                [pilot.get_phonenumber() for pilot in available_pilots], [pilot.get_home_address() for pilot in available_pilots],\
                [pilot.get_email() for pilot in available_pilots], [pilot.get_state() for pilot in available_pilots])

                for i, pilot in enumerate(available_pilots):
                    if pilot in pilot_list_start_val:
                        greyed_out_option_index_list.append(i)

                ComponentUI.print_frame_table_menu(pilot_info_tuple, pilot_value_tuple, len(available_pilots),
                    VoyageUI.__FRAME_IN_USE_STR, "All available pilots", True, greyed_out_option_index_list)

                if len(greyed_out_option_index_list) >= 10:
                    user_input = ComponentUI.get_user_input()
                elif not pilot_list:
                    user_input = ComponentUI.get_user_input("Insert number of desired captain: ")
                else:
                    user_input = ComponentUI.get_user_input("Insert number of desired pilot: ")

                user_input = ComponentUI.remove_brackets(user_input)

                if user_input.startswith("s"):
                    if pilot_list:
                        additional_pilot_count = len(pilot_list)-1
                        user_input = "Captain {} {}{}".format(pilot_list[0].get_name(),\
                        "+ " + str(additional_pilot_count) + " pilot" if additional_pilot_count != 0\
                        else "", "" if additional_pilot_count in [0,1] else "s")
                    else:
                        user_input = "No pilots registered"
                    break

                if not user_input.isdigit() or len(available_pilots) < int(user_input):
                    continue

                index = int(user_input) - 1

                if index in greyed_out_option_index_list:
                    continue

                pilot_list.append(available_pilots[index])
                greyed_out_option_index_list.append(index)

            else:
                ComponentUI.print_header(VoyageUI.__FRAME_IN_USE_STR)
                print(TextEditor.format_text("All available pilots", TextEditor.UNDERLINE_TEXT))
                ComponentUI.centered_text_message("There are no available pilots", "", 3)
                user_input = ComponentUI.get_user_input()
                break

        if "pilot" not in user_input and user_input not in VoyageUI.__NAVIGATION_BAR_OPTIONS:
            if pilot_list:
                additional_pilot_count = len(pilot_list)-1
                user_input = "Captain {} {}{}".format(pilot_list[0].get_name(),\
                "+ " + str(additional_pilot_count) + " pilot" if additional_pilot_count != 0\
                else "", "" if additional_pilot_count in [0,1] else "s")
            else:
                user_input = "No pilots registered"

        return user_input, pilot_list

    @staticmethod
    def __flight_attendant_select(voyage_schedule, flight_attendant_list_start_val=[]):
        ''' process to select a cabin manager and other flight attendant '''

        flight_attendant_info_tuple = ("Name", "SSN", "Phone number", "Home address", "Email", "State")
        available_flight_attendants = LogicAPI.get_available_flight_attendants(voyage_schedule)
        flight_attendant_list = flight_attendant_list_start_val
        user_input = ""

        greyed_out_option_index_list = []

        for flight_attendant in flight_attendant_list:
            available_flight_attendants.append(flight_attendant)

        while user_input not in VoyageUI.__NAVIGATION_BAR_OPTIONS:

            if available_flight_attendants:
                flight_attendant_value_tuple = ([flight_attendant.get_name() for flight_attendant in available_flight_attendants],[flight_attendant.get_ssn() for flight_attendant in available_flight_attendants],\
                [flight_attendant.get_phonenumber() for flight_attendant in available_flight_attendants], [flight_attendant.get_home_address() for flight_attendant in available_flight_attendants],\
                [flight_attendant.get_email() for flight_attendant in available_flight_attendants], [flight_attendant.get_state() for flight_attendant in available_flight_attendants])

                for i, flight_attendant in enumerate(available_flight_attendants):
                    if flight_attendant in flight_attendant_list_start_val:
                        greyed_out_option_index_list.append(i)

                ComponentUI.print_frame_table_menu(flight_attendant_info_tuple, flight_attendant_value_tuple, len(available_flight_attendants),
                    VoyageUI.__FRAME_IN_USE_STR, "All available flight attendants", True, greyed_out_option_index_list)

                if not flight_attendant_list:
                    user_input = ComponentUI.get_user_input("Insert number of desired cabin manager: ")
                else:
                    user_input = ComponentUI.get_user_input("Insert number of desired flight attendant: ")

                user_input = ComponentUI.remove_brackets(user_input)

                if user_input.startswith("s"):
                    if flight_attendant_list:
                        additional_flight_attendant_count = len(flight_attendant_list)-1
                        user_input = "Cabin manager {} {}{}".format(flight_attendant_list[0].get_name(),\
                        "+ " + str(additional_flight_attendant_count) + " flight attendant" if additional_flight_attendant_count != 0\
                        else "", "" if additional_flight_attendant_count in [0,1] else "s")
                    else:
                        user_input = "No flight attendants registered"
                    break

                if not user_input.isdigit() or len(available_flight_attendants) < int(user_input):
                    continue

                index = int(user_input) - 1

                if index in greyed_out_option_index_list:
                    continue

                flight_attendant_list.append(available_flight_attendants[index])
                greyed_out_option_index_list.append(index)

            else:
                ComponentUI.print_header(VoyageUI.__FRAME_IN_USE_STR)
                print(TextEditor.format_text("All available flight attendants", TextEditor.UNDERLINE_TEXT))
                ComponentUI.centered_text_message("There are no available flight attendants","", 3)
                user_input = ComponentUI.get_user_input()
                break

        if "flight attendant" not in user_input and user_input not in VoyageUI.__NAVIGATION_BAR_OPTIONS:
            if flight_attendant_list:
                additional_flight_attendant_count = len(flight_attendant_list)-1
                user_input = "Cabin manager {} {}{}".format(flight_attendant_list[0].get_name(),\
                "+ " + str(additional_flight_attendant_count) + " flight attendant" if additional_flight_attendant_count != 0\
                else "", "" if additional_flight_attendant_count in [0,1] else "s")
            else:
                user_input = "No flight attendants registered"

        return user_input, flight_attendant_list

    @staticmethod
    def __airplane_select(voyage_schedule):
        ''' display menu for available airplanes '''

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
                print(TextEditor.format_text("All available airplanes", TextEditor.UNDERLINE_TEXT))
                start_date_and_time = str(voyage_schedule[0].day) + "-" + str(voyage_schedule[0].month) + "-" + str(voyage_schedule[0].year)\
                     + " - " + str(voyage_schedule[1].day) + "-" + str(voyage_schedule[1].month) + "-" + str(voyage_schedule[1].year)
                ComponentUI.centered_text_message("There are no available airplanes between: {}".format(start_date_and_time),"", 3)
                user_input = ComponentUI.get_user_input()
                break

        return user_input, airplane

    @staticmethod
    def __schedule_select(selected_flight_route):
        ''' process to select schdeule dates and times '''
        
        schedule_option_tuple = ("First flight date", "Time of first flight", "Second flight date", "Time of second flight")
        
        user_input_list = [""] * len(schedule_option_tuple)
        valid_user_input_bool_list = [True] * len(schedule_option_tuple)

        all_voyages = LogicAPI.get_all_voyages()

        flight1 = None
        flight2 = None
        voyage_schedule = None

        flight1_start_date = None
        flight1_start_time = None

        flight2_start_date = None
        flight2_start_time = None
        user_input = ""

        while user_input not in VoyageUI.__NAVIGATION_BAR_OPTIONS:

            greyed_out_option_index_list = [1, 2, 3]

            if user_input_list[0] and not valid_user_input_bool_list[0]:
                greyed_out_option_index_list = [1, 2, 3]
            elif user_input_list[2] and not valid_user_input_bool_list[2]:
                greyed_out_option_index_list = [0, 1, 3]
            elif user_input_list[1] and not valid_user_input_bool_list[1]:
                greyed_out_option_index_list = [0, 2, 3]
            elif user_input_list[3] and not valid_user_input_bool_list[3]:
                greyed_out_option_index_list = [0, 1, 2]
            elif user_input_list[2] and valid_user_input_bool_list[2]:
                greyed_out_option_index_list = []
            elif user_input_list[1] and valid_user_input_bool_list[1]:
                greyed_out_option_index_list = [3]
            elif user_input_list[0] and valid_user_input_bool_list[0]:
                greyed_out_option_index_list = [2, 3]
            

            ComponentUI.print_frame_constructor_menu(schedule_option_tuple,\
            VoyageUI.__FRAME_IN_USE_STR, "Voyage schedule", user_input_list, True, greyed_out_option_index_list=greyed_out_option_index_list)

            user_input = ComponentUI.get_user_input()

            user_input = ComponentUI.remove_brackets(user_input)

            if not user_input.startswith('s'):

                if not user_input or not user_input.isdigit() or int(user_input) > len(schedule_option_tuple):
                    continue

                user_input = ComponentUI.remove_brackets(user_input)

                index = int(user_input) - 1

                if index in greyed_out_option_index_list:
                    continue

                ComponentUI.print_frame_constructor_menu(schedule_option_tuple,\
                VoyageUI.__FRAME_IN_USE_STR, "Voyage schedule", user_input_list, False, index)

                if index == 0:
                    user_input, flight1_start_date, valid_user_input_bool_list[index] = VoyageUI.__date_select()
                    if flight1_start_date and flight2_start_date:
                        if flight1_start_date > flight2_start_date:
                            user_input = user_input + " " + TextEditor.color_text_background("The second flight can not start before the first one", TextEditor.RED_BACKGROUND)
                            valid_user_input_bool_list[index] = False
                
                elif index == 1:
                    user_input, flight1_start_time, valid_user_input_bool_list[index] = VoyageUI.__time_select()
                    if flight1_start_time and flight2_start_time and flight2_start_date and flight1_start_date:
                        flight_time_hours, flight_time_minutes = [int(time) for time in selected_flight_route.get_flight_time().split(':')]
                        flight1_start_date_and_time = datetime.datetime(flight1_start_date.year, flight1_start_date.month, flight1_start_date.day,\
                            flight1_start_time.hour, flight1_start_time.minute)
                        flight2_start_date_and_time = datetime.datetime(flight2_start_date.year, flight2_start_date.month, flight2_start_date.day,\
                            flight2_start_time.hour, flight2_start_time.minute)
                        if flight2_start_date_and_time < flight1_start_date_and_time + datetime.timedelta(hours=flight_time_hours, minutes=flight_time_minutes):
                                user_input = user_input + " " + TextEditor.color_text_background("The first flight time is {} hours and {} minutes".format(flight_time_hours,\
                                    flight_time_minutes), TextEditor.RED_BACKGROUND)
                                valid_user_input_bool_list[index] = False
                    if flight1_start_time and flight1_start_date:
                        for voyage in all_voyages:
                            f1 = voyage.get_flights()[0]
                            if f1.get_departure_time().date() == flight1_start_date and f1.get_departure_time().time() == flight1_start_time:
                                user_input = user_input + " " + TextEditor.color_text_background("Another airplane is departing at that time!", TextEditor.RED_BACKGROUND)
                                valid_user_input_bool_list[index] = False
                elif index == 2:
                    user_input, flight2_start_date, valid_user_input_bool_list[index] = VoyageUI.__date_select()
                    if flight1_start_date and flight2_start_date:
                        if flight1_start_date > flight2_start_date:
                            user_input = user_input + " " + TextEditor.color_text_background("The second flight can not start before the first one", TextEditor.RED_BACKGROUND)
                            valid_user_input_bool_list[index] = False
                    
                elif index == 3:
                    user_input, flight2_start_time, valid_user_input_bool_list[index] = VoyageUI.__time_select()
                    #Error check
                    if flight1_start_time and flight2_start_time and flight2_start_date and flight1_start_date:
                        flight_time_hours, flight_time_minutes = [int(time) for time in selected_flight_route.get_flight_time().split(':')]
                        flight1_start_date_and_time = datetime.datetime(flight1_start_date.year, flight1_start_date.month, flight1_start_date.day,\
                            flight1_start_time.hour, flight1_start_time.minute)
                        flight2_start_date_and_time = datetime.datetime(flight2_start_date.year, flight2_start_date.month, flight2_start_date.day,\
                            flight2_start_time.hour, flight2_start_time.minute)
                        if flight2_start_date_and_time < flight1_start_date_and_time + datetime.timedelta(hours=flight_time_hours, minutes=flight_time_minutes):
                                user_input = user_input + " " + TextEditor.color_text_background("The first flight time is {} hours and {} minutes".format(flight_time_hours,\
                                    flight_time_minutes), TextEditor.RED_BACKGROUND)
                                valid_user_input_bool_list[index] = False

                else:
                    continue

                if not user_input:
                    user_input = user_input_list[index]

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
    def __time_select():
        ''' handeling selection of time '''

        user_input = input("Insert time(hh:mm):").strip()

        time = None

        valid_input_bool = True

        user_input = user_input.replace("/", ":").replace("-", ":")

        if not user_input:
            return user_input, time, valid_input_bool

        user_input = ComponentUI.remove_brackets(user_input)

        split_list = user_input.split(":")

        if not user_input.replace(":", "").isdigit() or len(split_list) != 2 or not split_list[0].isdigit() or not split_list[1].isdigit():
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
    def __date_select(futur_only=True):
        ''' handeling selection of date '''

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

            if datetime.date.today() > date and futur_only:
                user_input = user_input + " " + TextEditor.color_text_background("Date has passed, another input is required", TextEditor.RED_BACKGROUND)
                valid_input_bool = False

        return user_input, date, valid_input_bool

    @staticmethod
    def __show_ongoing_voyages():
        ''' Displaying table of voyages that are ongoing '''
        LogicAPI.update_states() #UPDATES ALL STATES BEFOR DISPLAYING


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
            ComponentUI.print_frame_table_menu(table_header_tuple, voyage_value_tuple, table_height, VoyageUI.__FRAME_IN_USE_STR,"Ongoing and upcoming voyages")
            user_input = ComponentUI.get_user_input()
            user_input = ComponentUI.remove_brackets(user_input)
            if not user_input.isdigit() or int(user_input) > table_height:
                    continue
            table_index = int(user_input)-1
            ongoing_voyage = ongoing_voyages_list[table_index]        

            user_input = VoyageUI.show_voyage(ongoing_voyage)

        return user_input

    @staticmethod
    def __show_completed_voyages():
        ''' Displaying table of voyages that are completed '''
        LogicAPI.update_states() #UPDATES ALL STATES BEFOR DISPLAYING

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
            ComponentUI.print_frame_table_menu(table_header_tuple, voyage_value_tuple, table_height, VoyageUI.__FRAME_IN_USE_STR,"Completed voyages")
            user_input = ComponentUI.get_user_input()
            user_input = ComponentUI.remove_brackets(user_input)
            if not user_input.isdigit() or int(user_input) > table_height:
                continue
            if completed_voyages_list: 
                table_index = int(user_input)-1
                voyage = completed_voyages_list[table_index]        

                user_input = VoyageUI.show_voyage(voyage)
            else:
                ComponentUI.print_header(VoyageUI.__FRAME_IN_USE_STR)
                print(TextEditor.format_text("All completed voyages", TextEditor.UNDERLINE_TEXT))
                ComponentUI.centered_text_message("There are no completed voyages at the moment !","", 3)
                user_input = ComponentUI.get_user_input()
                break

        return user_input

    @staticmethod    
    def __show_find_voyages_by_date():
        ''' Select date and Displaying table of voyages for selected date '''
        LogicAPI.update_states() #UPDATES ALL STATES BEFOR DISPLAYING

        user_input = ""

        info_header_tuple = ("Destination", "Airplane name", "Start time", "End time", "State")

        while user_input not in VoyageUI.__NAVIGATION_BAR_OPTIONS:
            ComponentUI.print_header(VoyageUI. __FRAME_IN_USE_STR)
            print(TextEditor.format_text("Find voyages by date", TextEditor.UNDERLINE_TEXT))

            ComponentUI.fill_window_and_print_action_line(1)

            user_input, date, valid_input_bool = VoyageUI.__date_select(futur_only=False)

            if not user_input:
                continue

            voyages_list = []
            voyages_list = LogicAPI.get_voyages_by_date(date)

            ComponentUI.print_header(VoyageUI.__FRAME_IN_USE_STR)
            print(TextEditor.format_text("Find voyages by date", TextEditor.UNDERLINE_TEXT))

            if not voyages_list or not valid_input_bool:
                
                ComponentUI.centered_text_message("Could not find a voyage on date: {}".format(user_input),"", 3)
            
                return ComponentUI.get_user_input()

            else:
                
                voyage_info_tuple = ([voyage.get_flights()[0].get_arrival_location() for voyage in voyages_list],\
                [voyage.get_airplane().get_name() for voyage in voyages_list],\
                [voyage.get_schedule()[0] for voyage in voyages_list],\
                [voyage.get_schedule()[1] for voyage in voyages_list],\
                [voyage.get_state() for voyage in voyages_list])

                table_height = len(voyages_list)
                ComponentUI.print_frame_table_menu(info_header_tuple, voyage_info_tuple, table_height, VoyageUI.__FRAME_IN_USE_STR,"Voyages by date")
                user_input = ComponentUI.get_user_input()
                user_input = ComponentUI.remove_brackets(user_input)
                if not user_input.isdigit() or int(user_input) > table_height:
                        continue
                table_index = int(user_input)-1
                voyage = voyages_list[table_index]        
                user_input = VoyageUI.show_voyage(voyage)


            return user_input
    
    @staticmethod
    def __show_find_voyages_by_week():
        ''' Select week number and Displaying table of voyages for selected week '''
        LogicAPI.update_states() #UPDATES ALL STATES BEFOR DISPLAYING

        user_input = ""

        info_header_tuple = ("Destination", "Airplane name", "Start time", "End time", "State")

        while user_input not in VoyageUI.__NAVIGATION_BAR_OPTIONS:
            ComponentUI.print_header(VoyageUI. __FRAME_IN_USE_STR)
            print(TextEditor.format_text("Find voyages by week", TextEditor.UNDERLINE_TEXT))

            ComponentUI.fill_window_and_print_action_line(1)

            user_input = input("Insert a week number: ").strip()

            if not user_input:
                continue

            voyages_list = []

            if user_input.isdigit():
                voyages_list = LogicAPI.get_voyages_by_week(int(user_input))

            if not voyages_list:
                ComponentUI.print_header(VoyageUI.__FRAME_IN_USE_STR)
                print(TextEditor.format_text("Find voyages by week", TextEditor.UNDERLINE_TEXT))
                
                ComponentUI.centered_text_message("Could not find a voyage on week: {}".format(user_input),"", 3)
            
                return ComponentUI.get_user_input()

            else:
                voyage_info_tuple = ([voyage.get_flights()[0].get_arrival_location() for voyage in voyages_list],\
                [voyage.get_airplane().get_name() for voyage in voyages_list],\
                [voyage.get_schedule()[0] for voyage in voyages_list],\
                [voyage.get_schedule()[1] for voyage in voyages_list],\
                [voyage.get_state() for voyage in voyages_list])

                table_height = len(voyages_list)
                ComponentUI.print_frame_table_menu(info_header_tuple, voyage_info_tuple, table_height, VoyageUI.__FRAME_IN_USE_STR,"Voyages by week")
                user_input = ComponentUI.get_user_input()
                user_input = ComponentUI.remove_brackets(user_input)
                if not user_input.isdigit() or int(user_input) > table_height:
                    continue
                table_index = int(user_input)-1
                voyage = voyages_list[table_index]        
                user_input = VoyageUI.show_voyage(voyage)


            return user_input
    
    @staticmethod
    def __show_find_voyages_by_destination():
        ''' Select destination by typing and Displaying table of voyages for selected destination '''
        LogicAPI.update_states() #UPDATES ALL STATES BEFOR DISPLAYING

        user_input = ""

        info_header_tuple = ("Destination", "Airplane name", "Start time", "End time", "State")

        while user_input not in VoyageUI.__NAVIGATION_BAR_OPTIONS:
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
                print(TextEditor.format_text("Find voyages by destination", TextEditor.UNDERLINE_TEXT))
                ComponentUI.centered_text_message("Could not find a voyage going to destination: {}".format(user_input),"", 3)
            
                return ComponentUI.get_user_input()

            else:
                voyage_info_tuple = ([voyage.get_flights()[0].get_arrival_location() for voyage in voyages_list],\
                [voyage.get_airplane().get_name() for voyage in voyages_list],\
                [voyage.get_schedule()[0] for voyage in voyages_list],\
                [voyage.get_schedule()[1] for voyage in voyages_list],\
                [voyage.get_state() for voyage in voyages_list])

                table_height = len(voyages_list)
                ComponentUI.print_frame_table_menu(info_header_tuple, voyage_info_tuple, table_height, VoyageUI.__FRAME_IN_USE_STR,"Voyages by destination")
                user_input = ComponentUI.get_user_input()
                user_input = ComponentUI.remove_brackets(user_input)
                if not user_input.isdigit() or int(user_input) > table_height:
                        continue
                table_index = int(user_input)-1
                voyage = voyages_list[table_index]        
                user_input = VoyageUI.show_voyage(voyage)


            return user_input

    @staticmethod
    def show_voyage(voyage):
        ''' Displaying and edit selected voyage  '''
        LogicAPI.update_states() #UPDATES ALL STATES BEFOR DISPLAYING

        info_tuple = ("Destination", "Pilots", "Flight attendants", "Airplane name", "Schedule", "State")

        pilot_list = voyage.get_pilots()
        flight_attendant_list = voyage.get_flight_attendants()

        airplane = voyage.get_airplane()
        schedule = voyage.get_schedule()
        state = voyage.get_state()

        pilots_str = ""

        if pilot_list:
            additional_pilot_count = len(pilot_list)-1
            pilots_str = "Captain {} {} {}".format(pilot_list[0].get_name(),\
            "+ " + str(additional_pilot_count) + " pilot" if additional_pilot_count != 0\
            else "", "" if additional_pilot_count in [0,1] else "s")
        else:
            pilots_str = "No pilots registered"

        flight_attendants_str = "" 

        if flight_attendant_list:
            additional_flight_attendant_count = len(flight_attendant_list)-1
            flight_attendants_str = "Cabin manager {} {} {}".format(flight_attendant_list[0].get_name(),\
            "+ " + str(additional_flight_attendant_count) + " flight attendant" if additional_flight_attendant_count != 0\
            else "", "" if additional_flight_attendant_count in [0,1] else "s")
        else:
            flight_attendants_str = "No flight attendants registered"

        user_input = ''
        user_input_list = [
            voyage.get_flights()[0].get_arrival_location(),
            pilots_str,
            flight_attendants_str,
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
                    user_input, pilot_list = VoyageUI.__pilot_select(schedule, airplane.get_type(), pilot_list)
                    if not pilot_list:
                        user_input = user_input_list[index]
                elif(index == 2):
                    user_input, flight_attendant_list = VoyageUI.__flight_attendant_select(schedule, flight_attendant_list)
                    if not flight_attendant_list:
                        user_input = user_input_list[index]

                if user_input in VoyageUI.__NAVIGATION_BAR_OPTIONS:
                    continue

                user_input_list[index] = user_input
                user_input = ""

            elif user_input.startswith('s'): # save send to API edited values of voyage
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
                    user_input = "A voyage has been edited"
                    break

        return user_input
