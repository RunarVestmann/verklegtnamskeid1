from employee import Employee

class Pilot(Employee):

    def __init__(self, name, ssn, mobile_phone, home_phone, home_address, email, state, pilot_license):
        super().__init__(name, ssn, mobile_phone, home_phone, home_address, email, state)
        self.__pilot_license = pilot_license

    def get_license(self):
        return self.__pilot_license

    def set_license(self, pilot_license):
        self.__pilot_license = pilot_license
