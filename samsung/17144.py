
"""
공기청정기는 항상 1번 열에 설치되어 있고, 크기는 두 행을 차지한다. 공기청정기가 설치되어 있지 않은 칸에는 미세먼지가 있고, (r, c)에 있는 미세먼지의 양은 Ar,c이다.

1초 동안 아래 적힌 일이 순서대로 일어난다.

미세먼지가 확산된다. 확산은 미세먼지가 있는 모든 칸에서 동시에 일어난다.
(r, c)에 있는 미세먼지는 인접한 네 방향으로 확산된다.
인접한 방향에 공기청정기가 있거나, 칸이 없으면 그 방향으로는 확산이 일어나지 않는다.
확산되는 양은 Ar,c/5이고 소수점은 버린다.
(r, c)에 남은 미세먼지의 양은 Ar,c - (Ar,c/5)×(확산된 방향의 개수)이다.

공기청정기가 작동한다.
공기청정기에서는 바람이 나온다.
위쪽 공기청정기의 바람은 반시계방향으로 순환하고, 아래쪽 공기청정기의 바람은 시계방향으로 순환한다.
바람이 불면 미세먼지가 바람의 방향대로 모두 한 칸씩 이동한다.
공기청정기에서 부는 바람은 미세먼지가 없는 바람이고, 공기청정기로 들어간 미세먼지는 모두 정화된다.
다음은 확산의 예시이다.

첫째 줄에 R, C, T (6 ≤ R, C ≤ 50, 1 ≤ T ≤ 1,000) 가 주어진다.
둘째 줄부터 R개의 줄에 Ar,c (-1 ≤ Ar,c ≤ 1,000)가 주어진다. 
공기청정기가 설치된 곳은 Ar,c가 -1이고, 나머지 값은 미세먼지의 양이다. -1은 2번 위아래로 붙어져 있고, 가장 윗 행, 아랫 행과 두 칸이상 떨어져 있다.

첫째 줄에 T초가 지난 후 구사과 방에 남아있는 미세먼지의 양을 출력한다.
rxc격자판 
"""
def copy(ori,r,c):
    dist = [[0 for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            dist[i][j] = ori[i][j]
    return dist 

def f1(room,r,c,air):
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    room2 = copy(room,r,c)
    for i in range(r):
        for j in range(c):
            if (r,c) ==(air,0) or (r,c) == (air+1,0) or room[i][j] <= 0:
                continue
            cnt = 0
            dust = room[i][j]
            for px,py in zip(dx,dy):
                nx,ny = i+px, j+py 
                if 0<=nx<r and 0<=ny<c and room[nx][ny] != -1 : 
                    room2[nx][ny] += dust//5 
                    cnt+=1
            room2[i][j] -= (dust//5)*cnt
    return f2(room2,r,c,air)

def f2(room,r,c,air):
    for i in range(air-1,0,-1): # 에어컨 위 
        room[i][0] = room[i-1][0]

    for i in range(air+2,r-1): #에어컨 아래 
        room[i][0] = room[i+1][0]

    for j in range(c-1): #위아래 왼쪽으로 밀기 
        room[0][j] = room[0][j+1]
        room[r-1][j] = room[r-1][j+1]

    for i in range(air): # 끝에서 올라가는거 
        room[i][c-1] = room[i+1][c-1]

    for i in range(r-1,air+1,-1): #끝에서 내려가는거 
        room[i][c-1] = room[i-1][c-1]

    for j in range(c-1, 1, -1): #가운데줄 
        room[air][j] = room[air][j-1] 
        room[air+1][j] = room[air+1][j-1]
    room[air][1] = 0 
    room[air+1][1] = 0 

    return room

if __name__ == "__main__":
    r,c,t = map(int,input().split())  
    room = [list(map(int,input().split())) for _ in range(r) ]
    dust = []
    x = 0
    for i in range(r):
        if room[i][0] == -1 : 
            x = i 
            break 
    for _ in range(t):
        room = f1(room,r,c,x) 
        # for ro in room:
        #     print(ro)

    answer = 0 

    for r in room : 
        answer += sum(r)
    print(answer+2)
            

            

"""
https://www.acmicpc.net/board/view/86764
7 8 1
0 0 0 0 0 0 0 9
0 0 0 0 3 0 0 8
-1 0 5 0 0 0 22 0
-1 8 0 0 0 0 0 0
0 0 0 0 0 10 43 0
0 0 5 0 15 0 0 0
0 0 40 0 0 0 20 0

188 
"""