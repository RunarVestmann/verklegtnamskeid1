from user_interface.airplanes_ui import AirplanesUI
from user_interface.employees_ui import EmployeeUI
from user_interface.flight_route_ui import FlightRouteUI
from user_interface.voyage_ui import VoyageUI
from user_interface.quit_ui import QuitUI
from user_interface.main_menu_ui import MainMenuUI

from user_interface.component_ui import ComponentUI

class Frame:

    @staticmethod
    def initialize():

        #A tuple with each input the navigation bar accepts
        valid_navigation_bar_inputs = ComponentUI.get_navigation_options_tuple()

        #All the different top level frames
        frames_tuple = (VoyageUI, EmployeeUI, AirplanesUI, FlightRouteUI, QuitUI)

        #The first frame is the Main Menu
        current_frame = MainMenuUI

        while True:

            #Show the current frame and get the exit input when the user wants to change frames
            user_input = current_frame.show()

            #Don't do anything if the user presses enter
            if not user_input:
                continue

            user_input = ComponentUI.remove_brackets(user_input)

            #Change the frame if the user enters a valid navigation bar input
            if user_input.startswith(valid_navigation_bar_inputs):

                #Get which frame the user wants to see in the form of an index
                selected_index = Frame.__get_navigation_bar_index(user_input, valid_navigation_bar_inputs)

                #Change the frame according to that index
                current_frame = frames_tuple[selected_index]

    @staticmethod
    def __get_navigation_bar_index(user_input, valid_navigation_bar_inputs):
        for valid_input in valid_navigation_bar_inputs:
            if user_input.startswith(valid_input):
                return valid_navigation_bar_inputs.index(valid_input)
