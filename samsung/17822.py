import sys 
from collections import deque 

def spin(arr,t,d):
    if d== 0:
        for _ in range(t):
            arr.appendleft(arr.pop())
    else : 
        for _ in range(t):
            arr.append(arr.popleft())

def check(board,n,m):
    temp_board = [deque([board[i][j] for j in range(m)]) for i in range(n)]
    dx = [0,1] 
    dy = [1,0]
    check = False 
    for i in range(n):
        for j in range(m): 
            for px, py in zip (dx,dy): 
                nx,ny = i+px, (j+py)%m
                if 0<=nx<n and 0<=ny<m and board[i][j] != 0 and board[i][j] == board[nx][ny] : 
                    temp_board[nx][ny] = 0
                    temp_board[i][j] = 0
                    check = True 
    if not check: 
        son = 0 
        mot = 0 
        for i in range(n):
            for j in range(m):
                son += board[i][j]
                if board[i][j] : 
                    mot+=1
        if mot == 0 : 
            return board, False 
        avg = son/mot
        for i in range(n):
            for j in range(m):
                if board[i][j] == 0 : 
                    continue 
                if board[i][j] < avg :
                    temp_board[i][j] += 1 
                elif board[i][j] > avg :
                    temp_board[i][j] -= 1
    return temp_board,True 


if __name__ == "__main__":
    n,m,t = map(int,sys.stdin.readline().split())
    board = [deque(list(map(int,sys.stdin.readline().split()))) for _ in range (n)] 
    command = [list(map(int,sys.stdin.readline().split())) for _ in range(t)]
    for comm in command :  
        #comm[0]의 배수 comm[1] 방향으로 comm[2]칸 회전 
        x,d,k = comm
        for i in range(x,n+1,x):
            spin(board[i-1],k,d)
        board,check_board = check(board,n,m)
        if not check_board : 
            break 
    # for b in board : 
    #     print(b)
    score =0 
    for b in board:
        score += sum(b)
    print(score)
        

"""
4 4 1
1 1 2 3
5 2 4 2
3 1 3 5
2 1 3 2
2 0 1
반지름이 1, 2, ..., N인 원판이 크기가 작아지는 순으로 바닥에 놓여있고, 원판의 중심은 모두 같다. 원판의 반지름이 i이면, 
그 원판을 i번째 원판이라고 한다. 각각의 원판에는 M개의 정수가 적혀있고, i번째 원판에 적힌 j번째 수의 위치는 (i, j)로 표현한다. 수의 위치는 다음을 만족한다.
(i, 1)은 (i, 2), (i, M)과 인접하다.
(i, M)은 (i, M-1), (i, 1)과 인접하다.
(i, j)는 (i, j-1), (i, j+1)과 인접하다. (2 ≤ j ≤ M-1)
(1, j)는 (2, j)와 인접하다.
(N, j)는 (N-1, j)와 인접하다.
(i, j)는 (i-1, j), (i+1, j)와 인접하다. (2 ≤ i ≤ N-1)

command[0]의 배수인 원판을 di 방향으로 ki칸 회전
di 0 인경우 시계방향 1인경우 반시계방향
원판을 아래와 같은 방법으로 총 T번 회전시키려고 한다. 원판의 회전 방법은 미리 정해져 있고, i번째 회전할때 사용하는 변수는 xi, di, ki이다.

번호가 xi의 배수인 원판을 di방향으로 ki칸 회전시킨다. di가 0인 경우는 시계 방향, 1인 경우는 반시계 방향이다.
원판에 수가 남아 있으면, 인접하면서 수가 같은 것을 모두 찾는다.
그러한 수가 있는 경우에는 원판에서 인접하면서 같은 수를 모두 지운다.
없는 경우에는 원판에 적힌 수의 평균을 구하고, 평균보다 큰 수에서 1을 빼고, 작은 수에는 1을 더한다.
원판을 T번 회전시킨 후 원판에 적힌 수의 합을 구해보자.
"""