from cachetools import cached, LRUCache
import time
  
@cached(cache = LRUCache(maxsize = 3))
def myfunc(n):
    # This delay resembles some task
    time.sleep(n)
    return (f"Executed: {n}")

s = time.time()
print(myfunc(3))
print("Time Taken to execute: ", time.time() - s, "\n")

s = time.time()
print(myfunc(3))
print("Time Taken to execute: ", time.time() - s, "\n")

s = time.time()
print(myfunc(2))
print("Time Taken to execute: ", time.time() - s, "\n")

s = time.time()
print(myfunc(1))
print("Time Taken to execute: ", time.time() - s, "\n")

s = time.time()
print(myfunc(4))
print("Time Taken to execute: ", time.time() - s, "\n")

s = time.time()
print(myfunc(1))
print("Time Taken to execute: ", time.time() - s, "\n")

s = time.time()
print(myfunc(3))
print("Time Taken to execute: ", time.time() - s, "\n")

'''
Result:

Executed: 3
Time Taken to execute:  3.003572702407837 

Executed: 3
Time Taken to execute:  0.00012040138244628906 

Executed: 2
Time Taken to execute:  2.002492666244507 

Executed: 1
Time Taken to execute:  1.0015416145324707 

Executed: 4
Time Taken to execute:  4.004684925079346 

Executed: 1
Time Taken to execute:  0.0001659393310546875 

Executed: 3
Time Taken to execute:  3.0035295486450195 

'''