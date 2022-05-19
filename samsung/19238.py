

"""
 스타트 택시는 특이하게도 손님을 도착지로 데려다줄 때마다 연료가 충전되고, 연료가 바닥나면 그 날의 업무가 끝난다.

택시 기사 최백준은 오늘 M명의 승객을 태우는 것이 목표이다. 백준이 활동할 영역은 N×N 크기의 격자로 나타낼 수 있고, 
각 칸은 비어 있거나 벽이 놓여 있다. 
택시가 빈칸에 있을 때, 상하좌우로 인접한 빈칸 중 하나로 이동할 수 있다. 알고리즘 경력이 많은 백준은 특정 위치로 이동할 때 항상 최단경로로만 이동한다.
M명의 승객은 빈칸 중 하나에 서 있으며, 다른 빈칸 중 하나로 이동하려고 한다. 여러 승객이 같이 탑승하는 경우는 없다. 따라서 백준은 한 승객을 태워 목적지로 이동시키는 일을 M번 반복해야 한다. 
각 승객은 스스로 움직이지 않으며, 출발지에서만 택시에 탈 수 있고, 목적지에서만 택시에서 내릴 수 있다.

백준이 태울 승객을 고를 때는 현재 위치에서 최단거리가 가장 짧은 승객을 고른다. 
그런 승객이 여러 명이면 그중 행 번호가 가장 작은 승객을, 그런 승객도 여러 명이면 그중 열 번호가 가장 작은 승객을 고른다.
택시와 승객이 같은 위치에 서 있으면 그 승객까지의 최단거리는 0이다. 연료는 한 칸 이동할 때마다 1만큼 소모된다. 한 승객을 목적지로 성공적으로 이동시키면, 
그 승객을 태워 이동하면서 소모한 연료 양의 두 배가 충전된다. 
이동하는 도중에 연료가 바닥나면 이동에 실패하고, 그 날의 업무가 끝난다. 승객을 목적지로 이동시킨 동시에 연료가 바닥나는 경우는 실패한 것으로 간주하지 않는다.

첫 줄에 N, M, 그리고 초기 연료의 양이 주어진다. (2 ≤ N ≤ 20, 1 ≤ M ≤ N**2, 1 ≤ 초기 연료 ≤ 500,000) 연료는 무한히 많이 담을 수 있기 때문에, 초기 연료의 양을 넘어서 충전될 수도 있다.

다음 줄부터 N개의 줄에 걸쳐 백준이 활동할 영역의 지도가 주어진다. 0은 빈칸, 1은 벽을 나타낸다.

다음 줄에는 백준이 운전을 시작하는 칸의 행 번호와 열 번호가 주어진다. 행과 열 번호는 1 이상 N 이하의 자연수이고, 운전을 시작하는 칸은 빈칸이다.

그다음 줄부터 M개의 줄에 걸쳐 각 승객의 출발지의 행과 열 번호, 그리고 목적지의 행과 열 번호가 주어진다. 모든 출발지와 목적지는 빈칸이고, 모든 출발지는 서로 다르며, 각 손님의 출발지와 목적지는 다르다.
"""
import sys 
n,m,oil= map(int,sys.stdin.readline().split()) 
world = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
start = list(map(int,sys.stdin.readline().split())) 
infor = [list(map(int,sys.stdin.readline().split())) for _ in range(m)]
start.append(oil)
start[0] -= 1
start[1] -= 1 
move_key = {}
for i,(inf) in enumerate(infor): 
    x1,y1,x2,y2 = inf 
    world[x1-1][y1-1] = 2+i 
    move_key[2+i] = [x2-1,y2-1]
from collections import deque 

dx = [0,0,-1,1]
dy = [1,-1,0,0]
def search1(world,start): 
    if world[start[0]][start[1]] != 0 : 
        return start
    q = deque([start]) 
    check = [[True for _ in range(n)] for _ in range(n)]
    succ = []
    succ_oil = -2
    rex,rey = float('inf'),float('inf')
    while q : 
        x,y,o = q.popleft()
        if o == -1 : 
            return -1,-1,-1
        if (not succ) or succ_oil +1 == o : 
            for px,py in zip(dx,dy): 
                nx,ny = x+px, y+py
                if 0<=nx<n and 0<=ny<n and o>0 and check[nx][ny] and world[nx][ny] != 1 : 
                    q.append([nx,ny,o-1])
                    check[nx][ny] = False 
                    if world[nx][ny] != 0 and world[nx][ny] != 1 : 
                        succ.append([nx,ny,o-1])
                        succ_oil = o-1 
        elif succ and o == succ_oil : 
            for suc in succ : 
                if rex > suc[0] : 
                    rex,rey = suc[0],suc[1]
                elif rex == suc[0] and rey>suc[1] : 
                    rey = suc[1]
            break
    return [rex,rey,succ_oil]

def search_dist(world, start, move_key): 
    #TODO: 목적지까지 모셔주기 
    q = deque([start]) 
    check = [[1 for _ in range(n)] for _ in range(n)]
    sx,sy,so = start
    check[move_key[world[sx][sy]][0]][move_key[world[sx][sy]][1]] = 2
    # for w in world:
    #     print(w)
    # for c in check :
    #     print(c)
    # check[sx][sy] = 0 
    del move_key[world[sx][sy]]
    world[sx][sy] = 0
    while q : 
        x,y,o = q.popleft() 
        if o == -1 :
            return [-1,-1,-1] 
        for px,py in zip (dx,dy): 
            nx,ny = x+px, y+py 
            if 0<=nx<n and 0<=ny<n and o>0 and check[nx][ny] != 0  and world[nx][ny] != 1 : 
                if check[nx][ny] == 2 : 
                    # no = o-1 + 2*(so - (o-1))
                    no = 2*so - o + 1
                    return [nx,ny,no]
                check[nx][ny] = 0
                q.append([nx,ny,o-1])
    return [-1,-1,-1]


def taxi (world, start, move_key):
    while move_key:
        start = search1 (world,start)
        if start[0] == -1 or start[2] == -2 : 
            return -1 
        
        start = search_dist(world,start,move_key)
        if start[0] == -1 or start[2] == -2:
            return -1
        
    
    return start[2] 

print(taxi(world,start,move_key))
    
#TODO: 해당 승객부터 목적지까지의 거리 *2만큼 연료 충전됨 
#TODO: 연료 중간에 떨어지면 이동에 실패 -> 그날의 업무 끝 // 도착과 동시에 연료 바닥은 ㄱㅊㄱㅊ 


"""
6 3 15
0 0 1 0 0 0
0 0 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 1 0
0 0 0 1 0 0
6 5
2 2 5 6
5 4 1 6
4 2 3 5

6 3 15
0 0 1 0 0 0
0 0 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 1 0
0 0 0 1 0 0
6 5
2 2 5 6
5 4 1 6
4 2 3 5

3 3 1
0 0 0 
0 0 0 
0 0 0
1 1 
1 2 1 3 
2 3 2 2
2 1 3 1

3 3 2
0 0 0 
0 0 0 
0 0 0
1 1 
1 2 1 3 
2 3 2 2
2 1 3 1

3 2 100
0 0 0
1 1 1
0 0 0 
1 1
3 1 3 2 
1 2 1 3

3 2 100 
0 1 0 
1 1 0 
0 0 0 
1 1 
1 3 2 3 
3 3 3 2 

5 2 100 
0 0 0 0 0 
0 0 0 0 0 
1 1 1 1 1 
0 0 0 0 0 
0 0 0 0 0
1 1 
4 1 4 2 
5 1 5 2

10 1 5000
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
5 5
10 10 5 5
"""