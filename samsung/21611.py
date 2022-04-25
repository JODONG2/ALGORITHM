import sys 
from collections import deque 
n,m = map(int,sys.stdin.readline().split())
world = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
command = [list(map(int,sys.stdin.readline().split())) for _ in range(m)] 
shark = (n//2, n//2)

dir = [0,(-1,0),(1,0),(0,-1),(0,1)]

def magic(d,s): 
    x,y = shark 
    for _ in range(s): 
        x,y = x+dir[d][0], y+dir[d][1]
        world[x][y] = 0 

def world_pop(q):
    x,y = shark 
    limit = 0
    out = True 
    while out : 
        limit +=1 
        if limit == n : 
            limit -= 1 
            out = False  
        for _ in range(limit): #좌 
            y-=1
            if world[x][y] != 0 :
                q.append(world[x][y])
                world[x][y] = 0 
        if not out : 
            break 
        for _ in range(limit): #하
            x+=1
            if world[x][y] != 0 :
                q.append(world[x][y])
                world[x][y] = 0 
        limit+=1 
        for _ in range(limit): #우
            y+=1 
            if world[x][y] != 0 : 
                q.append(world[x][y]) 
                world[x][y] = 0 
        for _ in range(limit): #상
            x-=1 
            if world[x][y] != 0 :
                q.append(world[x][y])
                world[x][y] = 0 
    return q 

"""
111 222222 333 111 222 33333 2 1 33 111 333 222 111 3333 1 2 3 1 
111 333 111 222 2 1 33 111 333 222 111 1 2 3 1 
111 333 111 1 33 111 333 222 2 3 1 
111 333 33 111 333 3 1 
111 111 1 
"""                    
# def explosion(q,q2): # -> q2 역순으로 만듬 
#     print(q)
#     cnt = 0
#     while q : 
#         num = q.popleft()
#         if not q2 : 
#             q2.appendleft(num) 
#         elif q2[0] != num : 
#             index = 0
#             compare = q2[0]
#             while index < len(q2) and q2[index] == compare : 
#                 index+=1 
#             if index >= 4 : 
#                 for _ in range(index): 
#                     q2.popleft()
#                     answer[compare]+=1
#             q2.appendleft(num)
#         elif q2[0] == num : 
#             q2.appendleft(num)
#         print(q2)
#     index = 0 
#     if not q2 : 
#         return q2
#     compare = q2[0] 
#     while index<len(q2) and q2[index] == compare : 
#         index+=1 
#     if index>=4 : 
#         for _ in range(index):
#             q2.popleft()
#             answer[compare]+=1 
    
#     return q2 
def explosion(q,q2): # -> q2 역순으로 만듬 
    cnt = 1
    change = False
    while q : 
        # print(q2)
        num = q.popleft()
        if not q2 : 
            q2.appendleft(num) 
        elif q2[0] != num : 
            if cnt >= 4 : 
                for _ in range(cnt): 
                    answer[q2.popleft()]+=1
                change = True 
            cnt = 1
            q2.appendleft(num)
        elif q2[0] == num : 
            q2.appendleft(num)
            cnt+=1 
        if change and not q :
            q = deque([item for item in reversed(q2)])
            q2 = deque()
            change = False
            cnt = 1 

    index = 0 
    if not q2 : 
        return q2
    compare = q2[0] 
    while index<len(q2) and q2[index] == compare : 
        index+=1 
    if index>=4 : 
        for _ in range(index):
            q2.popleft()
            answer[compare]+=1 
    return q2 
def world_push(q2):
    x,y = shark 
    limit = 0
    out = True 
    while out : 
        limit +=1 
        if limit == n : 
            limit -= 1 
            out = False  
        for _ in range(limit): #좌 
            y-=1
            if q2 :
                world[x][y] = q2.pop()
            else : 
                world[x][y] = 0 

        if not out :
            q2 = deque()
            break 

        for _ in range(limit): #하
            x+=1
            if q2 :
                world[x][y] = q2.pop()
            else : 
                world[x][y] = 0 
        limit+=1 
        for _ in range(limit): #우
            y+=1 
            if q2 : 
                world[x][y] = q2.pop() 
            else : 
                world[x][y] = 0 
        for _ in range(limit): #상
            x-=1 
            if q2 :
                world[x][y] = q2.pop()
            else : 
                world[x][y] = 0 

def change_q2(q2): 
    q3 = deque() 
    while q2 : 
        num = q2.pop() 
        cnt = 1 
        while q2 and num == q2[-1] : 
            cnt+=1 
            q2.pop()
        q3.appendleft(cnt)
        q3.appendleft(num)
    return q3

answer = [0,0,0,0] 
for d1,s1 in command: 
    magic(d1, s1)
    q = deque()
    q = world_pop(q)
    q2 = deque()
    q2 = explosion(q,q2) 
    q2 = change_q2(q2)
    world_push(q2)

ret = 0 
for i,an in enumerate(answer):
    ret += i*an

print(ret)

"""
111 222222 333 111 222 33333 2 1 33 111 333 222 111 3333 1 2 3 1 
111 333 111 222 2 1 33 111 333 222 111 1 2 3 1 
111 333 111 1 33 111 333 222 2 3 1 
111 333 33 111 333 3 1 
111 111 1 


9 1
0 0 0 0 0 0 0 0 0
3 2 1 3 1 3 3 3 0
1 3 3 3 1 3 3 1 0
0 2 2 2 1 2 2 1 0
0 1 2 1 0 2 2 1 0
0 3 3 1 1 2 2 2 0
0 3 3 3 1 1 1 2 0
0 1 1 1 3 3 3 2 0
0 0 0 0 0 0 0 0 0
1 3 
->97 상 3 칸 삭제 

7 4
1 1 1 2 2 2 3
1 2 2 1 2 2 3
1 3 3 2 3 1 2
1 2 2 0 3 2 2
3 1 2 2 3 2 2
3 1 2 1 1 2 1
3 1 2 2 2 1 1
1 3
2 2
3 1
4 3

3 1
1 1 1
1 0 1 
1 1 1
1 1

5 1 
3 2 2 2 3 
3 2 2 2 3 
3 1 0 1 1 
3 2 2 2 3 
2 2 2 3 3 
4 2 

3 1
0 2 2
2 0 1
2 2 2
4 1

5 1
0 0 0 0 0
0 0 1 1 0
0 1 0 1 0
0 1 1 1 0
0 0 0 0 0
1 2

15 40
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
2 3 1 2 3 2 3 1 1 2 2 2 1 2 0
2 1 3 2 2 2 3 3 3 1 1 1 2 1 0
2 1 2 1 2 1 1 3 3 3 1 1 3 2 0
1 3 2 3 3 2 2 2 3 3 1 1 3 2 0
1 1 2 3 1 1 1 3 1 1 3 3 1 2 0
2 2 3 1 3 2 2 1 2 1 3 3 1 1 0
2 2 1 3 1 2 1 0 2 3 1 2 2 1 0
1 3 1 3 1 3 1 1 3 3 1 2 1 1 0
2 1 3 1 1 3 3 1 1 3 2 2 3 2 0
2 1 1 1 3 3 3 1 1 1 2 1 3 2 0
3 1 2 1 3 3 3 2 2 2 1 1 3 2 0
1 3 3 3 1 1 1 3 3 1 1 1 2 1 0
1 3 3 1 1 2 2 1 1 3 3 2 1 1 0
2 3 3 1 1 0 0 0 0 0 0 0 0 0 0
1 6
2 2
2 2
4 3
4 2
1 1
3 1
4 6
2 2
1 6
2 5
1 4
2 2
2 5
3 2
2 1
3 3
3 4
4 4
3 7
3 6
1 3
2 4
2 3
1 3
2 3
3 7
1 7
4 3
3 3
2 1
3 7
2 2
4 2
1 5
1 1
4 2
2 7
3 5
2 6

86
"""