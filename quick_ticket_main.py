"""
Python Based Movie Booking Management System Using Filesystem and Json
Drive Code Main
"""

import time

from theater import Theater
from utils import (
    custom_print_msg,
    user_input,
    user_input_int_type,
    create_required_json_files,
    create_user_transactions_json_file,
)
from constant import (
    ADD_MOVIE,
    BOOK_MOVIE,
    FURTHER_PROGRESS,
    SERVICE_SELECT,
    VALID_INPUT,
    COMPLETE,
    USERNAME_INPUT,
)


def main() -> None:
    """
    main Driver function for Step by Step Process
    """
    create_required_json_files()
    username = user_input(USERNAME_INPUT)
    theater_obj = Theater(username)
    create_user_transactions_json_file(username)
    further_progress = user_input(FURTHER_PROGRESS)
    if further_progress == "c":
        return
    service = user_input_int_type(SERVICE_SELECT)
    if service == BOOK_MOVIE.value:
        theater_obj.list_movies()
    elif service == ADD_MOVIE.value:
        theater_obj.add_movies()
    else:
        print(VALID_INPUT)


if __name__ == "__main__":
    """module for main driver code"""
    main()
    custom_print_msg(COMPLETE)
