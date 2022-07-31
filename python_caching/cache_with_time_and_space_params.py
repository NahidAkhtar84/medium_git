import time
from functools import lru_cache, wraps
from datetime import datetime, timedelta

def lru_cache_with_time_and_space_parameter(seconds: int, maxsize: int):
    def wrapper_cache(func):
        func = lru_cache(maxsize=maxsize)(func)
        func.lifetime = timedelta(seconds=seconds)
        func.expiration = datetime.utcnow() + func.lifetime

        @wraps(func)
        def wrapped_func(*args, **kwargs):
            if datetime.utcnow() >= func.expiration:
                func.cache_clear()
                func.expiration = datetime.utcnow() + func.lifetime
            return func(*args, **kwargs)

        return wrapped_func

    return wrapper_cache


@lru_cache_with_time_and_space_parameter(5, 32)
def myfunc(n):
    # This delay resembles some tas
    time.sleep(n)
    return (f"Executed: {n}")

s = time.time()
print(myfunc(2))
print("Time Taken to execute: ", time.time() - s, "\n")

s = time.time()
print(myfunc(2))
print("Time Taken to execute: ", time.time() - s, "\n")

s = time.time()
print(myfunc(6))
print("Time Taken to execute: ", time.time() - s, "\n")

s = time.time()
print(myfunc(6))
print("Time Taken to execute: ", time.time() - s, "\n")

s = time.time()
print(myfunc(2))
print("Time Taken to execute: ", time.time() - s, "\n")

s = time.time()
print(myfunc(1))
print("Time Taken to execute: ", time.time() - s, "\n")

s = time.time()
print(myfunc(1))
print("Time Taken to execute: ", time.time() - s, "\n")


'''
Result:

Executed: 2
Time Taken to execute:  2.0024309158325195 

Executed: 2
Time Taken to execute:  0.00011897087097167969 

Executed: 6
Time Taken to execute:  6.006444454193115 

Executed: 6
Time Taken to execute:  6.006414175033569 

Executed: 2
Time Taken to execute:  2.0024681091308594 

Executed: 1
Time Taken to execute:  1.0027210712432861 

Executed: 1
Time Taken to execute:  0.00016355514526367188 
'''
