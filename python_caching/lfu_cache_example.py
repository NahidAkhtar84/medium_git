from cachetools import cached, LFUCache
import time

@cached(cache = LFUCache(maxsize = 3))
def myfunc(n):
    s = time.time()
    time.sleep(n)
    print("\nTime taken to execute: ", time.time() - s)
    return (f"Executed: {n}")
  
print(myfunc(3))
print(myfunc(3))
print(myfunc(1))
print(myfunc(1))
print(myfunc(2))
print(myfunc(4))
print(myfunc(5))
print(myfunc(5))
print(myfunc(6))
print(myfunc(1))
print(myfunc(4))
print(myfunc(5))

'''
Result:


Time taken to execute:  3.003084182739258
Executed: 3
Executed: 3

Time taken to execute:  1.001054048538208
Executed: 1
Executed: 1

Time taken to execute:  2.0020992755889893
Executed: 2

Time taken to execute:  4.003973722457886
Executed: 4

Time taken to execute:  5.005094528198242
Executed: 5
Executed: 5

Time taken to execute:  6.006098508834839
Executed: 6
Executed: 1

Time taken to execute:  4.004076719284058
Executed: 4
Executed: 5
'''