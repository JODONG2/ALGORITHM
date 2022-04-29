

def check(film):
    for i in range(w):
        cnta = 0 
        cntb = 0 
        succ = False 
        for j in range(d): 
            if film[j][i] == 0:
                cnta+=1 
                if cnta == k : 
                    succ = True 
                    break 
                cntb = 0 
            else: 
                cntb+=1 
                if cntb == k:
                    succ = True 
                    break 
                cnta = 0  
        if not succ : 
            return False 
    return True 

def inject(film,d,w,k,cnt,index):
    if check(film):
        global answer 
        answer = min(answer,cnt)
    if cnt >= answer : 
        return 
    for i in range(d): 
        if index >=i :
            continue 
        temp = [film[i][j] for j in range(w)]
        for j in range(w):
            film[i][j] = 1 
        inject(film,d,w,k,cnt+1,i)
        for j in range(w):
            film[i][j] = 0 
        inject(film,d,w,k,cnt+1,i)
        for j in range(w): 
            film[i][j] = temp[j]

tc = int(input())
for t in range(1,tc+1):
    d,w,k = map(int,input().split()) 
    film = [list(map(int,input().split())) for _ in range(d)]
    answer=float('inf')
    inject(film,d,w,k,0,-1)
    print(answer)


"""
1          
6 8 3         
0 0 1 0 1 0 0 1
0 1 0 0 0 1 1 1
0 1 1 1 0 0 0 0
1 1 1 1 0 0 0 1
0 1 1 0 1 0 0 1
1 0 1 0 1 1 0 1

1
6 8 3         
1 1 1 1 0 0 1 0
0 0 1 1 0 1 0 1
1 1 1 1 0 0 1 0
1 1 1 0 0 1 1 0
1 1 0 1 1 1 1 0
1 1 1 0 0 1 1 0
->0
"""