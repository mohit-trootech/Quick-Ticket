"""Quick-Cart constant File to Store Constant Variable & Messages"""

import os
from enum import Enum
from enums import DataOption, UserRole, ServicesEnum, MoviesData

PAST_MOVIE = MoviesData.PAST_MOVIES
UPCOMING_MOVIE = MoviesData.UPCOMING_MOVIES
ADD_MOVIE = ServicesEnum.ADD_MOVIE
BOOK_MOVIE = ServicesEnum.BOOK_MOVIE
USER_JSON = DataOption.USER_JSON
MOVIE_JSON = DataOption.MOVIE_JSON
ROLE_HOST = UserRole.ROLE_HOST
ROLE_WATCHER = UserRole.ROLE_WATCHER
BASE_JSON_DIR = os.path.join(os.getcwd(), "quick_tickets_json")
TRANSACTION_FILENAME_FORMAT = "{username}_transactions.json"
DATA_JSON_PATH = os.path.join(BASE_JSON_DIR, "data.json")
DATA_JSON_FORMAT = {"USER_JSON": {}, "MOVIE_JSON": {}}


# Navigation Messages
USER_INFORMATION_MSG = "Please Enter User Information"

# Success Messages
DATA_INSERT_OK = "Data is Inserted Successfully"
USER_EXIST = "Please Login User {username} Already Exist"
USER_NOT_EXIST = "Please Continue Signup"
WELCOME = "Welcome to Quick Tickets {username}"
ADD_MOVIE_MSG = "Please Enter Movie Description: {moviename}"
TICKET_BOOKING_CONFIRM = (
    "Thank you Purchasing {quantity} Tickets\nTotal Amount: {price}"
)
COMPLETE = "Thank You Visit Again"
USER_CREATED = "User Created Successfully"


# Error Messages
AUTHENTICATE_ERROR = "Password Don't Match Try Again ;-(("
AUTHORIZE_ERROR = "You Are Not Authorized for This ;-(("
VAlUE_ERROR = "Please Enter Valid Integer Value, You are Left with {tries} Tries"
UNKNOWN_ERROR = "Unknown Exception Occurred Try Again ;-( : {err}"
TICKET_QUANTITY_CHECK = "Your are Left with {tries} Tries"
DATE_VALIDATION_ERROR = "Start Date Must be Smaller Than End Date"
DATA_NOT_FOUND = "No Movies Available"
VALID_INPUT = "Choose Valid Input"
INELIGIBLE_ERROR = "You are Under Age to Book Tickets Required 18 plus"
MOVIE_UNAVAILABLE = "Movie Booking Not Available Since Movie Screening is Ended"
TICKETS_UNAVAILABLE = "Try Booking the Tickets the are Available"
DATE_INPUT = "Enter Date[1-31]: "
MONTH_INPUT = "Enter Month[1-12]: "
YEAR_INPUT = "Enter Year: "

# User Input Messages
FURTHER_PROGRESS = "Press C/c to Cancel\nElse Press Enter to Continue: "
SERVICE_SELECT = "Please Select Service\n1. Book Movie\n2. Add Movie\nSelect from the Given Options in int Format: "
USERNAME_INPUT = "Please Enter Username: "
MOVIES_INPUT = "Please Choose\n1. Upcoming Movies\n2. Past Movies: "
SELECT_MOVIE_INPUT = "Please Select Movie: "
MOVIE_NAME_INPUT = "Please Enter Movie Name: "
ACTOR_NAME_INPUT = "Enter Actor Name: "
ACTRESS_NAME_INPUT = "Enter Actress Name: "
MOVIE_DURATION_INPUT = "Enter Movie Durations in Minutes: "
SEAT_INPUT = "Enter the Number of Seats: "
INPUT_START_DATE = "Enter Start Date"
INPUT_END_DATE = "Enter End Date"
DATE_SLOTS_INPUT = "Select Dates Slot: "
TIME_SLOT_INPUT = "Enter Time Slots: "
PASSWORD_INPUT = "Enter Your Password: "
USER_ROLE_INPUT = "Please Select User Role: "
NAME_INPUT = "Enter Name: "
AGE_INPUT = "Enter Age: "
EMAIL_INPUT = "Enter Email Address: "
QUANTITY_INPUT = "Select Ticket Quantity: "

if __name__ == "__main__":
    pass
