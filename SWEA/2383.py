def cal_dist(stair,human):
    ret = {}
    num = 0
    for i,s in enumerate(stair) : 
        sx,sy,st= s 
        for h_num,h in enumerate(human) : 
            x,y = h
            if i == 0 :
                ret[h_num+1] = [abs(sx-x)+abs(sy-y)]
            else :
                ret[h_num+1].append(abs(sx-x)+abs(sy-y))
    return ret

from collections import deque
def cal (s1,s2,dist,time,h_cnt):
    temp = {}
    for key,value in dist.items():
        temp[key]= value[:]
    cnt = 0
    t= 0
    sq1 = deque() 
    sq2 = deque()
    sq1_wait = deque()
    sq2_wait = deque()
    while t< time : 
        t+=1
        for s11,s22 in zip (s1,s2): 
            if s11!= 0 : 
                temp[s11][0] -=1 
                if temp[s11][0] == 0 : 
                    if len(sq1)<3 : 
                        sq1.append([s11,stair[0][2]+1])
                    else:
                        sq1_wait.append(s11)
            if s22!=0 :
                temp[s22][1] -=1 
                if temp[s22][1] == 0 : 
                    if len(sq2) < 3:
                        sq2.append([s22,stair[1][2]+1]) 
                    else : 
                        sq2_wait.append(s22)
        cnt1 = 0 
        cnt2 = 0
        for s in sq1 : 
            s[1] -= 1
            if s[1] == 0 : 
                cnt1 +=1 
        for s in sq2 : 
            s[1] -= 1 
            if s[1] == 0 :
                cnt2 += 1 

        for _ in range(cnt1):
            sq1.popleft()
            if sq1_wait : 
                sq1.append([sq1_wait.popleft(),stair[0][2]])
            cnt+=1
        for _ in range(cnt2):
            sq2.popleft()
            if sq2_wait:
                sq2.append([sq2_wait.popleft(),stair[1][2]])
            cnt+=1 
        if cnt == h_cnt : 
            return t+1 
    return time

def div(time,dist,s1,s2,h_cnt,depth,index): 
    print(s1,s2)
    if depth == 0 or depth == h_cnt : 
        time = min(time,cal(s1,s2,dist,time,h_cnt))
        if depth == h_cnt:
            return time 
    for i in range(h_cnt):
        if i <= index : 
            continue 
        s1[i],s2[i] = s2[i],s1[i]
        time = min(time,cal(s1,s2,dist,time,h_cnt))
        time = min(time, div(time,dist,s1,s2,h_cnt,depth+1,i))
        s1[i],s2[i] = s2[i],s1[i]
    return time 

test_case = int(input()) 
for t in range(1,test_case+1):
    n = int(input())
    room = [list(map(int,input().split())) for _ in range(n)] 
    human = []
    cnt = 1
    stair = [] 
    h_cnt = 0 
    for i in range(n):
        for j in range(n): 
            if room[i][j] == 1 :
                human.append([i,j])
                h_cnt += 1 
            elif room[i][j] != 0 : 
                stair.append([i,j,room[i][j]])
    dist = cal_dist(stair,human)
    answer = div(9999,dist,[i for i in range(1,h_cnt+1)], [ 0 for _ in range(h_cnt)], h_cnt, 0, -1)
    print(f"#{t} {answer}")
"""
1
5
0 1 1 0 0
0 0 1 0 3
0 1 0 1 0
0 0 0 0 0
1 0 5 0 0

1
9
0 0 0 1 0 0 0 0 0
0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 8
7 0 0 0 0 1 0 0 0
0 0 0 0 0 1 1 0 0
0 0 0 0 0 0 0 0 0
1 0 0 0 0 1 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0

->18 
"""


        