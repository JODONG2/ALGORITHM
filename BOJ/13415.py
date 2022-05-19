import sys 
from collections import deque 
len_num = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split())) 
rnd = int(sys.stdin.readline())
q = deque() 
for _ in range(rnd): 
    inc,dec = map(int,sys.stdin.readline().split())
    while q and max(q[-1]) <= max(inc,dec):
        q.pop()
    q.append((inc,dec)) 

if q :
    inc,dec = q.popleft() 
    if dec>= inc : 
        temp = sorted(arr[:dec], reverse = True) 
        for i in range(dec):
            arr[i] = temp[i] 
    else : 
        temp = sorted(arr[:inc])
        for i in range(inc): 
            arr[i] = temp[i] 
        for i in range(dec-1,(dec-1)//2,-1): 
            arr[dec-1 - i ],arr[i] = arr[i],arr[dec-1-i]
before_dec = -1
while q : 
    inc,dec = q.popleft() 
    # 10 4 
    # 3 2 
    if dec>=inc and before_dec >= dec : 
        continue 
    elif before_dec>=dec and before_dec>=inc and inc > dec: 
        for i in range(inc-1,(inc-1)//2, -1): # 1 2 3 4 5 
            arr[inc-1 - i ], arr[i] = arr[i], arr[inc-1-i]
        for i in range(dec-1 , (dec-1)//2, -1):
            arr[dec-1-i],arr[i] = arr[i],arr[dec-1-i] 
        before_dec = dec
    elif before_dec< inc and inc > dec : 
        temp = sorted(arr[:inc]) 
        for i in range(inc):
            arr[i] = temp[i] 
        for i in range(dec-1,(dec-1)//2, -1):
            arr[dec-1-i],arr[i] = arr[i],arr[dec-1-i] 
    elif before_dec < dec and inc <= dec :
        temp = sorted(arr[:dec],reverse=True)
        for i in range(dec):
            arr[i] = temp[i] 
print(*arr)

"""
10
1 2 3 4 5 6 7 8 9 10
2
10 4
3 5


4
4 1 2 3
1
3 2

6
1 2 3 4 5 6 
2
6 6
5 3

10
1 2 3 4 5 6 7 8 9 10
10
10 10
9 8 
8 7
7 6
10 10
9 8
7 6 
5 4
3 2
2 1 

10
1 2 3 4 5 6 7 8 9 10
10
10 10
9 9
8 8 
7 7 
6 6 
5 5
4 4
3 3
2 2
1 1
"""