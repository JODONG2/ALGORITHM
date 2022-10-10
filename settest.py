import random

def random_list(size:int,mini:int, maxi:int)->list: 
    result = []
    for _ in range(size):
        result.append(random.randint(mini,maxi))
    return result 

if __name__ == "__main__":
    arr1 = random_list(10,0,10) 
    arr2 = random_list(10,0,10) 
    print(arr1,'\n',arr2)
    print(list(set(arr1) | set(arr2)))
    
