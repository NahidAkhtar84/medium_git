from cachetools import cached, RRCache
import time

@cached(cache = RRCache(maxsize = 3))
def myfunc(n):
	s = time.time()
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
print(myfunc(6))
print("Time Taken to execute: ", time.time() - s, "\n")

s = time.time()
print(myfunc(5))
print("Time Taken to execute: ", time.time() - s, "\n")

s = time.time()
print(myfunc(1))
print("Time Taken to execute: ", time.time() - s, "\n")

s = time.time()
print(myfunc(2))
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
print(myfunc(5))
print("Time Taken to execute: ", time.time() - s, "\n")

'''
Result:

Executed: 3
Time Taken to execute:  3.003613233566284 

Executed: 3
Time Taken to execute:  0.00010895729064941406 

Executed: 2
Time Taken to execute:  2.0036702156066895 

Executed: 6
Time Taken to execute:  6.007461309432983 

Executed: 5
Time Taken to execute:  5.005535364151001 

Executed: 1
Time Taken to execute:  1.0015869140625 

Executed: 2
Time Taken to execute:  2.0025484561920166 

Executed: 6
Time Taken to execute:  6.006529808044434 

Executed: 2
Time Taken to execute:  2.002703905105591 

Executed: 1
Time Taken to execute:  0.00014352798461914062 

Executed: 5
Time Taken to execute:  5.005505800247192 
'''