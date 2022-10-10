#TODO: mergesort
#TODO: 잘개 쪼개기
#TODO: 좌우 비교하면서 합치기
#TODO: testcase
#TODO: metric -> time 
import random

def random_list(size:int)->list:
    #TODO: test case
    result = []
    for _ in range(size):
        result.append(random.randint(0,100)) 
    return result 
    
def mergesort(arr:list)->list:

    def divide(div_arr:list)->list: 
        len_arr = len(div_arr)
        if len_arr <= 1 : return div_arr
        mid = len_arr//2
        left_arr = div_arr[:mid]
        right_arr = div_arr[mid:]
        left_arr = divide(left_arr)
        right_arr = divide(right_arr)
        return merge(left_arr, right_arr)

    def merge(left:list,right:list)->list: 
        result = []
        r_position = 0 
        l_position = 0
        len_left = len(left)
        len_right = len(right)
        while len_left>l_position or len_right>r_position :
            if len(left)>l_position and len(right)>r_position : 
                if left[l_position] > right[r_position] : 
                    result.append(right[r_position])
                    r_position += 1
                else :
                    result.append(left[l_position])
                    l_position += 1
            elif len_left>l_position :
                result.append(left[l_position])
                l_position+=1
            elif len_right>r_position: 
                result.append(right[r_position])
                r_position +=1
        return result

    return divide(arr)

if __name__ == "__main__":
    arr = random_list(1000) 
    temp = mergesort(arr)
    
        

