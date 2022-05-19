import sys 
import heapq 
def charge(charges,now_oil,distance): 
    ret = 0
    q= []
    for i in range(cnt+1):
        if charges[i][0] > now_oil :
            while q and now_oil < charges[i][0]:
                plus = heapq.heappop(q)
                now_oil += plus[1]
                ret+=1
            heapq.heappush(q,(-charges[i][1], charges[i][1]))
            if now_oil >= distance:
                return ret 
            elif now_oil < charges[i][0]:
                return -1 
        else :
            heapq.heappush(q,(-charges[i][1],charges[i][1]))
        if now_oil >= distance:
            return ret 
    if now_oil < distance : 
        ret = -1
    return ret 
cnt = int(input()) 
charges = [list(map(int,sys.stdin.readline().split())) for _ in range(cnt)]
check = [True for _ in range(cnt)]
distance,oil = map(int,sys.stdin.readline().split()) 
charges.append([distance, 0])
charges.sort(key=lambda x: x[0])
print(charge(charges,oil,distance))

"""
5
1 5
5 7
6 1
7 10
8 3
20 10


6
5 6
7 8
6 10
11 5
13 2
18 5
30 10

4
4 1
5 1
11 3
15 10
25 10
"""