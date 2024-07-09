"""theater file to implement logical implementation of adding and updating movies"""

import pprint

from constant import (
    USER_JSON,
    ROLE_HOST,
    AUTHORIZE_ERROR,
    ADD_MOVIE,
    MOVIE_JSON,
    DATA_INSERT_OK,
    DATA_JSON_PATH,
)
from exceptions import AuthorizationError, DataNotFound
from users import User
from utils import (
    user_input_int_type,
    get_available_date_slots,
    custom_print_msg,
    read_json,
    user_input,
    get_date,
    create_time_slots,
    update_main_theater_data,
    generate_movie_list_based_on_date,
    get_available_time_slots,
    check_ticket_quantity,
    user_transactions_update,
    check_dates_validity,
)


class Theater(User):
    """__main__.Theater class to implement theater logic"""

    def __init__(self, username: str) -> None:
        """
        Theater class constructor
        @param username: str
        """
        super().__init__(username)
        self.ticket_price = 100
        self.movies_data = None
        self.movie_name = None
        self.upcoming_movies_data = None
        self.past_movies_data = None
        self.user_data = None
        self.user_role = None

    def list_movies(self) -> None:
        """
        method to list movies and call required method based on user input i.e. upcoming_movies_booking and
        past_movies_data_print
        @return: None
        """
        self.movies_data = read_json(DATA_JSON_PATH).get(MOVIE_JSON)
        date_specified_movies_list = generate_movie_list_based_on_date(self.movies_data)
        option = user_input_int_type(
            "Please Choose\n1. Upcoming Movies\n2. Past Movies: "
        )
        upcoming_movies_counter = dict(enumerate(date_specified_movies_list[0], 1))
        past_movie_counter = dict(enumerate(date_specified_movies_list[1], 1))
        if option == 1:
            if not any(upcoming_movies_counter):
                raise DataNotFound("No Upcoming Movies Available")
            self.upcoming_movies_booking(upcoming_movies_counter)
        elif option == 2:
            if not any(past_movie_counter):
                raise DataNotFound("No Past Movies Available")
            self.past_movies_data_print(past_movie_counter)
        else:
            print("Choose Valid Input")
            return

    def upcoming_movies_booking(self, upcoming_movies_counter: dict) -> None:
        """
        method to work with upcoming movies and list date slots and then call book_movie method
        @param upcoming_movies_counter: dict
        @return: None
        """
        pprint.pp(upcoming_movies_counter)
        movie_selected = user_input_int_type("Please Select Movie: ")
        self.upcoming_movies_data = self.movies_data.get(
            upcoming_movies_counter.get(movie_selected)
        )
        self.movie_name = upcoming_movies_counter.get(movie_selected)
        self.book_movies()

    def past_movies_data_print(self, past_movie_counter: dict) -> None:
        """
        method to print past movies data
        @param past_movie_counter: dict
        @return: None
        """
        pprint.pp(past_movie_counter)
        movie_selected = user_input_int_type("Please Select Movie: ")
        self.past_movies_data = self.movies_data.get(
            past_movie_counter.get(movie_selected)
        )
        pprint.pp(self.past_movies_data)

    def add_movie_authorization(self):
        """
        method to check the user Authorization for adding movies
        @return: None
        """
        if self.user_role == ROLE_HOST:
            return
        else:
            raise AuthorizationError(AUTHORIZE_ERROR)

    def add_movies(self) -> None:
        """
        method to add movies if user is authorized for this method
        @return: None
        """
        self.user_data = read_json(DATA_JSON_PATH).get(USER_JSON).get(self.username)
        self.user_role = self.user_data.get("role")
        self.add_movie_authorization()
        self.movie_name = user_input("Please Enter Movie Name: ")
        custom_print_msg(ADD_MOVIE.format(moviename=self.movie_name.capitalize()))
        actor = user_input("Enter Actor Name: ")
        actress = user_input("Enter Actress Name: ")
        duration = user_input_int_type("Enter Movie Durations in Minutes: ")
        seats = user_input_int_type("Enter the Number of Seats: ")
        custom_print_msg("Enter Start Date")
        start_date = get_date()
        custom_print_msg("Enter End Date")
        end_date = get_date()
        check_dates_validity(start_date, end_date)
        slots = create_time_slots(
            start_date=start_date,
            end_date=end_date,
            duration=duration,
            seats=seats,
        )
        movie_data_to_append = {
            "name": self.movie_name,
            "actor": actor,
            "actress": actress,
            "duration": duration,
            "start_date": str(start_date),
            "end_date": str(end_date),
            "slots": slots,
        }
        update_main_theater_data(self.movie_name, movie_data_to_append, MOVIE_JSON)
        custom_print_msg(DATA_INSERT_OK)

    def book_movies(self) -> None:
        """
        method to book tickets and show necessary information like date_slots & time_slots
        @return:None
        """
        pprint.pp(self.upcoming_movies_data)
        movie_slots = self.upcoming_movies_data.get("slots")
        # Get Available Date Slots Counter and Get User input for the Same
        date_slot_counter = get_available_date_slots(movie_slots)
        pprint.pp(date_slot_counter)
        select_date_slot = user_input_int_type("Select Dates Slot: ")
        date_slot = date_slot_counter.get(select_date_slot)
        # Get Available Time Slots Counter and Get User input for the Same
        available_time_slots = get_available_time_slots(
            movie_slots.get(date_slot), date_slot
        )
        pprint.pp(available_time_slots)
        select_time_slot = user_input_int_type("Enter Slots: ")
        time_slot = available_time_slots.get(select_time_slot)
        # Get Available Tickets Based on Time and Date Slot and Book Tickets for the Same Slot
        available_ticket = int(movie_slots.get(date_slot).get(time_slot))
        print(f"Available Tickets {available_ticket}")
        ticket_quantity = check_ticket_quantity(available_ticket)
        print(
            f"Thank you Purchasing {ticket_quantity} Tickets\n"
            f"Total Amount: {ticket_quantity*self.ticket_price}"
        )
        movie_slots.get(date_slot)[time_slot] = available_ticket - ticket_quantity
        update_main_theater_data(self.movie_name, self.upcoming_movies_data, MOVIE_JSON)
        user_transactions_update(
            self.username,
            self.movie_name,
            date_slot,
            time_slot,
            ticket_quantity,
            ticket_quantity * self.ticket_price,
        )


if __name__ == "__main__":
    # obj = Theater("mohit")
    # obj.list_movies()
    pass
