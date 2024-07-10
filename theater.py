"""theater file to implement logical implementation of adding and updating movies"""

from constant import (
    USER_JSON,
    ROLE_HOST,
    AUTHORIZE_ERROR,
    MOVIE_JSON,
    DATA_INSERT_OK,
    DATA_JSON_PATH,
    DATA_NOT_FOUND,
    VALID_INPUT,
    INPUT_START_DATE,
    INPUT_END_DATE,
    TICKET_BOOKING_CONFIRM,
    MOVIES_INPUT,
    ADD_MOVIE_MSG,
    PAST_MOVIE,
    UPCOMING_MOVIE,
    SELECT_MOVIE_INPUT,
    MOVIE_NAME_INPUT,
    ACTOR_NAME_INPUT,
    ACTRESS_NAME_INPUT,
    MOVIE_DURATION_INPUT,
    SEAT_INPUT,
    DATE_SLOTS_INPUT,
    TIME_SLOT_INPUT,
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
    update_main_data,
    generate_movie_list_based_on_date,
    get_available_time_slots,
    check_ticket_quantity,
    user_transactions_update,
    check_dates_validity,
    print_movie_data,
    print_counter_data_information,
    create_counter_of_sequences,
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
        method to list movies and call required method based on user input i.e. upcoming_movies_booking and past_movies_data_print
        """
        self.movies_data = read_json(DATA_JSON_PATH).get(MOVIE_JSON.name)
        option = user_input_int_type(MOVIES_INPUT)
        upcoming_movies_counter, past_movie_counter = generate_movie_list_based_on_date(
            self.movies_data
        )
        if option == UPCOMING_MOVIE.value:
            if not any(upcoming_movies_counter):
                raise DataNotFound(DATA_NOT_FOUND)
            self.upcoming_movies_booking(upcoming_movies_counter)
        elif option == PAST_MOVIE.value:
            if not any(past_movie_counter):
                raise DataNotFound(DATA_NOT_FOUND)
            self.past_movies_data_print(past_movie_counter)
        else:
            print(VALID_INPUT)
            return

    def upcoming_movies_booking(self, upcoming_movies_counter: dict) -> None:
        """
        method to work with upcoming movies and list date slots and then call book_movie method
        @param upcoming_movies_counter: dict
        """
        print_counter_data_information(upcoming_movies_counter)
        movie_selected = user_input_int_type(SELECT_MOVIE_INPUT)
        self.upcoming_movies_data = self.movies_data.get(
            upcoming_movies_counter.get(movie_selected)
        )
        self.movie_name = upcoming_movies_counter.get(movie_selected)
        self.book_movies()

    def past_movies_data_print(self, past_movie_counter: dict) -> None:
        """
        method to print past movies data
        @param past_movie_counter: dict
        """
        print_counter_data_information(past_movie_counter)
        movie_selected = user_input_int_type(SELECT_MOVIE_INPUT)
        self.past_movies_data = self.movies_data.get(
            past_movie_counter.get(movie_selected)
        )
        print_movie_data(self.past_movies_data)

    def add_movie_authorization(self):
        """
        method to check the user Authorization for adding movies
        """
        if not self.user_role == ROLE_HOST.name:
            raise AuthorizationError(AUTHORIZE_ERROR)

    def add_movies(self) -> None:
        """
        method to add movies if user is authorized for this method
        """
        self.user_data = (
            read_json(DATA_JSON_PATH).get(USER_JSON.name).get(self.username)
        )
        self.user_role = self.user_data.get("role")
        self.add_movie_authorization()
        self.movie_name = user_input(MOVIE_NAME_INPUT)
        custom_print_msg(ADD_MOVIE_MSG.format(moviename=self.movie_name.capitalize()))
        actor = user_input(ACTOR_NAME_INPUT)
        actress = user_input(ACTRESS_NAME_INPUT)
        duration = user_input_int_type(MOVIE_DURATION_INPUT)
        seats = user_input_int_type(SEAT_INPUT)
        custom_print_msg(INPUT_START_DATE)
        start_date = get_date()
        custom_print_msg(INPUT_END_DATE)
        end_date = get_date()
        check_dates_validity(start_date, end_date)
        slots = create_time_slots(
            start_date=start_date,
            end_date=end_date,
            duration=duration,
            seats=seats,
        )
        self.insert_movie_data(
            name=self.movie_name,
            actor=actor,
            actress=actress,
            duration=duration,
            start_date=str(start_date),
            end_date=str(end_date),
            slots=slots,
        )

    def insert_movie_data(self, **movie_data_to_insert):
        """
        create movie data entry into csv
        @param movie_data_to_insert: dict
        """
        update_main_data(self.movie_name, movie_data_to_insert, MOVIE_JSON.name)
        custom_print_msg(DATA_INSERT_OK)

    def book_movies(self) -> None:
        """
        method to book tickets and show necessary information like date_slots & time_slots
        """
        print_movie_data(self.upcoming_movies_data)
        movie_slots = self.upcoming_movies_data.get("slots")
        # Get Available Date Slots Counter and Get User input for the Same
        date_slot_counter = get_available_date_slots(movie_slots)
        print_counter_data_information(date_slot_counter)
        select_date_slot = user_input_int_type(DATE_SLOTS_INPUT)
        date_slot = date_slot_counter.get(select_date_slot)
        # Get Available Time Slots Counter and Get User input for the Same
        available_time_slots = get_available_time_slots(
            movie_slots.get(date_slot), date_slot
        )
        print_counter_data_information(available_time_slots)
        select_time_slot = user_input_int_type(TIME_SLOT_INPUT)
        time_slot = available_time_slots.get(select_time_slot)
        # Get Available Tickets Based on Time and Date Slot and Book Tickets for the Same Slot
        available_ticket = int(movie_slots.get(date_slot).get(time_slot))
        print(f"Available Tickets {available_ticket}")
        ticket_quantity = check_ticket_quantity(available_ticket)
        print(
            TICKET_BOOKING_CONFIRM.format(
                quantity=ticket_quantity, price=ticket_quantity * self.ticket_price
            )
        )
        movie_slots.get(date_slot)[time_slot] = available_ticket - ticket_quantity
        update_main_data(self.movie_name, self.upcoming_movies_data, MOVIE_JSON.name)
        user_transactions_update(
            username=self.username,
            movie_name=self.movie_name,
            date_slot=date_slot,
            time_slot=time_slot,
            ticket_quantity=ticket_quantity,
            total_amount=ticket_quantity * self.ticket_price,
        )


if __name__ == "__main__":
    pass
