"""
6 4
0100
1110
1000
0000
0111
0000

5 5
01000
11010
01010
01010
00010

5 5
01100
01000
01110
01000
00010

4 4
0101
0101
0001
1110
"""
import sys 
from collections import deque 
def solution(start):
    if n == 1 and m == 1 : 
        return 0
    q = deque(start)
    visit = [[True for _ in range(m)] for _ in range(n)]
    visit2 = [[True for _ in range(m)] for _ in range(n)]
    while q : 
        x,y,c,d = q.popleft() # c = 벽 부순 여부
        for px,py in zip(dx,dy):
            nx,ny = x+px,y+py 
            if 0<=nx<n and 0<=ny<m and visit[nx][ny] :
                if nx == n-1 and ny == m-1 : 
                    return d+1
                if not c and (not visit2[nx][ny] or maps[nx][ny] == '1'): 
                    continue 
                elif not c : 
                    visit2[nx][ny] = False 
                    q.append((nx,ny,c,d+1))
                elif c : 
                    if maps[nx][ny] == '1': 
                        visit2[nx][ny] = False 
                        visit[nx][ny] = False 
                        q.append((nx,ny,False,d+1)) 
                    else: 
                        visit[nx][ny] = False
                        visit2[nx][ny] = False 
                        q.append((nx,ny,c,d+1))
    return -1 

n,m = map(int, sys.stdin.readline().split()) 
maps = [sys.stdin.readline()[:-1] for _ in range(n)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
print(solution([(0,0,True,1)]))