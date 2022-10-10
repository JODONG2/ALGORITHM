"""
3
0 0 0
0 0 0
0 0 0
"""
import sys 

direction = [(0,1),(1,1),(1,0)]
answer = 0 
def move(room,n,x,y,d):
    if x == n-1 and y == n-1 : 
        global answer 
        answer += 1 
    for pd in range(-1,2,1):
        nd = d+pd 
        if 0<=nd<=2:
            px,py = direction[nd] 
            nx,ny = x+px, y+py 
            if nd == 2 and nx == n-1 and ny != n-1 :
                continue 
            if nd == 0 and nx != n-1 and ny == n-1 :
                continue 
            if 0<=nx<n and 0<=ny<n and room[nx][ny] != 1 :
                if nd == 1 : 
                    if nx-1 < 0 or room[nx-1][ny] == 1:
                        continue 
                    elif ny-1 <0 or room[nx][ny-1] == 1 : 
                        continue
                

                move(room,n,nx,ny,nd)

n = int(sys.stdin.readline())
room = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
if room[n-1][n-1] != 1 : 
    move(room,n,0,1,0)
print(answer)