board1= [i for i in range(0,41,2)]
#[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40] #20 
board2 = [0,2,4,6,8,10,13,16,19,25,30,35,40] # 12 
board3 = [0,2,4,6,8,10,12,14,16,18,20,22,24,25,30,35,40] # 16 
board4 = [0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,28,27,26,25,30,35,40] # 22 
board = [board1,board2,board3,board4]
#TODO: board[0][0] 에서 시작
#TODO: if r == 0 :
#TODO: board[r][c] == 10, 20, 30 이면 r += board[r][c]//10 
#TODO: 말을 고르고 이동할 칸에 이미 다른 말이 존재하면 그 말 선택 안됨 (단, 도착점에는 가능)
#TODO: 말이 이동을 마치면 그 칸에 적힌 숫자가 점수에 추가 됨 
#TODO: 주사위에서 나올 수 10개를 미리 알고 있을 때, 얻을 수 있는 점수의 최댓값을 구해보자.

"""
5 1 2 3 4 5 5 3 2 4
1 1 1 1 1 1 1 1 1 1

4 1 4 4 4 4 3 2 2 4  -> 205

4 1 3 4 4 4 3 3 2 4  -> 211

4 3 2 1 3 4 3 4 1 2  -> 202 

5 3 2 5 2 4 4 2 4 1  -> 231

3 1 2 5 5 3 2 4 4 3  -> 202

5 3 4 3 1 3 3 3 5 2  -> 216

5 4 5 2 2 2 5 3 1 4  -> 245

0 -> 10 19 40 -> 69 
1 -> 8 18 22 26 30 30 35 169 238 
"""
answer = 0
# sequence = [] 
def dfs(save_horse,command,index,score):
    if index == 10 : 
        global answer         
        answer = max(answer,score)
        # if score == 238:
        #     print(save_horse,sequence)
        return 
    
    for h in range(4): 
        if save_horse[h][0] == -1 :
            continue 
        # save_horse = horse[:]
        save_horse[h][1] += command[index] 

        hx,hy =save_horse[h][0],save_horse[h][1]

        if hy >= len(board[hx]) :
            save_horse[h][0] = -1 
            # sequence.append(h)
            dfs(save_horse,command,index+1,score)
            # sequence.pop()
            save_horse[h][0] = hx 
            save_horse[h][1] -= command[index]
        else : 
            is_move = False 
            if hx ==0 and board[hx][hy] % 10 == 0 and board[hx][hy] != 40 :
                save_horse[h][0] += board[hx][hy] // 10 
                is_move = True 

            is_duple = False 
            for i in range(4): 
                if i == h :
                    continue 
                cx,cy = save_horse[i][0], save_horse[i][1] 
                if cx == -1 :
                    continue
                
                if (hx!= 0 and cx!=0) and ((cy==hy and board[cx][cy] == 30 and board[hx][hy] == 30) or (board[cx][cy] == 35 and board[hx][hy] == 35)) :
                    is_duple = True 
                    break
                if save_horse[i] == save_horse[h] or (board[cx][cy] == 25 and board[hx][hy] == 25) or (board[cx][cy] == 40 and board[hx][hy] == 40 ): 
                    is_duple = True 
                    break 
            if is_duple : 
                if is_move : 
                    save_horse[h][0] = hx
                save_horse[h][1] -= command[index]
                continue 
            # sequence.append(h)
            dfs(save_horse,command,index+1, score+board[save_horse[h][0]][save_horse[h][1]])
            # sequence.pop()
            save_horse[h][0], save_horse[h][1] = hx, hy - command[index]
        if index == h: 
            break 
        
            

if __name__ == "__main__":
    command = list(map(int,input().split())) 
    horse = [[0,0]for _ in range(4)]
    dfs(horse, command, 0, 0)
    print(answer)

# 10 13 4 25 8 18 28 40 32 40 
# 23 27 52 60 78 106 146 178 218 