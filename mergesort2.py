#TODO: 머지소트
#TODO: 나누기
#TODO: 합치기 


import random 
import time 
def random_list(size:int)->list:
    result = []
    for _ in range(size):
        result.append(random.randint(0,100)) 
    return result

def test_time(func):
    def time_arrival(arr:list)->float:
        #save_arr = arr[:]
        now_time = time.time()
        result_arr = func(arr)
        end_time = time.time()
        print(f"{end_time - now_time:.5f}")
        return result_arr
    return time_arrival

@test_time
def mergesort(arr:list) -> list:

    def divide (div_arr) -> list:
        len_div_arr = len(div_arr) 
        if len_div_arr <= 1 : 
            return div_arr
        mid = len_div_arr//2
        left_arr = div_arr[:mid]
        right_arr = div_arr[mid:]
        left_arr = divide(left_arr)
        right_arr = divide(right_arr)
        return merge(left_arr, right_arr)
    
    def merge(left:list, right:list)-> list: 
        len_left = len(left)
        len_right= len(right) 
        pos_left = 0
        pos_right = 0
        result = []
        while len_left > pos_left and len_right > pos_right :
            if left[pos_left] > right[pos_right] : 
                result.append(right[pos_right])
                pos_right += 1
            else : 
                result.append(left[pos_left])
                pos_left += 1
        if len_left > pos_left : 
            result += left[pos_left:]
        elif len_right > pos_right: 
            result += right[pos_right:]
        return result 
    return divide(arr)

if __name__ == "__main__":
    arr = random_list(20)
    #arr = [34, 20, 13, 60, 74, 26, 81, 94, 11, 85]
    print(arr)
    sorted_arr = mergesort(arr)
    print(sorted_arr)