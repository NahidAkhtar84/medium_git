from cachetools import cached, LFUCache
import time

@cached(cache = LFUCache(maxsize = 3))
def myfunc(n):
    time.sleep(n)
    return (f"Executed: {n}")


s = time.time()
print(myfunc(3))
print("Time Taken to execute: ", time.time() - s, "\n")

s = time.time()
print(myfunc(3))
print("Time Taken to execute: ", time.time() - s, "\n")

s = time.time()
print(myfunc(1))
print("Time Taken to execute: ", time.time() - s, "\n")

s = time.time()
print(myfunc(1))
print("Time Taken to execute: ", time.time() - s, "\n")

s = time.time()
print(myfunc(2))
print("Time Taken to execute: ", time.time() - s, "\n")

s = time.time()
print(myfunc(4))
print("Time Taken to execute: ", time.time() - s, "\n")

s = time.time()
print(myfunc(5))
print("Time Taken to execute: ", time.time() - s, "\n")

s = time.time()
print(myfunc(5))
print("Time Taken to execute: ", time.time() - s, "\n")

s = time.time()
print(myfunc(6))
print("Time Taken to execute: ", time.time() - s, "\n")

s = time.time()
print(myfunc(1))
print("Time Taken to execute: ", time.time() - s, "\n")

s = time.time()
print(myfunc(4))
print("Time Taken to execute: ", time.time() - s, "\n")

s = time.time()
print(myfunc(5))
print("Time Taken to execute: ", time.time() - s, "\n")

'''
Result:

Executed: 3
Time Taken to execute:  3.003491163253784 

Executed: 3
Time Taken to execute:  0.00011420249938964844 

Executed: 1
Time Taken to execute:  1.0017178058624268 

Executed: 1
Time Taken to execute:  0.0001633167266845703 

Executed: 2
Time Taken to execute:  2.0025696754455566 

Executed: 4
Time Taken to execute:  4.004656791687012 

Executed: 5
Time Taken to execute:  5.005551099777222 

Executed: 5
Time Taken to execute:  0.00011658668518066406 

Executed: 6
Time Taken to execute:  6.006593942642212 

Executed: 1
Time Taken to execute:  0.0003552436828613281 

Executed: 4
Time Taken to execute:  4.004685401916504 

Executed: 5
Time Taken to execute:  0.0001475811004638672 

'''