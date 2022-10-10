#TODO: quicksort -> 2
#TODO: 왼쪽 오른쪽이 만나면 피벗 기준으로 좌우 나누기 -> 3
#TODO: pivot 기준으로 왼쪽은 작은거, 오른쪽은 큰 거. ->2
#TODO: pivot 최악 피하기. 
#TODO: metric -> time

import random
import time

def test_time(func):
    def time_arrival(arr:list,flag:bool)->float:
        #save_arr = arr[:]
        now_time = time.time()
        func(arr,flag)
        end_time = time.time()
        print(end_time - now_time)
    return time_arrival

def random_list(size:int) -> list: 
    result = []
    for _ in range(size):
        result.append(random.randint(0,100))
    return result

@test_time
def quicksort(arr:list,flag:bool)-> None: 
    def sort(left:int, right:int)->None:
        if left>=right: return 
        mid = divide(left,right)
        sort(left,mid-1)
        sort(mid,right)
    
    def divide(left:int, right:int)-> int:
        if flag:
            pivot = avoid_worst(arr[left],arr[right], arr[(left+right)//2])
        else:
            pivot = arr[left]

        while left<=right:
            while arr[left]<pivot : left+=1 
            while pivot<arr[right] : right-=1
            if left<=right:
                arr[left],arr[right] = arr[right],arr[left]
                left+=1 
                right-=1
        return left
  
    def avoid_worst(left:int, right:int, mid:int) -> int:
        # if left is right: 
        #     return left 
        # elif mid is right:
        #     return mid
        #return left+right+mid - max(left,right,mid) - min(left,right,mid)
        return random.randint(left,right)
        # if left>=mid and mid>=right:
        #     return mid 
        # elif left>=right and right>=mid: 
        #     return right 
        # else: 
        #     return left 

    return sort(0,len(arr)-1)
  
if __name__=="__main__":
    test_case= random_list(10000)
    quicksort(test_case,False)
    quicksort(test_case,True)
    quicksort(test_case,False)
  
  
  	