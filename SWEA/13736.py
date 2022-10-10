#FAIL
from collections import deque 
def data_input(): 
    p,q,k = map(int,input().split())
    return min(p,q),max(p,q),k 

def seq (p,q,k): 
    cnt = 0 
    comp = p
    dp = deque()
    check = set() 
    dp.append(p)
    check.add(p)
    answer = 0
    while cnt < k:
        print(check)
        print(dp)
        p,q = min(p+p, q-p), max(p+p, q-p)
        cnt+=1
        if p == 0 :
            return 0 
        elif p == comp :
            dp.append(p)
            return dp[k%cnt]
            
        elif p in check : 
            answer = p
            break
        else:
            dp.append(p)
            check.add(p)
    if cnt==k: 
        answer = p
    return answer 

if __name__ == "__main__":
    test_cases = int(input())
    for test_case in range(test_cases):
        p,q,k = data_input() # p<q , k 
        answer = seq(p,q,k)
        print(f"#{test_case+1} {answer}")
"""
4
4 9 1
4 9 2
4 9 3
500 2000 2000000000
11
4 9 0 
8 5 1 
3 10 2 
6 7 3 
12 1 4 
11 2 5 
9 4 6 
5 8 7 
500 2000 0 
1000 1500 1 
2000 500 2 

#1 5
#2 3
#3 6
#4 500
"""