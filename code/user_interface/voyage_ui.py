from user_interface.window import Window
from user_interface.text_editor import TextEditor
from user_interface.component_ui import ComponentUI
from apis.logic_api import LogicAPI
from data_models.voyage import Voyage

FRAME_IN_USE_STR = ComponentUI.get_main_options()[0]


class VoyageUI:
    __option_tuple = ('New voyage', 'Show ongoing voyages','Show completed voyages', 'Find voyages by date',\
         'Find voyages by week', 'Find voyages by destination')

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

            greyed_out_option_index_list = [1000] if not user_input_list[2] else [3,4]

            ComponentUI.print_frame_constructor_menu(option_tuple, FRAME_IN_USE_STR,\
                 "New voyage", user_input_list, True, greyed_out_option_index_list=greyed_out_option_index_list)
            
            user_input = ComponentUI.get_user_input()

            if not user_input:
                continue

            user_input = ComponentUI.remove_brackets(user_input)

            if user_input in valid_user_inputs:
                index = int(user_input) - 1

                ComponentUI.print_frame_constructor_menu(option_tuple, FRAME_IN_USE_STR,\
                 "New voyage", user_input_list, False, index, greyed_out_option_index_list=greyed_out_option_index_list)

                user_input = input(input_message_tuple[index]).strip()


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
                    user_input = "A new flight route has been registered"
                    break
                



        return user_input

    DUMMYNMBR=1
    @staticmethod
    def __show_ongoing_voyages():
        ComponentUI.print_header(ComponentUI.get_main_options()[0])
        print(TextEditor.format_text(VoyageUI.__option_tuple[1], TextEditor.UNDERLINE_TEXT))
        ComponentUI.fill_window_and_print_action_line(VoyageUI.DUMMYNMBR, False)
        pass

    
    
    @staticmethod
    def __show_completed_voyages():
        ComponentUI.print_header(ComponentUI.get_main_options()[0])
        print(TextEditor.format_text(VoyageUI.__option_tuple[2], TextEditor.UNDERLINE_TEXT))
        ComponentUI.fill_window_and_print_action_line(VoyageUI.DUMMYNMBR, False)
        pass
    
    @staticmethod    
    def __show_find_voyages_by_date():
        ComponentUI.print_header(ComponentUI.get_main_options()[0])
        print(TextEditor.format_text(VoyageUI.__option_tuple[3], TextEditor.UNDERLINE_TEXT))
        ComponentUI.fill_window_and_print_action_line(VoyageUI.DUMMYNMBR, False)
        pass
    
    @staticmethod
    def __show_find_voyages_by_week():
        ComponentUI.print_header(ComponentUI.get_main_options()[0])
        print(TextEditor.format_text(VoyageUI.__option_tuple[4], TextEditor.UNDERLINE_TEXT))
        ComponentUI.fill_window_and_print_action_line(VoyageUI.DUMMYNMBR, False)
        pass
    
    @staticmethod
    def __show_find_voyages_by_destination():
        ComponentUI.print_header(ComponentUI.get_main_options()[0])
        print(TextEditor.format_text(VoyageUI.__option_tuple[4], TextEditor.UNDERLINE_TEXT))
        ComponentUI.fill_window_and_print_action_line(VoyageUI.DUMMYNMBR, False)
        pass

 
        
        
