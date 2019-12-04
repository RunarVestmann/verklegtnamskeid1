class State:
    #State for employee and airplane
    __NOT_SCHEDULED_FOR_FLIGHT = "Not scheduled for flight today"
    __LANDED_ABROAD = "Landed abroad"
    __IN_FLIGHT_TO_ICELAND = "In flight to Iceland"
    __IN_FLIGHT_FROM_ICELAND = "In flight from Iceland"
    __WAITING_FOR_FLIGHT_FROM_ICELAND = "Waiting for flight from Iceland"
    __employee_and_airplane_states = (__NOT_SCHEDULED_FOR_FLIGHT,__WAITING_FOR_FLIGHT_FROM_ICELAND,__IN_FLIGHT_FROM_ICELAND,__LANDED_ABROAD,__IN_FLIGHT_TO_ICELAND)
    
    #State for voyages
    #__WAITING_FOR_FLIGHT_FROM_ICELAND = "Waiting for flight from Iceland"
    #__IN_FLIGHT_FROM_ICELAND = "In flight from Iceland"
    __WAITING_FOR_FLIGHT_TO_ICELAND = "Waiting for flight to Iceland"
    #__IN_FLIGHT_TO_ICELAND = "In flight to Iceland"
    __VOYAGE_COMPLETED = "Voyage completed"
    __voyage_state = (__WAITING_FOR_FLIGHT_FROM_ICELAND,__IN_FLIGHT_FROM_ICELAND,__WAITING_FOR_FLIGHT_TO_ICELAND,__IN_FLIGHT_TO_ICELAND,__VOYAGE_COMPLETED)

    @staticmethod
    def get_employee_state():
        return State.__employee_and_airplane_states

    
    @staticmethod
    def get_airplane_state():
        return State.__employee_and_airplane_states

    
    @staticmethod
    def get_voyage_state():
        return State.__voyage_state 