from user_interface.menu_ui import MenuUI
from user_interface.window import Window

class AirplanesUI:
 
    @staticmethod
    def show_airplanes_menu():
        MenuUI.print_header(MenuUI.get_main_options()[2])
        option_list = ('New airplane', 'Show all airplanes', 'Show airplanes in use', 'show all airplane types')
        print()
        for i, option in enumerate(option_list):
            print("({}) {}".format(i+1,option))
        MenuUI.fill_window_and_print_action_line(len(option_list)+1)
        user_input = input("Your action: ").lower().strip()
    
        if user_input == '1' or user_input == '(1)':
            AirplanesUI.show_new_airplane_constructor(option_list[0])

        elif user_input == '2' or user_input == '(2)':
            AirplanesUI.show_all_airplanes(option_list[1])

        elif user_input == '3' or user_input == '(3)':
            AirplanesUI.show_airplanes_in_use(option_list[2])

        elif user_input == '4' or user_input == '(4)':
            AirplanesUI.show_all_airplane_types(option_list[3])

        else:
            AirplanesUI.show_airplanes_menu()
    
    @staticmethod
    def show_new_airplane_constructor():
        pass

    @staticmethod
    def show_all_airplanes():
        pass

    @staticmethod
    def show_airplanes_in_use():
        pass
    
    @staticmethod
    def show_all_airplane_types():
        pass
