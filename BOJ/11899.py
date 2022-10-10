import sys 

bar = [0,(0,0),(0,1),(1,0)]
def put_bar(rg,rb,commands):
    #t,x,y -> 내가하던 x,y 
    answer = 0 
    for t,x,y in commands:
        go_right(rb,x,y,t) 
        go_down(rg,x,y,t)
        answer += pop_rgb(rb,rg)
        over(rb,rg)
    return answer 

def over(rb,rg): 
    succ_r = set() 
    succ_d = set()
    for i in range(4,6): 
        for j in range(4):
            if rb[j][i] == 1 : 
                succ_r.add(i)
            if rg[i][j] == 1:
                succ_d.add(i)
    if len(succ_r)>0 :
        len_r = len(succ_r)
        for i in range(9,3,-1):
            for j in range(4):
                rb[j][i] = rb[j][i-len_r]
    if len(succ_d)>0: 
        len_d = len(succ_d)
        for i in range(9,3,-1): 
            for j in range(4): 
                rg[i][j] = rg[i-len_d][j]


def go_right(rb,x,y,t) : 
    x2 = x+bar[t][0]
    y2 = y+bar[t][1] 
    while y2 <=9 : 
        if rb[x][y] == 0 and rb[x2][y2] == 0 :
            y+=1 
            y2+=1 
        else : 
            break 
    y2 -= 1
    y -= 1 
    rb[x][y], rb[x2][y2] = 1,1 

def go_down(rg,x,y,t): 
    x2 = x+bar[t][0] 
    y2 = y+bar[t][1] 
    while x2<=9 : 
        if rg[x][y] == 0 and rg[x2][y2] == 0 : 
            x2+=1
            x+=1 
        else : 
            break
    x2-=1 
    x -=1 
    rg[x][y],rg[x2][y2] = 1,1 
    


def pop_rgb(rb,rg) :
    ret =0  
    for i in range(6,10):
        succ_r = True
        succ_d = True  
        for j in range(4):
            if rb[j][i]==0 : 
                succ_r = False 
            if rg[i][j] == 0 :
                succ_d = False 
        if succ_r : 
            ret +=1 
            for k in range(i,3,-1):
                for h in range(4): 
                     rb[h][k] = rb[h][k-1]
        if succ_d : 
            ret +=1 
            for k in range(i,3,-1): 
                for h in range(4): 
                    rg[k][h] = rg[k-1][h]
    return ret 
            


if __name__ == "__main__": 
    n = int(input()) 
    command = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
    # t=1 -> 1x1
    # t=2 -> 1x2
    # t=3 -> 2x1
    rg = [[0 for _ in range(4)] for _ in range(10)] 
    rb = [[0 for _ in range(10)] for _ in range(4)]
    answer = put_bar(rg,rb,command)
    answer2= 0
    for g in rg :
        answer2+=sum(g)
    for b in rb :
        answer2+=sum(b)
    print(answer)
    print(answer2)