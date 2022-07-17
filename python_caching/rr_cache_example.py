from cachetools import cached, RRCache
import time

@cached(cache = RRCache(maxsize = 3))
def myfunc(n):
	s = time.time()
	time.sleep(n)
	print("\nTime Taken to execute: ", time.time() - s)
	return (f"Executed: {n}")

print(myfunc(3))
print(myfunc(3))
print(myfunc(2))
print(myfunc(6))
print(myfunc(5))
print(myfunc(1))
print(myfunc(3))
print(myfunc(3))
print(myfunc(6))
print(myfunc(2))
print(myfunc(1))
print(myfunc(5))

'''
Result:

Time Taken to execute:  3.0030834674835205
Executed: 3
Executed: 3

Time Taken to execute:  2.0020968914031982
Executed: 2

Time Taken to execute:  6.006072521209717
Executed: 6

Time Taken to execute:  5.005061388015747
Executed: 5

Time Taken to execute:  1.0010602474212646
Executed: 1

Time Taken to execute:  3.0030720233917236
Executed: 3
Executed: 3
Executed: 6

Time Taken to execute:  2.00205659866333
Executed: 2
Executed: 1

Time Taken to execute:  5.005077362060547
Executed: 5

'''