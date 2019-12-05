class Employee:

    def __init__(self, name, ssn, phonenumber, home_address, email, state):
        self.__name = name
        self.__ssn = ssn
        self.__phonenumber = phonenumber
        self.__home_address = home_address
        self.__email = email
        self.__state = state

    def get_name(self):
        return self.__name

    def get_ssn(self):
        return self.__ssn

    def get_phonenumber(self):
        return self.__phonenumber

    def set_phonenumber(self, phonenumber):
        self.__phonenumber = phonenumber

    def get_home_address(self):
        return self.__home_address

    def set_home_address(self, home_address):
        self.__home_address = home_address

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_state(self):
        return self.__state

    def set_state(self, state):
        self.__state = state
