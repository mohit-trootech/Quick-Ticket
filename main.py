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


def main() -> None:
    """
    main Driver function for Step by Step Process
    @return:None
    """
    create_required_json_files()
    username = user_input("Please Enter Username: ")
    theater_obj = Theater(username)
    create_user_transactions_json_file(username)
    further_progress = user_input("Press C/c to Cancel\nElse Press Enter to Continue: ")
    if further_progress == "c":
        return
    service = user_input_int_type(
        "Please Select Service\n"
        "1. Book Movie\n"
        "2. Add Movie\n"
        "Select from the Given Options in int Format: "
    )
    if service == 1:
        theater_obj.list_movies()
    elif service == 2:
        theater_obj.add_movies()
    else:
        print("Please Choose Valid Input")


if __name__ == "__main__":
    """module for main driver code"""
    main()
    custom_print_msg("Thank You Visit Again")
