"""User Signup and Signin class Logic"""

from constant import (
    ROLE_HOST,
    ROLE_WATCHER,
    USER_JSON,
    USER_EXIST,
    USER_NOT_EXIST,
    WELCOME,
    AUTHENTICATE_ERROR,
    AUTHORIZE_ERROR,
    INELIGIBLE_ERROR,
    DATA_JSON_PATH,
    USER_INFORMATION_MSG,
    PASSWORD_INPUT,
    USER_ROLE_INPUT,
    NAME_INPUT,
    AGE_INPUT,
    EMAIL_INPUT,
    USER_CREATED,
)
from exceptions import AuthenticationError, Ineligible, AuthorizationError
from enums import UserRole
from utils import (
    custom_print_msg,
    read_json,
    update_main_data,
    user_input,
    user_input_int_type,
    password_hash,
)


class User:
    """__main__ class to implement user signup & signin process"""

    def __init__(self, username: str) -> None:
        """
        user class Constructor
        @param username:str
        @param password:int
        """
        self.username = username
        self.is_user_exist()

    def sign_up(self):
        """
        method to implement signup process
        @return:
        """
        custom_print_msg(USER_INFORMATION_MSG)
        password = password_hash(input(PASSWORD_INPUT))
        print(
            "Available Roles\n"
            f"{ROLE_HOST.value}: {ROLE_HOST.name}\n"
            f"{ROLE_WATCHER.value}: {ROLE_WATCHER.name}"
        )
        role = UserRole(user_input_int_type(USER_ROLE_INPUT))
        if role not in [ROLE_HOST, ROLE_WATCHER]:
            raise AuthorizationError(AUTHORIZE_ERROR)
        name = user_input(NAME_INPUT)
        age = user_input_int_type(AGE_INPUT)
        if age < 18:
            raise Ineligible(INELIGIBLE_ERROR)
        email = user_input(EMAIL_INPUT)
        self.insert_signup_information(
            password=password, name=name, age=int(age), email=email, role=role.name
        )

    def is_user_exist(self) -> None:
        """
        method to check whether the user Exist
        @return: None
        """
        data = read_json(DATA_JSON_PATH)
        if not data.get(USER_JSON.name).get(self.username):
            custom_print_msg(USER_NOT_EXIST)
            self.sign_up()
            return
        custom_print_msg(USER_EXIST.format(username=self.username.capitalize()))
        self.sign_in()

    def insert_signup_information(self, date_type: str, **user_signup_data) -> None:
        """
        method to insert data into json
        @param date_type: str
        @param  user_signup_data:dict
        """
        update_main_data(
            self.username, date_type, user_signup_dataupdate_main_theater_data
        )
        custom_print_msg(USER_CREATED)

    def sign_in(self):
        """
        method to implement signup process
        @return: None
        """
        data = read_json(DATA_JSON_PATH).get(USER_JSON.name).get(self.username)
        password = input(PASSWORD_INPUT)
        if data.get("username") == self.username and data.get(
            "password"
        ) == password_hash(password):
            custom_print_msg(WELCOME.format(username=self.username.capitalize()))

        else:
            raise AuthenticationError(AUTHENTICATE_ERROR)


if __name__ == "__main__":
    pass
