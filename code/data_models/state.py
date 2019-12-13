class State:
    '''A class that holds the different states the airplanes, employees and voyages can be in'''

    ####  States for both employees and airplanes ####

    __NOT_SCHEDULED_FOR_FLIGHT = "Not scheduled for flight today"
    __LANDED_ABROAD = "Landed abroad"
    __IN_FLIGHT_TO_ICELAND = "In flight to Iceland"
    __IN_FLIGHT_FROM_ICELAND = "In flight from Iceland"
    __WAITING_FOR_FLIGHT_FROM_ICELAND = "Waiting for flight from Iceland"

    __employee_and_airplane_states = (__WAITING_FOR_FLIGHT_FROM_ICELAND, __IN_FLIGHT_FROM_ICELAND,\
        __LANDED_ABROAD, __IN_FLIGHT_TO_ICELAND,__NOT_SCHEDULED_FOR_FLIGHT)

    ####  States for voyages  ####

    #__WAITING_FOR_FLIGHT_FROM_ICELAND
    #__IN_FLIGHT_FROM_ICELAND
    __WAITING_FOR_FLIGHT_TO_ICELAND = "Waiting for flight to Iceland"
    #__IN_FLIGHT_TO_ICELAND
    __VOYAGE_COMPLETED = "Voyage completed"

    __voyage_states = (__WAITING_FOR_FLIGHT_FROM_ICELAND, __IN_FLIGHT_FROM_ICELAND,\
         __WAITING_FOR_FLIGHT_TO_ICELAND, __IN_FLIGHT_TO_ICELAND, __VOYAGE_COMPLETED)

    @staticmethod
    def get_employee_states():
        return State.__employee_and_airplane_states

    @staticmethod
    def get_airplane_states():
        return State.__employee_and_airplane_states

    @staticmethod
    def get_voyage_states():
        return State.__voyage_states
