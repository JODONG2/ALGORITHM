def check(A,index,len_p):
    num = A[index]
    visit = [num] 
    for _ in range(len_p-1):
        num = A[num]
        if num in visit:
            for v in visit:
                check_visit[v] = False 
            return 1 
        visit.append(num)
    return 0 

def circle(A,len_p):
    ret = 0 
    for i in range(len_p):
        if not check_visit[i]:
            continue 
        ret += check(A,i,len_p)
    return ret 
n = int(input())
P = list(map(int,input().split()))
len_P = len(P)
check_visit = [True for _ in range(n)] 
answer = circle(P,len_P)

print(answer)


