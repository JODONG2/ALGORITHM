
import random 
import time 

def time_of_arrival(func): 
    #TODO: metric -> time 
    def wrapper(arr):
        now_time = time.time()
        func(arr)
        end_time= time.time()
        print("TIME : ", end_time - now_time)
    return wrapper

def random_list(size:int)->list:
    #TODO: test case
    result = []
    for _ in range(size):
        result.append(random.randint(0,100)) 
    return result 

@time_of_arrival
def insertion_sort(arr:list)-> None: 
    #TODO: insertion sort
    len_arr = len(arr)  
    for start in range(1,len_arr):
        for end in range(start,0,-1):
            if arr[end] < arr[end-1]: 
                arr[end],arr[end-1] = arr[end-1], arr[end]

@time_of_arrival
def insertion_sort_recursion(arr:list)-> None: 
    def sort (index:int)->None:
        if index == 0: return 
        if arr[index] <arr[index-1] : 
            arr[index],arr[index-1] = arr[index-1],arr[index]
        return sort(index-1)
    def repeat(len_arr:int)->None :
        for start in range(1,len_arr): 
            sort(start)

    return repeat(len(arr))

if __name__ =="__main__":
    arr_origin = random_list(100)
    arr = arr_origin[:]
    insertion_sort_recursion(arr)
    arr = arr_origin[:] 
    insertion_sort(arr)
