from cachetools import cached, LRUCache
import time
  
@cached(cache = LRUCache(maxsize = 3))
def myfunc(n):
    # This delay resembles some task
    s = time.time()
    time.sleep(n)
    print("\nTime Taken: ", time.time() - s)
    return (f"Executed: {n}")

start_time1 = time.time()    
print(myfunc(3))
print("--- %s seconds ---for input 3-> First Time" % (time.time() - start_time1))

start_time2 = time.time() 
print(myfunc(3))
print("--- %s seconds ---for input 3-> Second Time(When cached)" % (time.time() - start_time2))

start_time3 = time.time() 
print(myfunc(2))
print("--- %s seconds ---for input 2-> First Time" % (time.time() - start_time3))

print(myfunc(1))
print(myfunc(4))
print(myfunc(1))

start_time4 = time.time()
print(myfunc(3))
print("--- %s seconds ---for input 3-> Third Time(As recently used data is 1)" % (time.time() - start_time4))


'''
Result:

Time Taken:  3.0031449794769287
Executed: 3
--- 3.003704309463501 seconds ---for input 3-> First Time
Executed: 3
--- 8.440017700195312e-05 seconds ---for input 3-> Second Time(When cached)

Time Taken:  2.0020751953125
Executed: 2
--- 2.002535820007324 seconds ---for input 2-> First Time

Time Taken:  1.0011036396026611
Executed: 1

Time Taken:  4.003228664398193
Executed: 4
Executed: 1

Time Taken:  3.003124237060547
Executed: 3
--- 3.003680944442749 seconds ---for input 3-> Third Time(As recently used data is 1)
'''