class Flight:
    def __init__(self, departure_location, departure_time, arrival_location, arrival_time, number, sold_ticket_count):
        self.__departure_location = departure_location
        self.__departure_time = departure_time
        self.__arrival_location = arrival_location
        self.__arrival_time = arrival_time
        self.__number = number
        self.__sold_ticket_count = sold_ticket_count
    
    def get_departure_location(self):
        return self.__departure_location

    def get_departure_time(self):
        return self.__departure_time
    
    def get_arrival_location(self):
        return self.__arrival_location
    
    def get_arrival_time(self):
        return self.__arrival_time
    
    def get_number(self):
        return self.__number
    
    def get_sold_ticket_count(self):
        return self.__sold_ticket_count
