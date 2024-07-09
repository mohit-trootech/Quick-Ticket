"""Quick-Cart constant File to Store Constant Variable & Messages"""

import os

BASE_JSON_DIR = os.path.join(os.getcwd(), "quick_tickets_json")
TRANSACTION_FILENAME_FORMAT = "{username}_transactions.json"
DATA_JSON_PATH = os.path.join(BASE_JSON_DIR, "data.json")
DATA_JSON_FORMAT = {"USER_JSON": {}, "MOVIE_JSON": {}}
DATA_OPTION = dict(enumerate(["USER_JSON", "MOVIE_JSON"], 1))
USER_JSON = DATA_OPTION.get(1)
MOVIE_JSON = DATA_OPTION.get(2)


# User Role
ROLE = tuple(enumerate(["host", "watcher"], 1))
ROLE_HOST = ROLE[0][1]
ROLE_WATCHER = ROLE[1][1]


# Success Messages
DATA_INSERT_OK = "Data is Inserted Successfully"
USER_EXIST = "Please Login User {username} Already Exist"
USER_NOT_EXIST = "Please Continue Signup"
WELCOME = "Welcome to Quick Tickets {username}"
ADD_MOVIE = "Please Enter Movie Description: {moviename}"

# Error Messages
AUTHENTICATE_ERROR = "Password Don't Match Try Again ;-(("
AUTHORIZE_ERROR = "You Are Not Authorized for This ;-(("
VAlUE_ERROR = "Please Enter Valid Integer Value, You are Left with {tries} Tries"
UNKNOWN_ERROR = "Unknown Exception Occurred Try Again ;-( : {err}"
TICKET_QUANTITY_CHECK = "Your are Left with {tries} Tries"
DATE_VALIDATION_ERROR = "Start Date Must be Smaller Than End Date"

if __name__ == "__main__":
    pass
