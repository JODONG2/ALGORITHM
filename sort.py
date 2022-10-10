#TODO: mergesort
#TODO: 나누기.
#TODO: 합치면서 정렬하기.

#TODO: TestCase 

import random 

def mergesort(arr:list)->None:

    def divide(div_arr:list) -> list:
        len_div_arr = len(div_arr) 
        if len_div_arr <= 1 : return div_arr 
        mid = len_div_arr//2
        left_arr = div_arr[:mid]
        right_arr = div_arr[mid:]
        left_arr = divide(left_arr)
        right_arr = divide(right_arr)
        print(left_arr , right_arr)
        return merge(left_arr, right_arr) 

    def merge(left:list, right:list) -> list:
        len_l = len(left) 
        len_r = len(right) 
        pos_l = 0
        pos_r = 0 
        result = []
        while len_l > pos_l and len_r > pos_r : 
            if left[pos_l] < right[pos_r] : 
                result.append(left[pos_l])
                pos_l +=1 
            else:
                result.append(right[pos_r]) 
                pos_r +=1
        if len_l > pos_l : 
            result+= left[pos_l:]
        if len_r > pos_r :
            result+= right[pos_r:]
        return result 

    return divide(arr)
        
if __name__ == "__main__":
    arr= [6, 8, 9, 5, 3, 9, 8, 8, 3, 9]
    sorted_arr = mergesort(arr) 
    print(sorted_arr)
