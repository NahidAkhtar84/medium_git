import streamlit as st
import time

@st.cache(suppress_st_warning=True)  # 👈 Changed this
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
Time Taken to execute:  2.1840202808380127 

Executed: 2
Time Taken to execute:  0.0053174495697021484 

Executed: 6
Time Taken to execute:  6.005890846252441 

Executed: 6
Time Taken to execute:  0.0037260055541992188 

Executed: 2
Time Taken to execute:  0.0067899227142333984 

Executed: 1
Time Taken to execute:  1.0083811283111572 

Executed: 1
Time Taken to execute:  0.0014271736145019531 
'''