import random 
import time

def random_list(size:int)-> list:
    result = []
    for _ in range(size): 
        result.append(random.randint(0,100))
    return result 


def quicksort(arr:list, flag:bool): 
    
    def sort(left:int, right:int) -> None:
        if left>=right: return 
        mid = divide(left,right)
        sort(left,mid-1)
        sort(mid,right)

    def divide(left:int,right:int)->int: 
        if flag:
            mid = avoid_worst(left,right,(left+right)//2)
        else:
            mid = random.randint(left,right)
        pivot = arr[mid]
        while left<=right: 
            while pivot>arr[left] : left+=1 
            while pivot<arr[right] : right-=1
            if right>=left : 
                arr[left],arr[right] = arr[right], arr[left] 
                left+=1 
                right-=1
        return left

    def avoid_worst(left:int,right:int,mid:int)-> int: 
        result = (arr[left]+ arr[right]+arr[mid] - max(arr[left],arr[right],arr[mid]) - min(arr[left],arr[right],arr[mid]))
        return left if result==arr[left] else (mid if result == arr[mid] else right)
    return sort(0,len(arr)-1)

arr2 = random_list(1000000)
arr=arr2[:]
now_time = time.time()
quicksort(arr,True)
print(f"{time.time() - now_time}")

arr=arr2[:]
now_time = time.time()
quicksort(arr,False)
print(f"{time.time() - now_time}")
