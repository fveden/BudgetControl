from log_settings import setup_logger
from time import perf_counter
from functools import wraps

logger_time = setup_logger("logs/TimeLog.log", "time_logger")


def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        _start = perf_counter()
        result = func(*args, **kwargs)
        _end = perf_counter()
        logger_time.debug(f'{func.__name__}: {_end - _start:.6f} sec.')
        return result
    return wrapper
