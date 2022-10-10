from collections import deque 

def X(a,b):
    return a+1, b+b 
def Y(a,b):
    return a+a, b+1 
print(2**250)
def X2_1(a,b): # a!=b
    cnt = 0 
    q = deque([(a,b,'',cnt)])
    while True:
        a,b,command,cnt = q.popleft()
        print(a,b,command,cnt)
        na,nb = X(a,b) 
        if na == nb : 
            return command+"X"
        else : 
            q.append((na,nb,command+"X",cnt+1))

        na,nb = Y(a,b)
        if na == nb : 
            return command+"Y" 
        else : 
            q.append((na,nb,command+"Y",cnt+1))


n = int(input()) 
for t in range(1,n+1):
    a,b = map(int,input().split()) 
    print(f"#{t} {X2_1(a,b)}")

# 7 99 
