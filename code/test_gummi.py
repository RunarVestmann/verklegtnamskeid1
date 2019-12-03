#from user_interface.quit_ui import QuitUI
from apis.logic_api import LogicAPI
print(LogicAPI.get_all_employees()[-1].get_name())
#QuitUI.show_quit_menu()