"""Quick-Ticket Utility Files Required Functions and Class Implementation"""

import json
import binascii
import os
from datetime import date, timedelta, datetime
from hashlib import sha512
import pandas

from constant import (
    DATA_JSON_PATH,
    DATA_JSON_FORMAT,
    VAlUE_ERROR,
    TICKET_QUANTITY_CHECK,
    BASE_JSON_DIR,
    TRANSACTION_FILENAME_FORMAT,
    DATE_VALIDATION_ERROR,
    MOVIE_UNAVAILABLE,
    QUANTITY_INPUT,
    TICKETS_UNAVAILABLE,
    DATE_INPUT,
    MONTH_INPUT,
    YEAR_INPUT,
)
from exceptions import UnavailableTickets, DateValidationError


def password_hash(passwd: str) -> str:
    """
    function to generate hash of password
    @param passwd:str
    @return:str
    """
    sha = sha512()
    sha.update(passwd.encode())
    return binascii.hexlify(sha.digest()).decode()


def custom_print_msg(msg: str) -> None:
    """
    Custom Function for Special Print Functionality
    @param msg:str
    """
    print(msg.center(50, "~"))


def user_input(msg: str) -> str:
    """
    custom function to get user input with strip and lower format data
    @param msg: str
    @return: str
    """
    return input(msg).lower().strip()


def user_input_int_type(msg: str) -> int:
    """
    custom function get user input in int format, if not int for 3 times raise error
    @param msg: str
    @return: int
    """
    input_tries = 3
    while True:
        try:
            value = int(input(msg))
            return value
        except ValueError:
            if input_tries > 0:
                print(VAlUE_ERROR.format(tries=input_tries))
                input_tries -= 1
            else:
                raise ValueError


def check_filepath_exists(filepath: str) -> bool:
    """
    function to check if the filepath exists
    @param filepath:str
    @return:bool
    """
    if os.path.exists(filepath):
        return False
    return True


def create_directory_if_not_exist(directory_path: str) -> None:
    """
    function to create a directory if not exist using os module
    @param directory_path: str
    """
    if check_filepath_exists(directory_path):
        os.mkdir(directory_path)


def create_file_path(*args) -> str:
    """
    function to generate filepath with variable length arguments
    @param args: list
    @return: str
    """
    return os.path.join(*args)


def create_counter_of_sequences(*args) -> dict:
    """
    return counter from available list object
    @param args: *args
    @return: dict
    """
    return dict(enumerate(*args, 1))


def read_json(file_path: str) -> dict:
    """
    function to read json file and Return Response
    @param file_path: str
    @return: dict
    """
    with open(file_path, "r") as fp:
        return json.load(fp)


def write_json(file_path: str, data: dict) -> dict:
    """
    function to write json file
    @param file_path: str
    @param data: dict
    """
    with open(file_path, "w") as fp:
        return json.dump(data, fp, indent=5)


def update_main_data(key_name: str, data_for_append: dict, data_type: str) -> None:
    """
    function to update main theater data into json file
    @param key_name:str
    @param data_for_append: dict
    @param data_type: str
    """
    data = read_json(DATA_JSON_PATH)
    data.get(data_type)[key_name] = data_for_append
    write_json(DATA_JSON_PATH, data)


def print_movie_data(movie_data: dict) -> None:
    """
    function to print movie Data
    @param movie_data:dict
    """
    print(
        f"Movie Name: {movie_data.get('name')}\n"
        f"Actor Name: {movie_data.get('actor')}\n"
        f"Actress Name: {movie_data.get('actress')}\n"
        f"Duration: {movie_data.get('duration')}\n"
        f"Ticket Price: 100 Rs"
    )
    if movie_data.get("end_date") < str(date.today()):
        print(MOVIE_UNAVAILABLE)


def print_counter_data_information(data: dict) -> None:
    """
    function to print Counter Data Information
    @param data:dict
    """
    print("Available Options")
    for key, value in data.items():
        print(f"{key}: {value}")


def create_required_json_files() -> None:
    """
    function to create requires json files
    """
    if check_filepath_exists(DATA_JSON_PATH):
        create_directory_if_not_exist(BASE_JSON_DIR)
        write_json(DATA_JSON_PATH, DATA_JSON_FORMAT)


def create_user_transactions_json_file(username: str):
    file_path = create_file_path(
        BASE_JSON_DIR, TRANSACTION_FILENAME_FORMAT.format(username=username)
    )
    if check_filepath_exists(file_path):
        write_json(file_path, {})


def user_transactions_update(**user_data) -> None:
    """
    function to write user transactions
    @param user_data: dict
    """
    file_path = create_file_path(
        BASE_JSON_DIR,
        TRANSACTION_FILENAME_FORMAT.format(username=user_data.get("username")),
    )
    if not check_filepath_exists(file_path):
        transactions_data = read_json(file_path)
        try:
            last_key = int(sorted(transactions_data.keys())[-1])
            last_key += 1
        except IndexError:
            last_key = 1
        transactions_data.setdefault(last_key, user_data)
        file_path = create_file_path(
            BASE_JSON_DIR,
            TRANSACTION_FILENAME_FORMAT.format(username=user_data.get("username")),
        )
        write_json(file_path, transactions_data)


def check_ticket_quantity(available_ticket: int) -> int:
    """
    function to check if ticket quantity for specific slot is available
    @param available_ticket: int
    @return: int
    """
    if available_ticket == 0:
        print("Houseful")
        exit()
    tries = 3
    while True:
        ticket_quantity = user_input_int_type(QUANTITY_INPUT)
        if ticket_quantity <= available_ticket:
            return ticket_quantity
        elif tries == 0:
            raise UnavailableTickets(TICKETS_UNAVAILABLE)
        else:
            print(TICKET_QUANTITY_CHECK.format(tries=tries))
            tries -= 1


def get_date():
    """
    function to return date object
    """
    d = int(input(DATE_INPUT))
    m = int(input(MONTH_INPUT))
    y = int(input(YEAR_INPUT))
    return date(y, m, d)


def generate_slots(duration: int, seats: int) -> dict:
    """
    function to generate slots: seats respectively
    @param duration: int
    @param seats: int
    @return: dict
    """
    duration = str(duration) + "min"
    datetime_slots = pandas.date_range(
        start="12:00", end="23:00", freq=duration
    ).strftime("%H:%M")
    return dict.fromkeys(datetime_slots, seats)


def create_time_slots(start_date, end_date, duration: int, seats: int) -> dict:
    """
    function to create time slots based on given start and end date
    @param seats: int
    @param duration: int
    @param start_date: date
    @param end_date: ate
    """
    slots = {}
    slots_seats_data = generate_slots(duration, seats)
    while start_date <= end_date:
        slots.setdefault(str(start_date), slots_seats_data)
        start_date = start_date + timedelta(days=1)
    return slots


def generate_movie_list_based_on_date(movie_data: dict) -> list:
    """
    function to return movie list enumerate object based on date
    @param movie_data: dict
    @return:list
    """
    upcoming_movie = []
    past_movies = []
    for movie_name, movie_data in movie_data.items():
        if str(date.today()) <= movie_data.get("end_date"):
            upcoming_movie.append(movie_name)
        else:
            past_movies.append(movie_name)
    return create_counter_of_sequences(upcoming_movie), create_counter_of_sequences(
        past_movies
    )


def get_available_date_slots(date_slots: dict) -> dict:
    """
    function to return date slots counter based on current date
    @param date_slots: dict
    @return: dict
    """
    counter = 1
    date_slot_counter = {}
    for dt in date_slots.keys():
        if str(date.today()) <= dt:
            date_slot_counter[counter] = dt
            counter += 1
    return date_slot_counter


def get_available_time_slots(slots: dict, date_slot: str) -> dict:
    """
    function to return time slots counter based on time, returns all slots after current time
    @param slots: dict
    @param date_slot: str
    @return: dict
    """
    counter = 1
    available_slots_counter = {}
    for slot in slots.keys():
        if date_slot == str(date.today()):
            if datetime.now().strftime("%H:%M") <= slot:
                available_slots_counter[counter] = slot
                counter += 1
        else:
            available_slots_counter[counter] = slot
            counter += 1
    return available_slots_counter


def check_dates_validity(start_date: str, end_date: str) -> None:
    """
    function to check date validity start date must less than end date
    @param start_date:str
    @param end_date: str
    """
    if start_date > end_date:
        raise DateValidationError(DATE_VALIDATION_ERROR)


if __name__ == "__main__":
    pass
