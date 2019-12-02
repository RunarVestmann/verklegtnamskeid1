class AircraftType:

    def __init__(self, plane_type, model, capacity, empty_weight, max_takeoff_weight,\
                 unit_thrust, service_ceiling, length, height, wingspan):
        self.__plane_type = plane_type
        self.__model = model
        self.__capacity = capacity
        self.__empty_weight = empty_weight
        self.__max_takeoff_weight = max_takeoff_weight
        self.__unit_thrust = unit_thrust
        self.__service_ceiling = service_ceiling
        self.__length = length
        self.__height = height
        self.__wingspan = wingspan

    def get_plane_type(self):
        return self.__plane_type

    def get_model(self):
        return self.__model

    def get_capacity(self):
        return self.__capacity

    def get_empty_weight(self):
        return self.__empty_weight

    def get_max_takeoff_weight(self):
        return self.__max_takeoff_weight

    def get_unit_thrust(self):
        return self.__unit_thrust

    def get_service_ceiling(self):
        return self.__service_ceiling

    def get_length(self):
        return self.__length

    def get_height(self):
        return self.__height

    def get_wingspan(self):
        return self.__wingspan
