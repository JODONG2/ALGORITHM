import sys 
answer = 26
def paste(x,y,paper):
    global answer 
    if sum(paper) >= answer :
        return 
    if y == 10 and x == 9 :
        answer = min(sum(paper),answer)
        return 
    if y >= 10 : 
        x += 1 
        y = 0 
        if x >= 10 : 
            answer = min(sum(paper), answer)
            return 
    ret = False 
    for i in range(10):
        for j in range(10):
            if world[i][j] == 1 : 
                ret = True 
                break 
        if ret :
            break 
    if not ret : 
        answer = min(answer,sum(paper))
        return

    if world[x][y] == 1 : 
        # print(x,y,paper)
        for k in range(5,0,-1): 
            if paper[k-1] == 5 or x + k > 10 or y + k > 10 : 
                continue 
            check = False 
            for i in range(k):
                for j in range(k): 
                    if world[x+i][y+j] == 0 : 
                        check = True 
                        break 
                if check : 
                    break 
            if not check : 
                for i in range(k):
                    for j in range(k): 
                        world[x+i][y+j] = 0
                paper[k-1] += 1 
                paste(x,y+k,paper)
                paper[k-1] -= 1 
                for i in range(k): 
                    for j in range(k): 
                        world[x+i][y+j] = 1 
    else : 
        paste(x,y+1,paper)
        
world = [list(map(int,sys.stdin.readline().split())) for _ in range(10)]
paper = [0,0,0,0,0]
paste(0,0,paper)
print(answer) if answer != 26 else print(-1)

"""

0 0 0 0 0 0 0 0 0 0
1 1 1 1 1 0 0 0 0 0
1 1 1 1 1 0 1 1 1 1
1 1 1 1 1 0 1 1 1 1
1 1 1 1 1 0 1 1 1 1
1 1 1 1 1 0 1 1 1 1
0 0 0 0 0 0 0 0 0 0
0 1 1 1 0 1 1 0 0 0
0 1 1 1 0 1 1 0 0 0
0 1 1 1 0 0 0 0 0 1

"""
