#구슬탈출2

""""
5 5
#####
#..B#
#.#.#
#RO.#
#####

7 7
#######
#...RB#
#.#####
#.....#
#####.#
#O....#
#######

-1
10 10
##########
#R#...##B#
#...#.##.#
#####.##.#
#......#.#
#.######.#
#.#....#.#
#.#.#.#..#
#...#.O#.#
##########


8 8
########
#.####.#
#...#B##
#.##.R.#
######.#
##.##O.#
###.##.#
########

7

8 8
########
#.####.#
#...#B##
#.##.R.#
######.#
##.##O.#
###.##.#
########

4 6
######
#R####
#B..O#
######

4 6
######
#R#O##
#B...#
######

8 8
########
#BR.#O.#
###.#..#
#...#..#
#.###..#
#..#..##
##...#.#
########
"""
from collections import deque
def input_data(): 
    N,M = map(int,input().split()) 
    board = [] 
    B = [-1,-1]
    R = [-1,-1]
    for i in range(N): 
        board.append(list(input()))
        if "B" in board[-1]: 
            B = [i,board[-1].index("B")] 
        if "R" in board[-1]:
            R  = [i,board[-1].index("R")]
        if "O" in board[-1]:
            end = [i,board[-1].index("O")]
    board[R[0]][R[1]] = "." 
    board[B[0]][B[1]] = "."
    return N,M,board,R,B,end

def move(board,ball,x,y,N,M): 
    bx,by = ball
    cnt = 0
    if board[bx+x][by+y] =='O':
        cnt+=1
        return [bx+x, by+y],cnt
    while 0<=bx+x<N and 0<=by+y<M and board[bx+x][by+y] =='.' :
        bx+=x
        by+=y 
        cnt+=1
        if board[bx+x][by+y] =='O':
            cnt+=1
            return [bx+x, by+y],cnt
    return [bx,by],cnt

def escape(): 
    N,M,board,R,B,end = input_data()

    dx = [0,0,1,-1]
    dy = [1,-1,0,0] 
    Q= deque() 
    move_cnt = 1
    Q.append([R,B,move_cnt,[0,0]])
    check = [[R,B]]
    while Q and move_cnt<11:
        R,B,move_cnt,dir=Q.popleft()
        if move_cnt > 10 : 
            break
        for px,py in zip(dx,dy):
            if px and dir[0]!=0 : 
                continue 
            elif py and dir[1]!=0 :
                continue

            new_R, dist_R = move(board,R,px,py,N,M) 
            new_B, dist_B = move(board,B,px,py,N,M)
            
            if new_R == end and not new_B == end :
                return move_cnt 
            elif new_B==end:
                continue
            if new_R==new_B : 
                if dist_R > dist_B: 
                    new_R[0] -= px 
                    new_R[1] -= py 
                else:
                    new_B[0] -= px
                    new_B[1] -= py
            if [new_R,new_B] in check : 
                continue 
            else:
                Q.append([new_R,new_B,move_cnt+1,[px,py]])
                check.append([new_R,new_B])
    return -1
        

if __name__ == "__main__":
    print(escape())