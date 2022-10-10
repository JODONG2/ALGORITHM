
import random 
import time 

def random_list(size:int) -> list : 
    result = []
    for _ in range(size):
        result.append(random.randint(0,100))
    return result 

def quicksort(arr:list, flag:bool)->None :

    def sort(left:int,right:int)->None : 
        stack = [left,right]
        while stack: 
            r = stack.pop() 
            l = stack.pop() 
            m = partition(l,r)
            if m < r : 
                stack.append(m)
                stack.append(r)
            if m-1>l : 
                stack.append(l) 
                stack.append(m-1)

    def partition(left:int, right:int) -> int: 
        if flag:
            mid = avoid_worst(left, right, (left+right)//2)
        else : 
            mid = left
        pivot = arr[mid]
        while left<=right:
            while arr[left]<pivot : left+=1 
            while pivot<arr[right] : right-=1
            if left<=right:
                arr[left], arr[right] = arr[right], arr[left]
                left+=1
                right-=1
        return left

    def avoid_worst(left:int,right:int,mid:int) -> int : 
        result = arr[left]+arr[right]+arr[mid] - max(arr[left],arr[right],arr[mid]) - min(arr[left],arr[right],arr[mid])
        return left if result == arr[left] else (right if result == arr[right] else mid)

    
    return sort(0,len(arr)-1)


def time_of_arrival(arr:list,flag:bool)->float:
    start_time = time.time()
    quicksort(arr,flag)
    end_time = time.time()
    return end_time - start_time

if __name__ == "__main__":
    
    arr = random_list(10000)
    arr.sort()
    arr_worst= arr[:]
    arr_avoid_worst = arr[:]
    print("Worst :",time_of_arrival(arr_worst,flag = False))
    print("Avoid worst :", time_of_arrival(arr_avoid_worst, flag = True))
