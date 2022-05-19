#2048

from copy import deepcopy
def input_data(): 
    N = int(input()) 
    board = [list(map(int,input().split())) for _ in range(N)]
    return N,board 

def find_max(board):
    maximum = 0 
    for line in board : 
        maximum = max(maximum, max(line)) 
    return maximum 
def show_board(board):
    print("-"*10)
    for b in board:
        print(b)
        
def up(board2,N,cnt):
    board = deepcopy(board2)
    # show_board(board)
    for i in range(N): 
        stack = [] 
        for j in range(N):
            if board[j][i] == 0 : 
                continue 
            elif stack and not stack[-1][1] and board[j][i] == stack[-1][0] :
                stack[-1][0]*=2
                stack[-1][1] = True 
                board[j][i] = 0 
            else:
                stack.append([board[j][i],False])
                board[j][i] =0
        for j in range(len(stack)):
            board[j][i] = stack[j][0]

    if cnt == 5 :
        return find_max(board)
    else : 
        return max(up(board,N,cnt+1), down(board,N,cnt+1),right(board,N,cnt+1),left(board,N,cnt+1))
def down(board2,N,cnt):
    board = deepcopy(board2)
    # show_board(board)
    for i in range(N): 
        stack = [] 
        for j in range(N-1,-1,-1):
            if board[j][i] == 0 : 
                continue 
            elif stack and not stack[-1][1] and board[j][i] == stack[-1][0] :
                stack[-1][0]*=2
                stack[-1][1] = True 
                board[j][i] = 0 
            else:
                stack.append([board[j][i],False])
                board[j][i] =0
        for j in range(len(stack)):
            board[N-j-1][i] = stack[j][0] 
    if cnt == 5 :
        return find_max(board)
    else : 
        return max(up(board,N,cnt+1), down(board,N,cnt+1),right(board,N,cnt+1),left(board,N,cnt+1))   
def right(board2,N,cnt):
    board = deepcopy(board2)
    # show_board(board)
    for i in range(N): 
        stack = [] 
        for j in range(N-1,-1,-1):
            if board[i][j] == 0 : 
                continue 
            elif stack and not stack[-1][1] and board[i][j] == stack[-1][0] :
                stack[-1][0]*=2
                stack[-1][1] = True 
                board[i][j] = 0 
            else:
                stack.append([board[i][j], False] )
                board[i][j] =0
        for j in range(len(stack)):
            board[i][N-j-1] = stack[j][0]
    if cnt == 5 :
        return find_max(board)
    else : 
        return max(up(board,N,cnt+1), down(board,N,cnt+1),right(board,N,cnt+1),left(board,N,cnt+1))   
def left(board2,N,cnt): 
    board = deepcopy(board2)
    # show_board(board)
    for i in range(N): 
        stack = [] 
        for j in range(N):
            if board[i][j] == 0 : 
                continue 
            elif stack and not stack[-1][1] and board[i][j] == stack[-1][0] :
                stack[-1][0]*=2
                stack[-1][1] = True
                board[i][j] = 0 
            else:
                stack.append([board[i][j],False])
                board[i][j] =0
        for j in range(len(stack)):
            board[i][j] = stack[j][0]

    if cnt == 5 :
        return find_max(board)
    else : 
        return max(up(board,N,cnt+1), down(board,N,cnt+1),right(board,N,cnt+1),left(board,N,cnt+1)) 

if __name__ == "__main__":
    N,board = input_data() 
    print(max(up(board,N,1), down(board,N,1),right(board,N,1),left(board,N,1)))


"""
5
2 0 0 0 0
2 0 0 0 0
4 0 0 0 0
2 0 0 0 0
2 0 0 0 0

4 0 0 0 0
4 0 0 0 0
4 0 0 0 0
0 0 0 0 0
0 0 0 0 0

7
2 2 2 2 2 2 2
2 0 2 2 2 2 2
2 0 2 2 2 2 2
2 0 2 2 2 2 2
2 2 2 0 2 2 2 
2 2 2 2 2 2 0
2 2 2 2 2 2 0
->32

4
2 2 4 16
0 0 0 0
0 0 0 0
0 0 0 0

10
16 16 8 32 32 0 0 8 8 8
16 0 0 0 0 8 0 0 0 16
0 0 0 0 0 0 0 0 0 2
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0

20
1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024
1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024
1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024
1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024
1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024
1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024
1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024
1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024
1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024
1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024
1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024
1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024
1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024
1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024
1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024
1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024
1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024
1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024
1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024
1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024
32768


10
0 0 64 32 32 0 0 0 0 0
0 32 32 64 0 0 0 0 0 0
0 0 128 0 0 0 0 0 0 0 
64 64 128 0 0 0 0 0 0 0
0 0 64 32 32 0 0 0 0 0
0 32 32 64 0 0 0 0 0 0
0 0 128 0 0 0 0 0 0 0 
64 64 128 0 0 0 0 0 0 0
128 32 2 4 0 0 0 0 0 0
0 0 128 0 0 0 0 0 0 0
->1024
"""