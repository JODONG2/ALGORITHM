import sys 
from collections import deque 

dx = [0,0,-1,1]
dy = [1,-1,0,0]
def cal_distance(q): 
    while q :
        x,y,dist = q.popleft()
        for px, py in zip(dx,dy):
            nx,ny = x+px, y+py
            if 0<=nx<n and 0<=ny<m and (maps[nx][ny] == '.' or maps[nx][ny] == 'V') and visit[nx][ny] == 0: 
                visit[nx][ny] = dist+1 
                q.append((nx,ny,dist+1))
import heapq
def navigation():
    # start[0].append(visit[start[0][0]][start[0][1]])
    x,y = start[0],start[1] 
    mini = visit[x][y] 
    q = deque([(x,y)]) 
    q = [] 
    heapq.heappush(q,(-mini ,x,y))
    check = [[True for _ in range(m)] for _ in range(n)]
    check[x][y] = False
    answer = float('inf')
    while q : 
        mini,x,y, = heapq.heappop(q) 
        answer = min(-mini,answer)
        for px,py in zip(dx,dy):
            nx,ny = x+px, y+py 
            if 0<=nx<n and 0<=ny<m and check[nx][ny] :
                if maps[nx][ny] == 'J':
                    return answer
                check[nx][ny] = False 
                heapq.heappush(q,(-visit[nx][ny],nx,ny))
    return answer
n,m = map(int,sys.stdin.readline().split()) 
maps = [list(sys.stdin.readline()[:-1]) for _ in range(n)]
visit = [[0 for _ in range(m)] for _ in range(n)] 
q= deque()
start = []
for i in range(n):
    for j in range(m):
        if maps[i][j] == '+':
            q.append((i,j,0))
        elif maps[i][j] == 'J':
            visit[i][j] = float('inf') 
        elif maps[i][j] == 'V':
            start = [i,j]
cal_distance(q)
print(navigation())
# for v in visit:
#     print(v)

"""
4 5
.....
.+++.
.+.+.
V+.J+

4 4
+...
....
....
V..J

7 6
......
......
..++..
V....J
..++..
......
......

7 6
......
......
..++..
V....J
..++..
......
.....+
"""