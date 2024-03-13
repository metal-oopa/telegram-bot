import os
from constants.constants import ERROR_MESSAGES


def get_environment_variable(key):
    value = os.environ.get(key)
    if not value:
        raise ValueError(f"{key} {ERROR_MESSAGES['not_found']}")
    return value
