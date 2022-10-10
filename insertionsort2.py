#TODO: Test case
#TODO: insertionsort 
#TODO: metric -> time 

import random
import time 
def random_list(size):
    result = []
    for _ in range(size):
        result.append(random.randint(0,100))
    return result 

def time_of_arrival(func):
    def wrapper(arr):
        for _ in range(2):
            start = time.time()
            func(arr) 
            end = time.time()
            print(f"{end-start:.20f}")

    return wrapper 

@time_of_arrival
def insertionsort(arr) : 
    len_arr = len(arr)
    for start in range(1,len_arr):
        for end in range(start,0,-1):
            if arr[end] < arr[end-1]:
                arr[end],arr[end-1] = arr[end-1], arr[end]

if __name__ == "__main__":
    arr = random_list(10)
    print(arr)
    insertionsort(arr) 
    print(arr)