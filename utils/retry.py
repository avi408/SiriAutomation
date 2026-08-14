import time
from functools import wraps


def retry(retries=3, delay=2):

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            last_exception = None

            for attempt in range(1, retries + 1):

                try:
                    return func(*args, **kwargs)

                except Exception as e:

                    last_exception = e

                    print(f"Retry {attempt}/{retries}: {e}")

                    time.sleep(delay)

            raise last_exception

        return wrapper

    return decorator