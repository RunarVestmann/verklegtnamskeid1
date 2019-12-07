from user_interface.window import Window
from user_interface.text_editor import TextEditor
from user_interface.component_ui import ComponentUI
from apis.logic_api import LogicAPI




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
        ComponentUI.print_header(ComponentUI.get_main_options()[0])
        print(TextEditor.format_text(VoyageUI.__option_tuple[0], TextEditor.UNDERLINE_TEXT))
        
        constructor_voyage_tuple = ('Flight route', 'Voyage schedule', 'Airplane', 'Pilots', 'Flight attendants')
        for i, option in enumerate(constructor_voyage_tuple):
            print("({}) {}: ".format(i+1,option))

        ComponentUI.fill_window_and_print_action_line(len(constructor_voyage_tuple)+1, True)
       # user_input = input("Your action: ").lower().strip()

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

 
        
        
