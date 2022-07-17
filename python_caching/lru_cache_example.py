from cachetools import cached, LRUCache
import time
  
@cached(cache = LRUCache(maxsize = 3))
def myfunc(n):
    # This delay resembles some task
    s = time.time()
    time.sleep(n)
    print("\nTime Taken to execute: ", time.time() - s)
    return (f"Executed: {n}")
   
print(myfunc(3))
print(myfunc(3))
print(myfunc(2))
print(myfunc(1))
print(myfunc(4))
print(myfunc(1))
print(myfunc(3))

'''
Result:

Time Taken to execute:  3.0030837059020996
Executed: 3
Executed: 3

Time Taken to execute:  2.002063751220703
Executed: 2

Time Taken to execute:  1.001054286956787
Executed: 1

Time Taken to execute:  4.004071950912476
Executed: 4
Executed: 1

Time Taken to execute:  3.0007569789886475
Executed: 3
'''