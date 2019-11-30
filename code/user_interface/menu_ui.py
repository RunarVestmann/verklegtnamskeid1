from window import Window

class MenuUI:

    @staticmethod
    def print_header():
        Window.clear()

        window_width, window_height = Window.get_size()

        print('*' * window_width)
        print("--x-O-x--".center(window_width))
        print()
        print("NaN Air".center(window_width, " "))
        print()
        print('*' * window_width)
