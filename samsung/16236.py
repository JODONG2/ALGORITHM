
"""
N×N 크기의 공간에 물고기 M마리와 아기 상어 1마리가 있다. 공간은 1×1 크기의 정사각형 칸으로 나누어져 있다. 한 칸에는 물고기가 최대 1마리 존재한다.

상어, 물고기 -> 크기 
가장 처음에 아기 상어의 크기는 2이고, 아기 상어는 1초에 상하좌우로 인접한 한 칸씩 이동한다.

아기 상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없고, 나머지 칸은 모두 지나갈 수 있다. 
아기 상어는 자신의 크기보다 작은 물고기만 먹을 수 있다. 
따라서, 크기가 같은 물고기는 먹을 수 없지만, 그 물고기가 있는 칸은 지나갈 수 있다. if 

움직이기
더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청한다.
먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.
거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값이다.
거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다. x,y가 작은값 x부터 

아기 상어의 이동은 1초 걸리고, 물고기를 먹는데 걸리는 시간은 없다고 가정한다. 
즉, 아기 상어가 먹을 수 있는 물고기가 있는 칸으로 이동했다면, 이동과 동시에 물고기를 먹는다. 물고기를 먹으면, 그 칸은 빈 칸이 된다.

아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가한다. 예를 들어, 크기가 2인 아기 상어는 물고기를 2마리 먹으면 크기가 3이 된다.
공간의 상태가 주어졌을 때, 아기 상어가 몇 초 동안 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는지 구하는 프로그램을 작성하시오.

output 
더이상 먹을 수 있는게 없을때까지 몇 초? 

input 
첫째 줄에 공간의 크기 N(2 ≤ N ≤ 20)이 주어진다.

둘째 줄부터 N개의 줄에 공간의 상태가 주어진다. 공간의 상태는 0, 1, 2, 3, 4, 5, 6, 9로 이루어져 있고, 아래와 같은 의미를 가진다.

0: 빈 칸
1, 2, 3, 4, 5, 6: 칸에 있는 물고기의 크기
9: 아기 상어의 위치 크기 == 2 
아기 상어는 공간에 한 마리 있다. 한마리만 존재 

"""
from collections import deque 
def move(x,y,fish,space,n): 
    t=0 
    position = deque([(x,y,t)]) 
    check = [[True for _ in range(n)] for _ in range(n)]
    check[x][y] = False 
    dx = [-1,0,0,1]
    dy = [0,-1,1,0]
    size = 2 
    cnt = 0
    time = deque()
    answer = 0 
    while fish and size > fish[0] and position : 
        if t == position[0][2] or not time :
            x,y,t = position.popleft()
            for px,py in zip(dx,dy):
                nx,ny = x+px, y+py 
                if 0<=nx<n and 0<=ny<n and check[nx][ny] and space[nx][ny]<=size:
                    check[nx][ny] = False 
                    if 0<space[nx][ny]<size :
                        time.append((nx,ny,t+1))
                        position.append((nx,ny,t+1))
                    else :
                        position.append((nx,ny,t+1))
        else :
            fish.popleft()
            nx,ny = float('inf'),float('inf')
            for ti in time : 
                if ti[0] < nx : 
                    nx,ny = ti[0], ti[1] 
                    answer = ti[2] 
                elif ti[0] == nx and ti[1] < ny :
                    nx,ny = ti[0], ti[1]
                    answer = ti[2]
            space[nx][ny] = 0 
            cnt += 1
            if cnt == size : 
                size += 1
                cnt = 0
            position = deque([(nx,ny,answer)])
            time = deque()
            for i in range(n):
                for j in range(n): 
                    check[i][j] = True 
            check[nx][ny] = False 
    return answer

if __name__ =="__main__":
    n = int(input()) 
    space = [list(map(int,input().split())) for _ in range(n)]
    x,y= 0,0
    fish = [] 
    for i in range(n):
        for j in range(n): 
            if space[i][j] != 0 : 
                if space[i][j] == 9 :
                    x,y= i,j
                    space[i][j] = 0 
                else : 
                    fish.append(space[i][j])
    fish = deque(sorted(fish))
    print(move(x,y,fish,space,n))




"""
https://www.acmicpc.net/board/view/42021

3
0 0 0
0 0 0
0 9 0
0

3
0 0 1
0 0 0
0 9 0
3

4
4 3 2 1
0 0 0 0
0 0 9 0
1 2 3 4
14 
"""
