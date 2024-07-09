"""User Signup and Signin class Logic"""

from constant import (
    ROLE,
    ROLE_HOST,
    ROLE_WATCHER,
    USER_JSON,
    USER_EXIST,
    USER_NOT_EXIST,
    WELCOME,
    AUTHENTICATE_ERROR,
    DATA_JSON_PATH,
)
from exceptions import AuthenticationError, UnderAge
from utils import (
    custom_print_msg,
    read_json,
    update_main_theater_data,
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
        custom_print_msg("Please Enter User Information")
        password = password_hash(input("Enter Your Password: "))
        role = user_input_int_type(f"Please Select User Role {ROLE}: ")
        if int(role) == 1:
            role = ROLE_HOST
        else:
            role = ROLE_WATCHER
        name = user_input("Enter Name: ")
        age = user_input_int_type("Enter Age: ")
        if age < 18:
            raise UnderAge("You are Under Age to Book Tickets Required 18 plus")
        email = user_input("Enter Email: ")
        status = self.insert_signup_information(password, name, int(age), email, role)
        if status:
            custom_print_msg("User Created Successfully")

    def is_user_exist(self) -> None:
        """
        method to check whether the user Exist
        @return: None
        """
        data = read_json(DATA_JSON_PATH)
        if not data.get(USER_JSON).get(self.username):
            custom_print_msg(USER_NOT_EXIST)
            self.sign_up()
            return
        else:
            custom_print_msg(USER_EXIST.format(username=self.username.capitalize()))
            self.sign_in()

    def insert_signup_information(
        self, password: str, name: str, age: int, email: str, role: str
    ) -> bool:
        """
        method to insert data into json
        @param  password:str
        @param name:str
        @param age:int
        @param email:str
        @param role:str
        @return:bool
        """

        data_for_append = {
            "username": self.username,
            "password": password,
            "name": name,
            "age": age,
            "email": email,
            "role": role,
        }
        update_main_theater_data(self.username, data_for_append, USER_JSON)
        return True

    def sign_in(self):
        """
        method to implement signup process
        @return: None
        """
        data = read_json(DATA_JSON_PATH).get(USER_JSON).get(self.username)
        password = input("Enter Your Password: ")
        if data.get("username") == self.username and data.get(
            "password"
        ) == password_hash(password):
            custom_print_msg(WELCOME.format(username=self.username.capitalize()))

        else:
            raise AuthenticationError(AUTHENTICATE_ERROR)


if __name__ == "__main__":
    pass
