from sys import stdin

import heapq as H
#n = int(sys.stdin.readline()) 
n = int(input())

lheap = [] 
rheap = []
answer = [] 
for _ in range(n) :
    #num = int(sys.stdin.readline()) 
    num = int(input())
    if len(lheap) == len(rheap):
        H.heappush(lheap, (-num, num))
    else : 
        H.heappush(rheap, (num,num)) 
    
    if rheap and (lheap[0][1] > rheap[0][0]):
        mini = H.heappop(rheap)[0] 
        maxi = H.heappop(lheap)[1] 
        H.heappush(lheap, (-mini,mini))
        H.heappush(rheap, (maxi,maxi))
    answer.append(lheap[0][1])
for ans in answer:
    print(ans) 

