from collections import deque 

def check(q1,q2):
    return sum(q1)==sum(q2)

def mix(q1,q2,compare,sq1,sq2,len_q):
    cnt = 0
    len_q = len_q*2
    while sq1 != compare:
        while sq1>sq2:
            q1_value = q1.popleft()
            sq1 -= q1_value 
            sq2 += q1_value 
            q2.append(q1_value)
            cnt+=1
        if cnt > len_q:
            return -1 
        while sq2>sq1 : 
            q2_value = q2.popleft()
            sq2 -= q2_value 
            sq1 += q2_value 
            q1.append(q2_value)
            cnt+=1
        if cnt>len_q:
            return -1
    return cnt 

def solution(queue1, queue2):
    answer = 0
    q1 = deque(queue1)
    q2 = deque(queue2)
    if check(q1,q2):
        return 0 
    q1q2 = sum(q1)+ sum(q2)
    if q1q2 % 2 == 1 :
        return -1 
    for index,(q11,q22) in enumerate(zip(q1,q2)):
        if q11 > q1q2 - q11 : 
            return -1 
        elif q11 == q1q2 - q11 : 
            return index*2 + len(q1) + 1
        elif q22 > q1q2 - q22 :
            return -1 
        elif q22 == q1q2 - q22 : 
            return index*2 + len(q2) + 1 
    answer = mix(q1,q2,q1q2//2,sum(q1),sum(q2),len(q1))
    return answer