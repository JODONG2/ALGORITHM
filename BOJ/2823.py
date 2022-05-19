"""
4 3
XXX
X.X
X.X
XXX
"""
import sys 
 
def solution() : 
    n,m = map(int , sys.stdin.readline().split())
    maps = [list(sys.stdin.readline()[:-1]) for _ in range(n)]
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    for i in range(n):
        for j in range(m):
            if maps[i][j] == ".":
                cnt = 0 
                for px,py in zip(dx,dy):
                    nx,ny = i+px,j+py
                    if 0<=nx<n and 0<=ny<m and maps[nx][ny] == ".":
                        cnt+=1 
                if cnt <= 1  :
                    return 1 
    return 0 

print(solution())