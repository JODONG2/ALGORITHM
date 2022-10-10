board1= [i for i in range(0,41,2)]
board2 = [0,2,4,6,8,10,13,16,19,25,30,35,40]
board3 = [0,2,4,6,8,10,12,14,16,18,20,22,24,25,30,35,40]
board4 = [0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,28,27,26,25,30,35,40]
board = [board1,board2,board3,board4]
answer = 0 
sequence = [] 
# temp += board[temp_horse[i][0]][temp_horse[i][1]] #아니면 도착한 칸의 점수 
    #             if temp_horse[i][0] == 0 and board[temp_horse[i][0]][temp_horse[i][1]] % 10 == 0 and board[temp_horse[i][0]][temp_horse[i][1]] != 40 :
    #                 temp_horse[i][0] += board[temp_horse[i][0]][temp_horse[i][1]] // 10 #10,20,30 만나면 길이 바뀜 
def dfs(command,point,index,horse):
    if index == 9 :
        print(sequence,point,horse,index)
        global answer
        answer = max(answer, point)
        return
    save_horse = horse[:]
    for c in range(10) : 
        if c <= index : 
            continue 
        for h in range(4):
            if horse[h][0] == -1 :
                continue 
            save_point = point 
            
            save_horse = horse[:]
            save_horse[h][1] += command[c]

            if save_horse[h][1] >= len(board[save_horse[h][0]]): 
                save_horse[h][0] = -1 
                sequence.append(h)
                dfs(command,point,c,save_horse)
                sequence.pop()
                continue
            else : 
                is_duple = False 
                compare = [save_horse[h][0],save_horse[h][1]]
                for is_same in range(4) : 
                    if save_horse[h][0] == 0 and board[save_horse[h][0]][save_horse[h][1]] % 10 == 0 : 
                        if board[save_horse[h][0]][save_horse[h][1]] != 40 : 
                            compare[0] +=1 
                    if is_same == h : 
                        continue 
                    elif save_horse[is_same] == compare and save_horse[is_same][0] != -1 : 
                        save_horse[h][1] -= command[c]
                        is_duple = True 
                        break 
                if is_duple : 
                    continue
                
                save_point += board[save_horse[h][0]][save_horse[h][1]]
                if save_horse[h][0] == 0 and board[save_horse[h][0]][save_horse[h][1]] % 10 == 0 : 
                    if board[save_horse[h][0]][save_horse[h][1]] != 40 : 
                        save_horse[h][0] += board[save_horse[h][0]][save_horse[h][1]] // 10 
                sequence.append(h)
                dfs (command,save_point,c, save_horse)
                sequence.pop()
                save_point -= board[save_horse[h][0]][save_horse[h][1]]
    return 
    # print(hor,'first hor ')
    # if index == 10 : 
    #     print(command,point,index,hor,sequence,hor)
    #     global answer 
    #     print(point)
    #     answer = max(point,answer)
    # temp_horse = [hor[i] for i in range(4)]
    # for c in range(10) : 
    #     if c <= index :
    #         continue 
    #     for i in range(4):
    #         temp = point 
    #         if temp_horse[i][0]==-1 : #도착한놈은 말로 안씀
    #             continue 

    #         # print(index,temp_horse,point)

    #         temp_horse[i][1] += command[c]
    #         print(temp_horse, 'first temp_horse')
    #         duple = False  #옮기는 칸에 말 있으면 안됨
    #         for j in range(4):
    #             if i == j : 
    #                 continue
    #             if temp_horse[j] == temp_horse[i] and temp_horse[j][0] != -1 : 
    #                 duple = True 
    #                 temp_horse[i][1] -= command[c] 
    #                 break 
    #         if duple : 
    #             continue 

    #         if len(board[temp_horse[i][0]]) <= temp_horse[i][1] : # 도착 넘어가면 점수 x..?!
    #             temp_horse[i][0] = -1 #말 도착 
    #         else :
    #             temp += board[temp_horse[i][0]][temp_horse[i][1]] #아니면 도착한 칸의 점수 
    #             if temp_horse[i][0] == 0 and board[temp_horse[i][0]][temp_horse[i][1]] % 10 == 0 and board[temp_horse[i][0]][temp_horse[i][1]] != 40 :
    #                 temp_horse[i][0] += board[temp_horse[i][0]][temp_horse[i][1]] // 10 #10,20,30 만나면 길이 바뀜 
    #         sequence.append(i)
    #         dfs(command,temp,c,temp_horse)
    #         sequence.pop()
    #         print(temp_horse,'compare',hor)
    #         temp_horse = [hor[k] for k in range(4)]
    #         print(temp_horse,'compare2',hor)

            
if __name__ == "__main__":
    command = list(map(int,input().split()))
    horse = [[0,0],[0,0],[0,0],[0,0]]
    dfs(command, 0, -1, horse)
    print(answer)