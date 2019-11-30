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
    def color_text(text, color):
        '''Returns a new string with the given font color'''
        return color + text + TextEditor.RESET_TEXT

    @staticmethod
    def color_text_background(text, background_color):
        '''Returns a new string with the given background color'''
        return background_color + text + TextEditor.RESET_TEXT

    @staticmethod
    def format_text(text, text_format):
        '''Returns a new string in the given format'''
        return text_format + text + TextEditor.RESET_TEXT

    @staticmethod
    def color_and_format_text(text, color, text_format):
        '''Returns a new string in the given color and format'''
        return color + text_format + text + TextEditor.RESET_TEXT

    @staticmethod
    def edit_text(text, color="", background_color="", text_format=""):
        '''Returns a new string in the given font color, background color and text format,
           if no argument is passed returns the unedited text'''

        #No arguments passed
        if not color and not background_color and not text_format:
            return text

        return background_color + color + text_format + text + TextEditor.RESET_TEXT
