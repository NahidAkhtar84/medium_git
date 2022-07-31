import time
from cachetools import cached, TTLCache

@cached(TTLCache(maxsize=12, ttl=5))
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
Time Taken to execute:  2.003089189529419 

Executed: 2
Time Taken to execute:  0.0001232624053955078 

Executed: 6
Time Taken to execute:  6.006647348403931 

Executed: 6
Time Taken to execute:  0.00012040138244628906 

Executed: 2
Time Taken to execute:  2.0025570392608643 

Executed: 1
Time Taken to execute:  1.000640869140625 

Executed: 1
Time Taken to execute:  0.00013566017150878906 
'''