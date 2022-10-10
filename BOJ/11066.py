
from collections import deque 
test = int(input()) 
for t in range(1,test+1):
    N = int(input())
    file = deque(sorted(list(map(int,input().split()))))
    print(file)
    temp = deque()
    answer = 0 
    while file :
        l = file.popleft()
        r = 0 
        if file : 
            r = file.popleft() 
        else : 
            answer += answer + l 
            break 
        if r : 
            temp = l+r
            if not file : 
                answer += temp 
                break 
            i = 0
            len_file = len(file)
            while file and len_file > i and file[i] < temp : 
                i+=1 
            file.insert(i,temp)
            answer += temp
            print(file,answer)
    print(answer ,"*answer*"*10)
            
        
