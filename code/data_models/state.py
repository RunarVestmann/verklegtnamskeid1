class State():
    __NOT_SCHEDULED_FOR_FLIGHT = "Not scheduled for flight today"
    __LANDED_ABROAD = "Landed abroad"
    __IN_FLIGHT_TO_ICELAND = "In flight to Iceland"
    __IN_FLIGHT_FROM_ICELAND = "In flight from Iceland"
    __WAITING_FOR_FLIGHT_FROM_ICELAND = "Waiting for flight from Iceland"
   
   @staticmethod
    def not_scheduled_for_flight():
        return State.__NOT_SCHEDULED_FOR_FLIGHT
    
    @staticmethod
    def landed_abroad():
        return State.__LANDED_ABROAD
    
    @staticmethod
    def in_flight_to_iceland():
        return State.__IN_FLIGHT_TO_ICELAND
    
    @staticmethod
    def in_flight_from_iceland():
        return State.__IN_FLIGHT_FROM_ICELAND
    
    @staticmethod
    def waiting_for_flight_from_iceland():
        return State.__WAITING_FOR_FLIGHT_FROM_ICELAND