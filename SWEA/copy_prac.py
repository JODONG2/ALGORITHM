import random
import time 
from copy import deepcopy as dc 
def dcopy(n):
    arr = [random.randint(0,100) for _ in range(n)] 
    start_time = time.time()
    arr2 = dc(arr) 
    return time.time() - start_time

def ncopy(n):
    arr = [random.randint(0,100) for _ in range(n)] 
    start_time = time.time()
    arr2= [a for a in arr] 
    return time.time() - start_time

def dcopy_2dim(n):
    arr = [[random.randint(0,100) for _ in range(n)] for _ in range(n)] 
    start_time = time.time()
    arr2 = dc(arr) 
    return time.time() - start_time

def ncopy_2dim(n):
    arr = [[random.randint(0,100) for _ in range(n)] for _ in range(n)]
    start_time = time.time() 
    arr2 = [a[:] for a in arr]
    return time.time()-start_time


arr3 = [[[i for i in range(10)]for _ in range(3)] for _ in range(10)] 
arr4 = [[[a for a in arr ]for arr in arr2 ] for arr2 in arr3] 
arr4[0][0][0] = 999999
print(arr3[0][0][0])
print("1000000 elements copy.deepcopy 1dim - : ",dcopy(1000000))
print("1000000 elements list comprehension 1dim - : ",ncopy(1000000))

dcopy(10)
ncopy(10)

print("100 * 1000 elements copy.deepcopy 2dim - : ",dcopy_2dim(1000)) 
print(" 100 * 1000 elements list comprehension 2dim - : " , ncopy_2dim(1000))