import os

class Window:

    @staticmethod
    def clear():
        '''Clears the window'''
        if os.name == "nt":
            os.system("cls") #Windows
        else:
            os.system("clear") #Linux / Mac

    @staticmethod
    def get_size():
        '''Returns a tuple containing the width and height of the window measured in characters'''
        if os.name == "nt":
            import shutil
            height, width = shutil.get_terminal_size()
        else:
            width, height = os.popen("stty size", "r").read().split()

        return width, height
