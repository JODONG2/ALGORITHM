import sys
from collections import deque 
ans = set()
maps = [sys.stdin.readline()[:-1] for _ in range(5)] 
start = [] 
dx = [0,1,0,-1] 
visit = [[True for _ in range(5)] for _ in range(5)] 
dy = [1,0,-1,0]

all_visit = set(tuple([5*x+y for y in range(5) for x in range(5)]))
def bfs(x,y):
    all_visit = [set() for _ in range(7)]
    all_visit[0].add(5*x+y)
    # all_visit = set([5*x+y])
    global ans 
    q = deque()
    visit = [5*x+y]
    footprint = [[] for _ in range(7)] 
    footprint[0].append(set([5*x+y]))
    q.append((x,y,0, visit))
    while q : 
        x,y,r,visit = q.popleft()
        if r == 6 : 
            break 
        for d in range(4): 
            nx = x +dx[d] 
            ny = y +dy[d] 
            if 0<= nx < 5 and 0<=ny < 5 and not (5*nx + ny) in visit: 
                v = visit[:]
                v.append((nx * 5 + ny))
                v.sort()
                if tuple(v) in all_visit[r+1] : 
                    continue 
                all_visit[r+1].add(tuple(v))
                footprint[r+1].append((set(v)))
                q.append((nx,ny,r+1, v))
                
    for i in range(7):
        for j in range(7): 
            for foot1 in footprint[i] : 
                for foot2 in footprint[j] : 
                    foot = foot1 | foot2
                    if len(foot) == 7 : 
                        cnt = 0 
                        for num in foot : 
                            x = num//5 
                            y = num % 5 
                            if maps[x][y] == 'S' : 
                                cnt +=1 
                        if cnt>=4 : 
                            ans.add(tuple(sorted(list(foot))))
                            # print(foot1 | foot2)
for i in range(5):
    for j in range(5): 
        bfs(i,j)
print(len(ans))
# print(all_visit)
# for a in ans : 
#     print(a)


"""
SSSSS
SSSSS
SSSSS
SSSSS
SSSSS

3546
나와야됨 
"""