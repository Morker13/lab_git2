def merge(dic1,dic2):
    dic3=dic1.copy()
    dic3.update(dic2)
    return dic3
dic1={1:"hello", 2:"world"}
dic2={3:"Python", 4:"Programming"}
merge(dic1,dic2) # {1: 'hello', 2: 'world', 3: 'Python', 4: 'Programming'}

import time
start_time= time.time()
def fun():
    a=2
    b=3
    c=a+b
end_time= time.time()
fun()
timetaken = end_time - start_time
print("Your program takes: ", timetaken)