"""
상어에는 1 이상 M 이하의 자연수 번호가 붙어 있고, 모든 번호는 서로 다르다.
상어들은 영역을 사수하기 위해 다른 상어들을 쫓아내려고 하는데, 1의 번호를 가진 어른 상어는 가장 강력해서 나머지 모두를 쫓아낼 수 있다.

N×N 크기의 격자 중 M개의 칸에 상어가 한 마리씩 들어 있다. 맨 처음에는 모든 상어가 자신의 위치에 자신의 냄새를 뿌린다. 
그 후 1초마다 모든 상어가 동시에 상하좌우로 인접한 칸 중 하나로 이동하고, 자신의 냄새를 그 칸에 뿌린다. 냄새는 상어가 k번 이동하고 나면 사라진다.
먼저 인접한 칸 중 아무 냄새가 없는 칸의 방향으로 잡는다. 그런 칸이 없으면 자신의 냄새가 있는 칸의 방향으로 잡는다. 
이때 가능한 칸이 여러 개일 수 있는데, 
그 경우에는 특정한 우선순위를 따른다. 우선순위는 상어마다 다를 수 있고, 
같은 상어라도 현재 상어가 보고 있는 방향에 따라 또 다를 수 있다. 
상어가 맨 처음에 보고 있는 방향은 입력으로 주어지고, 그 후에는 방금 이동한 방향이 보고 있는 방향이 된다.

모든 상어가 이동한 후 한 칸에 여러 마리의 상어가 남아 있으면, 가장 작은 번호를 가진 상어를 제외하고 모두 격자 밖으로 쫓겨난다.

첫 줄에는 N, M, k가 주어진다. (2 ≤ N ≤ 20, 2 ≤ M ≤ N2, 1 ≤ k ≤ 1,000)

그 다음 줄부터 N개의 줄에 걸쳐 격자의 모습이 주어진다. 0은 빈칸이고, 0이 아닌 수 x는 x번 상어가 들어있는 칸을 의미한다.

그 다음 줄에는 각 상어의 방향이 차례대로 주어진다. 1, 2, 3, 4는 각각 위, 아래, 왼쪽, 오른쪽을 의미한다.

그 다음 줄부터 각 상어의 방향 우선순위가 상어 당 4줄씩 차례대로 주어진다. 각 줄은 4개의 수로 이루어져 있다. 하나의 상어를 나타내는 네 줄 중 첫 번째 줄은 해당 상어가 위를 향할 때의 방향 우선순위, 두 번째 줄은 아래를 향할 때의 우선순위, 세 번째 줄은 왼쪽을 향할 때의 우선순위, 네 번째 줄은 오른쪽을 향할 때의 우선순위이다. 
각 우선순위에는 1부터 4까지의 자연수가 한 번씩 나타난다. 가장 먼저 나오는 방향이 최우선이다. 예를 들어, 
우선순위가 1 3 2 4라면, 방향의 순서는 위, 왼쪽, 아래, 오른쪽이다.

맨 처음에는 각 상어마다 인접한 빈 칸이 존재한다. 따라서 처음부터 이동을 못 하는 경우는 없다.
"""
import sys 

n,m,k = map(int,sys.stdin.readline().split()) 
space = [list(map(int,sys.stdin.readline().split())) for _ in range(n)] # x번 상어 0은 빈칸 
shark_position = {}
for i in range(n):
    for j in range(n): 
        if space[i][j] != 0 : 
            shark_position[space[i][j]] = [i,j]
        space[i][j] = [space[i][j],0]
# 위, 아래, 좌 우 
shark_dir = list(map(int,sys.stdin.readline().split()))

shark_pri= {} 
for i in range (1,m+1): 
    shark_pri[i] = [0]
    for _ in range(4) : 
        shark_pri[i].append(list(map(int,sys.stdin.readline().split())))
    # 1상 2하 3좌 4우  우선순위
direction = [0,(-1,0),(1,0),(0,-1),(0,1)] 

def shark_move(shark_position,shark_pri, shark_dir,space):
    #n x n m마리 k초동안 냄새 유지
    # for t in range(2):
    t = 0 
    while t<=1000 and len(shark_position) >1 : 
        t+=1
        temp_space = [[0 for _ in range(n)] for _ in range(n)]
        len_shark_list = len(shark_position)
        shark_key_list = list(shark_position.keys())
        for q in range(len_shark_list): 
            key = shark_key_list[q]
            x,y = shark_position[key] 
            d = shark_dir[key-1]
            space[x][y][1] = k 
            change_first = False 
            change_second = False 
            tx,ty,td = 0,0,d
            for nd in shark_pri[key][d] : 
                px,py = direction[nd] 
                nx,ny = x+px,y+py 
                if 0<=nx<n and 0<=ny<n and space[nx][ny][0] ==0 : 
                    shark_position[key] = [nx,ny]
                    shark_dir[key-1] = nd
                    space[nx][ny][1] = -1 
                    if temp_space[nx][ny] == 0 : #상어 잡아먹기 
                        temp_space[nx][ny] = key 
                    else : 
                        if temp_space[nx][ny] < key : 
                            del shark_position[key]
                        else : 
                            del shark_position[temp_space[nx][ny]]
                            temp_space[nx][ny] = key
                    change_first = True 
                    break 
                if 0<=nx<n and 0<=ny<n and not(change_first or change_second) and space[nx][ny][0] == space[x][y][0] : 
                    change_second = True 
                    tx,ty,td = nx,ny,nd 
            if (not change_first) and change_second : 
                shark_position[key] = [tx,ty] 
                shark_dir[key-1] = td 
                space[tx][ty][1] = -1 
                if temp_space[tx][ty] == 0 : 
                    temp_space[tx][ty] = key 
                else : 
                    if temp_space[tx][ty] < key : 
                        del shark_position[key] 
                    else : 
                        del shark_position[temp_space[tx][ty]]
        for i in range(n):
            for j in range(n): 
                if space[i][j][1] == -1 : 
                    space[i][j][1] = k 
                    space[i][j][0] = temp_space[i][j] 
                elif space[i][j][1] != 0 : 
                    space[i][j][1] -= 1
                    if space[i][j][1] == 0: 
                        space[i][j][0] = 0 
        # for s in space:
        #     print(s)
        # print(shark_position,t)
    return t 
t=shark_move(shark_position,shark_pri,shark_dir,space)            
if t != 1001 : 
    print(t)
else : 
    print(-1)

"""
4 5 12
0 0 3 0
0 1 0 4
2 0 0 0
0 5 0 0
2 1 2 3 4
4 1 3 2
4 2 3 1
1 2 4 3
2 3 1 4
1 3 2 4
4 1 3 2
2 3 1 4
4 2 3 1
1 2 4 3
4 3 2 1
1 4 3 2
4 2 3 1
2 3 1 4
1 3 2 4
4 3 2 1
1 4 3 2
2 3 1 4
3 2 4 1
2 3 4 1
1 2 4 3
-> 24

5 9 12
0 0 0 0 9
0 4 0 5 0
3 0 1 0 2
0 7 0 6 0
0 0 8 0 0
2 3 4 1 2 3 3 3 4
4 1 3 2
4 2 3 1
1 2 4 3
2 3 1 4
1 3 2 4
4 1 3 2
2 3 1 4
4 2 3 1
1 2 4 3
4 3 2 1
1 4 3 2
4 2 3 1
2 3 1 4
1 3 2 4
4 3 2 1
1 4 3 2
2 3 1 4
3 2 4 1
2 3 4 1
1 2 4 3
3 1 2 4
4 2 3 1
4 1 3 2
4 2 3 1
2 3 4 1
4 3 2 1
2 3 1 4
1 3 2 4
4 1 2 3
3 4 2 1
4 3 1 2
2 4 3 1
4 2 3 1
4 1 3 2
1 3 2 4
4 3 2 1
->31
"""