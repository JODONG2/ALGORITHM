from collections import deque 

if __name__ == "__main__": 
    qs = list(input())
    deq = deque()
    l = 0 
    r = 0 
    answer = 0 
    for q in qs :
        if not deq : 
            deq.append(q)
        else :
            if deq[-1] == "(" and q == ")": 
                deq.pop()
            else : 
                deq.append(q) 
    print(len(deq))
    