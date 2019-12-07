from logic.airplane_logic import AirplaneLogic, Airplane
from logic.aircraft_type_logic import AircraftTypeLogic, AircraftType
from logic.flight_attendant_logic import FlightAttendantLogic, FlightAttendant
from logic.flight_route_logic import FlightRouteLogic, FlightRoute
from logic.pilot_logic import PilotLogic, Pilot
from logic.employee_logic import EmployeeLogic, Employee
from logic.voyage_logic import VoyageLogic, Voyage
from logic.flight_logic import FlightLogic, Flight #Má sleppa öllu eftir kommuna þegar alvöru gögnin verða til notkunar


#from data_models.employee import Employee
# from data_models.flight_route import FlightRoute
# from data_models.pilot import Pilot
# from data_models.flight_attendant import FlightAttendant
# from data_models.airplane import Airplane
# from data_models.voyage import Voyage
# from data_models.flight import Flight
#import dateutil.parser
class LogicAPI:
    '''The logic layer API that enables the UI layer to save and
       get data from the data layer'''

    ####Employees####

    @staticmethod
    def get_all_employees():
        return [Pilot("Fannar","1803823879","7746969","4661200","Drekagili","fannark82@msn.is","Waiting for flight to Iceland","Silverplate B-29"),\
        Pilot("Patrik","2004972309","7721234","4601600","Skessugili","patrik97@simnet.is","Not scheduled for flight","Silverplate B-29"),\
        Pilot("Runar","2804803219","7776666","5812345","Dvergagili","runar80@hotmail.com","Landed abroad","Silverplate B-29"),\
        Pilot("Hordur","2411932369","7739009","4663800","Langholt","hordur93@gmail.com","In flight to Iceland","Boeing B-29"),\
        Pilot("Gummyb","2805755419","7711199","4406600","Elisarbetarhagi","gummyb@redhat.com","In flight from Iceland","Boeing B-29"),\
        FlightAttendant("Samantha","1112981199","5464723","7766889","Tussugil", "samantha@thecity.com","Not scheduled for flight"),\
        FlightAttendant("Veronica","1012981199","5564723","7866889","Mellugil", "veronica@thecity.com","Landed abroad")]
            
        # return EmployeeLogic.get_all_employees()

    @staticmethod
    def get_employees_on_duty():
        return [Pilot("Patrik","2004972309","7721234","4601600","Skessugili","patrik97@simnet.is","Not scheduled for flight","Silverplate B-29"),\
        Pilot("Runar","2804803219","7776666","5812345","Dvergagili","runar80@hotmail.com","Landed abroad","Silverplate B-29")]
        #return EmployeeLogic.get_employees_on_duty()

    @staticmethod
    def get_employees_off_duty():
        return [Pilot("Hordur","2411932369","7739009","4663800","Langholt","hordur93@gmail.com","In flight to Iceland","Boeing B-29"),\
        Pilot("Gummyb","2805755419","7711199","4406600","Elisarbetarhagi","gummyb@redhat.com","In flight from Iceland","Boeing B-29")]
        #return EmployeeLogic.get_employees_off_duty()

    ####Pilots####

    @staticmethod
    def get_all_pilots():
        return [Pilot("Fannar","1803823879","7746969","4661200","Drekagili","fannark82@msn.is","Waiting for flight to Iceland","Silverplate B-29"),\
        Pilot("Patrik","2004972309","7721234","4601600","Skessugili","patrik97@simnet.is","Not scheduled for flight","Silverplate B-29"),\
        Pilot("Runar","2804803219","7776666","5812345","Dvergagili","runar80@hotmail.com","Landed abroad","Silverplate B-29"),\
        Pilot("Hordur","2411932369","7739009","4663800","Langholt","hordur93@gmail.com","In flight to Iceland", "Boeing B-29"),\
        Pilot("Gummyb","2805755419","7711199","4406600","Elisarbetarhagi","gummyb@redhat.com","In flight from Iceland","Boeing B-29")]
        #return PilotLogic.get_all_pilots()

    @staticmethod
    def get_licensed_pilots(pilot_license):
        return [Pilot("Fannar","1803823879","7746969","4661200","Drekagili","fannark82@msn.is","Waiting for flight to Iceland","Silverplate B-29"),\
        Pilot("Patrik","2004972309","7721234","4601600","Skessugili","patrik97@simnet.is","Not scheduled for flight","Silverplate B-29")]
        #return PilotLogic.get_licensed_pilots(pilot_license)

    @staticmethod
    def save_new_pilot(pilot):
        PilotLogic.save_new_pilot(pilot)

        
    @staticmethod
    def is_pilot_ssn_available(pilot_ssn):
        PilotLogic.is_pilot_ssn_available(pilot_ssn)

    ####Flight attendants####

    @staticmethod
    def get_all_flight_attendants():
        return [FlightAttendant("Samantha","1112981199","5464723","7766889","Tussugil", "samantha@thecity.com","Not scheduled for flight"),\
        FlightAttendant("Veronica","1012981199","5564723","7866889","Mellugil", "veronica@thecity.com","Landed abroad")]      #return FlightAttendantLogic.get_all_flight_attendants()

    @staticmethod
    def save_new_flight_attendant(flight_attendant):
        FlightAttendantLogic.save_new_flight_attendant(flight_attendant)

    @staticmethod
    def is_flight_attendant_ssn_avaliable(flight_attendant_ssn):
        return FlightAttendantLogic.is_flight_attendant_ssn_avaliable(flight_attendant_ssn)
        
    ####Voyages####

    @staticmethod
    def save_new_voyage(voyage):
        VoyageLogic.save_new_voyage(voyage)

    @staticmethod
    def get_ongoing_voyages():
        voyage1 = Voyage( (Flight("Iceland","15:00","Nuuk","19:00","NA201",100),Flight("Nuuk","20:00","Iceland","00:00","NA202",20)),\
        [Pilot("Runar","2804803219","7776666","5812345","Dvergagili","runar80@hotmail.com","Landed abroad","Silverplate B-29"),\
        Pilot("Hordur","2411932369","7739009","4663800","Langholt","hordur93@gmail.com","In flight to Iceland", "Boeing B-29")],\
        [FlightAttendant("Samantha","1112981199","5464723","7766889","Tussugil", "samantha@thecity.com","Not scheduled for flight"),\
        FlightAttendant("Veronica","1012981199","5564723","7866889","Mellugil", "veronica@thecity.com","Landed abroad")],\
        Airplane("Bockscar","Silverplate B-29","Boeing",80,"In flight to Iceland"),\
        ("2019-12-23T18:00:00","2019-12-23T22:00:00"),\
        False,\
        "In flight to Iceland")
        return [voyage1]

        # return VoyageLogic.get_ongoing_voyages()

    @staticmethod
    def get_voyages_by_date(date):
        voyage1 = Voyage( (Flight("Iceland","15:00","Nuuk","19:00","NA201",100),Flight("Nuuk","20:00","Iceland","00:00","NA202",20)),\
        [Pilot("Runar","2804803219","7776666","5812345","Dvergagili","runar80@hotmail.com","Landed abroad","Silverplate B-29"),\
        Pilot("Hordur","2411932369","7739009","4663800","Langholt","hordur93@gmail.com","In flight to Iceland", "Boeing B-29")],\
        [FlightAttendant("Samantha","1112981199","5464723","7766889","Tussugil", "samantha@thecity.com","Not scheduled for flight"),\
        FlightAttendant("Veronica","1012981199","5564723","7866889","Mellugil", "veronica@thecity.com","Landed abroad")],\
        Airplane("Bockscar","Silverplate B-29","Boeing",80,"In flight to Iceland"),\
        ("2019-12-23T18:00:00","2019-12-23T22:00:00"),\
        False,\
        "In flight to Iceland")
        return [voyage1]
        #return VoyageLogic.get_voyages_by_date(date)

    @staticmethod
    def get_voyages_by_week(week):
        voyage1 = Voyage( (Flight("Iceland","15:00","Nuuk","19:00","NA201",100),Flight("Nuuk","20:00","Iceland","00:00","NA202",20)),\
        [Pilot("Runar","2804803219","7776666","5812345","Dvergagili","runar80@hotmail.com","Landed abroad","Silverplate B-29"),\
        Pilot("Hordur","2411932369","7739009","4663800","Langholt","hordur93@gmail.com","In flight to Iceland", "Boeing B-29")],\
        [FlightAttendant("Samantha","1112981199","5464723","7766889","Tussugil", "samantha@thecity.com","Not scheduled for flight"),\
        FlightAttendant("Veronica","1012981199","5564723","7866889","Mellugil", "veronica@thecity.com","Landed abroad")],\
        Airplane("Bockscar","Silverplate B-29","Boeing",80,"In flight to Iceland"),\
        ("2019-12-23T18:00:00","2019-12-23T22:00:00"),\
        False,\
        "In flight to Iceland")
        return [voyage1]
        #return VoyageLogic.get_voyages_by_week(week)

    @staticmethod
    def get_voyages_by_destination(destination):
        voyage1 = Voyage( (Flight("Iceland","15:00","Nuuk","19:00","NA201",100),Flight("Nuuk","20:00","Iceland","00:00","NA202",20)),\
        [Pilot("Runar","2804803219","7776666","5812345","Dvergagili","runar80@hotmail.com","Landed abroad","Silverplate B-29"),\
        Pilot("Hordur","2411932369","7739009","4663800","Langholt","hordur93@gmail.com","In flight to Iceland", "Boeing B-29")],\
        [FlightAttendant("Samantha","1112981199","5464723","7766889","Tussugil", "samantha@thecity.com","Not scheduled for flight"),\
        FlightAttendant("Veronica","1012981199","5564723","7866889","Mellugil", "veronica@thecity.com","Landed abroad")],\
        Airplane("Bockscar","Silverplate B-29","Boeing",80,"In flight to Iceland"),\
        ("2019-12-23T18:00:00","2019-12-23T22:00:00"),\
        False,\
        "In flight to Iceland")
        return [voyage1]
        #return VoyageLogic.get_voyages_by_destination(destination)

    @staticmethod
    def get_airplane_voyages(airplane):
        return VoyageLogic.get_airplane_voyages(airplane)
    
    @staticmethod
    def is_voyage_schedule_start_day_and_time_available(voyage_day_and_time):
        return VoyageLogic.is_voyage_schedule_start_day_and_time_available(voyage_day_and_time)

    ####Airplanes####
    
    @staticmethod
    def is_airplane_name_available(plane_name):
        return AirplaneLogic.is_airplane_name_available(plane_name)

    @staticmethod
    def save_new_airplane(airplane):
        return AirplaneLogic.save_new_airplane(airplane)

    @staticmethod
    def get_all_airplanes():
        return [Airplane("Enola","Boeing B-29","Boeing",146,"Landed abroad"),\
        Airplane("Bockscar","Silverplate B-29","Boeing",80,"In flight to Iceland")]
        #return AirplaneLogic.get_all_airplanes()

    @staticmethod
    def get_all_airplanes_in_use():
        return [Airplane("Enola","Boeing B-29","Boeing",146,"Landed abroad"),\
        Airplane("Bockscar","Silverplate B-29","Boeing",80,"In flight to Iceland")]
        #return AirplaneLogic.get_all_airplanes_in_use()

    @staticmethod
    def get_all_airplane_types():
        return [Airplane("Enola","Boeing B-29","Boeing",146,"Landed abroad"),\
        Airplane("Bockscar","Silverplate B-29","Boeing",80,"In flight to Iceland")]
        #return AircraftTypeLogic.get_all_aircraft_types()

    @staticmethod
    def get_all_available_airplanes(schedule_tuple):
        return [Airplane("Enola","Boeing B-29","Boeing",146,"Landed abroad"),\
        Airplane("Bockscar","Silverplate B-29","Boeing",80,"In flight to Iceland")]
        #return AirplaneLogic.get_all_available_airplanes()

    ####Flight routes####

    @staticmethod
    def save_new_flight_route(flight_route):
        FlightRouteLogic.save_new_flight_route(flight_route)

    @staticmethod
    def get_all_flight_routes():
        Nuuk = FlightRoute("Greenland","Nuuk","G2192","4:00","1570km","Oddur","1234666")
        Kulusuk = FlightRoute("Greenland","Kulusuk","G3892","2:00","871km","Baldur","1126662")
        Thorhavn = FlightRoute("Faroe Islands","Thorhavn","F8198","1:10","493km","Sverre","9991234")
        Tingwall = FlightRoute("Hjaltlandseyjum","Tingwall","H8219","3:00","1100km","mcdougal","9991298")
        Longyearbyen = FlightRoute("Svalbarda","Longyearbyen","S2174","4:20","1761","Olle","8829053")
        return[Nuuk,Kulusuk,Thorhavn,Tingwall,Longyearbyen]


        # return DataAPI.get_all_flight_routes()
    @staticmethod
    def get_all_flights():
        return FlightLogic.get_all_flights() 

    @staticmethod
    def get_flight(departure_time):
        return FlightLogic.get_flight(departure_time)

    @staticmethod
    def save_new_flight(flight):
        FlightLogic.save_new_flight(flight)
    
    @staticmethod
    def is_airport_id_available(airport_id):
        return FlightRouteLogic.is_airport_id_available(airport_id)