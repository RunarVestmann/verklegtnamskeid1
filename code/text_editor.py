class TextEditor:
    '''A class that can change both the color and
       the format of strings when they are printed in the terminal'''

    #Text Background colors
    BLACK_BACKGROUND = "\033[40m"
    BLUE_BACKGROUND = "\033[44m"
    CYAN_BACKGROUND = "\033[46m"
    GREEN_BACKGROUND = "\033[42m"
    GRAY_BACKGROUND = "\033[47m"
    ORANGE_BACKGROUND = "\033[43m"
    PURPLE_BACKGROUND = "\033[45m"
    RED_BACKGROUND = "\033[41m"

    #Text Colors
    BLACK_TEXT = "\033[30m"
    BLUE_TEXT = "\033[34m"
    CYAN_TEXT = "\033[36m"
    DARKGRAY_TEXT = "\033[90m"
    GREEN_TEXT = "\033[32m"
    LIGHTBLUE_TEXT = "\033[94m"
    LIGHTCYAN_TEXT = "\033[96m"
    LIGHTGREEN_TEXT = "\033[92m"
    LIGHTGREY_TEXT = "\033[37m"
    LIGHTRED_TEXT = "\033[91m"
    ORANGE_TEXT = "\033[33m"
    PINK_TEXT = "\033[95m"
    PURPLE_TEXT = "\033[35m"
    RED_TEXT = "\033[31m"
    YELLOW_TEXT = "\033[93m"

    #Text formatting
    BOLD_TEXT = "\033[1m"
    UNDERLINE_TEXT = "\033[4m"

    RESET_TEXT = "\033[0m"

    @staticmethod
    def color_text(text, desired_color):
        '''Returns a string in the desired color'''
        return desired_color + text + TextEditor.RESET_TEXT

    @staticmethod
    def format_text(text, desired_format):
        '''Returns a string in the desired format'''
        return desired_format + text + TextEditor.RESET_TEXT

    @staticmethod
    def color_and_format_text(text, desired_color, desired_format):
        '''Returns a string in the desired color and format'''
        return desired_color + desired_format + text + TextEditor.RESET_TEXT
