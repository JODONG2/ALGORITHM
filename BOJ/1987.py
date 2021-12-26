dx = [0,0,1,-1]
dy = [1,-1,0,0]
def BFS(x,y):
    Q = set([(x, y, board[x][y])])
    global answer
    while Q:
        x,y,ans = Q.pop()
        for i in range(4):
            new_x = x+dx[i]
            new_y = y+dy[i]
            if 0<=new_x<C and 0<=new_y<R and board[new_x][new_y] not in ans :
                Q.add((new_x, new_y, ans+ board[new_x][new_y]))
                answer = max(answer,len(ans)+1)

R,C = map(int,input().split()) 
board = []
for _ in range(R):
    board.append(list(map(str,input())))
answer = 1
BFS(0,0)
print(answer)