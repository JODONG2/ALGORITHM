import sys 
from itertools import combinations 
n,m = map(int,sys.stdin.readline().split())
friends = set()
for _ in range(m):
    can = ['0']*(n+1)
    tmp = list(map(int,sys.stdin.readline().split()))
    for i in tmp[1:] : 
        can[i] = '1'
    friends.add(int(''.join(can),2)) 
len_friends = len(friends)
ans = -1 
for cnt in range(1,len_friends) :
    for comb in combinations(friends,cnt) : 
        tmp = 0 
        for co in comb: 
            tmp|=co
        k=0 
        for i in range(n):
            if tmp&(1<<i):
                k+=1 
        if k==n : 
            ans = cnt 
            break 
    if ans != -1 :
        break 
print(ans)

