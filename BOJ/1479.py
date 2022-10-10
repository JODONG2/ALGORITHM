from itertools import combinations 
import sys 

n,m = map(int,sys.stdin.readline().split())
guitar = set()
for _ in range(n):
    gu, play = sys.stdin.readline().split()
    bin_play = ''
    for p in play : 
        bin_play += '1' if p =='Y' else '0'
    guitar.add(int(bin_play,2))
guitar -={0}
if not guitar :
    print(-1)
else:
    maxi = 0 
    ans = 0
    for i in range(1,n+1):
        for comb in combinations(guitar,i):
            tmp = 0
            for c in comb:
                tmp|=c
            cnt = 0 
            for j in range(m):
                if tmp & (1<<j):
                    cnt+=1 
            if cnt > maxi : 
                maxi = cnt 
                ans = i
    print(ans)