from menu_ui import MenuUI
from window import Window

class QuitUI:

    @staticmethod
    def __print_quit_menu_body():

        width, height = Window.get_size()
        body_height = height - MenuUI.HEADER_HEIGHT

        offsetted_body_height_center = (body_height//2) - 2

        for _ in range(offsetted_body_height_center):
            print()
        print("Are you sure you want to quit?".center(width))
        print("(Y)es    (N)o".center(width))
        for _ in range(offsetted_body_height_center):
            print()
        print("_" * width)


    @staticmethod
    def show_quit_menu():
        user_input = ''
        while user_input != 'y':
            MenuUI.print_header(MenuUI.MAIN_OPTIONS[4])
            QuitUI.__print_quit_menu_body()
            user_input = input("Your action: ").lower().strip()
            if user_input.startswith('y'):
                exit(0)
            elif user_input.startswith('n'):
                MenuUI.show_main_menu()

QuitUI.show_quit_menu()