# 두 인덱스의 두 값 사이 값이 배열에 없으면 근접한 인덱스고, 가장 근접한 인덱스를 구하라 

def solution(A):
    # write your code in Python 3.6
    # B = sorted(A)
    if len(A) == 1 : return -2 
    B = [(i,num) for i,num in enumerate(A)]
    B.sort(key= lambda x: x[1])
    # B = [(index,value),...] 
    ans = float('inf')
    for i in range(len(B)-1): 
        if B[i][0] < B[i+1][0] : 
            ans = min(ans, B[i+1][1] - B[i][1])
            if ans == 0 : 
                return ans 
                
    if ans > 100000000 : ans = -2 

    return ans 




solution([0, 3, 3, 7, 5, 3, 11, 1])