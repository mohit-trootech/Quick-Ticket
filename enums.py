"""File to Store Enum classes"""

from enum import Enum


class UserRole(Enum):
    """class for User Role options"""

    ROLE_HOST = 1
    ROLE_WATCHER = 2


class DataOption(Enum):
    """class for Data Save Options"""

    USER_JSON = 1
    MOVIE_JSON = 2


class ServicesEnum(Enum):
    """class for Services Selection Add or Book Movies"""

    BOOK_MOVIE = 1
    ADD_MOVIE = 2


class MoviesData(Enum):
    """class for Services Selection Add or Book Movies"""

    UPCOMING_MOVIES = 1
    PAST_MOVIES = 2
