
"""
A번 말이 이동하려는 칸이
흰색인 경우에는 그 칸으로 이동한다. 이동하려는 칸에 말이 이미 있는 경우에는 가장 위에 A번 말을 올려놓는다.
A번 말의 위에 다른 말이 있는 경우에는 A번 말과 위에 있는 모든 말이 이동한다.
예를 들어, A, B, C로 쌓여있고, 이동하려는 칸에 D, E가 있는 경우에는 A번 말이 이동한 후에는 D, E, A, B, C가 된다.
빨간색인 경우에는 이동한 후에 A번 말과 그 위에 있는 모든 말의 쌓여있는 순서를 반대로 바꾼다.
A, B, C가 이동하고, 이동하려는 칸에 말이 없는 경우에는 C, B, A가 된다.
A, D, F, G가 이동하고, 이동하려는 칸에 말이 E, C, B로 있는 경우에는 E, C, B, G, F, D, A가 된다.
파란색인 경우에는 A번 말의 이동 방향을 반대로 하고 한 칸 이동한다. 방향을 반대로 바꾼 후에 이동하려는 칸이 파란색인 경우에는 이동하지 않고 가만히 있는다.
체스판을 벗어나는 경우에는 파란색과 같은 경우이다.

체스판의 정보는 정수로 이루어져 있고, 각 정수는 칸의 색을 의미한다. 0은 흰색, 1은 빨간색, 2는 파란색이다.
세 개의 정수로 이루어져 있고, 순서대로 행, 열의 번호, 이동 방향이다. 
행과 열의 번호는 1부터 시작하고, 이동 방향은 4보다 작거나 같은 자연수이고 1부터 순서대로 →, ←, ↑, ↓의 의미를 갖는다.
게임이 종료되는 턴의 번호를 출력한다. 그 값이 1,000보다 크거나 절대로 게임이 종료되지 않는 경우에는 -1을 출력한다.

"""
from collections import deque 

n,k = map(int,input().split()) 
board = [list(map(int,input().split())) for _ in range(n)]
a = [list(map(int,input().split())) for _ in range(k)]
position = [[deque() for _ in range(n)] for _ in range(n)]
hor_dic = {} 
for i,aa in enumerate(a) : 
    aa[0] -=1 
    aa[1] -=1
    position[aa[0]][aa[1]].append(i+1)
    hor_dic[i+1] = aa 

direction = [0,(0,1),(0,-1),(-1,0),(1,0)]
hor = list(hor_dic.keys())
answer = - 1 
t= 0
change_dic = {1:2, 2:1, 3:4, 4:3}
while answer == -1 and t< 1000:
    t+=1 
    for ho in hor :
        x,y,d = hor_dic[ho]
        print(x,y,d,t, ho)
        for p in position : 
            print(p)
        print("*"*50)
        moving = deque()
        ho2 = position[x][y].pop()
        moving.append(ho2)
        while ho != ho2 : 
            ho2 = position[x][y].pop() 
            moving.append(ho2)
        nx,ny = x+direction[d][0] , y+direction[d][1]
        # while not FINISH and cnt < 2 : 
        if 0<=nx<n and 0<=ny<n : 
            if board[nx][ny] == 1 : 
                while moving:
                    key = moving.popleft()
                    position[nx][ny].append(key)
                    hor_dic[key][0],hor_dic[key][1] = nx,ny  
            elif board[nx][ny] == 2 : 
                d = change_dic[d]
                tx,ty = x+direction[d][0], y+direction[d][1]
                if 0<=tx<n and 0<= ty < n and board[tx][ty] != 2 : 
                    nx,ny= tx,ty
                else : 
                    nx,ny = x,y
                if board[nx][ny] == 0 or board[nx][ny] ==2 or ( nx == x and ny == y): 
                    while moving : 
                        key = moving.pop() 
                        position[nx][ny].append(key) 
                        hor_dic[key][0],hor_dic[key][1] = nx,ny
                elif board[nx][ny] == 1 : 
                    while moving:
                        key= moving.popleft()
                        position[nx][ny].append(key) 
                        hor_dic[key][0],hor_dic[key][1] = nx,ny
            elif board[nx][ny] == 0 : 
                while moving : 
                    key = moving.pop()
                    position[nx][ny].append(key)
                    hor_dic[key][0],hor_dic[key][1] = nx,ny  
        else : 
            # nx,ny = x,y
            d = change_dic[d]
            tx,ty = x+direction[d][0], y+direction[d][1]
            if 0<=tx<n and 0<= ty < n and board[tx][ty] != 2 : 
                nx,ny= tx,ty
            else : 
                nx,ny = x,y

            if board[nx][ny] == 0 or board[nx][ny] == 2 or (nx == x or ny == y): 
                while moving : 
                        key = moving.pop() 
                        position[nx][ny].append(key) 
                        hor_dic[key][0],hor_dic[key][1] = nx,ny
            elif board[nx][ny] == 1:
                while moving :
                    key = moving.popleft()
                    position[nx][ny].append(key) 
                    hor_dic[key][0],hor_dic[key][1] = nx,ny
        # if cnt == 2 : 
        #     while moving :
        #         position[x][y].append(moving.pop())
        #     nx,ny = x,y
        if len(position[nx][ny]) >= 4 :
            answer = t
            break
        else : 
            hor_dic[ho] = [nx,ny,d]
    
for p in position :
    print(p)
print(answer)
"""
4 4
0 0 2 0
0 0 1 0
0 0 1 2
0 2 0 0
2 1 1
3 2 3
2 2 1
4 1 2
-1

4 4
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
1 1 1
1 2 1
1 3 1
1 4 1
1

4 4 
0 0 0 0 
0 1 0 0 
0 2 0 0 
0 2 0 0 
4 1 2
1 1 1 
1 2 1 
1 3 1

6 10
0 1 2 0 1 1
1 2 0 1 1 0
2 1 0 1 1 0
1 0 1 1 0 2
2 0 1 2 0 1
0 2 1 0 2 1
1 1 1
2 2 2
3 3 4
4 4 1
5 5 3
6 6 2
1 6 3
6 1 2
2 4 3
4 2 1

4 4 
0 0 0 0 
0 1 0 0 
0 2 0 0 
2 1 2 0 
4 2 1
1 1 1 
1 2 1 
3 2 4

4 4 
0 0 0 0 
0 1 0 0 
0 2 0 0 
0 2 2 0 
4 2 1
1 1 1 
1 2 1 
1 3 1

4 4 
0 1 0 1 
1 0 2 0 
0 1 0 2
1 0 1 0
1 1 1 
2 1 1
3 1 1 
2 4 3

4 5 
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
1 4 3
1 1 1 
2 1 1
3 1 1
4 1 1 


7 10
0 1 1 0 1 1 2
1 1 0 1 1 0 1
2 1 0 1 1 0 1
1 0 1 1 0 2 0
2 0 1 2 0 1 0
0 2 1 0 2 1 0
0 0 0 1 0 1 0
1 1 1
2 2 2
3 3 4
4 4 1
5 5 3
6 6 2
1 6 3
6 1 2
2 4 3
4 2 1
"""
