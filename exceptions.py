"""python file to implement custom exceptions"""


class AuthenticationError(BaseException):
    """custom exception for Authentication"""

    def __init__(self, msg):
        super(AuthenticationError, self).__init__(msg)


class AuthorizationError(BaseException):
    """custom exception for user Authorization"""

    def __init__(self, msg):
        super(AuthorizationError, self).__init__(msg)


class UnavailableTickets(BaseException):
    """custom exception for tickets unavailable"""

    def __init__(self, msg):
        super(UnavailableTickets, self).__init__(msg)


class DataNotFound(BaseException):
    """custom exception for tickets unavailable"""

    def __init__(self, msg):
        super(DataNotFound, self).__init__(msg)


class UnderAge(BaseException):
    """custom exception for tickets unavailable"""

    def __init__(self, msg):
        super(UnderAge, self).__init__(msg)


class DateValidationError(BaseException):
    """custom exception for tickets unavailable"""

    def __init__(self, msg):
        super(DateValidationError, self).__init__(msg)


if __name__ == "__main__":
    pass
