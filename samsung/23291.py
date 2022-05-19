import sys 
from collections import deque 
n,k = map(int,sys.stdin.readline().split())
fish = list(map(int,sys.stdin.readline().split()))

def plus_mini(fish):
    mini = min(fish)
    for i in range(len(fish)): 
        if fish[i] == mini : fish[i] += 1 
dx = [0,1]
dy = [1,0]
def stacking(fish): 
    #firsh
    r = 1 
    c = 1 
    len_fish = len(fish)
    while r+1 <= len_fish - ((r*c)+c):
        if r== c :
            c+=1 
        else: 
            r+=1 
    # print(r,c,"RC")
    len_c = len_fish - r*c
    stack = [[-1 for _ in range(len_c)] for _ in range(r)] 
    last = r*c -1 
    tr = r-1 
    tc = 0
    limit = 0
    
    while last != -1 : 
        while tr >= limit : 
            stack[tr][tc] = fish[last] 
            last -=1 
            tr -= 1 
        if last == -1 : 
            # print('out when go up ')
            break 
        tr += 1  # -1 된거 다시 0 으로 
        tc += 1  # 0,0은 이미 채움

        while tc < c-limit : 
            stack[tr][tc] = fish[last] 
            last-=1 
            tc +=1 
        if last == -1:
            # print('out when go right ')
            break 
        tc -= 1 # t=c라서 - 1해줌 
        tr += 1 # 0,c-1 은 채움 
        while tr < r-limit : 
            stack[tr][tc] = fish[last]
            last -= 1 
            tr +=1 
        tr -= 1 # t=r이라  -1 한 번 해줌 
        tc -=1 # r-1,c-1은 이미 채움 
        limit +=1 #왼쪽 올라갈때 하나 막혔음 이미 
        if last == -1:
            # print("out when go down")
            break 
        while tc >= limit : 
            stack[tr][tc] = fish[last]
            last -= 1 
            tc -= 1 
        if last == -1:
            # print("out when go left ")
            break 
        tc += 1 
        tr -= 1 

    stack.append(fish[r*c:])

    for s in stack:
        print(s)

    plma = [[0 for _ in range(len_c)] for _ in range(r+1)] 
    for x in range(r+1):
        for y in range(len_c): 
            if stack[x][y] == -1 : 
                continue 
            for px,py in zip (dx,dy): 
                nx,ny = x+px, y+py
                if 0<=nx<r+1 and 0<=ny<len_c and stack[nx][ny] != -1 :
                    item = stack[x][y] - stack[nx][ny] 
                    if item <= -5 : 
                        item = (-item)//5 
                        plma[nx][ny] -= item 
                        plma[x][y] += item 
                    elif item >= 5 : 
                        item = item // 5 
                        plma[nx][ny] += item 
                        plma[x][y] -= item 
    
    stack2 = [[stack[i][j] + plma[i][j] for j in range(len_c)] for i in range(r+1)]
    # for s in stack2: # succ
    #     print(s)
    # print("line:94")
    stack = [0 for _ in range(len_fish)]
    index = 0
    for i in range(len_c):
        for j in range(r,-1,-1):
            if stack2[j][i] == -1 : 
                break
            stack[index] = stack2[j][i]
            index+=1 
    # print(stack)

    # if len_c != c : 
    #     for i in range(len_c-c,len_c):
    #         stack[index] = stack2[r][i]
    #         index+=1

    # print(stack) # succ 
    c = len_fish // 4 
    r = len_fish // c 
    temp_fish = deque(stack[: -c]) 
    # print(temp_fish)
    stack2= [[0 for _ in range(c)] for _ in range(r-1)]
    tr,tc = r-2,c-1
    left = True 
    while temp_fish : 
        stack2[tr][tc] = temp_fish.popleft()
        if left:
            tc -=1 
            if tc == -1 : 
                left=False 
                tr -= 1 
                tc += 1
        else: 
            tc+=1 
            if tc == c :
                left=True 
                tr -=1 
                tc -=1  
    stack2.append(stack[-c:])
    # for s in stack2 : 
    #     print(s)
    plma = [[0 for _ in range(c)] for _ in range(r)]
    for x in range(r):
        for y in range(c): 
            for px,py in zip(dx,dy):
                nx,ny = x+px, y+py 
                if 0<=nx<r and 0<=ny<c :
                    item = stack2[x][y] - stack2[nx][ny] 
                    if item <= -5 : 
                        item = (-item)//5 
                        plma[x][y] += item 
                        plma[nx][ny] -= item 
                    elif item>=5:
                        item = item // 5 
                        plma[x][y] -= item 
                        plma[nx][ny] += item 
    # print("*"*10)
    # for p in plma:
    #     print(p)
    stack = [[stack2[i][j]+plma[i][j] for j in range(c)] for i in range(r)]
    # print("*"*10)
    # for s in stack:
    #     print(s)
    
    stack2 = [0 for _ in range(len_fish)]
    index = 0
    tr = r-1 
    tc = 0 
    for i in range(c):
        for j in range(r-1,-1,-1):
            stack2[index] = stack[j][i]
            index+=1 
    # print(stack2)
    return stack2
answer = 0 
while True : 
    answer +=1 
    plus_mini(fish)
    fish = stacking(fish)
    if max(fish)-min(fish) <= k :
        break 
print(answer)
    
    

"""

6 1
1 2 3 4 5 6

7 1
1 2 3 4 5 6 7

8 1
1 2 3 4 5 6 7 8 

9 1
1 2 3 4 5 6 7 8 9 

10 1
1 2 3 4 5 6 7 8 9 10

12 1
1 2 3 4 5 6 7 8 9 10 11 12

16 0
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16

20 0
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 
24 0 
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24

"""