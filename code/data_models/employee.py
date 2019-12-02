class Employee:

    def __init__(self, name, ssn, mobile_phone, home_phone, home_address, email, state):
        self.__name = name
        self.__ssn = ssn
        self.__mobile_phone = mobile_phone
        self.__home_phone = home_phone
        self.__home_address = home_address
        self.__email = email
        self.__state = state

    def get_name(self):
        return self.__name

    def get_ssn(self):
        return self.__ssn

    def get_mobile_phone(self):
        return self.__mobile_phone

    def set_mobile_phone(self, mobile_phone):
        self.__mobile_phone = mobile_phone

    def get_home_phone(self):
        return self.__home_phone

    def set_home_phone(self, home_phone):
        self.__home_phone = home_phone

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
