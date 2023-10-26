import time
from functools import wraps
from typing import Callable

from hyperon_das_atomdb.exceptions import (
    ConnectionServerException,
    RetryException,
)


def set_is_toplevel(function: Callable) -> Callable:
    @wraps(function)
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        result['is_toplevel'] = True
        return result

    return wrapper


def retry(attempts: int, timeout_seconds: int):
    def decorator(function: Callable) -> Callable:
        @wraps(function)
        def wrapper(*args, **kwargs):
            waiting_time_seconds = 0.1
            retry_count = 0
            timer_count = 0

            while retry_count < attempts and timer_count < timeout_seconds:
                try:
                    response = function(*args, **kwargs)
                    if response is not None:
                        return
                except Exception as e:
                    raise ConnectionServerException(
                        message='An error occurs while connecting to the server'
                    )
                else:
                    time.sleep(waiting_time_seconds)
                    retry_count += 1
                    timer_count += waiting_time_seconds

            raise RetryException(
                message='The number of attempts has been exceeded or a timeout has occurred',
                details={'attempts': retry_count, 'time': timer_count},
            )

        return wrapper

    return decorator
