from collections import deque 
"""
5 17 
5 10 20 
4 9 19 / 6 11 
"""
x,y = map(int,input().split()) 
answer = y-x 
check = [float('inf') for _ in range(y*2)]
def func(x,y):
    q = deque([(x,0)])
    limit = y-x 
    while q :
        now, time = q.popleft()
        if time >= limit : 
            continue 
        if now*2 == y:
            return time 
        else :
            if now < y and check[now*2] > time:
                check[now*2]= time
                q.append((now*2, time))
        if now-1 == y :
            return time+1
        else:
            if now-1 > 0 and check[now-1] > time+1:
                check[now-1] = time+1 
                q.append((now-1,time+1))
        if now+1 == y :
            return time+1 
        else:
            if now < y and check[now+1] > time+1:
                check[now+1] = time+1 
                q.append((now+1,time+1))
        
        
if x >= y : 
    answer = x-y 
    print(answer)
else: 
    # print(func(x,y))
    answer = func(x,y)
    print(min(answer,check[y]))

    

1 2 4 8 16 32 64 128  
3 6 12 24 48 96 
5 10 20 40 80
6 12 24 48 96 
7 14 28 56
9 18 36 72  
1 2 4 8 16 32 31 30 
90 -> 15 * 6  
30 * 3 