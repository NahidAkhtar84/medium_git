import time

CACHE_LIMIT = 3
fifo_cache = []

def myfunc(n):
  if n not in fifo_cache:
    s = time.time()
    time.sleep(n)
    fifo_cache.append(n)
    if len(fifo_cache)>CACHE_LIMIT:
      fifo_cache.pop(0)
    print("\nTime taken to execute: ", time.time() - s)
    return (f"Executed: {n}")
  else:

    return (f"Executed: {n}")

print(myfunc(3))
print(myfunc(2))
print(myfunc(3))
print(myfunc(1))
print(myfunc(4))
print(myfunc(5))
print(myfunc(2))

'''
Result:


Time taken to execute:  3.0037641525268555
Executed: 3

Time taken to execute:  2.0012123584747314
Executed: 2
Executed: 3

Time taken to execute:  1.0002245903015137
Executed: 1

Time taken to execute:  4.0041139125823975
Executed: 4

Time taken to execute:  5.005074501037598
Executed: 5

Time taken to execute:  2.002068519592285
Executed: 2
'''