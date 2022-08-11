import time

CACHE_LIMIT = 3
fifo_cache = []

def myfunc(n):
  if n not in fifo_cache:
    time.sleep(n)
    fifo_cache.append(n)
    if len(fifo_cache)>CACHE_LIMIT:
      fifo_cache.pop(0)

  return (f"Executed: {n}")

s = time.time()
print(myfunc(3))
print("Time Taken to execute: ", time.time() - s, "\n")

s = time.time()
print(myfunc(2))
print("Time Taken to execute: ", time.time() - s, "\n")

s = time.time()
print(myfunc(3))
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

s = time.time()
print(myfunc(2))
print("Time Taken to execute: ", time.time() - s, "\n")

'''
Result:

Executed: 3
Time Taken to execute:  3.003526449203491 

Executed: 2
Time Taken to execute:  2.002443552017212 

Executed: 3
Time Taken to execute:  0.00011157989501953125 

Executed: 1
Time Taken to execute:  1.0014557838439941 

Executed: 4
Time Taken to execute:  4.004620790481567 

Executed: 5
Time Taken to execute:  5.005484104156494 

Executed: 2
Time Taken to execute:  2.0024352073669434 
'''