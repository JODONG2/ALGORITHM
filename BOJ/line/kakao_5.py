
def UPDATE2(board,merge_value,v1,v2): 
    for i in range(50): 
        for j in range(50): 
            if board[i][j][0] : 
                continue 
            if board[i][j][1] == v1 : 
                board[i][j][1] = v2 

    for idx,v in enumerate(merge_value):
        if v == v1 : 
            merge_value[idx] = v2 

def UPDATE (board,merge_value,*arg): 
    if len(arg) == 3 : 
        return UPDATE2(board,merge_value,arg[1],arg[2])
    r,c,v = int(arg[1])-1,int(arg[2])-1,arg[3]
    if board[r][c][0] : 
        merge_value[board[r][c][2]] = v 
    else : 
        board[r][c][1] = v

def MERGE(board,idx,merge_value,_,r1,c1,r2,c2):
    r1 = int(r1) - 1 
    r2 = int(r2) - 1 
    c1 = int(c1) - 1 
    c2 = int(c2) - 1 
    idx += 1
    if board[r1][c1][0] : 
        board[r2][c2][2] = board[r1][c1][2] 
        board[r2][c2][0] = True 
        if merge_value[board[r1][c1][2]] == '' and board[r2][c2][1] != '': 
            merge_value[board[r1][c1][2]] = board[r2][c2][1] 
        return False 
    elif board[r1][c1][0] and board[r2][c2][0] : 
        for i in range(50): 
            for j in range(50): 
                if board[i][j][2] == board[r2][c2][2] 
    elif board[r2][c2][0] : 
        board[r1][c1][2] = board[r2][c2][2] 
        board[r1][c1][0] = True 
        if merge_value[board[r2][c2][2]] == '' and board[r1][c1][1] != '': 
            merge_value[board[r2][c2][2]] = board[r1][c1][1] 
        return False 
    else : 
        board[r1][c1][0] = True   
        board[r2][c2][0] = True  
        board[r1][c1][2] = idx 
        board[r2][c2][2] = idx 
        if board[r1][c1][1] != '' : 
            merge_value.append(board[r1][c1][1])
        elif board[r2][c2][1] != '': 
            merge_value.append(board[r2][c2][1])
        else : 
            merge_value.append('')
        return True     
def UNMERGE(board,merge_value,_,r1,c1):
    r1 = int(r1)-1
    c1 = int(c1) -1
    if board[r1][c1][2] == -1 : 
        return 
    for i in range(50):
        for j in range(50): 
            if i == r1 and j == c1 : 
                continue 
            if board[i][j][2] == board[r1][c1][2] : 
                board[i][j][0] = False 
                board[i][j][1] = ''
                board[i][j][2] = -1 
    if merge_value[board[r1][c1][2]] != '' : 
        board[r1][c1][1] = merge_value[board[r1][c1][2]] 
    else : 
        board[r1][c1][1] = '' 

def PRINT(board,merge_value,_,r1,c1):
    r1 = int(r1)-1 
    c1 = int(c1)-1 
    if board[r1][c1][0] : 
        return(merge_value[board[r1][c1][2]])
    elif board[r1][c1][1] !='': 
        return board[r1][c1][1]
    else : 
        return 'EMPTY'

def solution(commands):
    answer = []
    merge_id = 0
    merge_value = [] 
    board = [[[False, '', -1] for _ in range(50)] for _ in range(50)] # isMerger, value, merge_id 
    for command in commands : 
        comm = command.split()
        if comm[0] == "UPDATE": 
            UPDATE(board,merge_value, *comm)
        elif comm[0] == "MERGE" : 
            if MERGE(board,merge_id,merge_value,*comm):
                merge_id += 1 
        elif comm[0] == "PRINT" : 
            answer.append(PRINT(board,merge_value,*comm))

        elif comm[0] == "UNMERGE" : 
            UNMERGE(board,merge_value,*comm)

    
    return answer

print(solution(["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]))
print(solution(["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"]))