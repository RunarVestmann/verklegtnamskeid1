import datetime
from data_models.state import State
from data_models.voyage import Voyage
from logic.airplane_logic import AirplaneLogic
from logic.employee_logic import EmployeeLogic
from logic.voyage_logic import VoyageLogic
from apis.data_api import DataAPI

class StateLogic:

    @staticmethod
    def __update_state_of_voyage(voyage, current_date_and_time):

        flights = voyage.get_flights()

        flight1_departure_time = flights[0].get_departure_time()
        flight1_arrival_time = flights[0].get_arrival_time()

        flight2_departure_time = flights[1].get_departure_time()
        flight2_arrival_time = flights[1].get_arrival_time()

        #state_of_voyage = voyage.get_state()

        voyage_states = State.get_voyage_states()

        
        if flight2_arrival_time <= current_date_and_time:
            voyage.set_state(voyage_states[4])

        elif flight2_departure_time <= current_date_and_time:
            voyage.set_state(voyage_states[3])

        elif flight1_arrival_time <= current_date_and_time:
            voyage.set_state(voyage_states[2])
        
        elif flight1_departure_time <= current_date_and_time:
            voyage.set_state(voyage_states[1])

        else:
            voyage.set_state(voyage_states[0])    


        # #Waiting for flight from Iceland -> In flight from Iceland
        # if state_of_voyage == voyage_states[0]:
        #     if flight1_departure_time <= current_date_and_time:
        #         voyage.set_state(voyage_states[1])

        #     # if flight1_departure_time <= current_date_and_time\
        #     # and flight1_arrival_time > current_date_and_time:
        #     #     voyage.set_state(voyage_states[1])

        # #In flight from Iceland -> Waiting for flight to Iceland
        # elif state_of_voyage == voyage_states[1]:
        #     if flight1_arrival_time <= current_date_and_time\
        #     and flight2_departure_time > current_date_and_time:
        #         voyage.set_state(voyage_states[2])

        # #Waiting for flight to Iceland -> In flight to Iceland
        # elif state_of_voyage == voyage_states[2]:
        #     if flight2_departure_time <= current_date_and_time\
        #     and flight2_arrival_time > current_date_and_time:
        #         voyage.set_state(voyage_states[3])

        # #In flight to Iceland -> Voyage completed
        # elif state_of_voyage == voyage_states[3]:
        #     if flight2_arrival_time <= current_date_and_time:
        #         voyage.set_state(voyage_states[4])


    @staticmethod
    def __update_state_of_entity(entity, state_of_voyage):

        voyage_states = State.get_voyage_states()
        entity_states = State.get_employee_states()

        state_index = voyage_states.index(state_of_voyage)
        entity.set_state(entity_states[state_index])

        # #Waiting for flight from Iceland
        # if state_of_voyage == voyage_states[0]:
        #     entity.set_state(voyage_states[1])

        # #In flight from Iceland
        # elif state_of_voyage == voyage_states[1]:
        #     entity.set_state(voyage_states[2])


        # #Waiting for flight to Iceland
        # elif state_of_voyage == voyage_states[2]:
        #     entity.set_state(voyage_states[3])


        # #In flight to Iceland
        # elif state_of_voyage == voyage_states[3]:
        #     entity.set_state(voyage_states[4])

        # elif state_of_voyage == voyage_states[4]:
        #     entity.set_state(voyage_states[0])

    @staticmethod
    def initialize():
        all_voyages = VoyageLogic.get_all_voyages()

        current_date_and_time = datetime.datetime.now()

        for voyage in all_voyages:
            previous_state_of_voyage = voyage.get_state()

            airplane = voyage.get_airplane()

            employees_in_voyage = voyage.get_pilots() + voyage.get_flight_attendants()

            StateLogic.__update_state_of_voyage(voyage, current_date_and_time)

            state_of_voyage = voyage.get_state()

            #Update the airplanes state
            StateLogic.__update_state_of_entity(airplane, state_of_voyage)

            #Update the states of all the employees
            for employee in employees_in_voyage:
                StateLogic.__update_state_of_entity(employee, state_of_voyage)


            if previous_state_of_voyage != state_of_voyage:
                DataAPI.change_saved_voyage(voyage, voyage)
                DataAPI.change_saved_airplane(airplane, airplane)
 
                __pilot_count = len(voyage.get_pilots())
                for i, employee in enumerate(employees_in_voyage):
                    if i < __pilot_count:
                        DataAPI.change_saved_pilot(employee,employee)
                    else:
                        DataAPI.change_saved_flight_attendant(employee,employee)
           

                    
                
                
                

