"""
8
11100110
11010010
10011010
11101100
01000111
00110001
11011000
11000111
9
111110111
111110111
000000001
000000001
000000001
111111011
100000000
100000000
111111111
"""
import sys 
from collections import deque 
direction = [(0,1),(0,-1),(-1,0),(1,0)]
def f1():
    q = deque([(0,0,0)]) 
    while q:
        x,y,cnt = q.popleft()
        for px,py in direction:
            nx,ny = x+px,y+py 
            if 0<=nx<n and 0<=ny<n and check[nx][ny] > cnt : 
                check[nx][ny] = cnt 
                if maps[nx][ny] == 1 : 
                    q.append((nx,ny,cnt))
                else :
                    q.append((nx,ny,cnt+1))
n = int(sys.stdin.readline())
maps = [list(map(int,list(sys.stdin.readline()[:-1]))) for _ in range(n)]
check = [[float('inf') for _ in range(n)] for _ in range(n)] 
check[0][0] = 0 
# for m in maps:
#     print(m)
f1()
print(check[-1][-1])

